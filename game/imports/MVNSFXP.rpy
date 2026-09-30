init python:

    
    lucifyvars = """
    uniform vec4 u_lucify_color;
    uniform float u_inverse;
    uniform float u_state;
        """
    
    lucifyShader="""
        vec4 col = gl_FragColor;
        if (col.a == 0.0) discard;
        float value = max(col.r,max(col.b,col.g));
        value = mix(value, 1.0-value, u_inverse);
        col = vec4(value);
        col *= u_lucify_color;
        gl_FragColor = mix(gl_FragColor, col, u_state);
    """

    candleVars = """
    varying vec2 v__uv;
    uniform vec2  res0;
    uniform float u_time;  
    uniform sampler2D tex0;
    uniform vec2  u_center;   
    uniform float u_radius;   
    uniform float u_softness; 
    uniform float u_power;    
    uniform vec3  u_color;    
    uniform float u_strength; 
    uniform float u_flickerAmp; 
    uniform float u_flickerSpeed;
    uniform float u_noise;      
    uniform float u_swayAmp;    
    uniform float u_swaySpeed;  
    uniform float u_flkDetail;  
    uniform float u_flkBias;    
    uniform float u_flkGust;    
    uniform float u_warmShift;  
    uniform float u_bendTop;    
    uniform float u_bendLeft;   
    uniform float u_bendRight;  
    uniform float u_edgeSoft;   
    uniform float u_warpPow;    
    uniform float u_bendSway;   
    """

    candleFunct = """
    float hash(float x){ return fract(sin(x)*43758.5453123); }

    float noise1(float x){
        float i=floor(x), f=fract(x);
        float a=hash(i), b=hash(i+1.0);
        float u=f*f*(3.0-2.0*f);
        return mix(a,b,u);
    }

    float fbm(float x){
        float v=0.0, amp=0.5, freq=1.0;
        for(int i=0;i<4;i++){ v+=amp*noise1(x*freq); freq*=2.0; amp*=0.5; }
        return v;
    }

    float bias(float x, float a){
        x = clamp(x, 0.0001, 0.9999);
        float k = log(a)/log(0.5);
        return pow(x, k);
    }
    """

    candleFrag = """
    vec2 uv = v__uv;
    float aspect = res0.x / max(res0.y, 1.0);  
    float bt = u_time * u_bendSway;
    float bendTop   = u_bendTop   * sin(bt);
    float bendLeft  = u_bendLeft  * sin(bt + 1.2);
    float bendRight = u_bendRight * sin(bt - 1.2);  
    float mLeft  = smoothstep(0.0, u_edgeSoft, uv.x);
    float mRight = smoothstep(0.0, u_edgeSoft, 1.0 - uv.x);
    float mTop   = 1.0 - smoothstep(0.0, u_edgeSoft, uv.y);
    float wY = pow(1.0-uv.y, max(u_warpPow, 0.001));
    

    vec2 disp = vec2(0.0);
    disp.x += (-bendLeft * mLeft + bendRight * mRight) * wY;
    disp.y += (-bendTop  * mTop)  * wY;
    vec2 uvp = clamp(uv + disp, vec2(0.0), vec2(1.0));

    float wt = 6.28318530718 * u_swaySpeed * u_time;   // 2pi 
    vec2 sway = vec2(sin(wt), cos(wt * 0.9)) * u_swayAmp;
    sway.x /= aspect; // oblongness
    vec2 c = u_center + sway;
    vec2 d = uvp - c;
    d.x *= aspect;
    float r = length(d);
    float v = 1.0 - smoothstep(u_radius, u_radius + u_softness, r);
    v = pow(clamp(v, 0.0, 1.0), max(u_power, 0.001));   
    float t = u_time;   
    float gust   = fbm(t * max(0.05, u_flickerSpeed * 0.15));
    float base   = fbm(t * u_flickerSpeed);
    float detail = fbm(t * u_flickerSpeed * max(2.0, u_flkDetail));
    float raw    = mix(base, detail, 0.35);
    float shaped = bias(raw, clamp(u_flkBias, 0.0, 1.0));
    float ampVar = mix(0.6, 1.0, clamp(u_flkGust, 0.0, 1.0) * gust);
    float centered = (shaped - 0.5) * 1.8;                 // ~[-0.9..0.9]
    float flicker  = 1.0 + (u_flickerAmp * ampVar) * centered;
    vec4 original = texture2D(tex0, uvp);
    vec3 warmHi = vec3(1.0, 0.88, 0.45);
    vec3 tint   = mix(u_color, warmHi, clamp(u_warmShift, 0.0, 1.0) * max(centered, 0.0));
    float intensity = clamp(v * flicker * u_strength, 0.0, 1.0);
    vec3 outRGB = original.rgb * flicker + tint * intensity;
    gl_FragColor = vec4(outRGB, original.a);
    """

    #Extremely wasteful way of implementing it, but it's fast and easy.  
    #The other calculations still *happen*, but we're throwing them out.
    candleHaloOnly = """
    gl_FragColor = vec4(tint * intensity, original.a);
    """

    candleWarpOnly = """
    gl_FragColor = original;
    """

    # Heavily depends on the attached visual to look nice, but there's some use cases.
    candleEmissionEffect = """
    outRGB = original.rgb * flicker * tint * intensity;
    gl_FragColor = vec4(outRGB, original.a);
    """

    # Kinda neat for eclipse style effects.
    candleSilhouette = """
    outRGB = (flicker * tint * intensity)-original.a;
    gl_FragColor = vec4(outRGB, original.a);
    """

    glitch_vars = """
    varying vec2 v__uv;
    uniform vec2  res0;          // framebuffer size
    uniform float u_time;        // seconds
    uniform sampler2D tex0;      // the image/sprite to glitch
    uniform float u_intensity;   // 0..1 overall drive
    uniform float u_gate;        // 0..1 on/off or burst amount
    uniform float u_seed;        // randomization seed
    uniform float u_gridX;       // columns (e.g. 40)
    uniform float u_gridY;       // rows    (e.g. 25)
    uniform float u_shuffle;     // 0..1 probability of a cell shuffle
    uniform float u_jitterAmp;   // UV units (0.0..0.02)
    uniform float u_jitterFreq;  // Hz
    uniform float u_bandAmp;     // pixels (converted to UV)
    uniform float u_bandWidth;   // 0..1 (thickness)
    uniform float u_bandSpeed;   // bands drift speed
    uniform float u_bandDensity; // bands across the screen height
    uniform float u_rgbSplit;    // pixels
    uniform float u_scanAmp;     // 0..1
    uniform float u_snowAmp;     // 0..1    
    uniform float u_flipProbX;   // 0..1 probability to flip horizontally
    uniform float u_flipProbY;   // 0..1 probability to flip vertically
    uniform float u_invertProb;  // 0..1 probability to invert colors
    uniform float u_invertMix;   // 0..1 amount of inversion when triggered
    uniform float u_reseedRate;  // Hz; how often flip/invert decisions reseed (0=static)
    """

    glitch_fn = """
    float hash1(float x){ return fract(sin(x)*43758.5453123); }
    float hash2(vec2 p){ return fract(sin(dot(p, vec2(12.9898,78.233))) * 43758.5453); }

    // cheap 1D noise, effect is huge as it is
    float n1(float x){
        float i=floor(x), f=fract(x);
        float a=hash1(i), b=hash1(i+1.0);
        float u=f*f*(3.0-2.0*f);
        return mix(a,b,u);
    }
    """

    glitch_frag = """
    vec2 uv = v__uv;
    float drive = clamp(u_intensity * u_gate, 0.0, 1.0);
    if (drive <= 0.0001) {
        gl_FragColor = texture2D(tex0, uv);
        return;
    }

    vec2 grid = max(vec2(1.0), vec2(u_gridX, u_gridY));
    vec2 gUV  = uv * grid;
    vec2 cell = floor(gUV);
    vec2 fuv  = fract(gUV);

    // shuffle decision per original cell
    float r  = hash2(cell + vec2(floor(u_time*11.0)+u_seed, 7.0));
    float th = 1.0 - u_shuffle * drive;
    float doShuffle = step(th, r);

    float kx = floor(fract(r*3.17)*3.0) - 1.0;  // -1,0,1
    float ky = floor(fract(r*7.31)*3.0) - 1.0;  // -1,0,1
    vec2 cell2 = mod(cell + doShuffle * vec2(kx, ky), grid);  // destination cell

    float epoch = (u_reseedRate > 0.0) ? floor(u_time * u_reseedRate) : 0.0;

    float rFx = hash2(cell2 + vec2(epoch + u_seed*2.3, 21.7));
    float rFy = hash2(cell2 + vec2(epoch + u_seed*5.1, 47.9));
    float rIv = hash2(cell2 + vec2(epoch + u_seed*7.7, 93.1));

    float doFlipX  = step(1.0 - u_flipProbX  * drive, rFx);
    float doFlipY  = step(1.0 - u_flipProbY  * drive, rFy);
    float doInvert = step(1.0 - u_invertProb * drive, rIv);

    // do a flip!
    vec2 fuv2 = fuv;
    fuv2.x = mix(fuv2.x, 1.0 - fuv2.x, doFlipX);
    fuv2.y = mix(fuv2.y, 1.0 - fuv2.y, doFlipY);

    vec2 puvx    = fwidth(uv);            
    vec2 padUV = clamp(puvx * grid * 0.5, 
                   vec2(0.0005),     
                   vec2(0.49));      
    fuv2 = clamp(fuv2, padUV, 1.0 - padUV);

    vec2 uvA = (cell2 + fuv2) / grid;
    float t = u_time;
    float phx = 6.2831853 * (hash2(cell2 + vec2(1.23,4.56)+u_seed) + t*u_jitterFreq);
    float phy = 6.2831853 * (hash2(cell2 + vec2(7.89,0.12)+u_seed) + t*u_jitterFreq*1.3);
    vec2 jitter = vec2(sin(phx), cos(phy)) * (u_jitterAmp * drive);
    vec2 uvB = uvA + jitter;

    float bands   = max(1.0, u_bandDensity);
    float yScaled = uv.y * bands + t * u_bandSpeed;
    float fracY   = fract(yScaled);
    float bandMask = smoothstep(0.0, u_bandWidth, fracY) * (1.0 - smoothstep(1.0 - u_bandWidth, 1.0, fracY));

    float bandId = floor(yScaled);
    float rBand  = hash1(bandId + u_seed*13.37);
    float px     = (rBand*2.0 - 1.0) * u_bandAmp * drive; // pixels
    float tearUV = px / max(res0.x, 1.0);

    vec2 uvC = uvB;
    uvC.x += bandMask * tearUV;

    float ca = (u_rgbSplit / max(res0.x, 1.0)) * drive;
    vec4 sR = texture2D(tex0, clamp(uvC + vec2(+ca, 0.0), 0.0, 1.0));
    vec4 sG = texture2D(tex0, clamp(uvC, 0.0, 1.0));
    vec4 sB = texture2D(tex0, clamp(uvC + vec2(-ca, 0.0), 0.0, 1.0));

    float a  = sG.a;  // use center tap’s alpha as the output alpha
    float ar = max(a, 1e-3); //lmao
    vec3 rS = (sR.a > 0.0) ? (sR.rgb / max(sR.a, 1e-3)) : vec3(0.0);
    vec3 gS = (sG.a > 0.0) ? (sG.rgb / ar)              : vec3(0.0);
    vec3 bS = (sB.a > 0.0) ? (sB.rgb / max(sB.a, 1e-3)) : vec3(0.0);
    vec3 colS = vec3(rS.r, gS.g, bS.b);
    float edgeW = smoothstep(0.03, 0.12, a);
    colS *= edgeW;

    float invAmt = doInvert * clamp(u_invertMix, 0.0, 1.0) * edgeW;
    colS = mix(colS, 1.0 - colS, invAmt);
    float scan = 1.0 - u_scanAmp * drive * (0.5 + 0.5 * sin(uv.y * res0.y * 3.14159265));
    colS *= scan;
    float snow = (hash2(uv * res0 + vec2(floor(u_time*120.0)+u_seed, 0.0)) * 2.0 - 1.0);
    colS += snow * (0.02 * u_snowAmp * drive) * edgeW;

    vec3 col = colS * a;
    gl_FragColor = vec4(col, a);
"""
    oozeVars = """
    attribute vec2 a_tex_coord;
    varying vec2 v__uv;
    uniform sampler2D tex0;
    uniform vec2 res0;            
    uniform float u_time;          
    uniform float u_fromtop;      
    uniform float u_scale;         
    uniform float u_thresh;        
    uniform float u_progress;  
    uniform float u_scrollDist;
    uniform float u_phase;     
    uniform float u_amp;           
    uniform float u_freq;          
    uniform float u_heightEdge0;   
    uniform float u_heightEdge1;   
    uniform float u_heightGain;    
    uniform vec3  u_lightDir;      
    uniform vec3  u_color;         
    uniform float u_lipSoft;       
    """

    oozeFunctions= """
    float hash(float x){
    return fract(sin(x) * 43758.5453123);
}

float noise1(float x, float seed){
    float i = floor(x);
    float f = fract(x);
    float a = hash(i + seed*13.37);
    float b = hash(i + 1.0 + seed*13.37);
    float u = f*f*(3.0 - 2.0*f); // smoothstep
    return mix(a, b, u);
}

float fbm(float x, float seed){
    float v = 0.0;
    float amp = 0.5;
    float freq = 1.0;
    // 4 octaves is plenty for an edge
    for (int i=0;i<4;i++){
        v += amp * noise1(x * freq, seed);
        freq *= 2.0;
        amp  *= 0.5;
    }
    return v;
}
"""

    oozeFragment = """
    vec2 fragCoord = v__uv * res0;
    vec2 uv = fragCoord / res0;
    uv.x /= (res0.y / max(res0.x, 1.0));
    uv.y = abs(u_fromtop-uv.y);                 
    vec2 pp = uv * u_scale;
    float p = clamp(u_progress, 0.0, 1.0);
    float scroll = u_scrollDist * p;
    vec2 ppw = pp;
    ppw.y += (
        0.3 * u_amp * sin(1.3 * u_freq * ppw.x + ppw.y + u_phase) +
        0.15* u_amp * sin(2.6 * u_freq * ppw.x + ppw.y + u_phase) +
        0.1 * u_amp * sin(11.7* u_freq * ppw.x + u_phase) +
        0.05* u_amp * sin(13.9* u_freq * ppw.x + u_phase)
    );
    ppw += vec2(0.0, 1.0) * scroll;   // progress drives the lip downward
    float d = abs(ppw.y - u_thresh);
    float h = clamp(smoothstep(u_heightEdge0, u_heightEdge1, d), 0.0, 1.0);
    h = pow(h, 0.2) * u_heightGain;
    vec2 eps = vec2(u_scale) / max(res0, vec2(1.0)); // ≈1px in pp
    vec2 ppw_x = pp + vec2(eps.x, 0.0);
    ppw_x.y += (
        0.3 * u_amp * sin(1.3 * u_freq * ppw_x.x + ppw_x.y + u_phase) +
        0.15* u_amp * sin(2.6 * u_freq * ppw_x.x + ppw_x.y + u_phase) +
        0.1 * u_amp * sin(11.7* u_freq * ppw_x.x + u_phase) +
        0.05* u_amp * sin(13.9* u_freq * ppw_x.x + u_phase)
    );
    ppw_x += vec2(0.0, 1.0) * scroll;
    float dpx = abs(ppw_x.y - u_thresh);
    float hx  = clamp(smoothstep(u_heightEdge0, u_heightEdge1, dpx), 0.0, 1.0);
    hx = pow(hx, 0.2) * u_heightGain;
    vec2 ppw_y = pp + vec2(0.0, eps.y);
    ppw_y.y += (
        0.3 * u_amp * sin(1.3 * u_freq * ppw_y.x + ppw_y.y + u_phase) +
        0.15* u_amp * sin(2.6 * u_freq * ppw_y.x + ppw_y.y + u_phase) +
        0.1 * u_amp * sin(11.7* u_freq * ppw_y.x + u_phase) +
        0.05* u_amp * sin(13.9* u_freq * ppw_y.x + u_phase)
    );
    ppw_y += vec2(0.0, 1.0) * scroll;
    float dpy = abs(ppw_y.y - u_thresh);
    float hy  = clamp(smoothstep(u_heightEdge0, u_heightEdge1, dpy), 0.0, 1.0);
    hy = pow(hy, 0.2) * u_heightGain;
    vec2 g = vec2(hx - h, hy - h) / eps;
    vec3 N = normalize(vec3(-g.x, 1.0, -g.y));
    vec3 L = normalize(u_lightDir);
    vec3 bloodCol = pow(max(dot(N, L), 0.0), 10.0) * vec3(1.0) + u_color;
    float s = max(u_lipSoft, 1.0 / 2000.0);
    float fillMask = smoothstep(u_thresh - s, u_thresh + s, ppw.y);

    gl_FragColor = vec4(bloodCol * fillMask, fillMask);
"""
    oozeReplace = """
    vec4 orgcolor = texture2D(tex0, v__uv);
    gl_FragColor = mix(orgcolor, vec4(bloodCol* fillMask, fillMask), fillMask);
    """
    oozeReveal = """
    vec4 orgcolor = texture2D(tex0, v__uv);
    gl_FragColor = orgcolor* vec4(bloodCol* fillMask, fillMask);
    """

    oozeSubTractReveal = """
    vec4 orgcolor = texture2D(tex0, v__uv);
    gl_FragColor = vec4((bloodCol-orgcolor.rgb)* fillMask, fillMask);
    """
    oozeFromBlack = """
    vec4 orgcolor = vec4(0.0,0.0,0.0,0.0);
    gl_FragColor = vec4(orgcolor.rgb)* fillMask, fillMask);
    """

    oozeTextureMask = """
    vec4 orgcolor = texture2D(tex0, v__uv);
    float lumin = max(orgcolor.r,max(orgcolor.b,orgcolor.g));
    gl_FragColor = vec4(bloodCol* (fillMask-lumin), fillMask-lumin);
    """

    oozeTextureMaskFromBlack = """
    vec4 orgcolor = texture2D(tex0, v__uv);
    float lumin = max(orgcolor.r,max(orgcolor.b,orgcolor.g)); //Should be white or black but someone's gonna do it.
    gl_FragColor = mix(vec4(0.0,0.0,0.0,1.0),vec4(bloodCol * (fillMask-lumin), fillMask-lumin),fillMask-lumin);
    """

    renpy.register_shader(
        "MakeVisualNovels.SimpleOoze",
        variables=oozeVars,
        vertex_300="v__uv = a_tex_coord;",
        fragment_functions=oozeFunctions,
        fragment_300=oozeFragment
    )

    renpy.register_shader(
        "MakeVisualNovels.Ooze",
        variables=oozeVars,
        vertex_300="v__uv = a_tex_coord;",
        fragment_functions=oozeFunctions,
        fragment_300=oozeFragment+oozeReplace
    )

    renpy.register_shader(
        "MakeVisualNovels.OozeFromBlack",
        variables=oozeVars,
        vertex_300="v__uv = a_tex_coord;",
        fragment_functions=oozeFunctions,
        fragment_300=oozeFragment+oozeFromBlack
    )

    renpy.register_shader(
        "MakeVisualNovels.OozeSubtract",
        variables=oozeVars,
        vertex_300="v__uv = a_tex_coord;",
        fragment_functions=oozeFunctions,
        fragment_300=oozeFragment+oozeSubTractReveal
    )

    renpy.register_shader(
        "MakeVisualNovels.OozeOut",
        variables=oozeVars,
        vertex_300="v__uv = a_tex_coord;",
        fragment_functions=oozeFunctions,
        fragment_300=oozeFragment+oozeTextureMaskFromBlack
    )

    renpy.register_shader(
        "MakeVisualNovels.OozeIn",
        variables=oozeVars,
        vertex_300="v__uv = a_tex_coord;",
        fragment_functions=oozeFunctions,
        fragment_300=oozeFragment+oozeReveal
    )
    
    renpy.register_shader("MakeVisualNovels.Lucify", variables=lucifyvars, fragment_300=lucifyShader)

    renpy.register_shader(
        "MakeVisualNovels.HorrorGlitch",
        variables=glitch_vars,
        fragment_functions=glitch_fn,
        vertex_300="v__uv = a_tex_coord;",
        fragment_300=glitch_frag
    )

    renpy.register_shader(
        "MakeVisualNovels.Candle",
        variables=candleVars,
        vertex_300="v__uv = a_tex_coord;",
        fragment_functions=candleFunct,
        fragment_300=candleFrag
    )

    renpy.register_shader(
        "MakeVisualNovels.CandleHalo",
        variables=candleVars,
        vertex_300="v__uv = a_tex_coord;",
        fragment_functions=candleFunct,
        fragment_300=candleFrag+candleHaloOnly
    )

    renpy.register_shader(
        "MakeVisualNovels.CandleWarp",
        variables=candleVars,
        vertex_300="v__uv = a_tex_coord;",
        fragment_functions=candleFunct,
        fragment_300=candleFrag+candleWarpOnly
    )

    renpy.register_shader(
        "MakeVisualNovels.CandleEmission",
        variables=candleVars,
        vertex_300="v__uv = a_tex_coord;",
        fragment_functions=candleFunct,
        fragment_300=candleFrag+candleEmissionEffect
    )

    renpy.register_shader(
        "MakeVisualNovels.CandleSilhouette",
        variables=candleVars,
        vertex_300="v__uv = a_tex_coord;",
        fragment_functions=candleFunct,
        fragment_300=candleFrag+candleSilhouette
    )

