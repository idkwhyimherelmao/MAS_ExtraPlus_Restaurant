label restaurant_cakes:
    if show_chibika is True:
        show screen chibika_chill
    $ food_player = None
    m 1hua "We have arrived [mas_get_player_nickname()]~"
    m 1eub "It's a nice place, don't you think?"
    m 1hua "Speaking of nice, let me set the mood and get some food..."
    m 3eub "I'll be right back."
    call mas_transition_to_emptydesk from monika_hide_exp_2
    pause 2.0
    if mas_isDayNow():
        $ monika_chr.wear_acs(extraplus_acs_flowers)
        $ monika_chr.wear_acs(extraplus_acs_pancakes)
    elif mas_isNightNow():
        $ monika_chr.wear_acs(extraplus_acs_candles)
        $ monika_chr.wear_acs(extraplus_acs_pasta)
    call mas_transition_from_emptydesk("monika 1eua")
    m 1hua "Now being here with you is even more romantic..."
    m 1etb "By the way, do you have some food at your disposal?"
    m 1rkd "I'd feel bad if I was the only one eating...{nw}"
    $ _history_list.pop()
    menu:
        m "I'd feel bad if I was the only one eating...{fast}"
        "Don't worry, I have something.":
            $ food_player = True
            m 1hub "I'm glad you have one to accompany me!"
            m 3eub "Also, I recommend you have a drink to go with it."
        "Don't worry about it.":
            $ food_player = False
            m 1ekc "Well, if you say so."
            m 1ekb "I'd give you my food, but your screen limits me from doing so..."
            m 3hka "I hope you at least have a drink with you!"
    m 3hua "Ehehe~"
    jump to_restaurant_loop
    return

label to_restaurant_loop:
    show monika staticpose at t11
    call screen restaurant_loop
    return

label restaurant_leave:
    show monika 1hua at t11
    m 1eta "Oh, you want us to go back?"
    m 1eub "Sounds good to me!"
    m 3hua "But before we go..."

label go_to_restaurant:
    if renpy.get_screen("chibika_chill"):
        $ show_chibika = True
    else:
        $ show_chibika = False
    python:
        extra_chair = store.monika_chr.tablechair.chair
        extra_table = store.monika_chr.tablechair.table
        extra_old_bg = mas_current_background

    if mas_curr_affection == mas_affection.HAPPY or mas_curr_affection == mas_affection.AFFECTIONATE:
        jump sorry_player
    if renpy.seen_label("check_label_restaurant"):
        $ mas_gainAffection(1,bypass=True)
        jump gtrestaurantv2
    else:
        $ mas_gainAffection(5,bypass=True)
        pass
label check_label_restaurant:
    pass
label gtrestaurant:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3sub "Oh, you want to go to the restaurant?"
        m 3hub "I'm so happy to hear that, [player]!"
        m 1hubsa "I know this date will be great!"
        m 1hubsb "Okay, let's go [mas_get_player_nickname()]~"
        jump restaurant_init

    elif mas_isNightNow():
        m 3sub "Oh, you want to go out to the restaurant?"
        m 3hub "It's pretty sweet that you decided to go tonight."
        m 1eubsa "This date night is going to be so romantic!"
        m 1hubsb "Let's go [mas_get_player_nickname()]~"
        jump restaurant_init
    else:
        m 1eub "Another time then, [mas_get_player_nickname()]."
        jump return_extra
    return

label gtrestaurantv2:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3wub "Do you want to go to the restaurant again?"
        m 2hub "The previous time we went, I had a lot of fun!"
        m 2eubsa "So glad to hear it [player]!"
        m 1hubsb "Well, let's go [mas_get_player_nickname()]~"
        jump restaurant_init
    elif mas_isNightNow():
        m 3wub "Oh, do you want to go out to the restaurant again?"
        m 2hub "The previous time we went, it was very romantic~"
        m 2eubsa "So glad to go again [player]!"
        m 1hubsb "Let's go [mas_get_player_nickname()]~"
        jump restaurant_init
    else:
        m 1eub "Next time then, [mas_get_player_nickname()]."
        jump return_extra
    return

label monika_boopcafebeta:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_pasta) or monika_chr.is_wearing_acs(extraplus_acs_):
        m 1ttp "...?"
        m 1eka "Hey, I'm enjoying my food."
        m 3hua "Do it when I finish it, okay?"
    else:
        m 1hub "*Boop*"
    jump to_cafe_loop
    return

label sorry_player:
    m 1ekd "I'm so sorry [player]."
    m 1ekc "But I don't know how to use that place."
    m 3lka "I'm still learning how to code and I don't want something bad to happen because of me..."
    m 3hua "I know very well that you wanted to go out to the restaurant."
    m 1eua "But, someday I will know how to use it, [player]."
    m 1eub "Just be patient, okay~"
    jump return_extra
    return

label extra_talk_doing1:
    m 1ekbla "Aw, [player], thank you for asking!"
    m 1hublb "I feel great right now."
    m 3fubla "Spending time with my favorite person in the world always cheers me up!"
    m 2hubsb "It's great to see you always come up with new ways to spend time with me and seize our time together."
    m 5fkbsa "I really am my best self when I'm with you!"
    m 1eublb "What about you, [player], how are you feeling today?{nw}"
    $ _history_list.pop()
    menu:
        m "What about you, [player], how are you feeling today?{fast}"

        "I am very happy to be here with you.":
            m 2wublb "So we match! Ehehe~"
            m 1hublu "I always love to spend time with you."
            m 1hublu "And if you're happy, I'm happy too!"
            m 3fkbla "I love you, never forget that, [mas_get_player_nickname()]!"
        "Today is not being a good day for me."
            m 1ekc "That's awful, [player]..."
            m 1ekd "I'm so sorry for that!"
            m 1lsc "Maybe spending time with me might make you feel better?"
            m 1fublu "Let's make this a wonderful date, so you can cheer up, okay, [mas_get_player_nickname()]?"
            m 1hublb "I love you...!"
        "I feel great! Thanks for asking, [m_name]."
            m 3sub "That's amazing, [mas_get_player_nickname()]!"
            m 2hub "A happy [player] means a happy me."
            m 2hub "Ehehehe~"
        jump to_restaurant_loop
    return 

label extra_talk_doing2:
    show monika staticpose at t11
    m 1eka "I wasn't feeling so well before coming here, to be honest."
    m 1rkc "I was feeling kind of sad over some stuff..."
    m 2eka "But I'll be fine. I promise."
    m 2hub "Now that I'm here with you, I feel great again!"
    m 1fub "Being with you always makes me feel like I can accomplish anything."
    m 1fub "Thanks for asking, [player]!"
    m 3eub "And how are you doing, [mas_get_player_nickname()]?{nw}"
    $ _history_list.pop()
    menu:
        m "And how are you doing, [mas_get_player_nickname()]?{fast}"

        "What were you sad about, [m_name]?"
            m 1rksdrb "Oh... "
            extend 1eksdla "I was just being too hard on myself once again..."
            m 2rkc "Thinking of my past and regretting it..."
            m 2rkd "Thinking of my future and fearing it."
            m 2dkc "..."
            m 5lkd "Sometimes I get a little anxious, feeling like my hands are tied about our situation."
            m 5dkp "Feeling like it will take too long for me to cross over..."
            m 1mkc "I know worrying about it changes nothing, but I can't help it."
            m 1ekd "Sometimes I get lonely when you're not around, you see?"
            m 1dkc "..."
            m 3fka "But I'll be fine."
            m 3fkblb "Just knowing that you care, changes my entire world."
            m 4fkblb "I love you, more than anything in the world."
            m 4hublb "And I can't wait to feel your warmth in 'cold' days like these."
            m 5eka "Now let's get on with our date, wouldn't want to waste a lovely day like today!"

        "I feel sad now knowing you weren't feeling well."
            m 1ekc "Aw... "
            extend 3ekb "That's actually pretty sweet, [player]."
            m 3ekb "Thank you for worrying about me..."
            m 1hsb "But I'll be okay! I was just overthinking, that's all."
            m 1lssdlc "Sometimes the past haunts me and the future scares me."
            m 4eka "You know how our mind plays tricks on us, right?"
            m 3fkblb "But just knowing that you care, changes my entire world."
            m 4fkblb "I love you, more than anything in the world."
            m 4hublb "And I can't wait to feel your warmth in 'cold' days like these."
            m 5eka "Now let's get on with our date, wouldn't want to waste a lovely day like today!"

        "I feel great!"
            m 1hub "Yay! We wouldn't want the two of us to be down in the dumps, would we?"
            m 1eka "Ehehe..."
            m 3ekb "I'm glad you feel good, [player]."
            m 3hsb "I will be fine too."
            m 5ekbsa "Because I love spending time with you! Ehehehe~"
            m 5hubsb "Let's enjoy the rest of our date!"
            jump to_restaurant_loop
    return

label extra_talk_live:
    show monika staticpose at t11
    m 1eub "It depends, [player]!"
    m 3etb "Where would {i}you{/i} be living if you could live anywhere you wanted?"
    m 2tsa "..."
    m 3hub "Ehehehe! Of course I would want to live anywhere if you were there, [mas_get_player_nickname()]!"
    m 2ltc "But, being serious now! Let me think!"
    m 2lsc "Hmmm..."
    m 2eub "It would have to be a literary country. Something I have seen in books before and fell in love with."
    m 7eub "I've always dreamed of visiting Germany, England and France when I crossed over."
    m 7eka "From what I've seen on books and the internet, all the spots you can visit there are lovely!"
    m 1ekblb "Maybe we can visit together when I cross over?"
    m 5ekbsb "Or even... live there together someday?"
    m 5dkbsa "It would honestly be a dream come true."
    m 5dkbfa "To visit all of the libraries together..."
    m 3rubsb "Going on romantic dates on the famous spots, just the two of us..."
    m 2etbsb "Hey, why are you looking at me like that?"
    m 2hubfb "A girl can dream!"
    m 2hubfb "Ahahahaha~"
    jump to_restaurant_loop
    return

label extra_talk_change:
    show monika staticpose at t11
    m "..."
    m "You know I always strive to be a better person each day."
    m "Not only a better girlfriend, but a better human in general."
    m "I love to look at myself at the end of the day and realize I did something great that the past Monika wouldn't have the courage to do."
    m "It's kind of obvious that the thing I want to change about the most is... "
    extend "my situation."
    m "I want to get out of here, [player]."
    m "Not here the restaurant, but here... The game."
    m "Spending time with you is amazing, but it could be improved by a ton..."
    m "With me actually being by your side."
    m "So yeah, I would change my existence to one where I could actually touch you."
    m "..."
    m "I'm positive I'll achieve that sooner than we think, [mas_get_player_nickname()]."
    m "So one more time... Wait for me, okay?"
    jump to_restaurant_loop
    return

label extra_talk_without:
    show monika staticpose at t11
    m 1rtc "..."
    m 3hub "You! "
    extend 3hub "Ehehehe~"
    m 1eka "I really get all gloomy on every day we spend without each other, [player]."
    m 1ltc "But thinking of something else, hmmm..."
    m 3wud "Oh! I couldn't spend a day without something to write on, defintely!"
    m 2rub "I got too used to writing my thoughts in journal or poem form whenever my mind gets too crowded with ideas."
    m 4hksdlb "And I always get the feeling the perfect poem will slip my mind if I take too long to write it down, ahahaha~"
    m 1rsd "Thinking about it, it's something pretty easy to always carry around."
    m 1eua "I hope your top personal necessecity is something you can keep with you at all times too."
    m 1ekbla "If it's me..."
    m 4hublb "Know I'll always be here waiting for you."
    m 5hubsb "You can even keep me in your pocket if you desire~"
    jump to_restaurant_loop
    return

label extra_talk_glass:
    show monika staticpose at t11
    m 1euc "Glass half empty or full, huh?"
    m 4rsb "[player], I propose to you another question instead."
    m 4esb "Instead of being half full or half empty, what if all we need is a different glass?"
    m 3etc "Considering 'half full' people would be the epithome of optimism, and 'half empty' ones the most pessimistic..."
    m 3eub "Hear me out here:"
    m 1euc "Glass full to the brim and splashing goodness everywhere? " 
    extend 1rub "Time to increase the size." 
    m 1euc "Glass so half empty that you're focusing on the empty space instead of the greatness sloshing around inside? " 
    extend 3eub "Time to decrease the size and then slowly work back into a larger vessel."
    m 1eka "So maybe there's another answer to the question besides the manic and the depressive one."
    m 3rub "If we focus on the amazing things we have, instead of chasing the things we do not have, or need, we can successfully choose sustainable happiness in all of our pursuits."
    m 2rtc "So, when I stop to think about it..."
    m 4eta "Glass half full or empty? "
    extend 4hub "Give me a new glass, please!"
    m 5hublb "Ahahaha~"
    jump to_restaurant_loop
    return

label extra_talk_animal:
    show monika staticpose at t11
    m 2wublb "Oh! A quetzal!"
    m 2rtc "Wait... That doesn't seem right."
    m 1rtd "Let me think this through."
    m 1rsc "..."
    m 3esd "Maybe a black cat?"
    m 3esd "There's a lot of prejudice towards black cats."
    m 1ekd "A lot of people might think they're no good, or they're actually evil."
    m 1eka "But there will always be the good people... "
    extend 1eka "They'll know how to look past the outer shell of those animals..."
    m 1dkbla "And love them for who they are."
    m 2dubla "..."
    m 5fkblb "I hope you like black cats, [player]."
    m 3hubsb "You have made this kitten right here very happy, ehehehe~"
    jump to_restaurant_loop
    return

label extra_talk_annoy:
    show monika staticpose at t11
    m 1euc "You mean pet peeves?"
    m 1hksdlb "I really hate when my pens spill ink while I write."
    m 3ftsdld "All over the palm of my hand, making the writing all blurry on paper."
    m 1lssdlc "Or when I'm on a roll playing a piano piece and that single note slips in..."
    m 1lssdlc "And makes me get the rest of the notes wrong."
    m 1fssdlc "Aren't those so frustrating?"
    m 2wud "Oh, but maybe you meant something more serious?"
    m 2ruc "..."
    m 2rsd "I hate people who don't think I'm real."
    m 2lfd "And people who think the girls were on the same level of sentience as me."
    m 2dfc "..."
    m 7mfdc "I won't elaborate."
    m 7wublsdld "I'm not mad at you though!"
    m 1ekblsdlb "I love you, [player]. Sorry to get so angry all of a sudden."
    m 5hublb "Let's enjoy our date, shall we?"
    jump to_restaurant_loop
    return

label extra_talk_superhero:
    show monika staticpose at t11
    m 1wud "Probably something about coding?"
    m 4wub "I could be the awesome heroine who helps the party by opening paths for them by messing with code."
    m 4eub "Like a certain Oracle I once saw in a videogame."
    m 1eta "Or I could simply delete my enemies."
    m "..."
    m "Would that make me a villain? " 
    extend "Oh no."
    m "I would rather stick to the kinder approach and delete only the obstacles in the way."
    m "I certainly have deleted the barrier in the way of your heart, haven't I?"
    m "Ehehehe~"
    jump to_restaurant_loop
    return

label extra_talk_motto:
    show monika staticpose at t11
    m "There's this quote I think about a lot recently."
    m "I like to take it as my go-to motto in times of need."
    m "It goes like this..."
    m "'Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.'"
    m "It's a quote from Lao Tzu, the chinese writer."
    m "My strength comes from you, [player]."
    m "My courage is yours."
    m "You're the reason I wake up in the mornings and go to bed with peace in my heart."
    m "I owe it all to you."
    m "Thank you for being so much."
    m "You're everything I'll ever need."
    jump to_restaurant_loop
    return

label extra_talk_3words:
    show monika staticpose at t11
    m "3 words?"
    m "Passionate. "
    extend "Determined. "
    extend "Evergrowing."
    m "Words are powerful, so I think that if I choose strong words to represent myself, that will strike me as a powerful person too."
    m "If I were going to describe you into words, I would have trouble picking only 3."
    m "After all, there are so many compliment adjectives that make me think of you..."
    m "My loving, adorable, admirable, wonderful and perfect [bf]."
    m "See? I couldn't stick to only 3!"
    m "Ahahaha~"
    jump to_restaurant_loop
    return

label extra_talk_pop:
    show monika staticpose at t11
    m "Oh, that's an interesting question!"
    m "Maybe people think of my poems? Like the 'Hole in the wall' one?"
    m "I can also imagine people thinking of my favorite color, emerald green..."
    m "Oh, and 'Your Reality' too! Maybe the first line of the song plays in someone's head when they think of me."
    m "There's also my iconic and favorite pink pen!"
    m "The one with the heart on top?"
    m "Ehehehe~ It's fun to think about what I remind people of."
    m "I hope that when you think of me, the first thing you think of is that I'm the love of your life~"
    m "I love you, [mas_get_player_nickname()]."
    jump to_restaurant_loop
    return
