import webbrowser


def cave():
    print "You have entered the cave with two paths. Will you go left or right"
    answer = raw_input("> ")
    choice = False
    while choice is False:
        if 'left' in answer:
            choice = True
            columbus()
        elif 'right' in answer:
            print 'Oh no a group of terrible leprechauns. Turn back or they will eat you'
            choice = True
            fall()
            start_over()
        else:
            print "Pick a valid choice"
            answer = raw_input('> ')


def columbus():
    print 'Welcome to Columbus. The streets are filled with leprechauns. What should you do'
    print "Should we: \n1. Jump down in the sewer \n2. Stop and eat at a Chipotle\n"
    print 'Enter a number before leprechauns come and eat you'
    choice = raw_input()
    if "1" in choice:
        print "It's dark down here. I hope I don't get eaten by an alligator"
        sewer()
    elif "2" in choice:
        print 'Your eating right now, really, meanwhile the leprechauns blew up the planet.'
        start_over()
    else:
        print "Leprechauns came and ate you."
        start_over()


def fall():
    print 'As you were leaving you fell down and cracked your face open.'
    start_over()


def start():
    print "The world is run by evil leprechauns and you must find Tim Rohrer to defeat them. He'll know what to do"
    print "But we don't know where Tim Rorher is, are you ready to go find him"
    print "Type yes or no"
    answer = raw_input("> ")
    choice = False
    while choice is False:
        if "yes" in answer:
            print "Let the adventure begin"
            choice = True
            option()
        elif "no" in answer:
            print "OK then you can let the evil leprechauns run the world and eat your brain"
        else:
            print "Type yes or no"
            answer = raw_input('> ')


def option():
    print "Where should we go?"
    print "1. Columbus\n2. Utah\n\nPick a number"
    answer = raw_input("> ")
    choice = False
    while choice is False:
        if '1' in answer:
            print "Ok then, let's go to Columbus"
            choice = True
            columbus()
        elif "2" in answer:
            print "Let's go to Utah"
            choice = True
            utah()
        else:
            print "Pick a valid choice"
            answer = raw_input("> ")


def utah():
    print "Welcome to Utah. Do you want to go skiing"
    print "1. Yes\n2. No\n\nPick a number"
    answer = raw_input("> ")
    choice = False
    while choice is False:
        if '1' in answer:
            print "You went skiing and ran into Tim's wife"
            choice = True
            lauren()
        elif "2" in answer:
            print "Let's go to McDonalds"
            choice = True
            mcdonalds()
        else:
            print "Pick a valid choice"
            answer = raw_input("> ")


def mcdonalds():
    print "What should we order?"
    print "1. Chicken Nuggets\n2. Big-Mac\n\nType a number"
    answer = raw_input("> ")
    choice = False
    while choice is False:
        if '1' in answer:
            print "There is a clue in the chicken nuggets"
            print "It says that 'The person are are looking for is in Michigan"
            print "Should we go to Michigan"
            print "1. Yes\n2. No\n\nType a number"
            answer = raw_input("> ")
            choice = False
            while choice is False:
                if '1' in answer:
                    choice = True
                    michigan()
                elif "2" in answer:
                    choice = True
                    exit(0)
                else:
                    print "Pick a valid choice"
                    answer = raw_input()
        elif "2" in answer:
            print "The cook poisoned your Big-Mac and you died"
            start_over()
        else:
            print "Pick a valid choice"
            answer = raw_input()


def start_over():
    print "You lose. Do you want to start over"
    print "1. Yes\n2. No\n\nType a number"
    answer = raw_input("> ")
    choice = False
    while choice is False:
        if '1' in answer:
            choice = True
            start()
        elif "2" in answer:
            choice = True
            exit(0)
        else:
            print "Pick a valid choice"
            answer = raw_input()


def sewer():
    print "It sure is dark down here"
    print "What should you do"
    print "1. Go left\n2. Go right \n\nPick a number"
    answer = raw_input("> ")
    choice = False
    while choice is False:
        if '1' in answer:
            print "You ran into an alligator and it ate your face off"
            choice = True
            start_over()
        elif "2" in answer:
            print "I see a door with a gatekeeper in front of it"
            choice = True
            print "The gatekeeper allows you to enter"
            print "The door leads to a secret underground cave"
            cave()
        else:
            print "Pick a valid choice"
            answer = raw_input("> ")


def lauren():
    print "Lauren is Tim's wife and says that Tim is in Michigan at a lumberjack convention"
    print "What should you do?"
    print "1. Go to the lumberjack convention in Michigan\n2. Go ride a pony at the local Wal-Mart \n\nPick a number"
    answer = raw_input("> ")
    choice = False
    while choice is False:
        if '1' in answer:
            print "OK, let's go to Michigan"
            michigan()
        elif "2" in answer:
            choice = True
            pony()
        else:
            print "Pick a valid choice"
            answer = raw_input("> ")


def utah_again():
    print "Tim was reunited with Lauren and lived happily ever after"
    win()


def pony():
    print "As you were going to Wal-mart, you tripped over a woodchuck and died"
    start_over()


def win():
    print "You won the game"
    print "Should we watch the victory video?"
    print "1. Yes\n2. No"
    answer = raw_input("> ")
    choice = False
    while choice is False:
        if '1' in answer:
            choice = True
            url = "https://www.youtube.com/watch?v=S_IAqwrvEuU"
            webbrowser.open(url)
        elif "2" in answer:
            exit(0)
        else:
            print "Pick a valid choice"
            answer = raw_input("> ")


def michigan():
    print "Welcome to the lumberjack convention"
    print "On no, Tim is surrounded by evil gremlins who are trying to eat his face"
    print "What should you do?"
    print "1. Attack\n2. Sing \n\nPick a number"
    answer = raw_input("> ")
    choice = False
    while choice is False:
        if '1' in answer:
            choice = True
            print "I choose you Pickachu"
            print "Pickachu confronts the gremlins and kills them with thunderbolt"
            print "You saved Tim"
            print "We should go back to Lauren in Utah"
            utah_again()
        elif "2" in answer:
            print "Your singing is hideous."
            choice = True
            print "The gremlins came and ate your face off"
            start_over()
        else:
            print "Pick a valid choice"
            answer = raw_input("> ")


start()
