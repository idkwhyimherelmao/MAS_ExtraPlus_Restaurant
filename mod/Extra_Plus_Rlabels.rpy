init python:
    mas_override_label("walk_extra", "walk_extra2")

label walk_extra2:
    show monika staticpose at t21
    python:
        monika_talk = renpy.substitute(renpy.random.choice(date_talk))
        walk_menu = []
        walk_menu.append((_("Cafe"), "cafe"))
        walk_menu.append((_("Restaurant"), "restaurant"))
        walk_menu.append((_("Nevermind"), "nevermind"))

        renpy.say(m, monika_talk, interact=False)
        playerchoice = renpy.display_menu(walk_menu, screen="talk_choice")

    if playerchoice == "restaurant":
        show monika at t11
        jump go_to_restaurant
    elif playerchoice == "nevermind":
        jump return_extra
    return

label restaurant_init:
    $ HKBHideButtons()
    hide screen chibika_chill
    hide monika
    scene black
    with dissolve
    pause 2.0
    call mas_background_change(submod_background_restaurant, skip_leadin=True, skip_outro=True)
    show monika 1eua at t11
    $ HKBShowButtons()
    jump restaurant_cakes
    
label restaurant_talkdemo:
    show monika staticpose at t21
    $ rng_global = renpy.random.randint(1,2)
    if rng_global == 1:
        python:
            cafe_menu = []
            cafe_menu.append((_("How are you doing, [m_name]?"), "t1"))
            cafe_menu.append((_("If you could live anywhere, where would it be?"), "t2"))
            cafe_menu.append((_("What would you change about yourself if you could?"), "t3"))
            cafe_menu.append((_("Can we leave?"), "t4"))
            cafe_menu.append((_("Next"), "next"))
            cafe_menu.append((_("Nevermind"),"nevermind"))

            playerchoice = renpy.display_menu(cafe_menu, screen="talk_choice")

        if playerchoice == "t1":
            jump extra_talk_doing1
        elif playerchoice == "t2":
            jump extra_talk_live
        elif playerchoice == "t3":
            jump extra_talk_change
        elif playerchoice == "t4":
            jump cafe_leave
        elif playerchoice == "next":
            jump cafe_talkdemonext
        elif playerchoice == "nevermind":
            jump to_cafe_loop
        return

    elif rng_global == 2:
        python:
            cafe_menu = []
            cafe_menu.append((_("How are you doing, [m_name]?"), "t1"))
            cafe_menu.append((_("If you were a super-hero, what powers would you have?"), "t2"))
            cafe_menu.append((_("Do you have a life motto?"), "t3"))
            cafe_menu.append((_("Can we leave?"), "t4"))
            cafe_menu.append((_("Next"), "next"))
            cafe_menu.append((_("Nevermind"),"nevermind"))

            playerchoice = renpy.display_menu(cafe_menu, screen="talk_choice")

        if playerchoice == "t1":
            jump extra_talk_doing2
        elif playerchoice == "t2":
            jump extra_talk_superhero
        elif playerchoice == "t3":
            jump extra_talk_motto
        elif playerchoice == "t4":
            jump cafe_leave
        elif playerchoice == "next":
            jump cafe_talkdemonext
        elif playerchoice == "nevermind":
            jump to_cafe_loop
    return

label cafe_talkdemonext:
    show monika staticpose at t21
    $ rng_global = renpy.random.randint(1,2)
    if rng_global == 1:
        python:
            cafenext_menu = []
            cafenext_menu.append((_("Aside from necessities, what's the one thing you couldn't go a day without?"), "t5"))
            cafenext_menu.append((_("Is your glass half full or half empty?"), "t6"))
            cafenext_menu.append((_("What annoys you most?"), "t7"))
            cafenext_menu.append((_("Previous"), "previous"))
            cafenext_menu.append((_("Nevermind"),"nevermind"))

            playerchoice = renpy.display_menu(cafenext_menu, screen="talk_choice")

        if playerchoice == "t5":
            jump extra_talk_without
        elif playerchoice == "t6":
            jump extra_talk_glass
        elif playerchoice == "t7":
            jump extra_talk_annoy
        elif playerchoice == "previous":
            jump cafe_talkdemo
        elif playerchoice == "nevermind":
            jump to_cafe_loop
        return

    elif rng_global == 2:
        python:
            cafenext_menu = []
            cafenext_menu.append((_("Describe yourself in three words."), "t5"))
            cafenext_menu.append((_("What do you think is the first thing to pop into everyone's minds when they think about you?"), "t6"))
            cafenext_menu.append((_("If you were an animal, what animal would you be?"), "t7"))
            cafenext_menu.append((_("Previous"), "previous"))
            cafenext_menu.append((_("Nevermind"),"nevermind"))

            playerchoice = renpy.display_menu(cafenext_menu, screen="talk_choice")

        if playerchoice == "t5":
            jump extra_talk_3words
        elif playerchoice == "t6":
            jump extra_talk_pop
        elif playerchoice == "t7":
            jump extra_talk_animal
        elif playerchoice == "previous":
            jump cafe_talkdemo
        elif playerchoice == "nevermind":
            jump to_cafe_loop
        return

    screen restaurant_loop():
        if monika_chr.is_wearing_acs(extraplus_acs_remptyplate):
            pass
        else:
            timer 900.0 action [Hide("restaurant_loop"), Jump("monika_no_food")]

label to_restaurant_loop:
    show monika staticpose at t11
    call screen restaurant_loop
    return
