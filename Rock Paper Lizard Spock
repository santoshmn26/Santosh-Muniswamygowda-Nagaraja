def line_display(): #function to print the '-' lines
    print('-------------------------------')
player_score=0     #initilizing the scores
computer_score=0
num=1
def scores(a,b): #function to update scores
    global player_score # Using both the players scores as global
    global computer_score
    if(a==b):
        print('Its a tie')
        player_score+=1
        computer_score+=1
    elif(a>b):
        print('You won!')
        player_score+=2
    else:
        print('Computer won!')
        computer_score+=2
def show_scores(final_score=1):
    if(final_score!=3):
        line_display()
        print('Your Scores: ',player_score,',','  Player Scores: ',computer_score)
    else:
        if(player_score==computer_score):
            line_display()
            print('Your Scores: ',player_score,',','  Player Scores: ',computer_score)
            line_display()
            print('Its a tie!')
        elif(player_score>computer_score):
            line_display()
            print('Your Scores: ',player_score,',','  Player Scores: ',computer_score)
            line_display()
            print('You are the winner!')
        else:
            line_display()
            print('Your Scores: ',player_score,',','  Player Scores: ',computer_score)
            line_display()
            print('The computer is the winner!')
        line_display()
        print('Good Bye!')
        line_display()
        return
def play_game():
    line_display()
    computer_choices=['rock','paper','scissor','lizard','spock']
    print('Game options:')
    line_display()
    print('Rock\nPaper\nScissor\nLizard\nSpock')
    choice=input('Enter your choice <x to exit the main menu>:')
    choice=choice.lower()
    import random
    random_num=random.randint(0,4)
    computer_choice=computer_choices[random_num]
    if((choice=='x')| (choice=='X')):
        return
    elif choice not in computer_choices:
        print('Invalid choice!')
        play_game()
    else:
        print('Computer choice:',computer_choice)
        if(choice==computer_choice):
            scores(1,1) # sending both 1's to the function scores indicates its a tie
        elif((choice=='rock')&(computer_choice=='lizard')):# only winning conditions for player
            scores(2,1) # sending 2,1 indicates that the player won and is getting a score of +2
        elif((choice=='rock')&(computer_choice=='scissor')):# only winning conditions for player
            scores(2,1)
        elif((choice=='paper')&(computer_choice=='rock')):# only winning conditions for player
            scores(2,1)
        elif((choice=='paper')&(computer_choice=='spock')):# only winning conditions for player
            scores(2,1)
        elif((choice=='scissor')&(computer_choice=='paper')):# only winning conditions for player
            scores(2,1)
        elif((choice=='scissor')&(computer_choice=='lizard')):# only winning conditions for player
            scores(2,1)
        elif((choice=='lizard')&(computer_choice=='rock')):# only winning conditions for player
            scores(2,1)
        elif((choice=='lizard')&(computer_choice=='paper')):# only winning conditions for player
            scores(2,1)
        elif((choice=='Spock')&(computer_choice=='Scissor')):# only winning conditions for player
            scores(2,1)
        elif((choice=='Spock')&(computer_choice=='Rock')):# only winning conditions for player
            scores(2,1)
        else:# all remaining conditions are loosing for the player
            scores(1,2)# sending 1,2 indicates that the computer won and is getting a score of +2
while (num):
    print('Rock Paper Scissor Lizard Spock')
    line_display()
    print('Main menu:')
    line_display()
    print('[1] Play\n[2] Scores\n[3] Exit\n')
    num=int(input('Select an option <3 to Exit>:'))
    if(num==1):
        play_game()
    elif(num==2):
        show_scores()
    elif(num==3):
        show_scores(3)
        k=input('Press any key to continue...')
        num=0
    else:
        print('Invalid Choice')
        continue
    line_display()
