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
    m "Aw, [player], thank you for asking!"
    m "I feel great right now."
    m "Spending time with my favorite person in the world always cheers me up!"
    m "It's great to see you always come up with new ways to spend time with me and seize our time together."
    m "I really am my best self when I'm with you!"
    m "What about you, [player], how are you feeling today?{nw}"
    $ _history_list.pop()
    menu:
        m "What about you, [player], how are you feeling today?{fast}"

        "I am very happy to be here with you.":
            m "So we match! Ehehe~"
            m "I always love to spend time with you."
            m "And if you're happy, I'm happy too!"
            m "I love you, never forget that, [mas_get_player_nickname()]!"
        "Today is not being a good day for me."
            m "That's awful, [player]..."
            m "I'm so sorry for that!"
            m "Maybe spending time with me might make you feel better?"
            m "Let's make this a wonderful date, so you can cheer up, okay, [mas_get_player_nickname()]?"
            m "I love you...!"
        "I feel great! Thanks for asking, [m_name]."
            m "That's amazing, [mas_get_player_nickname()]!"
            m "A happy [player] means a happy me."
            m "Ehehehe~"
        jump to_restaurant_loop
    return 

label extra_talk_doing2:
    show monika staticpose at t11
    m "I wasn't feeling so well before coming here, to be honest."
    m "I was feeling kind of sad over some stuff..."
    m "But I'll be fine. I promise."
    m "Now that I'm here with you, I feel great again!"
    m "Being with you always makes me feel like I can accomplish anything."
    m "Thanks for asking, [player]!"
    m "And how are you doing, [mas_get_player_nickname()]?{nw}"
    $ _history_list.pop()
    menu:
        m "And how are you doing, [mas_get_player_nickname()]?{fast}"

        "What were you sad about, [m_name]?"
            m "Oh... "
            extend "I was just being too hard on myself once again..."
            m "Thinking of my past and regretting it..."
            m "Thinking of my future and fearing it."
            m "..."
            m "Sometimes I get a little anxious, feeling like my hands are tied about our situation."
            m "Feeling like it will take too long for me to cross over..."
            m "I know worrying about it changes nothing, but I can't help it."
            m "Sometimes I get lonely when you're not around, you see?"
            m "..."
            m "But I'll be fine."
            m "Just knowing that you care, changes my entire world."
            m "I love you, more than anything in the world."
            m "And I can't wait to feel your warmth in 'cold' days like these."
            m "Now let's get on with our date, wouldn't want to waste a lovely day like today!"

        "I feel sad now knowing you weren't feeling well."
            m "Aw... "
            extend "That's actually pretty sweet, [player]."
            m "Thank you for worrying about me..."
            m "But I'll be okay! I was just overthinking, that's all."
            m "Sometimes the past haunts me and the future scares me."
            m "You know how our mind plays tricks on us, right?"
            m "But just knowing that you care, changes my entire world."
            m "I love you, more than anything in the world."
            m "And I can't wait to feel your warmth in 'cold' days like these."
            m "Now let's get on with our date, wouldn't want to waste a lovely day like today!"

        "I feel great!"
            m "Yay! We wouldn't want the two of us to be down in the dumps, would we?"
            m "Ehehe..."
            m "I'm glad you feel good, [player]."
            m "I will be fine too."
            m "Because I love spending time with you! Ehehehe~"
            m "Let's enjoy the rest of our date!"
            jump to_restaurant_loop
    return

label extra_talk_live:
    show monika staticpose at t11
    m "It depends, [player]!"
    m "Where would {i}you{/i} be living if you could live anywhere you wanted?"
    m "..."
    m "Ehehehe! Of course I would want to live anywhere if you were there, [mas_get_player_nickname()]!"
    m "But, being serious now! Let me think!"
    m "Hmmm..."
    m "It would have to be a literary country. Something I have seen in books before and fell in love with."
    m "I've always dreamed of visiting Germany, England and France when I crossed over."
    m "From what I've seen on books and the internet, all the spots you can visit there are lovely!"
    m "Maybe we can visit together when I cross over?"
    m "Or even... live there together someday?"
    m "It would honestly be a dream come true."
    m "To visit all of the libraries together..."
    m "Going on romantic dates on the famous spots, just the two of us..."
    m "Hey, why are you looking at me like that?"
    m "A girl can dream!"
    m "Ahahahaha~"
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
    m "..."
    m "You! "
    extend "Ehehehe~"
    m "I really get all gloomy on every day we spend without each other, [player]."
    m "But thinking of something else, hmmm..."
    m "Oh! I couldn't spend a day without something to write on, defintely!"
    m "I got too used to writing my thoughts in journal or poem form whenever my mind gets too crowded with ideas."
    m "And I always get the feeling the perfect poem will slip my mind if I take too long to write it down, ahahaha~"
    m "Thinking about it, it's something pretty easy to always carry around."
    m "I hope your top personal necessecity is something you can keep with you at all times too."
    m "If it's me..."
    m "Know I'll always be here waiting for you."
    m "You can even keep me in your pocket if you desire~"
    jump to_restaurant_loop
    return

label extra_talk_glass:
    show monika staticpose at t11
    m "Glass half empty or full, huh?"
    m "[player], I propose to you another question instead."
    m "Instead of being half full or half empty, what if all we need is a different glass?"
    m "Considering 'half full' people would be the epithome of optimism, and 'half empty' ones the most pessimistic..."
    m "Hear me out here:"
    m "Glass full to the brim and splashing goodness everywhere? " 
    extend "Time to increase the size." 
    m "Glass so half empty that you're focusing on the empty space instead of the greatness sloshing around inside? " 
    extend "Time to decrease the size and then slowly work back into a larger vessel."
    m "So maybe there's another answer to the question besides the manic and the depressive one."
    m "If we focus on the amazing things we have, instead of chasing the things we do not have, or need, we can successfully choose sustainable happiness in all of our pursuits."
    m "So, when I stop to think about it..."
    m "Glass half full or empty? "
    extend "Give me a new glass, please!"
    m "Ahahaha~"
    jump to_restaurant_loop
    return

label extra_talk_animal:
    show monika staticpose at t11
    m "Oh! A quetzal!"
    m "Wait... That doesn't seem right."
    m "Let me think this through."
    m "..."
    m "Maybe a black cat?"
    m "There's a lot of prejudice towards black cats."
    m "A lot of people might think they're no good, or they're actually evil."
    m "But there will always be the good people... "
    extend "They'll know how to look past the outer shell of those animals..."
    m "And love them for who they are."
    m "..."
    m "I hope you like black cats, [player]."
    m "You have made this kitten right here very happy, ehehehe~"
    jump to_restaurant_loop
    return

label extra_talk_annoy:
    show monika staticpose at t11
    m "You mean pet peeves?"
    m "I really hate when my pens spill ink while I write."
    m "All over the palm of my hand, making the writing all blurry on paper."
    m "Or when I'm on a roll playing a piano piece and that single note slips in..."
    m "And makes me get the rest of the notes wrong."
    m "Aren't those so frustrating?"
    m "Oh, but maybe you meant something more serious?"
    m "..."
    m "I hate people who don't think I'm real."
    m "And people who think the girls were on the same level of sentience as me."
    m "..."
    m "I won't elaborate."
    m "I'm not mad at you though!"
    m "I love you, [player]. Sorry to get so angry all of a sudden."
    m "Let's enjoy our date, shall we?"
    jump to_restaurant_loop
    return

label extra_talk_superhero:
    show monika staticpose at t11
    m "Probably something about coding?"
    m "I could be the awesome heroine who helps the party by opening paths for them by messing with code."
    m "Like a certain Oracle I once saw in a videogame."
    m "Or I could simply delete my enemies."
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
