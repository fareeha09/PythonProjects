start = '''
You open your eyes and look around to see yourself in a dark, grimy cell.
With you are three people you never expected to be in the same room,
much less with you.
There's Justin Bieber.
Nicki Minaj.
And...Donald Trump???
One thing is clear...
You have to ESCAPE THE JAIL
You have to choose ONE of these characters to go with you.
'''

print(start)
chosen = "'Great! You chose me,"
opps = "Oops! "
dead = " you're dead. Better start over!"

def choose_character():
    person= input("Do you choose [Justin Bieber], [Nicki Minaj], or [Donald Trump]?")
    if person == 'Justin Bieber':
        print (chosen + " Justin Bieber'")
        chose_JB()
    elif person== 'Nicki Minaj':
        print (chosen + " Nicki Minaj'")
    elif person== 'Donald Trump':
        print (chosen + " Donald Trump'")
    else:
        print ("Who's that? Please retype answer")
        choose_character()

def chose_JB():
    action_cell= input("'Should we [smash the wall] or [steal the key]?'")
    if action_cell == 'smash the wall':
        print (oops + "a rock fell on your head," + dead)
        choose_character()
    elif action_cell == 'steal the key':
        print("You manage to snag the key as a guard walks past.")
        print("'Great! We've stolen the key. Let's go!'")
        print("'The dungeon is so dark, and I haven't eaten anything for ages.'")
        print("'Ughhh, I can't see anything.' *smashes into a wall*")
        print("'Hey... I smell somethin good from my left!'")
        print("'But I hear guards too.'")
        print("'I don't hear or smell anything on the right.'")
        chose_dir()
    else:
        print("'What? Why would you want to do that?'")
        chose_JB()

def chose_dir():
    action_dir = input("Do we turn [left] or [right]?")

choose_character()
