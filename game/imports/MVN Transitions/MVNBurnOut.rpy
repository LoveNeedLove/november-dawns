init python:
    burn_dissolve_vars = """
    uniform float u_progress;
    uniform float u_softness;
    uniform sampler2D tex0;
    uniform sampler2D u_map;
    varying vec2 v_tex_coord;
    attribute vec2 a_tex_coord;
    uniform vec3 u_low_color;
    uniform vec3 u_mid_color;
    uniform vec3 u_high_color;
    uniform vec3 u_max_color;
"""

    burn_dissolve_hide = """
    vec4 base = texture2D(tex0, v_tex_coord);
    float map_val = 1.0- texture2D(u_map, v_tex_coord).r;

    float edge0 = u_progress - u_softness;
    float edge1 = u_progress + u_softness;

    float soft_mask = smoothstep(edge0, edge1, map_val);
    float hard_mask = step(u_progress, map_val);

    float burn_band = soft_mask - hard_mask;
    float burn = clamp(burn_band / u_softness, 0.0, 1.0);

    vec3 burn_color;

    if (burn < 0.25)
        burn_color = u_low_color;                       
    else if (burn < 0.5)
        burn_color = u_mid_color;             
    else if (burn < 0.85)
        burn_color = u_high_color;            
    else
        burn_color = u_max_color;             

    vec3 final_rgb = base.rgb * hard_mask + burn_color * burn;

    gl_FragColor = vec4(final_rgb, base.a * hard_mask);
"""

    burn_dissolve_show = """
    vec4 base = texture2D(tex0, v_tex_coord);
    float map_val = 1.0- texture2D(u_map, v_tex_coord).r;

    float edge0 = u_progress - u_softness;
    float edge1 = u_progress + u_softness;

    float soft_mask = smoothstep(edge0, edge1, map_val);
    float hard_mask = step(u_progress, map_val);

    float burn_band = soft_mask - hard_mask;
    float burn = clamp(burn_band / u_softness, 0.0, 1.0);

    vec3 burn_color;
    //Normally I'd cry more about doing it this way, but the effects are short lived.
    if (burn < 0.25)
        burn_color = u_low_color;                       
    else if (burn < 0.5)
        burn_color = u_mid_color;             
    else if (burn < 0.85)
        burn_color = u_high_color;            
    else
        burn_color = u_max_color;  

    float inv = 1.0 - hard_mask;

    vec3 final_rgb = base.rgb * inv + burn_color * burn;

    gl_FragColor = vec4(final_rgb, base.a * inv);
"""

    renpy.register_shader(
    "MakeVisualNovels.BurnDissolveShow",
    variables=burn_dissolve_vars,
    vertex_300="v_tex_coord = a_tex_coord;",
    fragment_300=burn_dissolve_show,
)

    renpy.register_shader(
    "MakeVisualNovels.BurnDissolveHide",
    variables=burn_dissolve_vars,
    vertex_300="v_tex_coord = a_tex_coord;",
    fragment_300=burn_dissolve_hide,
)
