  #Honestly kinda huge.  There's so many possible options I could put into this
transform MVN_CandleLight:
    mesh True
    shader "MakeVisualNovels.Candle"
    blend "add"
    mesh_pad (0,0,0,0) #Adjust this if your effect gets clipped off
    u_center   (0.5, 0.65) #Halo location relative to the object its put on.
    u_radius   0.028 #Size of the halo
    u_softness 0.34 # Softness of the halo
    u_power 0.9 # Intensity of the halo
    u_color (1.00, 0.76, 0.34) # Color of the halo and flicker
    u_strength 0.8 
    u_flickerAmp 0.88 # Strength of the flicker effect
    u_flickerSpeed 1.2 # How frequent the flickers happen
    u_flkDetail 8.0 # Flicker parameter
    u_flkBias 0.62 # Flicker parameter
    u_flkGust 1.45 # Flicker parameter
    u_warmShift 0.15 # Shifts the color more red at its height
    u_swayAmp   0.008 # Strength of the halo sway
    u_swaySpeed 0.9 # Speed of the halo sway
    u_bendTop   0.001 # How far upwards to bend
    u_bendLeft   0.00 # How far left to bend
    u_bendRight  0.018 # How far right to bend
    u_edgeSoft   0.85 # Softness of the bend's edge
    u_warpPow   2.0 # Size of the bend
    u_bendSway   5.2 # Frequency of the bend
    pause 0
    repeat 

#Keeps the object its applied to, but the warp is nullified by the settings.
transform MVN_Glowight:
    mesh True
    shader "MakeVisualNovels.Candle"
    blend "add"
    mesh_pad (0,0,0,0)
    u_center   (0.5, 0.65)
    u_radius   0.006
    u_softness 0.34
    u_power 0.9
    u_color (1.00, 0.76, 0.34)
    u_strength 0.5
    u_flickerAmp 0.28
    u_flickerSpeed 1.2
    u_flkDetail 3.0
    u_flkBias 0.62
    u_flkGust 0.45
    u_warmShift 0.0
    u_swayAmp   0.00
    u_swaySpeed 0.0
    u_bendTop   0.00
    u_bendLeft   0.0
    u_bendRight  0.0
    u_edgeSoft   0.
    u_warpPow   3.0
    u_bendSway   0.0
    pause 0
    repeat 

#Produces only the halo
transform MVN_CandleHalo:
    mesh True
    shader "MakeVisualNovels.CandleHalo"
    blend "add"
    mesh_pad (0,0,0,0)
    u_center   (0.5, 0.65)
    u_radius   0.028
    u_softness 0.34
    u_power 0.9
    u_color (1.00, 0.76, 0.34)
    u_strength 0.8
    u_flickerAmp 0.88
    u_flickerSpeed 1.2
    u_flkDetail 8.0
    u_flkBias 0.62
    u_flkGust 1.45
    u_warmShift 0.15
    u_swayAmp   0.008
    u_swaySpeed 0.9
    u_bendTop   0.001
    u_bendLeft   0.00
    u_bendRight  0.018
    u_edgeSoft   0.85
    u_warpPow   2.0
    u_bendSway   5.2
    pause 0
    repeat 

#Applies only the warping effect, without the halo.
transform MVN_CandleWarp:
    mesh True
    shader "MakeVisualNovels.CandleWarp"
    blend "add"
    mesh_pad (0,0,0,0)
    u_center   (0.5, 0.65)
    u_radius   0.006
    u_softness 0.34
    u_power 0.9
    u_color (1.00, 0.76, 0.34)
    u_strength 0.5
    u_flickerAmp 0.28
    u_flickerSpeed 1.2
    u_flkDetail 3.0
    u_flkBias 0.62
    u_flkGust 0.45
    u_warmShift 0.15
    u_swayAmp   0.008
    u_swaySpeed 0.9
    u_bendTop   0.001
    u_bendLeft   0.016
    u_bendRight  0.018
    u_edgeSoft   0.85
    u_warpPow   3.0
    u_bendSway   5.2
    pause 0
    repeat 


# A kitchen sink effect that houses a lot of digital horror effects in one.
transform MVN_GlitchFX:
    mesh True # Without the mesh, unintended artifacts will pop up.
    shader "MakeVisualNovels.HorrorGlitch"
    u_intensity 0.9 # Gate and Intensity drive whether or not this effect is on.  If either are 0, the effect is off.  
    u_gate  1.0 # This allows you to animate the two seperately, or turn it off while retaining one or the other.   
    u_seed  3.0 # Used for randomization of the effects
    u_reseedRate 2.0 # How often the flips and inversions happen.
    u_gridX 10.0 # How many horizontal slices of the graphic there will be.  Multiply by the Y for total number of slices.
    u_gridY 10.0 # How many vertical slices of the graphic there will be.
    u_flipProbX 0.02 # Likelyhood that a given location will flip on its X axis
    u_flipProbY 0.01 # Likelyhood that a given location will flip on its X axis
    u_invertProb 0.03 # Likelyhood that a given grid will invert its colors.
    u_invertMix 1.0 # Mix value of the inversion.  Lower causes a shift, higher causes more color crushing and distortion, 0 is off.
    u_shuffle   0.05 # Likelyhood that a given grid will be relocated.  Higher numbers are more chaotic.
    u_jitterAmp 0.03 # The strength of the jittering sub effect.  0 turns it off.
    u_jitterFreq 0.03  # How often the jitters happen.  Higher numbers are more fluid and frequent movements.
    u_bandAmp    0.0 # Strength of the band distortion subeffect. Displacement in number of pixels  0 turns it off.  
    u_bandWidth  0.00 # Width of the bands.
    u_bandSpeed  0.0 # How fast the bands travel.
    u_bandDensity 0.0 # How many bands, 2-5 is pretty good in some settings.
    u_rgbSplit  0.0 # Strength of the chromatic shifting effect in pixels.
    u_scanAmp 0.0 # Strength of the scanline effect.
    u_snowAmp  0.0 # Strength of the snow effect   
    pause 2.0
    repeat


transform MVN_VHS2:
    mesh True # Without the mesh, unintended artifacts will pop up.
    shader "MakeVisualNovels.HorrorGlitch"
    u_intensity 0.9 
    u_gate  1.0 
    u_seed  3.0 
    u_reseedRate 2.0 
    u_gridX 0.0
    u_gridY 0.0
    u_flipProbX 0.0
    u_flipProbY 0.0 
    u_invertProb 0.0
    u_invertMix 1.0
    u_shuffle   0.1
    u_jitterAmp 0.0 
    u_jitterFreq 5.5
    u_bandAmp    25.0
    u_bandWidth  0.05
    u_bandSpeed  0.25
    u_bandDensity 3.0
    u_rgbSplit 8.0 
    u_scanAmp 1.0 
    u_snowAmp 1.0 
    pause 0
    repeat

transform MVN_MyDigitalWorld:
    mesh True
    shader "MakeVisualNovels.HorrorGlitch"
    u_intensity 0.9
    u_gate  1.0   
    u_seed  3.0
    u_gridX 1920.0
    u_gridY 1080.0
    u_shuffle   1.0
    u_jitterAmp 0.001
    u_jitterFreq 0.25 
    u_bandAmp    0.0
    u_bandWidth  0.0
    u_bandSpeed  0.0
    u_bandDensity 0.0
    u_rgbSplit  0.0  
    u_scanAmp   0.0
    u_snowAmp   0.0
    u_flipProbX 0.35
    u_flipProbY 0.25
    u_invertProb 0.18
    u_invertMix 0.0
    u_reseedRate 2.0
    pause 0 
    repeat

transform MVN_Snap:
    mesh True
    shader "MakeVisualNovels.HorrorGlitch"
    u_intensity 0.9
    u_gate  1.0   
    u_seed  3.0
    u_gridX 1920.0
    u_gridY 1080.0
    u_shuffle   1.0
    u_jitterAmp 0.001
    u_jitterFreq 0.25 
    u_bandAmp    5.0
    u_bandWidth  5.0
    u_bandSpeed  1.0
    u_bandDensity 50.0
    u_rgbSplit  0.0  
    u_scanAmp   0.0
    u_snowAmp   0.0
    u_flipProbX 0.35
    u_flipProbY 0.25
    u_invertProb 0.18
    u_invertMix 0.0
    u_reseedRate 2.0
    pause 2.0
    linear 5.0 u_jitterAmp 0.1
    pause 1.0
    linear 5.0 u_jitterAmp 0.001
    repeat


transform MVN_MalfunctionFX:
    mesh True
    shader "MakeVisualNovels.HorrorGlitch"
    mesh_pad (10,10,10,10)
    u_intensity 1.0
    u_seed  3.0
    u_gridX 5.0
    u_gridY 20.0
    u_shuffle   0.1
    u_jitterAmp 0.0
    u_jitterFreq 5.5  
    u_bandAmp    0.0
    u_bandWidth  0.3
    u_bandSpeed  0.5
    u_bandDensity 0.2
    u_rgbSplit  0.0 
    u_scanAmp   0.0
    u_snowAmp   0.0
    u_flipProbX 0.35
    u_flipProbY 0.25
    u_invertProb 0.18
    u_invertMix 1.0
    u_reseedRate 2.0
    u_gate 0.0   
    pause 3.0
    u_gate 1.0
    pause 0.1
    u_gate 0.0
    pause 0.2
    u_gate 1.0
    pause 0.1
    repeat

transform MVN_LineGlitchFX:
    shader "MakeVisualNovels.HorrorGlitch"
    mesh True
    u_intensity 0.9
    u_gate  1.0   
    u_seed  3.0
    u_gridX 1.0
    u_gridY 200.0
    u_shuffle   0.05
    u_jitterAmp 0.0001
    u_jitterFreq 0.008  
    u_bandAmp    0.0
    u_bandWidth  0.0
    u_bandSpeed  0.0
    u_bandDensity 0.0
    u_rgbSplit  0.0 
    u_scanAmp   0.0
    u_snowAmp   0.0
    u_flipProbX 0.35
    u_flipProbY 0.25
    u_invertProb 0.08
    u_invertMix 0.0
    u_reseedRate 2.0
    pause 0
    repeat
    

#The ooze's edge is actually a mesh of sin waves, so think of these parameters in the frame of waves
transform MVN_Ooze:
        shader "MakeVisualNovels.SimpleOoze"
        u_scale 4.0 # Scale of the waves
        u_thresh  5.6
        u_phase 0.0
        u_scrollDist 7.0 # How far the effect travels 6.4-6.6 should handle it, but I like overshooting to 7.0
        u_heightEdge0 0.0
        u_heightEdge1 0.15
        u_heightGain 8.0
        u_amp 2.0
        u_freq 1.0
        u_lightDir (0.5, 0.7, -0.5) # For the shine effect on the edge of the ooze
        u_color (0.3, 0.7, 0.3)  
        u_lipSoft  0.006
        u_progress 0.0 # Overall progress of the effect.  Animate this to make it move.
        u_fromtop 1.0 # Which direction the effect should come from. 1.0 is top, 0.0 is bottom.
        linear (8.0) u_progress 1.2


# To use the transition effect, just use 'with MVN_OozeTransition', and optionally adjust the duration.
transform MVN_OozeTransition(duration=4.0, *,new_widget=None, old_widget=None):
        delay duration
        old_widget
        events False
        shader "MakeVisualNovels.Ooze"
        mesh True
        u_scale 4.0
        u_thresh  5.6
        u_phase 0.0 
        u_scrollDist 7.0
        u_heightEdge0 0.0
        u_heightEdge1 0.15
        u_heightGain 8.0
        u_amp 2.0
        u_freq 1.0
        u_lightDir (0.5, 0.7, -0.5)
        u_color (0.3, 0.7, 0.3)  
        u_lipSoft  0.006
        u_progress 0.0
        u_fromtop 1.0
        linear (duration/2) u_progress 1.2
        
        new_widget   
        events True
        mesh True
        shader "MakeVisualNovels.Ooze"
        u_scale 4.0
        u_thresh  5.6
        u_phase 0.0 
        u_scrollDist 7.0
        u_heightEdge0 0.0
        u_heightEdge1 0.15
        u_heightGain 8.0
        u_amp 2.0
        u_freq 1.0
        u_lightDir (0.5, 0.7, -0.5)
        u_color (0.3, 0.7, 0.3)  
        u_lipSoft  0.006  
        u_progress 1.2
        u_fromtop 0.0
        linear (duration/2) u_progress 0.0



transform MVN_BloodOverlay:
        shader "MakeVisualNovels.Ooze"
        u_scale 4.0
        u_thresh  5.6
        u_phase 0.0
        u_scrollDist 7.0
        u_heightEdge0 0.0
        u_heightEdge1 0.15
        u_heightGain 8.0
        u_amp 2.0
        u_freq 1.0
        u_lightDir (0.5, 0.7, -0.5)
        u_color (0.7, 0.2, 0.2)  
        u_lipSoft  0.006
        u_progress 0.0
        u_fromtop 1.0
        linear (8.0) u_progress 1.2


transform Lucify(color=(0.6, 0.8, 0.8, 1.0), inverse=0.0):
    mesh True
    shader "MakeVisualNovels.Lucify"
    blend "normal"
    u_lucify_color color
    u_inverse inverse
    u_state 1.0
    pause 0
    repeat

transform Ghost(color=(1.0, 1.0, 1.0, 2.0), inverse=0.0):
    mesh True
    shader "MakeVisualNovels.Lucify"
    blend "normal"
    u_lucify_color color
    u_inverse inverse
    u_state 1.0
    pause 0
    repeat

transform GreenGhast(color=(0.0, 0.8, 0.2, 2.0), inverse=0.0):
    mesh True
    shader "MakeVisualNovels.Lucify"
    blend "normal"
    u_lucify_color color
    u_inverse inverse
    u_state 1.0
    pause 0
    repeat

transform RedWraith(color=(1.0, 0.3, 0.3, 2.0), inverse=0.0):
    mesh True
    shader "MakeVisualNovels.Lucify"
    blend "normal"
    u_lucify_color color
    u_inverse inverse
    u_state 1.0
    pause 0
    repeat


transform Ghelly(color=(1.0, 0.38, 0.69, 1.8), inverse=0.0):
    mesh True
    shader "MakeVisualNovels.Lucify"
    blend "normal"
    u_lucify_color color
    u_inverse inverse
    u_state 1.0
    pause 0
    repeat

transform LucifyDemo(color=(0.6, 0.8, 0.8, 1.0), inverse=0.0):
    mesh True
    shader "MakeVisualNovels.Lucify"
    blend "normal"
    u_lucify_color color
    u_inverse inverse
    u_state 0.0
    pause 1.0
    linear 1.0 u_state 1.0
    pause 1.0
    linear 1.0 u_inverse 1.0
    pause 1.0
    linear 1.0 u_state 0.0
    repeat