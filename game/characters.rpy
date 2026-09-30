init -1:  
    define e = Character("Eileen")
    
    define narrator = Character(None, what_italic=True, what_color="#242323")
    define m = Character("Maj")
    define f = Character("Fransk",color="#b14b4b", image= "fransk")
    define l = Character("Lou",color="#dba100", image= "lou")
    define s = Character("Stheno",color="#08ecce", image= "stheno")
    define p = Character("Pani",color="#4bb159", image= "pani")
    define v = Character("Carmille",color="#4b5ab1", image= "carmille")
    define c = Character("Cassie",color="#a84bb1", image= "cassie")
    define k = Character("Kid",color="#242020", image= "kid")
    define a = Character("Agent",color="#91555d", image= "agent")
    define d = Character("Cassie's Dad",color="#b14b4b", image= "cassies_dad")


    $ config.tag_layer["Carmille"] = "front_sprites"

init python:
    chara_list = [m,f,l,s,p,v,c,k,a,d]
    for char in chara_list:
        config.tag_layer[char.name.lower()] = "front_sprites"
