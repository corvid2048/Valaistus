define n = Character("Nero")
define s = Character("Soturi")
define k = Character("Konna")
define x = Character("???")
define god = Character("Axaris")
define cadriel = Character("Cadriel")
define aniel = Character("Aniel")
define katalaian_soldier = Character("Katalai Soldier")
define v = Character("Vesuvius")

define centerleft = Position(xpos=0.35, ypos=1.0)
define centerright = Position(xpos=0.65, ypos=1.0)

label start:
    scene bg_throne_room
    show god_placeholder
    god "“Come forth, my heroes! I have summoned you forth to this world to lead the forces of good into battle against the demons and devils of Katalai that threaten to plunge our divine kingdom of Valaistus into eternal darkness!”"
    hide god_placeholder
    show nero_placeholder at centerleft
    show soturi_placeholder at center
    show konna_placeholder at centerright
    "In the center of the throne room stand three heroes. Though they have only just arrived in this place, they appear unfazed."
    "Nero: He carries a heavy wooden staff, clearly intended for magic. It looks like it would hit quite hard in a pinch, though. His robes swirl in the wind. Glowing motes of dust seem to swirl around him." 
    "Soturi: They have a sharp, polished spear in one hand and a shield in the other. Strapped to their hip is a sword. Their armor appears well cared-for. Their heraldry is a deep royal purple and bright scarlet."
    "Konna: She carries a bow. Strapped to her back is a quiver of arrows. Her belt has several daggers tucked into it, and she seems like she would have more hidden elsewhere on her person. She wears light armor and a cloak."

menu:
    "Who are you?"
    "Nero":
        $ nero = True
        $ soturi = False
        $ konna = False
        hide soturi_placeholder
        hide konna_placeholder
    "Soturi":
        $ nero = False
        $ soturi = True
        $ konna = False
        hide nero_placeholder
        hide konna_placeholder
        show soturi_placeholder at centerleft with move
    "Konna":
        $ nero = False
        $ soturi = False
        $ konna = True
        hide nero_placeholder
        hide soturi_placeholder
        show konna_placeholder at centerleft with move

label character_chosen:
    show god_placeholder at centerright
    god "“Welcome to the armies of Valaistus. Katalai will not stand a chance with you in charge.”"
    god "“Your first task is a simple one.”"
    god "“You must journey to the Edge of the Skies to ensure the forces of Katalai remain at bay. If you find traces of their presence, take all necessary steps to eliminate them.”"

menu:
    "“As you wish, my liege.”":
        jump edge_of_skies
    "“I will not fail you.”":
        jump edge_of_skies
    "Nod silently.":
        jump edge_of_skies
    "Bow and leave.":
        jump edge_of_skies

label edge_of_skies:
    hide god_placeholder
    hide nero_placeholder
    hide soturi_placeholder
    hide konna_placeholder
    scene bg_edge_of_skies_placeholder
    show angel_soldier_left_placeholder at centerleft
    show angel_soldier_right_placeholder at centerright
    if nero == True:
        show nero_placeholder at center
    if soturi == True:
        show soturi_placeholder at center
    if konna == True:
        show konna_placeholder at center
    "The Edge of the Skies is a vast, empty expanse where the clouds beneath your feet disappear into naught but open sky. The wind howls around you, and the sun shines brightly overhead."
    $ edge_of_skies_described = False
    $ katalai_signs_explained = False

menu:
    "Look around." if edge_of_skies_described is not True:
        $ edge_of_skies_described = True
        $ didnt_look_around = False
        jump edge_of_skies_description
    "Ask what signs of Katalai's presence to look for." if katalai_signs_explained is not True:
        $ katalai_signs_explained = True
        $ didnt_look_around = False
        jump edge_of_skies_katalai_signs
    "Begin your search for Katalaian forces." if edge_of_skies_described is True and katalai_signs_explained is True:
        jump edge_of_skies_search
    "This isn't my problem. Leave.":
        $ didnt_look_around = True
        $ injured_soldier_met = False
        $ injured_soldier_killed = False
        $ investigate_breach_edge_of_skies = False
        $ follow_footprints_edge_of_skies = False
        jump return_to_palace_edge_of_skies

label edge_of_skies_description:
    "You can see far below you a dense forest of thick black, brown, and red leaves. A pungent smell of smoke and sulfur wafts up from the forest with each gust of wind."
    "Along the edge of the clouds, a nearly transparent barrier of light golden light shimmers in the wind. It seems to be a magical barrier. While it might've once been strong enough to keep the forces of Katalai at bay, it is now broken in several places."
    "Behind you, an army of angelic soldiers stand at attention, their wings spread wide and their weapons at the ready."
    "They put on a brave face, but you can see the exhaustion in their eyes. They have been fighting the forces of Katalai for a long time, and they are weary."
    
menu:
    "Look around." if edge_of_skies_described is not True:
        $ edge_of_skies_described = True
        $ didnt_look_around = False
        jump edge_of_skies_description
    "Ask what signs of Katalai's presence to look for." if katalai_signs_explained is not True:
        $ katalai_signs_explained = True
        $ didnt_look_around = False
        jump edge_of_skies_katalai_signs
    "Begin your search for Katalaian forces." if edge_of_skies_described is True and katalai_signs_explained is True:
        jump edge_of_skies_search
    "This isn't my problem. Leave.":
        $ didnt_look_around = True
        $ injured_soldier_met = False
        $ injured_soldier_killed = False
        $ investigate_breach_edge_of_skies = False
        $ follow_footprints_edge_of_skies = False
        jump return_to_palace_edge_of_skies

label edge_of_skies_katalai_signs:
    if nero == True:
        n "“Tell me what signs Katalai's soldiers leave behind.”"
    if soturi == True:
        s "“What signs should I look for to know if Katalaian soldiers are nearby?”"
    if konna == True:
        k "“Tell me what signs I should take note of to detect Katalaian presence.”"
    aniel "“Their clawed footprints stain the white clouds grey. Their blood is a deep oily black, and it turns the land we stand upon into thunderclouds.”"
    cadriel "“Their weapons are crude and jagged, and they are often covered in the golden ichor of my angelic bretheren. Most are not skilled warriors, but they are numerous and relentless.”"
    cadriel "“Their generals posess overwhelming power. They will not stop until they have destroyed everything in their path.”"
    aniel "“These signs are unmistakable, but there are other, more subtle signs that you may encounter. If you see shards of broken light, check that the wall has not been breached.”"
    aniel "“Some of Katalai's soldiers are skilled in magic, and they will use it to break through our defenses. Others among their numbers are small and stealty, leaving only the faintest traces of their presence.”"
    cadriel "“With a keen enough eye, you may be able to spot the single feather, the single scale, the single hair they have left half-buried in the ground.”"
    aniel "“Vigilance is key. If you see any of these signs, you must take all necessary steps to eliminate them. Do not let them reach the lands of Valaistus. If they do, it will be the end of our world.”"
    
menu:
    "Look around." if edge_of_skies_described is not True:
        $ edge_of_skies_described = True
        $ didnt_look_around = False
        jump edge_of_skies_description
    "Ask what signs of Katalai's presence to look for." if katalai_signs_explained is not True:
        $ katalai_signs_explained = True
        $ didnt_look_around = False
        jump edge_of_skies_katalai_signs
    "Begin your search for Katalaian forces." if edge_of_skies_described is True and katalai_signs_explained is True:
        jump edge_of_skies_search
    "This isn't my problem. Leave.":
        $ didnt_look_around = True
        $ injured_soldier_met = False
        $ injured_soldier_killed = False
        $ investigate_breach_edge_of_skies = False
        $ follow_footprints_edge_of_skies = False
        jump return_to_palace_edge_of_skies

label edge_of_skies_search:
    "You begin your search for Katalai's forces by following along the golden barrier. You keep your eyes peeled for any signs of their presence, and you are careful to avoid any areas that seem particularly dangerous."
    "After some time, you spot a handful of glittering shards of broken light. You approach them cautiously, and you see that they are indeed the remnants of a breach in the barrier."

menu:
    "Investigate the breach.":
        $ investigate_breach_edge_of_skies = True
        jump investigate_breach_edge_of_skies
    "Return to the palace to report your findings.":
        $ investigate_breach_edge_of_skies = False 
        $ follow_footprints_edge_of_skies = False
        $ injured_soldier_met = False
        $ injured_soldier_killed = False
        jump return_to_palace_edge_of_skies

label investigate_breach_edge_of_skies:
    "The wall here appears to have been shattered by a powerful force, and you can see small grey footprints and tiny black specks leading away from the breach."

menu:
    "Follow the footprints.":
        $ follow_footprints_edge_of_skies = True
        jump follow_footprints_edge_of_skies
    "Return to the palace to report your findings.":
        $ follow_footprints_edge_of_skies = False
        $ injured_soldier_met = False
        $ injured_soldier_killed = False
        jump return_to_palace_edge_of_skies

label follow_footprints_edge_of_skies:
    "The footprints follow a long, winding path through the clouds. You follow them for some time, and eventually you come to a small cave hidden among the clouds. The edge of the cave is stained a dark grey, nearly black. The footprints lead inside."
    scene bg_cave_placeholder
    hide angel_soldier_left_placeholder
    hide angel_soldier_right_placeholder
    hide nero_placeholder
    hide soturi_placeholder
    hide konna_placeholder
    if nero == True:
        show nero_placeholder at center
    if soturi == True:
        show soturi_placeholder at center
    if konna == True:
        show konna_placeholder at center
    "Inside the cave is a shockingly tight squeeze. Your angelic armies are unable to follow you inside, but you press on. The cave is dark and damp, and the air is thick with the smell of sulfur."
    "You can hear faint sounds echoing from deeper within the cave."
    "You follow the sounds, and eventually you come to a small chamber. Inside, you see just one Katalai soldier, surrounded by a number of their fallen comrades."
    $ injured_soldier_met = True
    if nero == True:
        show nero_placeholder at centerleft with move
    if soturi == True:
        show soturi_placeholder at centerleft with move
    if konna == True:
        show konna_placeholder at centerleft with move
    show vesuvius_placeholder at centerright
    "The soldier is badly injured, and they are clearly struggling to stay alive. They look up at you with fear in their eyes."

menu:
    "“Hey! Calm down. I'm not going to hurt you.”":
        $ injured_soldier_killed = False
        jump edge_of_skies_katalaian_soldier
    "Attack the soldier.":
        $ injured_soldier_killed = True
        "The soldier lets out a final, pitiful cry as you strike them down. Their body falls to the ground with a sickening thud."
        jump edge_of_skies_leave_cave

label edge_of_skies_katalaian_soldier:
    "The soldier does not seem to trust you, but knows they can't escape. They take a deep breath and speak."
    katalaian_soldier "“Please... don't hurt me. I'm just trying to survive.”"
    katalaian_soldier "“I was sent here to scout the area, but even getting past your defenses was a challenge. I barely made it to this cave alive.”"
    katalaian_soldier "“I don't want to fight anymore. I just want to go home.”"
    katalaian_soldier "“Please... let me go. I won't tell anyone you were here. I promise.”"
menu:
    "“I won't tell anyone you were here.”":
        $ injured_soldier_killed = False
        katalaian_soldier "“Thank you. I won't forget this.”"
        katalaian_soldier "“Call me Vesuvius, friend.”"
        jump edge_of_skies_leave_cave
    "“How can I trust you?”":
        katalaian_soldier "“I understand your hesitation. Would it help if I told you more about me?”"
        katalaian_soldier "“My name is Vesuvius. I was born in Katalai, but I never wanted to be a soldier. I was conscripted into the army two years ago. I was fourteen at the time, and I was terrified. I didn't know what to do, and I didn't want to die.”"
        v "“I still don't want to die. The war between our nations has caused so much suffering. Katalai does not hate Valaistus. We do not want to fight. All we want is to be able to live in peace.”"
        v "“I've seen and done things that I regret, and I want to make amends for them.”"
        v "“I know I can't undo the past, but I can try to make a better future. Please, let me go. I won't tell anyone you were here.”"
        v "“Please...”"
        menu:
            "“I'm sorry. I can't let you live.”":
                $ injured_soldier_killed = True
                "The soldier lets out a final, pitiful cry as you strike them down. Their body falls to the ground with a sickening thud."
                jump edge_of_skies_leave_cave
            "“I won't hurt you.”":
                $ injured_soldier_killed = False
                v "“Thank you. I won't forget this.”"
                jump edge_of_skies_leave_cave
    "“I can't let you go. You are a threat to Valaistus.”":
        $ injured_soldier_killed = True
        "The soldier lets out a final, pitiful cry as you strike them down. Their body falls to the ground with a sickening thud."
        jump edge_of_skies_leave_cave

label edge_of_skies_leave_cave:
    scene bg_edge_of_skies_placeholder
    hide vesuvius_placeholder
    show angel_soldier_left_placeholder at centerleft
    show angel_soldier_right_placeholder at centerright
    if nero == True:
        show nero_placeholder at center
    if soturi == True:
        show soturi_placeholder at center
    if konna == True:
        show konna_placeholder at center
    "You leave the cave and return to your angelic army."
    if nero == True:
        n "“There is no longer a single living soul within this cave.”"
        n "“The Katalaian threat has been held at bay.”"
        n "“We must return to the palace and report back immediately. Lord Axaris will want to hear of this.”"
    if soturi == True:
        s "“There is no longer a single living soul within this cave.”"
        s "“The Katalaian threat has been held at bay.”"
        s "“We must return to the palace and report back immediately. Lord Axaris will want to hear of this.”"
    if konna == True:
        k "“There is no longer a single living soul within this cave.”"
        k "“The Katalaian threat has been held at bay.”"
        k "“We must return to the palace and report back immediately. Lord Axaris will want to hear of this.”"

label return_to_palace_edge_of_skies:
    scene bg_throne_room
    hide angel_soldier_left_placeholder
    hide angel_soldier_right_placeholder
    hide nero_placeholder
    hide soturi_placeholder
    hide konna_placeholder
    if nero == True:
        show nero_placeholder at centerleft
    if soturi == True:
        show soturi_placeholder at centerleft
    if konna == True:
        show konna_placeholder at centerleft
    show god_placeholder at centerright
    "You return to the palace to report your findings to Axaris and his advisors."
    god "“Welcome back, my hero. What news do you bring?”"
    if didnt_look_around is True:
        if nero == True:
            n "“I did not find any signs of Katala's presence. The Edge of the Skies is as secure as ever.”"
            jump edge_of_skies_report_complete
        if soturi == True:
            s "“I didn't detect any sign of Katala's soldiers invading through the Edge of the Skies”"
            jump edge_of_skies_report_complete
        if konna == True:
            k "“It is all quiet at the Edge of the Skies.”"
            jump edge_of_skies_report_complete
    if investigate_breach_edge_of_skies is True:
        if nero == True:
            n "“I found a breach in the barrier. There were Katalaian footprints leading away from it.”"
        if soturi == True:
            s "“I found a breach in the barrier. There were Katalaian footprints leading away from it.”"
        if konna == True:
            k "“I found a breach in the barrier. There were Katalaian footprints leading away from it.”"
    if follow_footprints_edge_of_skies is True:
        if nero == True:
            n "“I followed the footprints and found a cave with several Katalaians.”"
        if soturi == True:
            s "“I followed the footprints and found a cave with several Katalaians.”"
        if konna == True:
            k "“I followed the footprints and found a cave with several Katalaians.”"

if injured_soldier_met is True:
    menu:
        "“They were all dead on arrival.” (lie)":
            jump edge_of_skies_report_complete
        "“Most were dead when I got there, but I killed the survivors.” (truth)" if injured_soldier_killed is True:
            jump edge_of_skies_report_complete
        "“Most were dead when I got there, but I killed the survivors.” (lie)" if injured_soldier_killed is not True:
            jump edge_of_skies_report_complete

label edge_of_skies_report_complete:
    god "“I see. Thank you for your report, my hero. You have done well.”"
    god "“You have proven yourself to be a capable and trustworthy leader. I am proud to have you in my service.”"



return