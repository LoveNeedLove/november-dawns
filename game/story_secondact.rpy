# ==============================================================================
# ACTE 2 : HISTOIRE NARRATIVE ET CONTRE-INTERROGATOIRES
# ==============================================================================

# --- SCÈNE 1 : DÉCOUVERTE DU SECRET DE LOU ET ACCORD ---

label scene_lou_werewolf_discovery:

    "..."

    m "Lou?"
    m "Is that... you?"

    "Why does he... look... like this?"

    m "Do you need any-"
    l "Get OUT!"
    f "Maj! Let me handle this."
    m "!"

    "{b}*SLAM!*{/b}"

    m "Franks... you saw that, he-"
    f "Lou is gonna be fine."
    f "He just needs some rest."
    m "That's not what I was talking about, he-"
    f "He's just Lou, ok?!"
    f "Don't get any id-"
    l "It's alright, Fransk."
    f "!"
    l "Maj... I can't explain what you saw, but I'm trying to do the right thing by locking myself up."
    l "Please, I beg you, don't tell anyone!"
    m "Lou..."
    l "I'll explain everything. I swear."
    m "Did you know, Fransk?"
    f "..."
    m "Look, I'm aware that I'm the new guy. But you gotta trust me!"
    f "Trust you?"
    f "What the hell, it's not like I can do anything to shut you up."
    f "Maj, we're a team now."
    m "A team?"
    f "Yup, I'll stay up in my room while you ensure that nobody gets bored."
    f "Once the party's over or Lou gets better, I'll make sure to tell you everything."
    f "Deal?"
    m "Sounds good to me."
    f "Don't worry about him, I'll watch over him from my room, I really need some rest."
    l "Before that, could you make sure I'm locked up? I can't trust myself to stay here."
    f "Don't worry bro, I have a key to the bathroom, you won't even be able to open the door from the inside when I use this!"
    l "Thanks!"
    m "Welp, I'll go join the others."
    f "Thanks. I'll close the door right behind you."

    "Each step feels like an eternity, and yet, there'll never be enough time for me to grasp what just happened."
    "Lou... was..."
    "Lou... is..."
    
    $ R_livingRoom.cutscene = "scene_living_room_return"
    call travel_to(R_livingRoom)
    return


# --- SCÈNE 2 : RETOUR AU SALON ET ÉPISODE DE LA BÂCHE ---

label scene_living_room_return:

    s "HOW'S LOU, ASSHOLE!"
    m "Ah!"
    v "Is he okay? Can we come check on him?"
    m "Right now Lou... is resting up. The chase almost made him faint."
    s "The fuck? He's supposed to be a quarterback!"
    c "We shouldn't have fucked with him that much Sthen... he was probably stressed or suffering from nicotine withdrawal..."
    s "Ugh..."
    s "Nicotine withdrawal...?"
    s "We gotta get this bitch to stop!"
    v "Stheno you have to calm down a bit..."
    v "Let's get us some drinks shall we?"
    c "Yeah! We could even go to the garden if you want!"
    p "And maybe have a smoke of our own..."
    s "Abby, you better make me another one of those cocktails."
    m "Yeah, sure!"
    c "I'll put on some music!"

    "Spending time with people sure is nice, but I can't help but shake that image of Lou out of my mind."
    "Those eyes..."

    call travel_to( R_kitchen,in_dialogue = True)
    s "You're gonna mix my drink forever or what!"
    m "!"
    s "Stop zoning out, man."
    m "S-sorry. Your cocktail's ready..."
    s "...Sure bro."
    m "*siiiiiigh*"
    p "You okay?"
    m "Huh? Yeah. I just have to go to the bathroom; I think?"
    p "Carm's in there I think. And I have to go too..."
    m "Drinks are getting to our bladders, huh?"
    p "Just go before me bro, you're acting weird as hell lmaooo."
    m "... yeah thanks."

    v "Going in?"
    m "Yeah..."
    v "Let's join up in the garden, fresh air will do us all some good!"
    m "Fine by me."

    "{i}*shut!*{/i}"
    call travel_to( R_F1bathroom,in_dialogue = True)

    "When life's too much to bear... pissing is always here to give you a break... break..."
    "..."
    "..."
    "...............!!!!!!"
    "Urgh! I really gotta go and join the others! Staying alone isn't great for my mental stability."

    "{i}*washhhhhhhhhh* *close!*{/i}"
    "{i}*open*{/i}"
    call travel_to(  R_entryHallway,in_dialogue = True)
    m "Ah! Pani!"
    p "Fuckk you're finally doneee, LET ME IN!"

    "{b}*SLAM!*{/b}"
    

    "...I feel bad for taking her turn. Now to the garden..."
    call travel_to( R_garden,in_dialogue = True)
    m "Huh, this looks nice!"
    v "Hey Maj! Over here!"
    m "Hey, is it okay for us to sit here? These couches are covered by tarp..."
    v "Eh, I'm sure it's okay."
    c "Did Pani go to the bathroom?"
    m "Yup, she couldn't wait for me to get out."
    c "Same for me, I'll go wait my turn."
    m "Sure!"
    s "So... what was up with Lou?"
    m "Lou?"
    v "Does nicotine withdrawal even do that?"
    v "Maybe it's his lungs that got fucked up from all the smoking?"
    s "I mean... could be? But it really fucking sucks, college football is pretty much all he's got going for him, too bad he's cooked."
    m "Isn't he also like... super smart?"
    s "Books have been with him all his life, but there's no money in that. If he doesn't get scouted soon his bum ass is sleeping on the streets for sure."
    m "...that's kinda mean."
    s "Well who the fuck asked you?"
    v "I'm sure Lou's gonna be fine! Everyone gets a bit winded out every once in a while."
    s "If you say so, Carm..."
    v "So, Maj, you're gonna pursue sociology?"
    m "Yeah, I guess I want to understand people better sometimes..."
    v "I get that! We're probably going to end up in the same class."
    m "You're also studying it?"
    v "Yup, same reason as you."
    m "Really? Why?"
    v "When I was smaller, I had this bad... condition. Which really got me stuck at home."
    v "Most of the time I was doing the chores and studying by myself."
    v "Once I earned my high school diploma, I decided enough was enough, and I'd go out and face the world."
    m "How'd you deal with the sickness?"
    v "I found a method-"
    s "*snicker* Wait 'till you see it."
    m "?"
    v "Anyways, for the first time I met people my age and was able to go out with them."
    v "That summer went well but I really sucked at social interactions!"
    v "So I figured, if I want to make more friends, I gotta study people."
    v "So I go-"

    p "'Sup guys."
    s "Hey! Pani!"
    v "I was just telling Maj abo-"
    p "What the hell are you sitting on?"
    s "? on the sofa."
    p "You fucking morons, the tarp's there to protect the fabric!"
    s "Yeah?"
    p "The friction with the tarp can really ruin it! You either sit directly on it or sit someplace else!"
    s "Fuck you... it's comfy as hell."
    v "Sthen..."

    "Carm's stare speaks for itself..."

    p "Are you aware of your insolence?"
    s "My what? Say that again?"
    p "This couch is worth at least 10 thousand dollars! I won't let you damage it!"
    s "It's their fault for buying this piece of shit for that much."
    p "YOU DON'T UNDERSTAND!"
    v "Sthen! Please! Let's comply! You know how much Pani cares about these things!"
    s "Nah."
    p "So you choose to die on this hill..."
    v "Let's just take the tarp to the garage, it'll take a second."

    "They're all so... intense."

    m "Stheno..."
    s "What was that, Abby?"
    m "I-"
    m "..."
    m "Let's just remove the fucking tarp, no need to make a scene."
    s "Fine, jeez yall are such fucking goody two-shoes."
    p "Yayyyyyy :)"
    s "So, where do we put this?"
    v "I remember Fransk storing them in the garage, there's 4 pieces so we should be able to make it in one trip!"
    m "Sure."  

    $ R_garage.cutscene = "scene_phones_missing_pani_faint"

    return


# --- SCÈNE 3 : LES TÉLÉPHONES DISPARUS ET L'ÉVANOUISSEMENT DE PANI ---

label scene_phones_missing_pani_faint:

    m "Is here okay?"
    s "Probably..."
    v "What are you looking for Sthen?"
    s "It's just... this basket..."
    v "What's up with it?"
    m "Isn't that the one where Fransk collected our phones?"
    s "Yeah..."
    m "Okay?"
    s "Just... Why is it empty?"
    m "?"

    "She's right, there's no phone to be seen."

    c "What are yall doing in the garage?"
    m "We couldn't find the phones. Could you check the living room?"
    c "Sure, I'm already there."

    s "What the hell?"
    s "{i}*rummage rummage rummage*{/i}"
    s "Where's my fucking phone?!"
    v "Fransk must've put them somewhere, no?"
    s "But when? and where?"
    p "Guys..."
    v "Maybe there's another basket just like it? Then it could be in the kitchen."
    s "Kitchen? Got it."
    call travel_to( R_kitchen,in_dialogue = True)
    s "{i}*rummage rummage rummage*{/i}"
    v "Any signs?"
    s "Help me look, asshole!"
    v "I'll check a few closets..."
    p "Sink."
    m "Right..."

    "By the looks of it there's no sign of any baskets, or phones for that matter."

    s "Fuck! Where is it!"
    p "{i}*poooooooour*{/i}"
    s "I need my fucking phone!"
    p "{i}*GLUG GLUG GLUG*{/i}"
    s "I can't even afford a new one."
    p "{i}*pouuuuuuuuuuur*{/i}"
    s "I've got like, so many apps and shit on it!"
    p "{i}*GLUG GLUG GLUG GLUG GLUG*{/i}"
    s "WOULD YOU STOP FUCKING DRINKING?"
    p "Sorry Sthen..."
    p "I just..."
    s "?"
    p "I just don't... feel... Sthen..."
    s "Pani, you okay?"
    p "don't... feel...."
    p "..."
    p "{b}*SLAM!*{/b}"
    v "Pani!"
    s "What the fuck?"

    "Shit! I have to check her pulse!"
    "... Okay."
    "She's breathing... but definitely unconscious."

    m "She's breathing... but definitely unconscious."
    s "How the fuck...?"
    c "Is she alright?"
    m "I don't know, she just fainted out of nowhere!"
    c "What? Like Lou?"
    m "!"

    "Could she also be... like... Him? ... No!"

    m "Lou didn't faint! This could be the alcohol."
    v "But Pani's so used to drinking... she wouldn't be wasted that soon."
    m "I guess?"
    v "Wait... what is this?"
    m "?"
    v "Next to the empty trashcan she just toppled, something's shining!"

    "Without even hesitating Stheno starts rummaging through the trash."

    s "Are you talking about this?"
    c "What's that?"
    s "A piece of aluminium... Something's written, Nyc... Nyctozepam?"
    c "Is that some kind of medicine?"
    m "I... I know about it!"
    m "It's like a super strong sedative for people who have debilitating insomnia."
    s "Insomnia?"
    m "Yeah, it can knock out an adult of average weight in approximately 15 minutes when ingested."
    s "15? That's can't be real."
    v "This is probably unrelated to this accident, she must've fainted, not fallen asleep."
    p "{i}*SNOOOOOOOOORE*{/i}"
    c "..."
    v "..."
    m "... She's definitely sleeping."
    v "We have to figure out what happened."
    m "Right."
    $ eventMgr.add_event(QuickEvent("pani_faint",{"talk_carmille_investigation_pani","talk_stheno_investigation_pani", "talk_cassie_investigation_pani"},"cx_pani_poisoning"))

    return


# --- CONTRE-INTERROGATOIRE : QUI A DROGUÉ PANI ? ---


label cx_pani_poisoning:

    m "... Doesn't seem like there's anything left to check."
    v "There could be clues in the living room."
    m "I don't think so, her drink was clearly roofied."
    c "Roofied?"
    s "That's fucking crazy! None of us could do it."
    m "The facts seem to coincide. I'm sorry Stheno."
    s "Sorry? Yeah, you're goddamn right to be sorry!"
    m "Excuse me?"
    s "You're the only one that could've done it!"

    $ current_cx = CrossExamination([
        Statement(s, "Pani's our best friend, you're the only one that could've done it."),
        Statement(s, "You probably drugged her before she went to the bathroom.",
                correct_evidence_id="bathroom_order",
                contradiction_label="cx_pani_objection_success"),
        Statement(s, "We're so lucky that you apparently know everything about that drug, how convenient!"),
        Statement(s, "Taking the lead in the research is the best way to conceal valuable information!")
    ])

    $ in_cross_examination = True
    $ cx_index = 0
    jump cx_display


label cx_pani_objection_success:
    m "Could I have? I don't think so."
    s "What do you mean?"
    m "Think about the window of opportunity. She had her eyes on the drink the whole time."
    s "Yeah? But she did go to the bathroom, didn't she?"
    m "Yes, but by the time I even got close to her glass you and Carm were already sitting in the garden."
    s "... You're right."
    m "?"

    "Is she being... reasonable?"

    s "Before going to the bathroom she handed me her glass, you wouldn't have had a chance to reach it."
    m "Or you would've killed me?"
    s "Exactly."
    m "Then... could anyone have done it?"

    call menu_choice_loop("Let's think... Who would've had the opportunity?",
    [    
        "Stheno",
        "Carmille",
        "Cassie",
        "None of them"],
        3
    )



label choice_none_of_them_success:

    "... This goes against everything we claimed up to this point, but it's the only answer that makes sense."

    m "None of us could've done it."
    s "?"
    c "What!?"
    v "I see, could she have done it to herself?"
    m "No, she wouldn't have any reason to do it. The drug just straight up knocks you out."
    v "In 15 minutes, right?"
    m "Yeah, if you're of average weight, which seems to be Pani's case."
    s "Damn right it is, fat shaming is not allowed!"

    "We're missing something, the key to this whole entire situation."

    p "{i}*SNOOOOOOOOOOOOOORE*{/i}"
    v "At least the drug's working..."
    c "She didn't sign up to be a test subject."
    s "Hey, new guy, are you sure you're not mistaken?"
    m "How so?"
    s "Maybe you have the wrong medication in mind, it wouldn't be a stretch to say that you mistook those pills for another kind."
    m "... Could I have?"

    "You could not. You know them all too well."

    m "!"
    s "Realize something?"
    m "I'm not mistaken."
    s "Are you really?"
    m "It was featured in one of the online courses. I promise."
    "Liar."
    v "Then what are we missing? I'm sure we covered everything..."
    c "Maybe we made some false assumptions?"
    "Carm is right, things aren't always as obvious as they may seem..."
    

    call menu_choice_loop("I think we need to take a deeper look at...",
    [    
        "The drug's delivery",
        "The drink",
        "Pani's Weight",
        "Time for the medication to take effect"],
        2
    )


label choice_pani_weight_success:

    m "..."
    m "The drug's onset of action could've been delayed."
    s "How so?"
    m "If Pani's weight is significantly superior to that of the average person..."
    s "What the fuck are you saying?!"
    c "That's really offensive, Maj!"
    m "I- But it could widen the timeframe where the medication could've been taken!"
    c "Yeah but Pani is a beautiful, totally thin, smoking hot young woman!"
    m "People can be that AND heavy."
    v "Dude... you're not looking good in this debate."
    m "I... Let's just try and pick her up!"
    s "You're not getting your hands anywhere near her, asshole!"
    s "Look, I can lift her mys-"
    m "?"
    s "Urggggggg......!"
    s "What the hell?"
    s "GRRRRRRRRRRRRRRRRR"
    s "She... she won't budge!"
    s "GRrrrrrRAAAAAAAAAAAAAAAAAAAAAAH"
    p "{i}*SNOOOOOORE*{/i}"
    s "I- I used all of my strength..."
    c "What the hell are you talking about, girl?"
    s "Try it! You take the legs, I take the arms."
    c "Sure"
    c "{i}*RAAAAAAAAAAAAAAAAAAAAAAAH*{/i}"
    m "They're giving it their all, huh..."
    v "If you were right then I don't know what to say to you bro..."
    m "H-Holy shit, she's barely moving."
    "{b}*RAAAAAAAAAAAAAAAAAAAAAAAAH*{/b}"
    v "Guys! You're lifting her up a bit! Keep going!"
    "{i}*clatter*{/i}"
    m "What was that sound?"
    s "PUT HER DOWN MY ARMS ARE ABOUT TO TEAR!"
    "{b}*THUD!*{/b}"
    c "Is she okay?!"
    p "{i}*SNOOOOOOOOOOORE*{/i}"
    s "Alright."
    c "Maybe it's her weird dress that's weighing her up? I couldn't get a grip on her legs."
    m "I just heard a noise when you lifted her up... Wait, what is this?"

    "Is that a small little cardboard box under Pani?"

    m "Ny... Nyctozepam!"
    s "What?"
    m "She must've had it on her this whole time!"
    s "What the fuck?!"
    m "The tab's missing two pills, quick get that piece of aluminum!"
    s "On it!"
    m "Look... it perfectly matches one of the empty slots!"
    s "Then... Did she do this to herself?"
    v "She was probably chasing a high... and with her weight thought that she needed something with an extra kick."
    "So we're just calling her heavy now?"
    s "All it did was send her to sleep a bit later, what a fucking idiot."
    m "What?"
    s "*snicker* BAHAHAHAHAHAHAHAHAHA, that stupid fucking junkie."
    m "Don't call her that!"
    s "She's so fucking pathetic, coming to a party with fucking drugs, it's like she hates being with us *snicker*"
    m "SHUT UP!"
    s "?"
    m "Stop doing this! She literally fainted, it could've been terrible."
    s "This?"
    m "Yeah! We just fucking met and you've constantly been belittling everyone's feelings and struggles, you're a fucking pain to be around!"
    v "Maj..."
    m "What? Y'all always pretend like it's nothing, but there's nothing that hurts more than this kind of childish behavior."
    s "Who the fuck are you to judge me, asshole?"
    m "Maybe you should treat your friends better instead of insulting them."
    s "You're saying I don't care?"
    m "I'm saying you're showing your love and worry in the worst way possible, stop acting so selfish and be honest with yourself."
    s "I'm gonna knock you the fuck out little bitch!"
    v "Sthen, Maj, STOP IT!"
    m "!"
    m "!"
    v "Lou and Pani are doing awful, this is not the time for this kind of shit."
    m "...you're right."
    s "Tsk."
    v "Maj, give me the medication, I'll put it back in her pocket."
    s "Let me do it, bitch. You're not allowed to touch her."
    v "Sure."

    "The way she acts... I know it's out of worry but she's not considerate enough..."

    s "What the shit ?!"
    v "What is it again?"
    s "She... She... h-her dress!"
    c "Is something wrong?"
    "{b}*THUD*{/b}"
    "What could've made her recoil like that?"
    s "It's... her ass..."
    c "?"
    s "It's hairy as hell!"
    c "That's kinda mean, Stheno."
    s "No... check it out!"
    c "Alright..."

    "Cassie kneels to undo the bottom of Pani's dress."

    c "She always hides her legs like this, but she shouldn't go to these lengths if they're just kinda hairy."
    s "..."
    c "Remove the knot here, remove this there..."
    c "Pull this right over... push this right under..."
    c "Cut this part out..."
    c "And there you g-"
    c "!"
    c "What the hell!!!"
    m "What's wrong Cass-"

    "And then I saw them. Under that dress. Two. ... A pair of... Hooves."

    m "!"
    v "Cassie! Hide them!"
    c "Shit!"
    "She re-does the bottom of the dress to the best of her abilities, but it's way too late."
    c "I- I can't!"
    m "What the fuck is going on?"
    c "Is she... a monster?"
    v "What should we do?! The government is known to track them!"
    m "...Them?"
    v "Yeah! Rumors were going around about monsters but I didn't know that Pani was one!"
    c "Should we call the police?"
    s "We can't."
    c "What?!"
    s "We can't, that would put Pani in danger."
    c "..."
    s "We have to protect her, no matter what."
    s "Because we're friends."
    v "..."

    "Monsters... they're real? Lou... and now Pani. There's no mistaking it, they are not human. They're..."

    s "Maj!"
    m "!"
    s "Snap out of it! Are you keeping the secret or not?"
    m "I-"
    s "Maj!"
    m "I will! I will."
    s "Good, then we're all agreeing?"
    m "Yeah, I need to tell Fransk about everything."
    v "Go do that, we'll try to lay her down somewhere safe."
    c "Yup, three oughta be enough to do it."
    m "Okay."

    "... What is going on here? Fucking monsters? How is that making sense?"

    $ R_F1hallway.cutscene = "scene_fransk_first_murder"
    return


# --- SCÈNE 4 : DISCUSSION AVEC LOU ET PREMIER MEURTRE DE FRANSK ---

label scene_fransk_first_murder:

    l "Hey Maj!"
    m "Lou?"
    l "Is something going on?"
    m "...Yeah, Pani fainted."
    l "What? How?"
    m "She mistook some drugs, sleeping pills."
    l "Fuck... How did Fransk react?"
    m "Fransk? He's still in his room no?"
    l "What? I'm sure he passed in front of the door."
    m "How so?"
    l "Nothing much, just smelled him briefly."
    "Smelled..."
    m "Lou... did you know about Pani?"
    l "What's with Pani?"
    m "She's... like you."
    l "What? I'm not a fucking junkie like her! She's not like me at all!"
    m "No, you don't get it."
    l "?"
    m "She's also... part... animal?"
    l "!"
    l "What?! She's... one of us?"
    m "Her feet, in their stead were... hooves, like that of a horse."
    l "A horse... so she's not like me!"
    m "?"
    l "I'm closer to a dog, you see?"
    m "A... dog?"
    l "How did you see her feet? She took off her weird dress? Or maybe watched the full moon?"
    m "Stenho kinda felt her ass when searching for her pocket..."
    l "What?! Felt her ass? What the fuck were y'all doing down there!"
    m "She was just trying to put back the meds!"
    l "I see... Well, to answer your question, I didn't know!"
    m "Really?"
    l "She always smelled a bit funky but I just assumed it was the herbs you know!"
    "What kind of conversation is this..."
    l "Now that you say so it's true that she always smelled like hay. I always thought it was the drugs but maybe she's a centaur or something!"
    m "How can you say that so casually?"
    m "Just suggesting that she's a monster!"
    m "It... it's not possible, this has to be a prank!"
    l "Hey Maj, listen."
    m "!"
    l "When you see me again, I'll be back to normal."
    l "But please don't get mistaken, we all have something to hide."
    l "For me... it's a whole other form, for her, it's some weird Satyr legs."
    l "People might do their best to be human, but when cracks start to show..."
    m "You're scared too."
    l "Of monsters? Of course!"
    m "That's why you locked yourself in the toilet?"
    l "Bro. You saw me, I won't pretend otherwise."
    m "..."
    l "Not even I can tell what I'm capable of, the full moon gives me energy that even I can't control!"
    l "So yeah, maybe it's fear, I guess I fear myself."
    l "But what I fear the most is hurting those around me!"
    "... Would a monster really say that?"

    m "... Thanks Lou."
    l "? For what."
    m "I don't know... A part of me needed to hear that."
    l "I see... Well, I can't wait to see you when I'm better!"
    m "Sure. Maybe you'll teach me about books or the NFL."
    l "You have no idea..."
    l "Oh, yeah! Go tell Fransk about the whole Pani situation, he'll handle it!"
    m "Allright!"

    "Fransk told me he needed to rest, I have no choice but to wake him up now."
    call travel_to( R_F1fransksRoom, in_dialogue = True)

    m "Fransk you have to know abou-!"

    "What... Fransk? ... ... ? ... ..."

    "{b}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!{/b}"
    call travel_to( R_entryHallway,in_dialogue = True)
    c "Maj?"
    m "Guys! GUYS!"
    c "Why are you screaming?"
    m "It's Fransk, he's... he's fucking injured or dead!"
    c "?"
    s "What do you mean?"
    m "Come up!"
    "{i}*rattle* *rattle* *rattle* *rattle*{/i}"
    m "It's locked? Wasn't it just open?"
    v "There's like a pad for a code here."
    l "You guys okay?"
    m "Lou! It's Fransk, he's... he's..."
    "{i}*rattle* *rattle* *rattle*{/i}"
    m "F-FUCK, OPEN UP"
    v "Try Fransk's birthday, it's 08-30-03"
    "{i}*beep beep boop beep* *BEEEEEP*{/i}"
    m "That's... that's not it!"
    s "Slow down! What's happening!"
    m "I- I went to get Fransk but when I opened... there... there was... blood, everywhere! And he... he..."
    s "Breathe!"
    v "Okay, we trust you, just stay here with Cassie."
    v "I'll go check the living room shelf for birthdays and potential passcodes."
    s "There's a window to his room in the garden. I'll try to climb or reach it in some way."
    m "...thanks..."

    "What is going on..."
    c "Are you okay?"
    "How did he..."
    l "Is he alright?"
    c "He's kinda out of it."
    "Is this my fault?"
    c "Can't remember his mom's birthday?"
    l "When did he get that bouquet?"
    "How... how... how... did I end up here again..."

    v "Maj! It took a while but I have some birthday dates!"
    m "Huh?"
    v "When searching through the library I found his parents' old passports!"
    c "It's been fifteen fucking minutes so I hope the passcode's in there."
    v "Let's try! Now!"
    "{i}*BEEEEEEP* *BEEEEEEEEP*{/i}"
    m "Fuck ! One more wrong try and the alarm rings!"
    v "I- I'll go get Stheno!"
    m "..."
    c "Please, Maj, don't panic."
    m "..."
    "It's over..."
    l "Maj, Cass, step down please."
    m "!"
    c "Lou, your voice is clearer!"
    l "I unlocked myself, but there's also a code on this side, so I have to kick it down."
    c "Kick it down? This door looks fucking heavy dude."
    l "Just, step away. Please."
    c "...Okay."

    "What is he doing... can he really do it?"
    "{b}*CRAAAACK*{/b}"

    m "!"
    l "...This is me now."
    m "Lou!"
    l "I'm stronger in this form... Now let's check on Fransk. We have no time to lose."
    v "We're ba-AAAAAAAAACK!"
    s "Lou! What the hell! Are you some kind of werewolf?"
    l "DOG, I'm a WERE-DOG. Not some kind of wild animal!"
    s "...okay?"
    l "Now let's check on Fransk!"
    v "He's right... there's no time to lose."
    call travel_to( R_F1hallway, in_dialogue = True)

    "You're not strong enough. You can't open this door. What waits beyond. Is stronger than us."
    "Shut-up... Stop following me..."
    "You can't do it."
    "Stop... Stop talking.... Stop. Stop. Fransk needs us."
    "Does he ? You're nothing but a-"

    m "SHUT UP!"

    "In one fell swing. I open the door."
    call travel_to(R_F1fransksRoom,in_dialogue = True)

    v "!"
    l "No! No! NOOOOOO!"
    c "There's no way!"
    s "Who... who the fuck... did this?"

    "A bloodbath... but something's wrong."

    m "It changed."
    s "What?"
    m "The room... it changed, it's different from before!"
    s "What are you talking about!"
    m "The blood... the body... things are way different!"
    s "What the fuck?"
    m "Someone manipulated the crime scene..."
    c "Do we call the police?"
    s "Maybe if we had a phone. And I won't call them while Lou looks like... that."
    c "...Yeah, that's fair enough."
    m "Let's investigate..."

    $ eventMgr.add_event(QuickEvent("first_fransk_investigation",{"hotspot_investigation_body","hotspot_investigation_carpet", "hotspot_investigation_dreamcatchers","hotspot_investigation_closet","hotspot_investigation_window_living","hotspot_investigation_window_garden","talk_carmille_investigation_murder","talk_lou_investigation_murder","talk_stheno_investigation_murder"},"scene_confronting_cassie_ghost"))

    return


# --- CONFRONTATION CASSIE ET LE SECRET DU FANTÔME ---


label scene_confronting_cassie_ghost:

    m "Let's step out for a bit, I've looked at everything I can..."
    l "Yeah, good idea."
    call travel_to( R_F1hallway,in_dialogue = True)
    l "Any more places you wanna check?"
    m "Not really..."
    l "Alright bro... ... Huh?"
    m "What is it?"
    l "HEY CASS!"
    c "Don't fucking scream like that!"
    l "Sorry... Aren't you gonna look? You're more clever than any of us, I'm sure you'd notice something we missed."
    c "Sorry... I can't..."
    m "Is the blood too much to bear?"
    c "Y-Yea, that's right..."
    l "What!? You used to love those true crime videos, they were borderline gore, bro!"
    m "Lou! This isn't some random stranger's blood we're talking about!"
    l "Yeah sure but I remember her talking about becoming a detective and loving forensics or something..."
    m "Maybe she changed her mind!"
    c "I didn't! They just didn't have the right courses for that here!"
    l "Then help us figure it out!"
    c "Ugh...."

    "Something's wrong, she clearly can't push herself to enter the room... Blood doesn't seem to bother her... and yet..."

    m "Was Fransk special to you?"
    l "What, no! Never!"
    c "Why are you answering that question for me!"
    l "Sorry! I just know what he liked, and you're not even close to his standards..."
    c "You womanizing-"
    m "Then you're a prime suspect."
    c "!"
    l "What! Her? No way! She never enters his room anyway!"
    m "Really?"
    l "Yeah even this morning while we were preparing things!"
    m "Still, you're the only one without an alibi. You went to the bathroom last, and we all had eyes on each other."
    l "She'd never do something like th-"
    c "Let me answer! Bad boy!"
    l "! I- NO I'M NOT A BAD BOYYYYY!"
    c "He's right though, not only would I never do such a thing!"
    m "Why?"
    c "I just..."

    "She's definitely hiding something..."
    

    call menu_choice_loop("The reason she's staying here is...",
    [    
        "She couldn't have entered the room",
        "She stabbed him",
        "She's hemophobic",
        "She's homophobic"],
        0
    )


label choice_cassie_cant_enter_success:

    m "The way you're acting... You're hiding something."
    c "?! N-No!"
    m "Okay then, enter Fransk's room please."
    c "I won't! The blood's too much."
    m "Put on a blindfold, I'll guide you."
    c "!"
    m "It's not that you're not willing, it's like you can't even enter the room!"
    c "..."
    m "The reason you can't enter is because of..."

    call force_present_proof("dreamcatchers")
    jump choice_dreamcatchers_success

label choice_dreamcatchers_success:

    m "Those dreamcatchers in Fransk's room..."
    c "!"
    m "Lou said that you were always scared to enter his room, right?"
    c "..."
    m "Then this seems like the only logical explanation."
    l "Does she have a fear of trinkets or something?"
    m "No... she's just sensible to that kind of stuff."
    c "!"
    m "You're not a regular human... right?"
    c "I'm just scared of entering a boy's room!"
    m "Sure, then you won't mind if Lou brings one of the dreamcatchers over here then."
    c "!"
    l "I can do that, if you want, he even had spares in his..."
    c "Don't! Alright? Don't!"
    m "... Tell us the truth."
    c "I'm... a ghost, a wandering soul..."
    l "What!"
    c "I roam around this world to take revenge for the life that I lost..."
    l "N-No way!"
    m "..."
    c "My spirit is contained inside this necklace I wear... I only took possession of this body to lead the student life I always dreamed of!"
    l "DID YOU TAKE IT FROM THE REAL CASSANDRA?"
    c "No, Cassie is my name. This girl forfeited her life to the god of the dead... I merely took what she was willing to live behind..."
    l "...H, How long?"
    c "22 years."
    l "?"
    c "I adorned the shape of a child. Desperate parents with no hope of having children quickly adopted me."
    l "!"
    c "I've always been your friend Lou. I'm not an evil spirit!"
    m "... That's unbelievable."
    l "But that explains everything!"
    c "?"
    l "Her B.O!"
    m "Body odor?"
    l "Yeah! She only ever smelled like vanilla lotion and shampoo!"
    c "You're right, as a spirit I have no distinctive smell."
    m "What exactly are you taking revenge on exactly?"
    c "!"
    m "Studying architecture might be a little bit peaceful for a vengeful spirit."
    c "My life was robbed away from me during my life as a political activist."
    m "!"
    c "The government had me assassinated! All I ever wanted was to gain access to proper education!"
    l "A suffragette ghost! That's fucking awesome!"
    m "...Alright, at least that clears things up... you're a ghost... that stole some baby's body... to get educated..."
    c "That sums it up quite well."
    m "..."
    l "Are you alright Maj? Aside from discovering that there's an afterlife."
    m "I had a feeling that more of us weren't human, but this just confirms it..."
    l "What?!"
    m "Something about the way they all reacted to you and Pani's identity. It was more of a light shock than actual life changing information."
    l "...Really?"
    m "Even Carm and Sthen, the way they're avoiding to call the police really makes it seem like it's an issue they've thought about multiple times..."
    l "I see/"
    m "And then there's the government thing."
    l "A regular person would quickly dismiss these rumors, but the only kind of people who would take them seriously would be..."
    m "Monsters themselves."
    l "... Maj, I can't speak for the others but please, don't call the police!"
    m "I won't, some of you are clearly innocent. But when factoring in supernatural abilities..."
    l "You're saying that one of us could've done it."
    m "..."
    l "Maj, there's still that mysterious smell! As long as another party is still involved, I can't allow you to investigate our friends about their personal secrets."
    m "... You're right, but there's something I must make sure of."
    l "? Yeah?"
    m "That smell, it only appeared once, right?"
    l "Yeah, it appeared- Wait..."
    m "If your sense of smell didn't betray you, that grassy guy entered Fransk's room, and then what?"
    l "!"
    m "If they didn't exit through the hall, or leave through the window..."
    l "Then they probably used a supernatural way to escape!"
    m "That's right. And I must figure that out. For now, let's gather up everyone in the living room."
    
    $ R_livingRoom.cutscene = "cx_murder_scent_investigation"
    call travel_to( R_F1hallway)

    return


# --- CONTRE-INTERROGATOIRE : L'INTRUS ET L'ODEUR D'HERBE ---

label cx_murder_scent_investigation:

    m "Thanks for joining me everyone."
    v "So, figure anything out?"
    m "I want to hear your theories, if we can reach a consensus then we might find the murderer."
    "I have to keep their potential abilities in mind. Stheno and Carmille are still human, but considering the fact that 3 of them have lied already then I can't be too sure."

    $ current_cx = CrossExamination([
        Statement(v, "Fransk was probably murdered during one of his naps."),
        Statement(l, "The murderer is potentially an outsider."),
        Statement(l, "They had this distinct smell of grass, and headed towards Fransk's room."),
        Statement(s, "They probably opened the door, and stabbed poor Fransk in the stomach.",
                correct_evidence_id="smell_order",
                contradiction_label="cx_smell_order_success"),
        Statement(v, "Now all that's left to figure out is their escape route!")
    ])

    $ in_cross_examination = True
    $ cx_index = 0
    jump cx_display


label cx_smell_order_success:
    m "This couldn't have happened."
    l "What! It makes sense to me!"
    m "If you simply recall the scent's order then the contradiction will reveal itself."
    l "First the grassy guy... then Fransk... Wait a minute!"
    m "Exactly, Fransk wouldn't have just gone to sleep with a killer in his midst. His room didn't have any hiding spots."
    c "Was Fransk waiting for the killer to join him up? Then he wouldn't have been surprised by their presence."
    m "No, I don't believe this is the case."
    c "Why?"
    m "Lou recalled having smelled Fransk's scent only a few moments after the grassy smelling suspect."
    c "Yeah, so?"
    m "I believe that Lou didn't smell Fransk's odor going to his room, but rather down the stairs."
    c "What, then that would mean... the person who came down the stairs was..."
    

    call menu_choice_loop("The person who came down was...",
    [    
        "Fransk himself",
        "The murderer",
        "The grassy guy",
        "Lou's mistake"],
        1
    )


label choice_the_murderer_stairs_success:

    m "The person Lou must've smelled at the time was probably the murderer themselves."
    l "No, I can't let you say that!"
    m "?"
    l "Someone covered their scent using Fransk's blood? Is that what you're affirming?"
    m "Could be their blood or any piece of clothing."
    l "Then you're forgetting something, where does that leave the lawn smelling figure?"
    m "..."

    "I must have some proof laying around. Let's think about it."

    call force_present_proof("garden_window")
    jump choice_garden_window_success


label choice_garden_window_success:

    m "Lou smelled the guy that smelled like grass first, which was soon followed by the smell of Fransk."
    m "If we think about that set-up for an instant, then the full image starts to appear."
    m "And it all starts with the garden window."
    l "Ah! I see what you mean!"
    m "It was obviously locked from the inside, which means that the person who locked it..."
    l "Must've remained inside..."
    m "If you pair that with the disappearance of our herby fellow..."
    v "Then they must've escaped to the garden!"
    l "Otherwise I would've smelled their grassy ass..."
    m "Leaving only one person, who smelled like the victim."
    c "Then the grassy guy could've also done it, no? Assuming that they escaped from the garden. The Fransk smelling individual could easily have been an accomplice, or someone else entirely."
    m "I admit that it is possible... but the window definitely proves that they've co-operated in some way."
    s "The Fransk smelling dude probably was the one to alter the crime scene, no?"
    l "No way, Maj discovered the body way after that, and he'd have seen them when he entered the room."
    m "Something's bothering me... How did the Fransk smelling guy even get up there?"
    c "I know! The both of them worked together, right? Grassy could've easily opened the window and reeled Fake Fransk from the garden using a rope or blanket!"
    m "This would require one of them to access the garden in the first place... which would've been difficult when considering the fact that we were all in its general idea."
    m "I could easily imagine someone escaping from the window while we were putting the tarp in the garage, but that whole stratagem seems highly unlikely."
    c "Then how did they get there?"
    

    call menu_choice_loop("How did they get there?",
    [    
        "The stairs",
        "The garden",
        "A secret passageway",
        "Using a special ability"],
        0
    )


label choice_stairs_again_success:

    m "Let's keep it simple, they used the stairs again."
    s "What! There's no way!"
    v "I have to agree with Stheno here, they could've disguised their smell as Fransk on the way down, but I would've picked up on SOMETHING on their way up, even Cassie slightly smells like shampoo!"

    "Is there a way to hide your smell from Lou's snout?"

    call force_present_proof("lous_jacket")
    jump choice_lous_jacket_success


label choice_lous_jacket_success:

    m "Lou, can you smell yourself?"
    l "What? I mean... I always do! So it just gets in the way mostly!"
    m "Then... What if they wore your jacket while going up?"
    l "That... THAT WOULD TOTALLY WOOOOORK!"
    s "Isn't his jacket in this living room?"
    l "Nope, during investigation we found it deep inside Fransk's closet."
    v "The time surrounding Lou's transformation was quite chaotic... Anyone could've picked the jacket without anybody noticing."
    m "Yeah, but to devise that plan you needed to be aware of Lou's weakness."
    v "Sure, that's just plain logi- ! ... What you're saying is-"
    m "Anyone here could've done it..."
    l "!"
    s "!"
    c "!"
    m "The person that smells like grass could've done it, they could've been the murderer. The one to actually stab Fransk."
    m "But someone close to the victim, someone that could've had access to Lou's jacket was at the very least an accomplice, no, even a mastermind."
    l "...This is crazy!"
    m "That individual is in our midst, that I'm sure of."
    s "...You fucking-"
    "{b}*SLAM*{/b}"
    v "Stheno!"

    "That punch just came out of nowhere!"

    s "I'm going to fucking KILL YOU asshole!"
    s "We're friends! We wouldn't fucking do this to each other!"
    m "..."
    c "Stheno, you have to calm down!"
    c "He actually backed up his claims, if you can prove him wrong, then I'm begging you to do so!"
    s "!"
    v "I don't want to doubt us! We've known each other forever! But the jacket being found up there can only mean that one of us was involved!"
    s "N-No! It can't be!"
    l "If you have anything to say against that! Then please, please say it!"
    s "..."
    c "Yeah, you can do it Sthen!"
    v "I know you can!"
    m "You punch hard... but I need to hear it, I deeply want to be wrong! Where's the contradiction?"
    s "Th-There's.... There's tha- There's... ... Hold on, I need to get my thoughts straight. ... ... ...! There's... none."
    l "..."
    c "Sh-shit!"
    v "There actually is."
    m "!"
    v "The shuffle. You came down after finding the body, Grassy was in the garden or gone somewhere, and \"the one\" that did it was back amongst us."
    m "...Yes."
    v "Then who could've disguised the scene? The only one that had access at the time was Lou, right?"
    l "Me!?"
    c "No, it can't be! We were actively talking to each other from underneath the doors, I can guarantee that he stayed in the upstairs bathroom!"
    l "Yeah, I was going to mention that, thanks Cassie!"
    v "So, we're back to square one?"
    m "No, we aren't. What you said just makes a ton of sense. The shuffle could only have happened when the doors were locked."
    v "Lou could've unlocked the door himself, no? It would also reframe our entire point of view."
    l "No, Fransk locked me up with a key, the only way I could open the door was by destroying the door."
    m "And when I checked up on him the lock was still in place."
    l "I only destroyed it to get to Cassie and Maj!"
    v "So this confirms the timeframe for the shuffling of the room?"
    m "Yes, and now it's only a matter of alibis. When considering the state of the room... as well as the search for the passcode."

    call menu_choice_loop("The culprit can only be...",
    [    
        "Stheno",
        "Carmille",
        "Lou",
        "Cassie"],
        1
    )


label choice_carmille_culprit_success:

    m "It's you, Carmille, Isn't it?"
    v "That's..."
    s "You're forgetting something! Carmille was in the living room! With no access whatsoever to Fransk's room!"
    m "I'd beg to differ, this qualifies as a passageway!"

    call force_present_proof("living_room_window")
    jump choice_window_living_room_carmille_success


label choice_window_living_room_carmille_success:

    m "This window could've been used to reach Fransk's room!"
    s "Are you fucking mad?! Not only was it CLOSED, but it's also way out of reach for a runt like him!"
    m "Not when you factor in his special ability."
    s "Special abilities?"
    c "That's fucking unfair! If we're considering those then Stenho can also be scrutinised! What if she's a monster that phases through widows or shit! Then she's just as sus as Carm is!"
    m "The living room window was opened sometime after Fransk died, this leaves the living room window as the most likely entryway."
    c "Yeah, but Stenho not only could've opened it she also could've pretended to make it locke-"
    v "That's not what Stenho's power does!"
    m "!"
    c "!"
    s "Carm!"
    l "You... Did you just confirm that she has an ability?"
    v "So what if I did? She couldn't have gone through the window, so let's review the facts..."
    "Carm... I can tell what you're doing."
    m "This clears it up, Stheno couldn't have done it, this only leaves-"
    s "What about the others? Yall could be hiding shit from us."
    m "Lou's just some kind of beefed up man with extra hair, Pani's knocked out and Cassie can't even enter Fransk's room."
    s "What's that about Cassie?"
    c "I'm a ghost... tied to this necklace."
    s "What?!"
    c "I can get out of my body by removing it, but as an incorporeal spirit that wouldn't do much..."
    m "Face it Sthen, Carm's the only one left."
    s "Well he couldn't have done it! His ability can't make him go through windows!"
    m "Then what abilities does he have!"
    s "As if I can tell you that!"
    m "Then we have no choice but to get other parties involved! This isn't the time to protect each other!"
    s "Shut the fuck up you-"
    v "I'm a vampire."
    m "!"
    s "Carm, no!"
    m "...Is that true?"
    v "Yes, it is. A bloodsucking, nefarious vampire..."
    s "Carm..."
    m "...This explains your \"illness\"."
    v "Yes, the sun's harmful to me."
    m "And this gives you a clear motive for doing this to Fransk."
    v "Sucking his blood, I suppose you're right."
    m "And this also explains how you could open the window."
    v "Nice try, but I disagree. Vampires don't have reflections, that doesn't mean we can go through walls."
    m "..."
    v "We also don't possess any telekinetic powers, so opening the window is out of the realm of possibility."
    m "!"

    "I see what you're doing... You want me to prove your guilt without the shadow of a doubt... I didn't get much time with you. But let me honor your wish!"

    m "You can fly, can't you?"
    v "Yes, but in the form of a bat. As far as I'm aware bats do not possess hands, so tilting the window is impossible for me."
    m "Yeah, sure it isn't. I'll put an end to this masquerade."

    call menu_choice_loop("You could've opened it easily using...",
    [    
        "Your mouth",
        "Your wings",
        "Echolocation",
        "Your feet"],
        0
    )

label choice_bat_mouth_success:

    m "..."
    m "By biting down on the handle, and using your wings as leverage, you could've easily opened it."
    v "..."
    m "All you had to do was let yourself fall while making sure to avoid the shelf, and then just fly again through the opening. Am I right?"
    v "So you-"
    s "There's no proof that he accomplished that!"
    v "Sthen..."
    s "You're just making this shit up as you go."
    v "Please..."
    s "Stop begging! You can't shut me up! I know you're innocent."
    v "... Maj..."
    m "On it. The proof that implicates Carmille is:"

    call force_present_proof("living_room_window")
    jump choice_window_proof_carmille_success


label choice_window_proof_carmille_success:

    m "If he did in fact bite down on the handle... then we should find bite marks on the handle."
    s "What of it? Who's to say they weren't there before?"
    m "There's still more."
    s "!"

    call menu_choice_loop("Something about this window confirms my theory...",
    [    
        "Bite marks",
        "Bat hair",
        "Faulty Handle",
        "It stayed open"],
        3
    )


label choice_window_stayed_open_success:

    m "The most damning evidence is the fact that we found this window in an open state."
    m "Had they tried not to be found, the perpetrator would've simply closed it."
    m "But the fact remains, it was open."
    s "!"
    m "This can only mean one thing, the window was used to enter Fransk's room! And the culprit was unable to close it on his way out. Carmille is the only plausible suspect."
    s "N-No! He can't be!"
    v "Stop it Sthen."
    m "!"
    v "You got it all figured out Maj."
    s "Carmille..."
    v "Truth is, I wasn't supposed to come here tonight. But Fransk really insisted that I should come."
    v "\"We have to welcome the new guy!\" he said."
    v "\"But... I'm supposed to feast tonight, if I don't go to the bloodbank, then I could lose control!' I answered."
    m "So why come?"
    v "He sent me pictures of blood sacks, three of them. He explicitly said that he kept them for me."
    m "Wait, was he aware-"
    v "Yes, he knew about my true nature..."
    l "He knew about you as well..."
    v "When I heard Maj scream, my blood boiled. I had found a way to quench my thirst, without shedding blood."
    s "If you told us we could've looked for the sacks with you! You didn't need to get involved!"
    v "...I waited for Sthen to get to the garden, then simply transformed to open the window."
    v "I clamped down on the handle, and used my wings to shift my weight in a way that granted me acess."
    l "*sniffle*"
    v "The rest is a blur... I simply remember waking up to that... horror. ..."
    v "You saw it too Maj, so much blood... it even made a leech like me sick to the stomach..."
    v "I used a black piece of cloth to try to restore Fransk's dignity... Rolled up the carpet and hid it behind the closet."
    v "Then simply made my way out the way I came in, without leaving a trace. ... That's it, that's the whole ordeal."
    m "So Fransk was already dead when you came in?"
    v "...I think so."
    c "Th-That could be a lie."
    m "No, I don't think so. Aside from the timing, something's clearly bothering me."
    c "And what is that?"
    m "The wound. You wouldn't need to stab him just to drain his blood."
    l "Right!"
    s "So... was this all for nothing? You're telling me the murderer AND his potential accomplice are still around?"
    m "No! Carm saw the crime scene from inside! He could give us some useful information!"
    v "R-Right! I'm sorry for lying to you all, but I'm now realising that I couldn't have possibly committed the murder!"
    l "Yeah... it makes sense. I'm willing to look past that."
    s "You blood sucking whore! You won't ever hear the end of it let me tell you!"
    s "I know you'd never hurt Fransk, I'm sure you just did what needed to be done."
    v "Guys... I don't know what to say..."
    m "From now on, you have to be truthful, let's get to the bottom of th-"

    jump scene_carmille_death
    return


# --- SCÈNE 5 : LA MORT DE CARMILLE ---

label scene_carmille_death:

    "IT IS NOW TIME FOR THE SECOND TRAITOR TO RECEIVE HIS PUNISHMENT"
    m "?"
    "MAY THE LIGHT PUT AN END TO ENDLESS SLAUGHTER!"
    l "The hell is this?"

    # (the lights turn purple)
    v "AAAAAAAH"
    v "THIS LIGHT! MY SKIN! IT BURNS!"
    l "Sh-Shit! Get him some shade!"
    s "DON'T GET UNDER THE COUCH DUMBASS, LIGHT CAN GET DOWN THERE!"
    c "Carm! Try to go out!"
    call travel_to( R_entryHallway,in_dialogue = True)
    "{i}*rattle rattle rattle*{/i}"
    s "Who locked the front fucking door?!"
    v "Th-The closet! I have my special hoodie in there!"
    s "GO GET IT!"
    m "Wait, isn't that closet locked too-"
    "{i}*open*{/i}"
    m "!"

    "Since when has it been unlocked?"

    s "I see it!"
    "{b}*THUNK*{/b}"
    v "AAAAAAAAAAAAAAH"
    c "What the fuck!"
    l "His skin's it's... sizzling!"
    s "G-Garlic! It's garlic!"
    v "RAAAAAAAARGH!"
    s "I'll get it off! AAAACK IT BURNS! FUCK IT! GRAAAAAAAARGH"
    "{b}*RIP*{/b}"
    m "!"
    s "HIS SKIN'S COMING OFF WITH IT! ... SH-SHIT, HE'S LOSING CONSCIOUSNESS!"
    v "Sthen..."
    s "CARM, WE'LL GET YOU SOME SHADE! I'LL CARRY YOU TO THE GARDEN!"
    v "Tell Fransk... I'm... I'm sorry..."
    s "CARM! HANG ON!"
    v "Sorry, for being... such a..."
    s "CARM!!!"
    v "Coward."

    "Dust. It's like there's already nothing left of him. Just, dust."

    s "Why?! He didn't deserve to die! *sobs*"
    c "Carmille..."
    s "Don't leave me Carm... *sobs*"
    m "...I can't believe it..."
    s "Don't leave me alone..."
    l "What the hell... just... happened?"
    s "WHYYYYYYYYYYY?!"
    m "Ugh!"

    "It's like I can't stop them. I barely knew him... but it doesn't matter to my tears. They just keep on coming."

    m "FUCK!"
    s "NOOOOOOOOO!"

    "The others are still bottling up their feelings, but it seems that Stenho's and mine have fused into an oasis of sorrow."

    l "Sh-Shit! I can't c-cry, not now! I can't... I just *THUD* *sob sob sob*"
    c "Carmille! *sob*"

    "Our tears flowing only mean one thing. They've never been closer to drying. And once the last tear is shed, so will be the mask that hides the truth."
    "..."
    "..."
    "..."

    p "Guys?"
    m "!"
    p "Did something happen?"
    s "Pani, you're awake!"
    l "Hey... it's me."
    p "Lou! Holy shit you're so puppy coded I love youuuuuu *rub rub rub rub*"
    c "Pani... this isn't the time..."
    p "Oh shit really? My bad"
    l "KEEP GOING!"
    p "Oki puppyyy *rub rub rub rub rub rub rub rub*"
    s "Pans."
    p "'Sup?"
    s "Fransk... and Carm... they're dead...."
    p "...for real?"
    m "Yeah, Fransk was murdered while you were unconscious, and Carm... ..."

    "The words are stuck in my throat!"

    s "He was killed by this fucked up trap..."
    p "I see..."
    c "We're sorry to drop it all on you like that, it must seem unbelievable."
    p "Okay, yall need a smoke."
    c "What?"
    p "Come on kiddies, toodle-oo. Follow me to the garden!"
    m "Sure... I could use the fresh air..."

    $ R_garden.cutscene = "scene_garden_smoke_break"
    return


# --- SCÈNE 6 : LE JARDIN, LE SOUVENIR ET LE MESSAGE DU SHED ---

label scene_garden_smoke_break:

    "The autumn breeze brushes up against my cheek... Nothing has ever felt more real than this."

    s "You really brought a blunt? You'll never fail to surprise me."
    p "Y'all need to relax, we'll just pass the joint around."

    "The smell of weed rises through the air. I've never smoked, but I know this odor all to well."

    p "Here Lou, take a puff."
    l "Fuck... Why not."
    "{i}*INHAAAAALE*{/i}"
    s "Don't hold it in! That doesn't do anything!"
    "{i}*PFEEEEEEEEEEEW*{/i}"
    l "I really needed that shit, you go Sthen."
    s "Give me that."

    "...Didn't think we'd be doing a rotation after what happened."

    s "Take it Cass."
    "{i}*PFFFFF* *PHEW*{/i}"
    s "Fuck! Carm's fucking dead!"
    c "Sthen..."
    s "I can't believe this shit..."
    l "Remember how much we used to fuck with him because of his weird ass hoodie? Can't believe he died looking for it."
    s "And he gave ME his last fucking words, I can't even pass them on to Fransk!"
    m "I don't know, maybe we can use Cassie as a messenger."
    p "The hell's that supposed to mean?"
    m "We didn't tell you? She's a ghost apparently."
    c "Shut the fuck up and take your turn asshat!"

    "Looks like it's my turn."

    m "I never smoked before... my dad would've buried me alive if he found out."
    l "This a religion thing?"
    m "It's more of a \"him having control over my every action\" thing."
    p "Then fuck him. Take an extra big hit."
    "{i}*HUFFFFFFFFFF*{/i}"
    "Huh, the taste's kinda... strange?"
    "{i}*PFEEEEEEW*{/i}"
    m "Holy shit this sucks, hahahahahaha"
    s "Pffffff, the fuck you laughing for."
    m "I don't fucking know *snickers*"
    l "WEWEWEWEEWEWE"
    s "The fuck kinda laugh is that?! HAHAHAHAHAHAHA"

    "...Could it be the drugs? Or just an irrepressible need to let it all out? I don't think I'll ever know the answer, but what I know is that letting it out it feels really fucking great."

    l "Fuck... fuck... I haven't laughed that hard since..."
    p "Since?"
    l "Since integration week with Fransk."
    c "Yeah, that was fun..."
    m "When was it?"
    l "Around 3 months ago, the school sent us pamphlets about this camping trip to get us acquainted."
    l "We ended up being the only ones going, some of us already knew each other, but that whole trip really cemented us as a friend group."
    m "Damn, makes me wish I was there..."
    s "Fuck no, that trip sucked already!"
    l "There was this one activity, night-time scavenge hunt, the organizers split us up into pairs and we had to take pictures of random shit spread around the forest."
    p "Issue being that it was super fucking dark outside and that the forset was notorious for being a natural maze."
    s "At the time I kept complaining, but Carm was nice enough to put up with my bullshit."
    s "We were lost in the forest when a big ass boar came out of fucking nowhere."
    s "That's when I showed Carm my ability..."
    m "I see... that's how he knew."
    s "To thank me for saving his ass he transformed into a bat and scouted for a way back."
    l "We actually all managed to find our way home by following the sound of Stheno's complaints."
    s "We never completed the scavenge hunt, but decided to call it quits and light up the campfire without the camp counselors knowing."
    p "We started a rotation just like this one lmao. Remember Fransk's impression of Lou? That shit was FRYING me."
    l "With the fucking shirt he stole? I could never forget that..."
    s "I barely knew anyone at the time, with me coming from another town and shit... But I can't believe that they're gone, those two have always been the most dependable of the bunch... ... Pass it."
    l "Sure sorry. I've known Fransk forever, so now I'm pretty much lost. I just wish I had shared my secret with y'all earlier you know? Just to lighten the burden on Fransk."
    s "Take it, Cass. What do you mean by that, Lou?"
    l "Fransk had his problems, you know? With his parents never being here, the nightmares and shit."
    l "He even had this fucking phobia of electricity, which didn't make it all that easy for him to live alone."
    l "But despite all of these hardships he always did his best to accommodate me and my \"needs\"."
    c "Yeah, he was pretty selfless..."
    l "Remember when he improvised a whole ass presentation to bail you out in high school?"
    c "Yeah... That was the first time we met too... I had forgotten to do the assignment and was panicking and he just gave me his notes and slides... When his turn came he just got up and acted out the geopolitical intricacies of the cold war..."
    l "Can't believe he got a passing grade with that bullshit, he even did a stupid ass russian accent."
    c "I really can't believe he's - SHIT!"
    s "What the hell did you just call him?"
    c "It's not that! Pani's cheap ass joint just broke down all over my skirt!"
    p "It's not cheap, you just let it smolder for too long without removing the ash..."
    l "There's a sink in the shed if you want."
    c "Yeah, sure, show me."
    p "I'm coming too, I need to clean the drool off my face..."
    l "Gross."
    s "..."

    "There they go... Wait, don't leave me alone with Stheno!"

    s "Hey, about earlier..."
    m "What's up?"
    s "I'm sorry for getting pissy, I can be an ass sometimes."
    m "..."
    s "I'm not too keen on meeting new people, guess I picked up on that during my years of living in hiding."
    m "I get it, you're keeping your guard up."
    s "Yeah... but I let that go too far, I can see that you're more chill then expected."
    m "Truth is, I never took what you said to heart. I could tell that you acted this way to protect yourself. I just don't like it when you berate others."
    s "You're making me sound like an asshole or something."
    m "You're more of an edgelord, like Shadow the Hedgehog."
    s "The fuck did you just say?"
    m "Sorry, it's a nerdy video game thi-"
    s "I FUCKING LOVE SONIC."
    m "For real? Which one is your favorite?"
    s "It's not that popular but it's Sonic Rush..."
    m "I fucking love that game!"
    s "Really!"
    m "I spent weeks trying to beat Blaze 'cause I couldn't mash fast enough."
    s "HA- You fucking suck-"

    c "Guys?"
    m "Is everything okay?"
    c "Sorry to interrupt but you have to check something out."
    m "?"
    c "It's in the shed, follow me."

    "What could be hiding in there?"

    c "Right here, on the wall."
    m "What the-"

    "{b}THE WEIGHT OF YOUR SINS WILL RAIN UPON YOUR HEADS.{/b}"

    m "Who the fuck wrote that?!"
    l "It wasn't written this morning, that's for sure."
    p "The paint's already drying, it must've been written approximately 2 hours ago."
    m "2 hours? So I was already here..."
    c "Weren't we playing that icebreaker game back then? None of us could've really done it..."
    "Could it be...!"
    m "There must be some hidden way to access the garden from outside. We would've noticed someone coming in during the icebreaker."
    l "This fence is quite high... there's no way som- ..."
    m "Weren't you saying something?"
    l "{i}*sniff sniff sniff sniff sniff sniff sniff*{/i}"
    "His snout twitching is kind of adorable."
    l "Here, behind the shed... there's a particular smell... Yeah! Right here!"
    m "Is that... a hole?!"
    l "Yeah, it seems like there's a small hole in the fence, small enough for something like a dog to go through, but any adult would definitely get stuck... A kid could fit though."
    "My hunch might just be correct!"
    l "More than that. This hole really stinks!"
    m "Stinks? Like what?"
    l "Like... freshly cut lawn or something like that..."
    m "!"
    l "Is something wrong?"
    m "Does the smell resemble the one in the hall?"
    l "! Now that you say it!"
    "Is that kid involved in Fransk's murder?"
    m "We have to investigate again, Carm mentioned that he hid something behind the closet. I also want to figure out why the front doors wouldn't open."

    $ eventMgr.add_event(QuickEvent("second_murder",{"hotspot_bookshelf_rope","hotspot_fatal_closet","hotspot_bloody_carpet_found","hotspot_black_cloth_recheck"}),"stheno_scream")
    return


# --- SCÈNE 7 : LE PIÈGE DE LA CUISINE ET LA RENCONTRE DANS LE FREEZER ---
#EVENT HERE



label stheno_scream:
    s "WHAT THE FUCK?!"
    l "What's going on?"
    m "Was that Stheno? We should get to the kitchen as soon as possible."
    $ R_kitchen.cutscene = "scene_kitchen_door_locked_chase"
    $ eventMgr.add_event(QuickEvent("kid_found",{"hotspot_garage_car","hotspot_garage_caulk_gun)"},"fin_garage_investigation"))
    return

label scene_kitchen_door_locked_chase:
    s "Fuck! Shit!"
    l "Is everything alright?"
    s "The fucking door to the garden's shut. We're stuck!"
    l "How's that even possible?"
    s "Look, the lock's completely covered with... glue?"
    l "I don't know, this looks more like plaster to me..."
    m "Whoever's locking the doors must've used this mixture to fix the doors shut."
    l "Nah, that'd be dumb, if I were this guy I'd probably put it in the locks directly, that would make it almost impossible to enter a key."
    m "That's clever, but why didn't they do it here?"
    l "That's obvious, the door to the garden doesn't really have a key, it's like a simple bathroom lock."
    m "And this is the only way to get to the garden?"
    l "Yeah."
    m "! If this lock can only be accessed from the inside, then it means that whoever just did this-"
    l "Should've also locked themselves!"
    m "Shit, they can exit through Fransk's window!"
    l "We were just there! They're probably close!"
    m "Let's check out the house!"
    s "I'll stay here, if the motherfucker tries to get upstairs then I'll catch their ass."
    return

#EVENT HERE
label fin_garage_investigation:
    l "That asshole's really in the garage?'"
    m "Yeah, he probably locked the kitchen door while everyone was busy investigating the trap and shit."
    l "The garage's pretty small... we should be able to catch him quick- ... *sniff sniff sniff sniff sniff sniff* No way!"
    m "Did you find something?"
    l "Dude, we have to get him out of there NOW! That's dangerous as hell!"
    m "What?"

    "Lou rushes to open... the freezer?"

    l "HEY LITTLE GUY! THIS COULD KILL YOU!"
    k "{i}*brrrrrrrrrr*{/i}"
    m "! This kid!"
    l "What, you know him?"
    k "{i}*clack clack clack clack clack*{/i}"
    m "He's the one that rang earlier... a trick-or-treater..."
    l "WHAT ARE YOU DOING IN HERE, KID?!"
    k "How'd you know my name?"
    l "What? Kid?"
    k "Yeah!"
    l "Uh, lucky guess?"
    k "Woa! Your costume is awesome!"
    l "Huh?"
    k "Mister werewolf! You look great! How did you get the teeth right?"
    l "It's uuuh... my job?"
    k "Wow! You must be a crazy dentist or something!"
    l "Yeah, yeah, that's it..."

    "Lou got so comfortable with us that he forgot about hiding his identity..."

    m "What are you doing here? I told you we don't have any candy."
    k "*whistle*"
    m "!"
    "This kid's ignoring me!"
    l "Answer him, child! Or the big bad wolf will devour you!"
    m "What happened to you being a dog?"
    k "HAHAHAHA, I like you wolfie! I'm here to pull out an insane trick!"
    m "A trick?"
    k "But I won't tell youuuu, *blblblblblblblbl*!"
    m "Guess I'll just show you then. The nature of your trick!"

    jump cx_kid_interrogation



# --- CONTRE-INTERROGATOIRE : LE TOUR DU GAMIN ET LE TÉMOIGNAGE ---

label cx_kid_interrogation:

    call force_present_proof("tied_up_shelf")
    jump choice_kid_shelf_trick_success


label choice_kid_shelf_trick_success:

    m "This rope was set up around the time where we were all gathered in the garden."
    k "!"
    m "It must be the \"trick\" you were talking about..."
    k "Can I go? You're boring..."
    m "?"
    k "The rope's not part of the trick, silly! It's like a red hero!"
    m "... You mean... red herring?"
    k "Yeah, that! Like my English teacher told me!"
    l "Using rope to mislead us? That's-"
    m "A lie. The rope was always part of your plan."

    call force_present_proof("shed_message")
    jump choice_shed_message_success


label choice_shed_message_success:

    m "\"THE WEIGHT OF YOUR SINS WILL RAIN UPON YOUR HEADS.\" Quite the dramatic way of saying you'll slam a bookshelf down on the ground..."
    k "You saw that?! My prank idea's awesome isn't it! I knew I had to do it when I saw that HUUUUGE bookshelf after sneaking in!"
    m "You little..."
    k "I entered the house when you were all playing that stupid game. I planned to find a hiding spot but ended up finding a perfect tool for a perfect trick!"
    m "..."
    l "What the hell are kids up to nowadays?"
    m "Tell me. How did you enter the house in the first place?"
    k "! *whistleeee*"
    m "No need to tell me. I know."

    call force_present_proof("garden_hole")
    jump choice_hole_in_garden_success


label choice_hole_in_garden_success:

    m "You found the hole in the fence, right?"
    k "! Sherlock Holmes?!"
    l "Wait, the hole?"
    m "Have you tried smelling him Lou? I had my suspicions but it would pretty much confirm it."
    l "Suspicions? *sniff* What could a kid like him even do? *sniff* It's no lik- ! ...No way! That smell!"
    m "Freshly cut lawn, right?"
    l "Yeah but not just that... his shoes... they reek of..."
    m "?"
    l "Fransk..."
    m "!"

    "Is this kid...?"

    m "Kid, you gotta tell us."
    k "Whut?"
    m "Did you pull any other tricks tonight?"
    k "Huh?"
    m "Like... upstairs?"
    k "Nuh huh! I didn't!"
    m "But you-"
    k "STOP BOTHERING ME! MEANIE!"
    m "It's just tha-"
    k "I'll just go now!"

    "This kid's running away!"
    l "This little- He just sneaked between my legs!"
    m "Let's chase him!"

    s "GET BACK HERE LITTLE FUCKER!"
    l "He's already in the hall! Stheno and Cassie must've failed to catch him..."
    call travel_to( R_entryHallway,in_dialogue = True)
    s "I'M GONNA GET YOUR LITTLE-"
    l "Hey Sthen, is everything okay?"
    s "! ... H-How?!"
    l "Yeah, that kid's fast as hell."
    m "We better get up soon before he unfastens the lock in Fransk's window."
    s "T-This doesn't make any sense?"
    m "What?"
    s "L-look!"

    "She points at the stairs, her face pale livid as can be."
    l "Did the kid get h- !"
    "This shouldn't be possible."

    # [Illu de Fransk debout]
    l "F-FRANSK?!"
    f "...What the fuck happened here?"
    s "Y-you had a fucking hole in your chest! How are you... even alive!?"
    f "...Lou? You chose to come out of the bathroom? Good for you man!"
    c "Fransk!"
    p "Yo! You missed the blunt rotation!"
    f "Sorry guys, I have some explanations to give yall..."
    m "... I'm... so glad!"
    l "You're back... *sob*"

    "This is nothing short of a miracle, I can't believe he's alive!"

    f "I'm a monster. Like the rest of you, well... except for Maj."
    m "! You knew about everyone?"
    f "Pretty much, I'm great at keeping secrets, aren't I? Anyways... I won't get into the details but I almost died when I was like 3, and my mom sewed me back up with her sciency bullshit."
    c "T-This whole time? You were also a monster?"
    f "Sorry for hiding this to you guys, but unlike y'all I don't have any abilities... It's more of a disability in fact..."
    m "Carm mentioned an IV..."
    f "Yeah there's this drawer under my mattress. The issue with my body is that I can't really sleep or make new blood cells. So my blood just kinda... spoils."
    s "Fucking ew."
    f "Yeah... every few hours I get super tired and have to inject myself with new blood."
    s "That explains the blood pouch pictures you sent to Carm!"
    f "? Yeah? He didn't really know about my condition."

    "Obviously... a vampire wouldn't willingly feed on rotten blood."

    f "Anyways, what the fuck happened to me in my sleep? I must've dozed off like fucking crazy."
    m "You were kinda... stabbed. Right in the torso. You lost so much blood..."
    f "Fuck, really! Then that explains everything."
    m "?"
    f "My heart beats thanks to a sort of pacemaker, it's super sensitive to current but without it blood wouldn't get to my body."
    l "I see! That's why you're always so scared of getting shocked!"
    f "Yeah, that could legit kill me."
    l "Then how did you get revived?"
    f "Simple, the IV kept pumping new blood into my system, the stabbing just flushed out the old stuff!"

    "The stabbing's one part, but Carm definitely took out the rest..."

    c "That was said so casually..."
    f "My body's made of various corpse parts, they kinda just soak up blood... It's not really comparable to a regular person's body. When they get new blood they just tend to... regenerate?"
    c "So... as long as your heart beats you're just kind of immortal?"
    f "Technically?"

    "No special abilities, my ass!"

    f "Where's Carm? I wanna see the guy!"
    c "!"
    l "..."
    m "Carm is..."
    s "Carm died."
    f "What?!"
    s "Someone knew about his identity and set up a fucked up trap using garlic."
    f "...Wh-What?! Carm? Carm's dead? How!?"
    l "We don't know... we heard this weird announcement, then the light turned fucking purple and he just started panicking-"
    f "Lights!? FUCK! FUCK FUCK FUCK! CARM!"
    m "Calm dow-"

    "And there he goes, rushing up the stairs."
    m "I'll go get-"

    "TRAITOR, TIME TO PAY FOR YOUR LIES"
    m "! This sound!"
    "MAY THE SPARK OF SIN PUT AN END TO YOURS"
    m "Fransk! Wait"
    call travel_to( R_F1hallway,in_dialogue = True)

    # [Entry hall cinématique]
    m "DON'T OPEN THE DOOR"
    "{i}*clack* *ZZAAAAAAAAAAPPPP*{/i}"
    f "GRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH"
    "{b}*THUD*{/b}"
    m "FRANSK!"
    f "My chest... hurts... My heart...!"
    m "Shut up! I know CPR, the others will get you some help!"
    f "... Tell Carm... No... He's dead..."
    m "1, 2, 3, 4. Stay with me! CALL AN AMBULANCE! 1, 2, 3, 4."
    f "I get why... she'd do that."
    m "1, 2, 3, 4."
    f "Mom... shouldn't have made me that way..."
    m "1, 2, 3, 4. Don't say that! 1, 2, 3, 4."
    f "Tell her I'm sorry... and that I wish I could've given her what she wanted..."
    m "You were more than enough! You didn't ask to be like this!"
    f "..."
    m "1, 2, 3, 4. 1, 2, 3, 4. 1, 2, 3, 4. 1, 2, 3, 4."
    p "Maj."
    m "1, 2, 3, 4."
    p "It's over."
    m "1, 2, 3, 4."
    p "Maj, his body..."
    m "1, 2, 3, 4. I'M MAKING HIS HEART BEAT! 1, 2, 3, 4."
    p "The seams..."
    m "1, 2, 3, 4."
    p "They're broken Maj..."
    m "1... 2..."

    "She was right... performing CPR on a disembodied torso isn't going to save anyo- Isn't going to save- Isn't..."
    "{b}*THUD*{/b}"
    m "FUCK! FUCK! FUCK! FUCK!"
    c "Fransk... we just got him back too..."
    m "FUCK!"
    s "Maj, calm down! We have to end this cruel joke, and figure out who did this to him."
    m "But-"
    l "Maj."
    m "Lou..."
    l "I got this from his room."
    m "A blanket?"
    l "I'll cover his body to make sure he rests, you figure this out for him."
    m "I- I can't-"
    l "Starting with-"
    m "I'M TELLING YOU I CAN'T-"
    l "Starting with the reason that pushed him to run over here in the first place."
    m "!"
    l "I know you can do it. I'll join you as soon as I can, okay?"
    m "... He said something about the IV being in a hidden drawer?"
    l "Attaboy, you go look for clues."
    m "... Alright. ... Thanks for everything."
    l "You give your best to help us, it's only natural."
    m "..."

    "Just like that, gone again. Lou's right, I have to put an end to this myself."
    $ eventMgr.add_event(QuickEvent("kid_reveal",{"hotspot_fransk_bed_drawer","hotspot_electric_door_handle", "hotspot_parent_room_mom_nightstand", "hotspot_parent_room_dad_nightstand"},"final_investigation_end"))
    
    return


# --- CONTRE-INTERROGATOIRE : LE GAMIN ET LE TÉLÉPHONE RETROUVÉ ---

label final_investigation_end:
    s "I FINALLY GOT YOU, FUCKING BRAT!"
    l "Stheno's voice always had some crazy reach..."
    m "She must've caught the kid, let's go ask some questions... That shout came from the garage."
    $ R_garage.cutscene = "cx_kid_final_testimony"

label cx_kid_final_testimony:
    s "You fucking brat... I fucking hate running... I'll make you regret that..."
    k "BLBLBLBL I HATE YOU UGLY LADY!"
    s "Who are you calling ugly?!"
    m "Sthen! Leave him to us! That kid might've witnessed the stabbing!"
    s "... Aight, but that fucker won't talk."
    m "?"
    s "Just try."

    $ current_cx = CrossExamination([
        Statement(k, "BLBLBLBLBLBLBLBL"),
        Statement(k, "I won't talk to you meanies!"),
        Statement(k, "You're still cursed! You'll have to survive my trick!"),
        Statement(k, "You have no way of weaseling out of it!",
                correct_evidence_id="hard_candy",
                contradiction_label="cx_kid_candy_success")
    ])

    $ in_cross_examination = True
    $ cx_index = 0
    jump cx_display


label cx_kid_candy_success:

    m "You're tricking us because of the candy situation, right?"
    k "Of course, it's trick or treat after all!"
    m "Well, here's a treat for you."
    k "Really?!"
    l "HEY! Aren't those for me?"
    m "... We should be able to talk now, right? No need in keeping grudges."
    k "Okay *MUNCH MUNCH* What *MUNCH* do you *MUNCH* wanna know?"
    m "I-"
    k "*MUNCH*"
    m "... What happened to you up-"
    k "Wanna know how I planned to trick you?"
    m "With the shelf, right?"
    k "Yeah, but first I hid your phones!"
    s "WHAT? WHERE ARE THEY?"
    k "I found 'em in a basket and just dumped them out through that window. I was going to wait for one of them to ring before dropping the shelf to surprise you!"
    s "This window?! It's like the one in the living room! It barely fucking opens! Lou, come here!"
    l "What?"
    s "Use your lanky ass arms to reach for our phones! I know you can do it!"
    l "Sure... HUUUUUUUUUUUUUUUURG... Shit, they're way out of reach, Sthen!"
    s "Come on! You can do it! You're a good boy!"
    l "Am I? Really?"
    s "Yup, if you get the phones at least."
    l "RAAAAAAAAAAAAAAAAH"
    m "..."
    l "I GOT ONE!"
    s "YEAH YOU'RE THE BEST BOY!"
    l "I couldn't get the rest though..."
    m "At least we can use it to contact the authorities! Whose phone is it?"
    s "It's... Carm's."
    m "!"
    s "Damn, he got so used to us stealing his phone that he removed the password entirely..."
    m "Can I check it out?"
    s "Really? You're gonna nosy around Carm's phone now?"
    m "Not really, I wanna check his DMs with Fransk."
    s "Let me do it... It's about the blood thing, right? Let's see... Carm didn't lie. There's a picture with blood pouches on it, alongside some very insistent messages begging him to come over tonight."
    m "He wasn't lying..."
    s "I'll keep going... ! What the- "

    "Her face is turning red!"

    m "Did you find anything?"
    s "NOTHING IMPORTANT! NOT RELEVANT!"
    l "Can we see?"
    s "No! Trust me! It's private!"
    m "...Alright."
    s "I'll go join Pani and Cassie in the living room, I wanna hear their opinions before calling the police or anything."
    m "That makes sense."
    k "Can I go join Pani and Cassie too? I wanna play Subway Surfers on that phone!"
    m "No, we still have a few questions for you."
    k "Sure, I tied up the shelf usin-"
    m "What happened upstairs?"
    k "!"
    m "You went to Fransk's room earlier, right? What happened there."
    k "I didn't!"
    m "I see, you're lying. We only have to check this piece of evidence to make it obvious."

    
    call force_present_proof("bloody_carpet")
    jump choice_kid_bloody_carpet_success


label choice_kid_bloody_carpet_success:

    m "See these small shoe-prints?"
    k "Yeah?"
    m "Mind showing us your sneakers? I bet they'll look awfully similar."
    k "N-No!"
    l "Kid, please."
    k "?"
    l "Our friend almost died because of what happened. You have to tell us the truth."
    k "... Died? The zombie guy?"
    l "Yeah the tall one with the varsity jacket."
    k "! Died?!"
    "What's so shocking?"
    k "It wasn't a trick?!"
    m "? What do you mean?"
    k "The masked guy...I thought it was a trick when I saw it..."
    l "The Who?"
    m "! What?! When?"
    k "When he pretended to stab the one in the zombie costume."
    l "Maj, are you hearing this?"
    m "Could you recognize that person?!"
    k "No... Is the zombie guy really real? He wasn't a prop?"
    m "...Yes."
    k "But he was okay on the stairs!"
    m "He was, but now he's gone."
    k "!"
    m "The masked guy tried to take him out once, and he succeeded on the second try."
    k "What?!"
    m "Please, tell us what you know."

    $ current_cx = CrossExamination([
        Statement(k, "I waited for everyone to get out of the kitchen and into the garden."),
        Statement(k, "When the last girl went to the bathroom, I bolted and reached the stairs."),
        Statement(k, "When I entered the room, the masked murderer was standing there."),
        Statement(k, "He told me it was all a prank and made me escape through the garden window."),
        Statement(k, "I haven't talked to him since, and he hasn't said anything else.",
                correct_evidence_id="caulk_gun",
                contradiction_label="cx_kid_caulk_gun_success"),
        Statement(k, "I figured, since he's doing his prank I better get going with mine."),
        Statement(k, "That's why I tied up the rope around the shelves. That's it!")
    ])

    $ in_cross_examination = True
    $ cx_index = 0
    jump cx_display


label cx_kid_caulk_gun_success:

    m "Why are you lying again?"
    k "What?"
    m "The plan for your trick was straightforward. Wait for a phone to ring, and then slam the bookshelf on the ground, right?"
    k "Yeah."
    m "Then why glue the locks shut?"
    k "!"
    m "Kid, tell us the truth. You won't get in trouble, only the grown up will."
    k "...*sniffle sniffle*"
    l "Shit, you're gonna make him cry..."
    k "I DIDN'T WANT TO BE A BAD GUYYYYYYYYY"
    m "!"
    k "THE- THE KILLER- THEY SAID I WAS GOING TO HELP THEM- THEY NEVER SAID IT WAS A PRANK, I ONLY ASSUMED!"
    m "It's alright! Stay calm!"
    k "TH-THEY GAVE ME THIS PHONEEEE!"
    m "!"
    l "It's Fransk's!"
    k "AND THEY SAID THEY'D MESSAGE ME!"
    l "Shit, someone removed the password on it! And he's not lying! There's multiple texts coming from the same hidden number!"
    k "AT FIRST THEY TOLD ME TO SHUT THE DOORS, AND I SAID I DIDN'T WANNAA"
    l "That's true."
    k "BUT THEN, THEN THEY SAID"
    l "\"If you don't obey, or if you talk about what you saw to anybody, I'll murder your fucking sister.\""
    m "That's- that's awful! How did the killer know about his sister?"
    k "P-PLEASE HELP MY BIG SISSS."
    l "Calm down, who is it?"
    k "PROTECT CASSIEEEE"
    m "!"
    l "Cassie has a brother?"
    m "Wait a second, do you know Cassie's secret?"
    k "*sniff sniff* What secret?"
    m "She told us everything, about the pendant and all."
    k "The pendant? Oh! That secret? It's nothing much, our grammy offered it to her for christmas when she was smaller."
    m "..."
    l "That's so sweet!"
    k "It's really pretty, isn't it?"
    m "Does she ever take it off?"
    k "Yeah when she showers! She makes me watch over it sometimes."
    m "..."
    k "Too bad our grammy died a few years back, it was her last gift..."
    l "That's so sad, I can understand why she's so attached to it."
    k "She gave me a monster-truck that Christmas! I still have it! It looks like this biiiig car here, and it has keys like these ones!"
    l "Are those the car keys? Where'd you find them?"
    k "In the freezer! They kept poking me while I was hiding."
    l "Hell yeah dude! You rock! We can-"
    m "Lou."
    l "?"
    m "Cassie lied."
    l "What do you mean?"
    m "... Kid, stay in the garage okay? We're going to warn your sister." 
    "... Why would she lie? Why lie about THAT?"
    $ R_livingRoom.cutscene = "scene_final_confrontation_cassie"
    return


# --- CONFRONTATION FINALE : CASSIE ANDERSON ---

label scene_final_confrontation_cassie:

    l "Guys! We have the car keys! We also found Fransk's phone!"
    s "Fished it out of the window?"
    l "Nah, the kid had it, said the killer gave it to him."
    s "Did he see the killer?"
    l "No, but they threatened him by leveraging-"
    m "Cassie."
    c "? What's up?"
    m "Did you lie?"
    c "About?"
    m "Your nature."
    c "?"
    m "..."
    l "Maj, what are you saying?"
    m "You're not a ghost, right?"
    l "! Wait, is that what you meant?!"
    m "..."
    s "Bullshit!"
    c "Why would I lie about that?!"
    m "Depends on how long you've kept that lie going, but for tonight there's enough of a reason."
    

    call menu_choice_loop("Her reason was...",
    [    
        "To join the monster gang",
        "It gives her an alibi",
        "To look mysterious",
        "She resents being human"],
        1
    )


label choice_cassie_alibi_motive_success:

    m "It gives you a hell of an alibi..."
    c "What do you mean?"

    "No reason in keeping this going, let's just spell it out for them."

    call force_present_proof("dreamcatchers")
    jump choice_final_dreamcatchers_success


label choice_final_dreamcatchers_success:

    m "Being a ghost must suck, holding a grudge, roaming the earth for eternity..."
    c "Yes, it does."
    m "Worst of all, you can get sucked into something as inconspicuous as a tiny dreamcatcher."
    c "!"
    m "Turns out, a ghost wouldn't have been able to stab Fransk, with his love of those ghost repelling trinkets."
    c "..."
    m "But a human... that's a whole other deal."
    c "You're suggesting that I tried to murder Fransk?"
    m "I really hope I'm wrong Cassie."
    c "That's stupid, Fransk would've resisted."
    p "Wasn't he injecting himself with blood at the time?"
    l "He said he didn't really feel the need to sleep, so it makes sense to say that he could've defended himself."
    m "Not if he wasn't attacked directly."
    l "What? Wasn't he stabbed?"
    m "Sure, but he could've been attacked without even knowing."
    l "How?"

    call force_present_proof("blood_pouch")
    jump choice_blood_pouch_attack_success


label choice_blood_pouch_attack_success:

    m "Lou found this hole in the blood pouch, it easily could've been used to inject a product into his bloodstream with him directly noticing that he was being attacked."
    c "And how exactly would that have led to his stabbing?"
    m "It all makes sense when you consider what was injected into the pouch..."

    call force_present_proof("nyctozepam")
    jump choice_nyctozepam_pouch_success


label choice_nyctozepam_pouch_success:

    m "Pani fainting from her drug usage always seemed suspect to me."
    p "? What drug usage?"
    m "With the chaos nobody thought to tell you, but you fainted because of a drug called Nyctozepam."
    p "What?! Sleeping pills don't make me high! They just take more time to take effect."
    m "And yet we found a box of them in your back pocket."
    p "?!"
    m "Two capsules were missing. One was obviously used to drug Pani, but the other..."
    c "..."
    m "If you were to extract the powder from the capsule, dilute it using the medical products owned by Fransk and inject it into his bloodstream using his IV..."
    p "Then he'd get knocked out as soon as the contaminated blood reached his body."
    m "Exactly, this murder could've been set up well in advance, the murderer only needed to wait for Fransk to go \"rest\"."
    c "Let me get this straight, you're suggesting that I not only knew about Fransk's nature, but that I chose to stab him while he was still hooked to his IV? That'd make me a pretty pathetic murderer."
    m "Not necessarily, you could've known that he was a monster, that he needed perfusions and even that electricity could kill him while still thinking that a good old knife to the chest would do the trick."
    c "Right, 'cause I totally could've done it with my single set of clothes, and the footprints at the scene clearly resembled mine..."
    m "Sarcasm, at this time? You better not underestimate us."

    call force_present_proof("black_robe")
    jump choice_black_robe_proof_success


label choice_black_robe_proof_success:

    m "Remember this shitty costume? Carm used it to cover Fransk's \"dead\" body."
    l "Right?"
    m "The blood pattern on it is... interesting. Most of the front is covered with blood, we assumed it happened while it was covering it, but it also could've come from the initial blood projections."
    l "I see!"
    m "There's also some interesting patterns. On the right cuff there's a patch with no trace of blood."
    p "As if the knife was being held by using the sleeves!"
    m "Right, and on the bottom of the dress there's two outlying patches of blood, almost as if someone deliberately stepped on the robe to camouflage their steps!"
    c "!"
    m "Face it Cassie, you're the only one who could've done it, beyond the shadow of a doubt."
    c "... So what?"
    m "!"
    c "I stabbed Fransk. Why does it matter?"
    s "You..."
    p "How could you say that?"
    l "*Growl...*"
    c "If I said that I knew about his regenerative abilities, wouldn't that be enough to affirm that it was nothing but a harmless prank?"
    m "!"
    c "In fact, he would've been totally fine if Carm didn't decide to gorge on what little blood remained."
    "...Who is she?"
    m "C-Cassie, is that you?"
    "Stheno's thinking the same..."
    c "Yes, it is I. I might be guilty of that prank, but when it comes to Fransk's ACTUAL murder as well as Carm's..."
    m "I know how they were done."
    c "Really? Please tell us."

    call force_present_proof("smart_home_remote")
    jump choice_remote_tag_reveal_success


label choice_remote_tag_reveal_success:

    m "Fransk's house automation remote is missing."
    c "House automation! As if I had access to-"
    l "SHUT THE FUCK UP!"
    m "!"

    "In a flash Lou pins Cassie on the floor next to the bookshelf."

    m "Lou! Don't!"
    l "You fucking liar! You had ample time to prepare that fucking plan of yours!"
    c "...*ack*"
    l "You set up the traps this morning! And you even removed the rubber coverings on the handle!"
    c "Stop...choking...me...you...mutt!"
    p "LOU LET HER GO!"
    "{b}*kick*{/b}"

    "Pani's kick looked like it hurt like hell, can't imagine how tough her hooves must be."

    m "Fuck! Pani!"
    c "*huff* *huff*"
    s "Cassie, you better explain yourself, now!"
    s "I don't have any remote, Maj is a fucking liar! Think about it! Why would I have set up two different plans to murder Fransk!"

    call menu_choice_loop("Cassie needed two plans because:",
    [    
        "Something went wrong",
        "She needed a backup",
        "The remote was glitching",
        "Someone else did it"],
        0
    )


label choice_something_went_wrong_success:

    m "Don't think about it too much, the proof is right in front of you. Or should I say, among you?"
    l "You mean... Me?!"
    m "Cassie couldn't foresee your sudden transformation. She couldn't find an opportunity to trigger the trap because Fransk went up to \"rest\" too early. And your presence also complicated things for her."
    l "I see..."
    m "There's also another proof that cements this claim..."
    
    call menu_choice_loop("What proves that she had to improvise is...",
    [    
        "The bed",
        "The IV",
        "The garlic",
        "The announcements"],
        3
    )


label choice_the_announcements_success:

    m "Please recall the announcements right before both murders occurred."
    m "Doesn't it sound like the order of the murders was... wrong?"
    m "Carm's was: \"IT IS NOW TIME FOR THE SECOND TRAITOR TO RECEIVE HIS PUNISHMENT MAY THE LIGHT PUT AN END TO YOUR ENDLESS SLAUGHTER!\""
    m "Fransk's: \"TRAITOR, TIME TO PAY FOR YOUR LIES MAY THIS SPARK PUT AN END TO YOUR ORIGINAL SIN\""
    m "It really sounds like Fransk was supposed to die before Carm."
    l "Yeah! Fransk would be the \"original traitor\" and Carm \"the second\"!"
    m "Now that I think about it, her second plan must've been improvised."
    l "Doesn't that contradict the whole \"blood pouch\" thing?"
    m "Not necessarily, it could've been a red herring."
    l "What?"
    m "Think about it, directly injecting the medication into Fransk wouldn't be too difficult, you'd just have to inject it into his skin or into the tube."
    m "Then, you could add another hole to the bag to make it seem like the plan was set-up way earlier."
    c "Your theories are laughable. If I truly had done that, Fransk would've noticed."
    m "Oh trust me, he did. And the absolute proof of that is..."
    

    call menu_choice_loop("The ultimate proof of her guilt is...",
    [    
        "The proof of struggle",
        "Fransk in the stairs",
        "The living room window",
        "Fransk's last words"],
        3
    )

label choice_fransk_last_words_success:

    "..."
    "This puts an end to this madness... From now on, there is no doubt in my heart. Cassie did it, I don't know why but she did. The only other human... Siding with the monsters... That's the choice I make."
    "... Let's get it over with"

    m "He told me."
    c "!"
    m "At first I thought that his last words were meant for his mother. But they start to make sense once you consider the motive."
    c "My motive?"
    m "Carmille and Fransk were both murdered. Fransk also mentioned Carmille first when thinking about his very last words..."
    s "SHIT! NO WAY IT'S THAT?"
    m "Stheno figured it out."
    s "IS IT BECAUSE THEY WERE FUCKING?!"
    m "Uh... I was thinking that they were lovers but that was close enough."
    l "No way? Them? FUCKING?"
    s "That's what I saw on Carm's phone! They were sexting like crazy!"
    p "Duh, y'alls gaydar must suckkkk."
    c "..."
    m "You harbored feelings for one of them, and discovered their secret relationship-"
    c "Stop right there."
    m "!"
    c "It is true, all of it."
    s "!"
    l "!"
    p "!"
    m "You... really did it because of their relationship?"
    c "In part, yes. I fell in love with Fransk during high school, and have never stopped loving him since."
    m "..."
    c "He always was out of reach, but I thought I'd make my move during our weekend in the forest. But on that day my world would slowly start to crumble... I witnessed Carmille's transformation into a bat. To think that I'd grown close to a monster, something that went beyond my understanding of the world..."
    "I somewhat understand this feeling..."
    c "My goal was clear, I needed to warn Fransk! But after I told him... he started avoiding me... At first, I didn't understand, but the thought grew increasingly strong: \"He must've been swayed by the monster! He's rejecting his humanity!\" That's when I started to pretend..."
    c "For a bit, I had gained everything I ever wished for. His attention, his secrets, his fears and worries. He never told me about his immortality, but for everything else I became his confidant. I even gained the trust of Carmille, who saw me as one of his peers."
    c "I was content, making progress and then my world turned upside-down again! There they were, in his room, on his bed, having sex! Passionate, disgusting, heartbreaking, monstrous INTERCOURSE. It's only then that I saw the true monsters they were. The way Carm hid from the sun itself, the disgusting stitches on Fransk's body. I rejected my humanity, and all for that?! I gave my heart to this atrocity!"
    l "Don't talk about them like this, they were our FRIENDS!"
    v "Lou, stay calm."
    c "Friends? Really?"
    l "They loved each other, you're the one that needed to move on!"
    c "Love? From a monster?"
    l "FUCK YOU MEAN \"FROM A MONSTER\"?"
    v "Lou!"
    c "YOU'LL NEVER UNDERSTAND WHAT IT MEANS TO BE HUMAN, YOU'RE ALL ATROCITIES."
    l "You fucking-"
    c "Had I known about the three of you I would've KILLED YOU, or sent you to rot!"
    m "Now who's sounding like the fucking monster?!"
    c "You're one to talk? Maj? Only a few hours with these animals and you're forgetting the most important part? It's us against them."
    m "Us? There's no humanity in your words."
    c "Then you're just like the rest of them, and just as deserving of eternal suffer-"
    l "THAT'S ENOUGH! I'LL SHUT YOU UP, FOR FUCKING GOOD. JUST FOR SAYING THAT CARM AND FRANSK DESERVED IT-"
    m "Lou!"
    c "*gasp*...*gasp*"
    m "You're choking her!"
    l "YEAH?! DID SHE GIVE A FUCK WHEN SHE TORTURED CARMILLE?"
    s "Stop it!"
    m "Lou! There's-"
    k "LEAVE MY SISTER ALONE!"
    "{i}*tuggggg*{/i}"
    "I can't comprehend the situation."
    "{b}*CRASHHH*{/b}"
    "All I can see now is Cassie's free and..."
    m "Lou!"
    l "GRRAAAAH TH-THIS SHIT'S HEAVY AS FUCK!"
    m "Hold on, wait for me!"
    "I try to support the falling shelf with all of my might, but Lou was right, we won't last long."
    k "I'M SORRY WOLFIE, I ONLY WANTED TO HELP LET ME PUSH WITH YOU!"
    "It might sound dumb but the kid's really giving me the strength I needed, we might just make it!"
    l "Come on guys! Push! I feel it! We can do it! Kid, Maj! You're giving me the strength I need!"
    m "Yeah, we'll get you out of this! Pani, Stheno! Come and help-"
    s "ABBY WATCH OUT!"

    "Suddenly, I feel it. My strength sapped away from me. I've accepted it, Cassie's hand just pulled me away from my burden, and in a second it will all come crashing down. I don't have a choice, Lou doesn't stand a chance. In desperation I throw out my hand."

    m "KID, QUICK!"
    "I pull with all of my might but..."

    "{b}*SLAAAAAAAAAAAAAAAAAAAAAAAAAAM*{/b}"
    m "GRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH"

    "My right leg, crushed. ... Lou... ... ..."

    m "GRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH"
    c "You will die with him."
    m "CASSIE, STOP, YOU DON'T GET IT!"
    c "I don't care for your leg, you deserve to die."
    m "It's not me! It's... Kid... Your brother, I grabbed onto his legs! There's a chance that he survives! Only his upper body was struck!"
    "The blood pooling around the child's body isn't a good sign, but we have to act fast. Act..."
    c "He chose the dog over me."
    m "?"
    c "The young are meant to serve their elders. I don't care for his death."
    m "How... you??"
    "How could she say something so... awful? All of that while digging through her bag..."
    c "If you liked Fransk so much, then you'll kill you with the same knife."
    m "PANI, STHEN, RUN!"
    "{b}*SHATTER*{/b}"
    s "Maj, look away!"

    "For a moment, I saw it. Stheno's true form."
    "{b}*THUD*{/b}"
    "Cassie, petrified, the face of pure hatred forever carved onto stone."

    s "Pani, free him, quick."
    "{i}*CREAAAAAK*{/i}"
    p "Drag your leg out, Maj."
    m "Wait, before setting the shelf down! Place a chair or something! Make it easy for the police to find their bodies!"
    p "...Sure."
    "{i}*dragggg*{/i}"
    p "Now come on, I'll get you to the car."
    m "The... car?"
    p "Lou gave me the keys earlier, he said the kid found it?"
    m "Y-Yeah."
    s "We have to move quick, they only stay in stone for a little bit."
    m "What?"
    s "What?! I'm not a killer!"
    m "..."

    "It's all a blur..."

    p "There you go, put on your seatbelt and don't try to move your leg!"
    s "Can you guide me Pani?"
    p "Sure!"
    m "Who's gonna drive us?"
    p "Me! I can drive."
    m "Using THAT licence?"
    p "Well yeah!"
    "..."
    "..."
    s "Maj?"
    m "!"
    s "I've contacted the authorities, a bed's ready for you at the hospital."
    m "..."
    s "Before going I had Pani pick up the phones, here's yours."
    m "Th-Thanks..."
    s "Listen, Pani and I will have to lay low, the government will probably try to question you very soon."
    m "I get it, your secret's safe with me. I won't mention anything that's irrelevant to the crime scene."
    s "Maj... I'm so sorry."
    m "..."
    s "I should've trusted you from the beginning."
    m "No. It takes time to figure out what makes each of us human."
    s "Human?"
    m "Your doubts, your worries... I can see where they come from when monsters like that try to rip your life away."
    s "Monsters... Yet I trusted her."
    m "See?"
    s "But she wasn't a monster."
    m "!"
    s "I know you don't mean harm when you use that word like that. But a monster is nothing more than a category of being."
    m "..."
    s "Me and Pani, we're monsters, and our lives are defined by that."
    p "Whether we want it or not."
    s "The way Cass acted... that's human."
    m "But y'all aren't-"
    p "Maybe you're giving humans a bit too much credit, Maj. Ask yourself, where's the \"monster\" in Cassie's actions, and where's the \"human\" in Carmilles or Fransk's or Lou's?"
    m "..."
    p "Just saying, there's not- Oh!"
    m "Keep going, I was curious to hear what you had to say..."
    p "Well, you'll have to find the answer yourself, seems like there's a whole ass medical crew ready for your arrival!"
    m "!"
    s "Come here, Abby. I wish I could've seen you, but I wouldn't want to turn you to stone. Take this hug as a \"see you!\""
    m "Sthen..."
    "{i}*CLICK*{/i}"
    "Are you Abdul-Majid?"
    p "That's him, guys!"
    "Okay, GO! GO! GO!"
    p "Bye bye! See you soon!"

    "As the doctors set me on the stretcher I can't help but feel... My consciousness.... fade...."

    return



# ==============================================================================
# ACTE 2 & CONCLUSION DU PROLOGUE - LABELS D'INTERACTION & SCÈNES
# ==============================================================================

# --- ENQUÊTE 2 : L'ÉVANOUISSEMENT DE PANI (HOTSPOTS & PERSONNAGES) ---

label talk_carmille_investigation_pani:
    v "...Something's bothering me."
    m "What is it?"
    v "Why would she ingest the medication willingly? It makes no fucking sense."
    m "Yeah, especially one that strong."
    v "I'm just scared... What if she was chasing a high?"
    m "I don't think so, this shit is so strong it just knocks you right out."
    v "Then... if she didn't take it herself... Then it means that someone did it."
    v "... ... could someone have injected it to her?"
    m "Not really, if injected directly into the bloodstream then it can take you out within seconds, we would've seen someone do it."
    v "...Maj, figure it out for her. Okay?"
    m "I'll do my best."

    # [Nyctozepam added to evidence]
    $ P_nyctozepam = Proof("Nyctozepam", 
                            "A powerful drug for treating insomnia. The capsules contain a fine powder.", 
                            "images/props/nyctozepam.png", 
                            R_kitchen, 
                            1850, 800, 
                            "nyctozepam")
    $ addProofToInventory(P_nyctozepam)

    $ eventMgr.unlock("talk_carmille_investigation_pani")
    return

label talk_stheno_investigation_pani:
    s "15 minutes... that's approximately the time where we got our drinks."
    m "Yeah, Lou went upstairs 20 minutes ago, so you're probably right on the money."
    s "Carm went first... followed by you, Pani and then Cassie."
    m "You didn't go?"
    s "I went before Carm, while you were chasing after Lou."
    m "I see."

    # [Bathroom Order added to evidence]
    $ P_bathroom_order = Proof("Bathroom order", 
                            "Stheno went to the bathroom when I was talking with Lou and Fransk. Later, Carm, Me, Pani and Cassie went in order.", 
                            "images/props/toilet.png", 
                            R_F1bathroom, 
                            450, 900, 
                            "bathroom_order")
    $ addProofToInventory(P_bathroom_order)

    $ eventMgr.unlock("talk_stheno_investigation_pani")
    return

label talk_cassie_investigation_pani:
    m "You were gone for a little bit. Let me recap everything that happened."
    c "Don't worry, Carm already told me."
    m "Okay, any idea where she put her drink?"
    c "Not really... but we all had eyes on it at some point."
    m "?"
    c "Sthen and I stayed with her until she went to the bathroom."
    c "And when my turn came, Carm was already sat."
    m "...This leaves the time the drinks were poured, no?"
    c "I guess so..."
    c "But I'm positive that she poured out her own drink, so this is highly unlikely."
    m "The night was going along so well..."
    c "I'm glad we talked earlier, at least we got acquainted."
    m "Yeah, I'm happy too."
    $ eventMgr.unlock("talk_cassie_investigation_pani")
    return



# --- ENQUÊTE 3 : MEURTRE DE FRANSK (CHAMBRE DE FRANSK) ---


label hotspot_investigation_body:
    l "..."
    l "I can't believe it man..."
    l "He's really gone..."
    m "When I first came in, his wound and face were clearly visible."
    l "What do you mean?"
    m "This black piece of cloth wasn't on here."
    m "Why would the killer risk getting caught just to hide the body?"
    l "...The body could be hiding a clue, right?"
    m "?"
    l "I won't shy away from the truth, we owe it to Fransk."
    m "I agree."
    v "If you don't mind I'll turn away for a bit. Mind explaining the details to me later?"
    s "Same as Carm."
    m "Yeah, sure."
    l "You ready bro?"
    m "...No point in waiting."
    "{i}*fwoosh*{/i}"
    m "God...god dammit!"
    l "This wound is just awful to look at, it's like a gaping hole in his torso..."
    m "It was probably done with some kind of knife..."
    l "Yeah, judging from the depth of it, I can safely assume that the blood came from here."

    # [Information about the body added to evidence] ?
    $ P_body_info = Proof("Information about the body", 
                            "Fransk was stabbed in the torso using a knife. The blood from the scene is definitely his.", 
                            "images/props/body.png", 
                            R_F1fransksRoom, 
                            1250, 300, 
                            "body_info")
    $ addProofToInventory(P_body_info)
    
    l "...Let's put it back the way we found it..."
    m "Yeah... Wait a sec-"
    l "Notice something?"
    m "This piece of cloth... something is hanging from it."
    l "?"
    m "Are these... sleeves?"
    l "Oh yeah, it looks like some kind of halloween costume, like the guy from Scream or something."
    m "It reminds me of a costume I saw earlier today, but it was way smaller. This must be the adult version of it."
    m "Was Fransk planning on getting dressed?"
    l "I'm really not that sure, we already celebrated halloween at the school and he came dressed as a stupid videogame character."
    l "If he wanted to get dressed tonight he probably wouldn't have bothered with getting a new one."
    m "Yeah, then I wonder where this came from..."
    l "I don't know, this could've been an earlier costume of his."
    m "Either way this piece of clothing was clearly involved in the murder."
    l "Or at the very least in hiding the wound."

    # [Black robe added to evidence]
    $ P_black_robe = Proof("Black Robe", 
                            "A black robe, probably coming from an old halloween costume. The front is covered in blood, which makes sense when you considered that it was used to cover the body.", 
                            "images/props/black_robe.png", 
                            R_F1fransksRoom, 
                            1300, 400, 
                            "black_robe")
    $ addProofToInventory(P_black_robe)   

    $ eventMgr.unlock("hotspot_investigation_body")
    return

label hotspot_investigation_carpet:
    v "Check this flooring out."
    l "Looks to me like the blood missed a huge square. What kind of wound does that?"
    v "None, there must've been a tarp of some kind."
    l "Now that you mention it! There used to be a stylish carpet here, I just saw it earlier."
    v "Yeah, that's what I thought."
    l "I checked the room out and I still haven't seen it."
    m "Let's keep an eye out for it, okay? If the killer bothered with hiding it then it must be important."
    
    $ eventMgr.unlock("hotspot_investigation_carpet")
    return

label hotspot_investigation_dreamcatchers:
    m "What's that?"
    l "Oh, those are Fransk's dreamcatchers."
    m "Aren't they a scam?"
    l "Fransk loved these things, he gifted me some when we were kids."
    m "You knew each other that long?"
    l "Yeah, most of us did..."
    m "..."
    l "You should've seen it, bro used to pee the bed every single night. Nightmares got so bad he couldn't sleep sometimes."
    m "Poor Fransk, that must've been awful."
    l "Yeah, until he bought these on a trip. He told me something about them being sewn centuries ago by native people. Real spiritual shit."
    m "That must've been some kinda scam... right?"
    l "That's what I thought too, but they ended up helping him a ton. So I don't think he cared."
    m "Maybe they're real after-all?"
    l "I'd like to ask him for his opinion. ..."
    "He's doing his best to stay composed but he must feel terrible..."

    # [Dreamcatchers added to evidence]
    $ P_dreamcatchers = Proof("Dreamcatchers", 
                            "Fransk allegedly loved these weird trinkets, they apparently helped with his nightmares.", 
                            "images/props/dreamcatchers.png", 
                            R_F1fransksRoom, 
                            1550, 500, 
                            "dreamcatchers")
    $ addProofToInventory(P_dreamcatchers)

    $ eventMgr.unlock("hotspot_investigation_dreamcatchers")
    return

label hotspot_investigation_closet:
    l "Yeah... that's what I remembered..."
    m "Did you say anything?"
    l "Oh? Uh nothing, just looking through some of his stuff, with the way the shelves are set up, there's no way someone could hide in here."
    m "Sure, but you could probably hide something, like a murder weapon."
    l "Yeah, right, let me see... Ugh, he just owns so much bullshit! Let me try something else."
    l "sniff sniff sniff... Huh?"
    m "Find anything suspicious?"
    l "I don't know, there's something I can't quite smell... Wait WHAT!"
    m "What is it?"
    l "Wh-What's my fucking jacket doing here!"
    m "Could Fransk have brought it upstairs after that whole ordeal for the vape?"
    l "...Sure but why hide it in his closet?"
    m "I'm drawing blanks here, can't tell you man."
    
    # [Lou's Jacket added to evidence]
    $ P_lous_jacket = Proof("Lou's Jacket", 
                            "Lou's jacket,which we was mysteriously moved to Fransk's room. It's really musky and smells like him.", 
                            "images/props/lous_jacket.png", 
                            R_F1fransksRoom, 
                            1400, 500, 
                            "lous_jacket")
    $ addProofToInventory(P_lous_jacket)

    $ eventMgr.unlock("hotspot_investigation_closet")
    return

label hotspot_investigation_window_living:
    l "This window... I can't believe they used it to hide my vape."
    s "Sorry for that Lou, we're so used to pranking you..."
    l "Hope this made you reconsider."
    s "Something's wrong..."
    l "Do you really not feel bad about what you did to me?"
    s "No- not that. Why's the window still open?"
    m "What? Wasn't it open during the vape theft?"
    s "Yeah, but while you were in the bathroom Fransk talked to us."
    m "?! He did! Then that means that he was still alive when I went to the bathroom!"
    s "Yeah, but the weird part is that he closed it after talking to us, said that he needed to rest and that he heard us from the living room while the window was open."
    m "I see... It tracks with what he told me after we brought Lou to the bathroom."
    s "Did Fransk open the window to warn us about the murder?"
    m "..."
    "I have a feeling that this window is more important than it may seem."

    # [Window added to evidence]
    $ P_living_window = Proof("Living Room Window", 
                            "A small window that slightly opens. Leads Fransk's room to the living room.", 
                            "images/props/living_room_window.png", 
                            R_livingRoom, 
                            850, 800, 
                            "living_room_window")
    $ addProofToInventory(P_living_window)

    $ eventMgr.unlock("hotspot_investigation_window_living")
    return

label hotspot_investigation_window_garden:
    l "The smell of blood is really getting to me, mind if I open these windows?"
    m "Yeah good idea."
    l "What the hell?"
    m "What's up?"
    l "There's some kind of knot tied up around the handles."
    m "Damn you're right, is that some kind of rope?"
    l "Yeah, it seems so. Probably comes from this very room."
    m "What makes you say that?"
    l "We used it for a visual arts assignment back in middle school. I always wanted to bite on it!"
    m "...You like playing rope?"
    l "What's that?"
    m "It's like you grab one of the ends with your teeth while I try to pull it away from your mouth."
    l "OOOH LOOKS FUN CAN WE PLAY?"
    "...His tail is wagging like crazy."
    m "Anyhow, was this window usually locked like this?"
    l "Nah, you could close it normally, the only thing it really lacked was a lock, but you can't really open it from outside."
    m "Yeah makes sense, whoever placed it here probably didn't escape from here then."
    l "So they must've gone through the stairs..."
    m "Exactly my thoughts."

    # [Window to the garden added to evidence]
    $ P_garden_window = Proof("Garden Window", 
                            "This big window in Fransk's room leads to the garden. Escaping from it seems doable, but it was tied shut with some rope.", 
                            "images/props/garden_window.png", 
                            R_F1fransksRoom, 
                            1700, 500, 
                            "garden_window")
    $ addProofToInventory(P_garden_window)
    
    $ eventMgr.unlock("hotspot_investigation_window_garden")
    return

label talk_carmille_investigation_murder:
    v "Fransk..."
    "He looks like he's deep in thought, better not bother him."
    v "Maj, will you try to figure out what happened?"
    m "! Yes, I'll do my best. I really need to have a solid account to tell the police once Pani and Lou can conceal their true forms."
    v "True forms..."
    m "?"
    v "I was just wondering about Fransk, he had some weird habits."
    m "Anything suspicious?"
    v "No, not at all! I'm just wondering about his medical records..."
    m "Was he ill?"
    v "Not that I know of, but he often needed to take private \"naps\"."
    m "Naps?"
    v "Yeah, when he got too stressed or tired he always said it gave him \"Bad blood' and found somewhere to rest up."
    m "I see, he could be narcoleptic."
    v "Yeah, that's what I wondered too but one day I found him resting in the locker rooms."
    v "He was laying down, reading and something was hooked to his shoulder from his backpack."
    l "From his backpack? What did it look like?"
    v "It was like some kind of... IV? I might be mistaken."
    l "Maybe he was diabetic. My uncle used to carry a little machine to pump insulin into his system. Otherwise he'd faint."
    v "Could be... but insulin dispensing systems are much more discreet nowadays, no?"
    m "Whatever it was, we should find traces of it in his room or backpack."
    v "That's exactly what I was thinking, but I couldn't find anything."
    l "Maybe you were wrong about seeing that?"
    v "...I don't know..."
    "If he really had some kind of condition then it would be important to note." 
    
    $ eventMgr.unlock("talk_carmille_investigation_murder")
    return

label talk_lou_investigation_murder:
    l "I can't believe that he's gone..."
    m "Despite everything that happened tonight, this is by far the most shocking."
    l "We promised we'd tell you the truth, right?"
    m "...I can't ask that of you now."
    l "No, someone has to know-"
    m "?"
    l "About how great of a guy he was..."
    m "Tell me."
    l "We both grew up here, in this shithole of a town."
    l "He'd never sleepover at my house, so I always spent nights here."
    "They were closer than I expected..."
    l "Before they got caught by the government my folks always warned me to lock myself up during full moons."
    m "Were they also werewolves?"
    l "DOGS! Were-dogs! And I'm not sure. At least one of them must've been."
    l "Neither of them ever transformed in front of me, and both were caught by the police."
    m "If one of them was human then it's really unfair!"
    l "Yeah, but they wouldn't snitch on each other."
    m "!"
    l "They both stayed silent to protect each other, and me."
    m "You?"
    l "Yup, monster genes are often recessive. So they just surveilled me for a time."
    m "...I see."
    l "Mom gave me a neat trick to get them off my scent."
    l "One day I stuffed a silver coin in my mouth and stared at the full moon."
    l "I didn't transform, but it burnt like hell that night."
    m "Werewolves are allergic to that, right?"
    l "Dude, DOG. I'm a were-dog. And yeah, it had properties that conceal our feline DNA or something..."
    m "I see..."
    l "It really felt like I was dying. But Fransk supported me all the way throughout."
    m "..."
    l "Later that night he brought me to the garden and let me transform into a were-pup."
    m "He did?!"
    l "Yeah, he said the pain probably came from my repressed transformation."
    m "Clever kid..."
    l "And he was right, when I transformed I really felt like I was surging with energy, especially from my jaw!"
    l "I ended up tearing and ripping some floaties to shred that night..."
    l "I got so amped up that I... lunged at him... frothing at the mouth."
    m "!"
    l "I wasn't myself... I could've hurt him! Until he said-"
    f "\"Lou... why do they keep you muzzled? You're the nicest boy I know!\""
    l "*sniffle* He always was this nice to the people around him!"
    l "Ever since that day I'd always come over during the full moon."
    m "His parents didn't mind?"
    l "His mom was never 'round, and I only saw his dad during birthdays."
    m "That's awful!"
    l "Fransk always did the cooking, and he used to pretend like cleaning up was some sort of game!"
    m "It's like he was trained for this..."
    l "...I couldn't have made it to where I am without him..."
    m "I'm really sorry, I didn't know about your friendship."
    l "I really couldn't wait to be alone with the both of you after the party, we had so many stories to tell..."
    "I guess I was the only one they could tell."
    l "When I smelled him earlier in the hall I really thought he joined you guys down."
    m "Yeah, you told me about it earlier."
    l "Guess I should explain myself, while I was in the bathroom, I smelled Fransk go down the stairs..."
    m "That must've been during the murder..."
    l "Yeah, but there was this weird smell before that... It appeared a bit before Fransk's smell."
    l "It had this unmistakable odor of..."
    m "Of!?"
    l "...like... freshly cut lawn?"
    m "!"
    l "It really smelled like wet grass or something?"
    m "Didn't you mention that Pani smelled like hay earlier?"
    l "I did, but I had never smelled this on someone before. At least not to this degree."
    m "But was it any of us!?"
    l "...I don't think so. If it were then I think I'd be able to tell."
    m "Do you have, like, the sense of smell of a wol- I mean! Dog?"
    l "Look bro, do I really look like a heartless predator to you!"
    m "No! I mean, you're kinda cute actually!"
    l "Cute?"
    m "Yes- No! I mean, intimidating!"
    l "Aww... I wish you called me cute..."
    "His tail's dragging on the floor..."
    l "Listen, I'm a beautiful Were-Dog, my lustrous coat comes from a great pedigree of German Shepherds!"
    m "Are you saying that a dog is part of your family tree?"
    l "Of course! Haven't you heard of the Witch of Baskerville? Bitch was known to fuse dogs with their owners!"
    m "...keep that story for later, we have a murder to solve."
    l "Sorry, my attention span is terribly low..."
    m "It's fine... thanks for telling me about your history."
    l "No problem! I'm here to help!"
    m "I should really keep what you think you smelled in mind, if there's really an unidentified smell then it means that the killer probably isn't one of us!"
    l "Yeah! That's right!"

    # [Lou's sense of smell added to evidence]
    $ P_lous_smell = Proof("Lous' sense of smell", 
                            "Around the time of Fransk's murder, Lou smelled a strong scent of grass, followed by the smell of Fransk.", 
                            "images/props/lous_sense_of_smell.png", 
                            R_F1bathroom, 
                            400, 350, 
                            "smell_order")
    $ addProofToInventory(P_lous_smell) 
    
    $ eventMgr.unlock("talk_lou_investigation_murder")
    return

label talk_stheno_investigation_murder:
    s "..."
    m "..."
    "We haven't talked since our fight... But I should really put it behind me."
    s "Listen..."
    m "Listen..."
    m "!"
    s "Look, asshole, I'm not forgiving you."
    m "..."
    s "But figuring out what happened to Fransk is more important to me than ignoring a pussy-ass, boney bitch like you."
    "...Wonderful prose, as always."
    s "So I'm willing to let you help me figure out this shit."
    m "Yeah, this isn't the best time to fight."
    s "So? Notice anything?"
    m "I still have to finish investigating, but I could tell you about the state of the room when I discovered the body."
    s "Go on."
    m "After Pani fainted, I headed towards Fransk's room to tell him about what happened."
    l "She was drugged right?"
    m "Exactly."
    s "Keep going."
    m "The floor was bloody as hell... and I could clearly see his face."
    s "I see. So wildly different."
    m "Yeah, most of the blood is missing, and the floor's way cleaner."
    s "Did you speak to anyone on the way?"
    m "Yeah, he asked me about Pan's secret identity and quickly mentioned what happened."
    s "I see."
    m "A few seconds after that I heard Maj, scream and bullet down the hall."
    s "Seconds? Then you must be telling the truth."
    m "-Really! You trust me?"
    s "Yeah, you couldn't have killed him in such a small amount of time, and we've been together for a fucking while."
    m "Th-Thanks!"
    s "Bitch, doesn't mean I respect you though."
    m "... Sure."
    s "The killer must've been an outsider then, none of us could've done it."
    m "We should look at each other's alib-"
    s "None of us."
    "...She might be hard to approach but she cares deeply about her friends..."
    $ eventMgr.unlock("talk_stheno_investigation_murder")
    return


# --- ENQUÊTE 4 : APRÈS LE MEURTRE DE CARMILLE (JARDIN, ENTRÉE & GARAGE) ---


label hotspot_bookshelf_rope:
    l "What the hell is this?"
    m "This is new, right?"
    c "You guys notice it too? This shit was already here when we came back in."
    m "Where does this rope even end?"
    c "In the garage. But no one was there. I even checked the car."
    m "Why would someone do this?"

    # [Tied Up Bookshelf added to evidence]
    $ P_tied_bookshelf = Proof("Tied Up Bookshelf", 
                            "The bookshelf was tied up with rope during our blunt rotation... The point of this evades me.", 
                            "images/props/tied_up_bookshelf.png", 
                            R_livingRoom, 
                            900, 1000, 
                            "tied_up_shelf")
    $ addProofToInventory(P_tied_bookshelf) 
    
    $ eventMgr.unlock("hotspot_bookshelf_rope")
    jump room_loop

label hotspot_fatal_closet:
    s "...Tsk!"
    "No wonder she's disturbed, Carm died right here, and in her arms..."
    s "The trap they set up was simple as fuck. They filled a bucket with garlic, and then simply set it up on the doorframe, waiting for someone to open it."
    m "Still, it's quite a weird plan. Had anyone opened the door before him, they'd simply end up smelling like garlic."
    s "Yeah... Wait? There's something inside Carm's hoodie."
    m "What is it?"
    s "Is that a- A cross?!"
    m "Isn't that super lethal to vampires?"
    s "Yeah..."
    m "It's now clear that Carm was the explicit target, this isn't some random prank gone wrong."
    s "Shit... This closet used to be locked, I'm sure of it. What was up with lights in the first place?"
    m "Yeah, they turned violet after a weird announcement rang out."
    s "Whoever set it up must've known that Carm could be harmed with UV rays."
    m "Aren't those everywhere?"
    s "Sure but they're usually cancelled out by other frequencies."
    m "I see... That blue light must've bombarded him with ultraviolet rays..."
    s "... I'll catch the fucker who did this and make him suffer."
    "Don't think I'll stop her."

    # [Deadly Closet added to evidence]
    $ P_deadly_closet = Proof("Deadly Closet", 
                            "The walk-in closet in the entry hall was weaponized to murder a vampire. The strong smell of garlic makes me want to puke.", 
                            "images/props/deadly_closet.png", 
                            R_entryHallway, 
                            400, 900, 
                            "deadly_closet")
    $ addProofToInventory(P_deadly_closet) 
    
    $ eventMgr.unlock("hotspot_fatal_closet")
    jump room_loop

label hotspot_bloody_carpet_found:
    m "There should be a carpet behind this closet."
    l "Let's check it out!"
    m "This must be it? Right?"
    l "Damn, it's bloody as hell..."
    m "Yeah, that's a hell of a smudge..."
    l "Shit... I don't see how it helps us."
    m "You're mistaken. Look, there are clear footsteps."
    l "Holy shit you're right! We can compare shoe-prints!"
    m "I don't think so, these smaller ones heading towards the window are clearly some kind of sneakers, but these other ones are really indistinct."
    l "Those could come from some kind of slippers..."
    m "Maybe, but that doesn't really help us..."

    # [Bloody Carpet added to evidence]
    $ P_bloody_carpet = Proof("Bloody Carpet", 
                            "Carmille hid this carpet behind the closet.  It features two distinct set of footprints: A small pair of sneaker, heading towards the window, and bigger indistinct one, heading towards the hallway.", 
                            "images/props/bloody_carpet.png", 
                            R_entryHallway, 
                            400, 1000, 
                            "bloody_carpet")
    $ addProofToInventory(P_bloody_carpet)
    
    $ eventMgr.unlock("hotspot_bloody_carpet_found")
    jump room_loop

label hotspot_black_cloth_recheck:
    m "Carm confirmed that he's the one that placed this onto the body."
    l "Yeah, wanna check it out?"
    m "Sure. ... It's just a mess... but some areas are suspicious."
    l "Yeah?"
    m "Look at the right cuff, it's all bloody except for a spot in the middle."
    l "How could that happen?"
    m "There's also something weird with the bottom of this cloak. The edge is all bloody but there are two spots that are especially covered with blood. ..."
    l "So? Any conclusions?"
    m "Not yet, but checking it out again was an excellent idea."

    # [Black robe added to evidence] ?
    $ P_black_robe = Proof("Black Robe", 
                            "The right cuff is covered with blood, except for a strange missing pattern. The bottom also features two huge stains, parallel from each other.", 
                            "images/props/black_robe.png", 
                            R_F1fransksRoom, 
                            1300, 400, 
                            "black_robe_marks_cuff")
    $ addProofToInventory(P_black_robe)
    
    $ eventMgr.unlock("hotspot_black_cloth_recheck")
    jump room_loop

label hotspot_garage_car:
    m "No one's here..."
    l "The car's locked anyways, I doubt that Fransk's mom would trust him with it after THAT incident..."
    m "What incident?"
    l "Dude, you don't wanna know about it."
    m "... Isn't there some sort of switch to open the garage door?"
    l "Nah there ain't. There's a remote linked to the car keys though."
    m "It must be hidden in the parent's room..."
    l "Yeah, Fransk's mom probably wouldn't trust me there after the incident."
    m "I'll just take your word for it..."
    $ eventMgr.unlock("hotspot_garage_car")
    jump room_loop

label hotspot_garage_caulk_gun:
    m "Is that some sort of tube?"
    l "Dude, you haven't seen the videos? That's a caulk gun."
    m "A WHAT Gun?"
    l "Caulk... it's like a pasty... paste that you use to repair leaks and shit."
    m "Oh, like some kind of sealant?"
    l "Yeah exactly!"
    m "..."
    l "..."
    m "..."
    l "..."
    m "You fucking idiot! This was probably used to seal the locks shut!"
    l "Damn, for real?!"
    m "The bastard who did that is probably still here somewhere!"

    # [Caulk gun added to evidence] ?
    $ P_caulk_gun = Proof("Caulk Gun", 
                            "A caulk gun found on the garage floor, it was most definitely used to render the main door and garden door unusable.", 
                            "images/props/caulk_gun.png", 
                            R_garage, 
                            2300, 800, 
                            "caulk_gun")
    $ addProofToInventory(P_caulk_gun)
    
    $ eventMgr.unlock("hotspot_garage_caulk_gun")
    jump room_loop


# --- ENQUÊTE 5 : CHAMBRE DES PARENTS & MEURTRE DE FRANSK AU MANCHE ÉLECTRIQUE ---



label hotspot_fransk_bed_drawer:
    m "There's supposed to be a drawer hidden here... Ah! There's a slit by his bedside! !"
    l "What's that?"
    m "It's some sort of pumping system, there's an empty pouch here, we can assume it's for blood, since there's a fair amount of it left."
    l "This must be one of the pouches he planned on giving to Carm..."
    m "Had he just waited an hour or two... then Fransk would have woken up..."
    l "Maj, please. This couldn't have happened."
    m "... You're right."
    l "Look, I'll take this pouch right out so we can analyze it."
    m "No need, we're not qualified to analyze blood."
    l "Yeah, you're right, the texture of this thing is fun though!"
    m "... right."
    "{i}*squeeze*{/i}"
    l "AH WHAT THE FUCK!? I tried squeezing it and blood got into my fucking eyes! It's like it fucking pissed on me!"
    m "Let me check it out... I see, it's because of this tiny hole in the middle."
    l "Does the liquid drop down from there?"
    m "No, it usually flows through this back-check valve right here..."
    l "Isn't that hole weird then?"
    m "Definitely."

    # [Pierced IV pouch added to evidence] ?
    $ P_IV_pouch = Proof("Pierced IV pouch", 
                            "Part of Fransk's treatment, a tiny hole is punctured at the top.", 
                            "images/props/pierced_iv_pouch.png", 
                            R_F1fransksRoom, 
                            1800, 700, 
                            "blood_pouch")
    $ addProofToInventory(P_IV_pouch)

    m "Wait, what's this? It looks like some sort of remote holder... There's 3 slots..."
    l "His phone charger's wedged into this left one, so we can assume that he kept his phone there at night. There's a remote in this middle one... got it! What the fuck is that for?"
    m "Probably the blood dispenser, the brand's the same as the machine."
    l "Yeah, there's also a tag stuck with clear tape in the back that clearly says \"Frans'k IV valve."
    m "That clears it up!"
    l "The last slot is empty, probably was left that way too."
    m "I don't know, you never know what you can find."
    "Putting my fingers in there probably isn't the best idea, all I can feel is dust and lint and- ah-ha!"
    m "Jackpot!"
    l "Is that some kind of wrinkled paper?"
    m "Yeah, looks like it was fixed onto some remote using tape, but considering how dirty it is you can tell that it fell off ages ago. Now let's see... !"
    "My heart sinks as I start to read these simple words."
    m "\"Fransk's home automation remote\"..."
    l "Home... automation? Like a smart house?"
    m "These things can be rigged to control lights and speakers..."
    l "Are you saying-"
    m "The killer probably used this to kill Carmille and Fransk..."
    l "!"
    "The killer is among us, their timing was perfect. To think that they orchestrated everything using a simple remote..."
    m "Lou, we have to keep this between us."
    l "The killer didn't notice this tag, right?"
    m "Yes, we can use that information to our advantage."
    l "Alright."

    # [Smart house remote added to evidence]
    $ P_house_remote = Proof("Smart House Remote", 
                            "A missing remote for controlling smart house features.", 
                            "images/props/smart_house_remote.png", 
                            R_F1fransksRoom, 
                            1900, 750, 
                            "smart_home_remote")
    $ addProofToInventory(P_house_remote)
    
    $ eventMgr.unlock("hotspot_fransk_bed_drawer")
    jump room_loop

label hotspot_electric_door_handle:
    m "This handle..."
    l "I can't believe they used it to murder Fransk, it should be impossible..."
    m "How so?"
    l "Fransk's mom is a security freak, she's a top scientist that works for the government or something."
    m "Right..."
    l "So they rigged every door and handle to the alarm system."
    m "That's fucking reckless when considering Fransk's weakness to electricity:"
    l "Yeah, that's why they put little rubbery condom-things on every door handle! To absorb electricity or something!"
    m "That's clever, you keep all of the safety features without putting Fransk in danger..."
    l "Yeah but that condom thing's missing!"
    m "Any idea when that could've happened?"
    l "Fransk's room was always left open before the stabbing... so we couldn't have noticed."
    m "Yeah..."
    $ eventMgr.unlock("hotspot_electric_door_handle")
    jump room_loop

label hotspot_parent_room_mom_nightstand:
    m "*rummage rummage* Aside from Fransk's baby photos I don't see anything of value..."
    v "Really?! That's valuable enough!"
    m "Shut up... There's some candy if you want."
    l "Damn! These are really fucking good!"
    m "You can keep them, then."
    l "No! You have them!"
    m "?"
    l "Just give them to me when I do good! And call me a good boy when doing so!"
    m "If that's what you want..."
    "I should stuff him full of candy, he's been nothing but great tonight..."

    # [Hard Candy added to evidence]
    $ P_hard_candy = Proof("Hard Candy", 
                            "Delicious hard candy found in Fransk's mom's nightstand.", 
                            "images/props/hard_candy.png", 
                            R_F1parentsRoom, 
                            1000, 450, 
                            "hard_candy")
    $ addProofToInventory(P_hard_candy)
    
    $ eventMgr.unlock("hotspot_parent_room_mom_nightstand")
    jump room_loop

label hotspot_parent_room_dad_nightstand:
    m "Holy shit! This drawer's full of junk!"
    l "Yikes, this'll take a while to sort through..."
    m "Maybe it won't. There's a manual for a smart house remote. We have to check it out!"
    l "This is huge!"
    m "\"Thank you for choosing SureThings' home automation and security services!\""
    l "Skip to the good part!"
    m "\"The remote features 3 preset buttons. By linking the remote to the SureThings app using your remote's unique ID, you can easily modify those presets to fit your needs!\""
    l "Sh-Shit! What kind of features are there?"
    m "\"Shutting down every curtain for the night? Turn your living room into an impromptu nightclub? Arm your security systems before travelling? Maybe all of these at the same time? The custom presets will do it all at the press of a button!\" ..."
    "I start shuffling through the book, my eyes darting on particular phrases."
    m "\"Prevent robberies by delivering nasty electric shocks using our patented SureThings smart handles...\""
    m "\"No need to strain your voice! Use the automated announcement system to call those silly kids to dinner!...\""
    m "There's no doubt in my mind, they used the remote."
    l "Using a smart house to murder someone... *GULP*"
    m "What is it?"
    l "Could it be... that AI is taking over? And that the house itself decided to murder Fransk?"
    m "... Shut up..."
    $ eventMgr.unlock("hotspot_parent_room_dad_nightstand")
    jump room_loop