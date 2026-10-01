define narrator = BlipCharacter(None, what_italic=True, what_color="#242323",
    voice=BlipVoice("audio/bleep_reg.wav", pitch=1.1, volume=0.6, frequency=3, pitch_var=0.05))

define m = BlipCharacter("Maj",
    voice=BlipVoice("audio/bleep_reg.wav", pitch=1.0, volume=0.6, frequency=2))

define f = BlipCharacter("Fransk", color="#b14b4b", image="fransk",
    voice=BlipVoice("audio/bleep_reg.wav", pitch=0.8, volume=0.6, frequency=2))

define l = BlipCharacter("Lou", color="#dba100", image="lou",
    voice=BlipVoice("audio/bleep_reg.wav", pitch=1.25, volume=0.6, frequency=2))

define s = BlipCharacter("Stheno", color="#08ecce", image="stheno",
    voice=BlipVoice("audio/bleep_reg.wav", pitch=0.9, volume=0.55, frequency=3, pitch_var=0.05))

define p = BlipCharacter("Pani", color="#4bb159", image="pani",
    voice=BlipVoice("audio/bleep_reg.wav", pitch=1.5, volume=0.6, frequency=2))

define v = BlipCharacter("Carmille", color="#4b5ab1", image="carmille",
    voice=BlipVoice("audio/bleep_reg.wav", pitch=0.85, volume=0.6, frequency=2, pitch_var=0.06))

define c = BlipCharacter("Cassie", color="#a84bb1", image="cassie",
    voice=BlipVoice("audio/bleep_reg.wav", pitch=1.35, volume=0.6, frequency=2))

define k = BlipCharacter("Kid", color="#242020", image="kid",
    voice=BlipVoice("audio/bleep_reg.wav", pitch=1.8, volume=0.55, frequency=1, min_interval=0.05, pitch_var=0.1))

define a = BlipCharacter("Agent", color="#91555d", image="agent",
    voice=BlipVoice("audio/bleep_reg.wav", pitch=0.65, volume=0.5, frequency=3, pitch_var=0.04))

define d = BlipCharacter("Cassie's Dad", color="#b14b4b", image="cassies_dad",
    voice=BlipVoice("audio/bleep_reg.wav", pitch=0.7, volume=0.6, frequency=2))

init python:
    chara_list = [m,f,l,s,p,v,c,k,a,d]
    for char in chara_list:
        config.tag_layer[char.name.lower()] = "front_sprites"
    
