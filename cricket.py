#play 1 over of cricket. here batsman starts at zero runs. Baller throws ball randomly: if no ball(nb) then batsman score +1, 
# if ok ball then batsman score +1 or +2 (random generate), 
# if bad ball then batsman score +4 or +6 (random generate)
# if great ball then batsman scores 0 runs
# if lbw ball then batsman gets out and print batsman score
import random


def menu():
    print("************ WELCOME TO IPL ***********")
    print("\tpress 1 to PLAY")
    print("\tpress 2 to EXIT")

    while True:
        choice=int(input("Enter your choice:"))
        if choice==1:
            play()
            break
        elif choice==2:
            exit()
        else:
            print("Invalid choice, try again!")


def displaymessage():
    status=True
    while(status):
        menu()
        yesno=input("Would you like to play IPL again? Press 'y' for yes and 'n' for no:")
        if yesno=='y':
            status=True
        elif yesno=='n':
            status=False
        else:
            print("Invalid Choice..")


def play():
    name=input("Please enter your name:")

    batsman_score=0
    balls=["nb","ok","bad","great","lbw"]
    noofballs=0

    print("\t\t\t------------- MATCH STARTS -------------")

    for i in range(6):
        b=random.choice(balls)
        noofballs+=1
        input("Press enter to face a ball:\n")
    #    print(b)
        if b=="nb":
            print("-> No Ball...Batsman gets 1 run!")
            batsman_score+=1
            print(name,":",batsman_score)
        elif b=="ok":
            score=random.randint(1,2)
            batsman_score+=score
            if score == 1:
                print("-> And thats a single..")
            elif score == 2:
                print("-> Two runs for the batsman!")
            print(name,":",batsman_score)

        elif b=="bad":
            score=random.randrange(4,7,2)
            if score==4:
                print("-> BOUNDARY!! Thats a FOUR..!! ")
            elif score == 6:
                print("-> BRAVO!! Thats a SIX..!! ")
            batsman_score+=score
            print(name,":",batsman_score)

        elif b=="great":
            batsman_score+=0
            print("-> No runs from this ball..")
            print(name,":",batsman_score)

        elif b=="lbw":
            print("-> And.. that's a WICKET! Batsman walks back to the pavillion !")
            break
        else:
            pass


        
    printscore(name,batsman_score,noofballs)


def printscore(name,batsman_score,noofballs):
    print("\n*************************")
    print("\t",name)
    print("Runs:",batsman_score,"\tBalls:",noofballs)
    print("*************************")


displaymessage()