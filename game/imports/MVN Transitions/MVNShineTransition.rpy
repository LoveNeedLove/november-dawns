init python:
    soft_dissolve_vars = """
    uniform float u_progress;
    uniform float u_softness;
    uniform sampler2D tex0;
    uniform sampler2D u_map;
    varying vec2 v_tex_coord;
    attribute vec2 a_tex_coord;
"""

    soft_dissolve_fragmentShow = """
    vec4 base = texture2D(tex0, v_tex_coord);
    float map_val = 1.0 - texture2D(u_map, v_tex_coord).r;

    float edge0 = u_progress - u_softness;
    float edge1 = u_progress + u_softness;

    float mask = smoothstep(edge0, edge1, map_val);
    float inv = 1.0 - mask;

    gl_FragColor = vec4(base.rgb * inv, base.a * inv);
"""

    soft_dissolve_fragmentHide = """
    vec4 base = texture2D(tex0, v_tex_coord);
    float map_val = 1.0 - texture2D(u_map, v_tex_coord).r;

    float edge0 = u_progress - u_softness;
    float edge1 = u_progress + u_softness;

    float mask = smoothstep(edge0, edge1, map_val);

    gl_FragColor = vec4(base.rgb * mask, base.a * mask);
"""

    renpy.register_shader(
    "MakeVisualNovels.SoftDissolveShow",
    variables=soft_dissolve_vars,
    vertex_300="v_tex_coord = a_tex_coord;",
    fragment_300=soft_dissolve_fragmentShow,
)

    renpy.register_shader(
    "MakeVisualNovels.SoftDissolveHide",
    variables=soft_dissolve_vars,
    vertex_300="v_tex_coord = a_tex_coord;",
    fragment_300=soft_dissolve_fragmentHide,
)


