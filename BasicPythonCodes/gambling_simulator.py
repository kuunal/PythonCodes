import random

def main():
    number_of_bets = 0
    number_of_wins = 0
    try:
        stake = int(input("Enter Stake Amount"))
        goal = int(input("Enter Goal Amount"))
    except ValueError:
        print("Plese provide valid details!")
        main()
    else:
        play(stake, goal, number_of_bets, number_of_wins)        

def play(stake, goal, number_of_bets, number_of_wins):
    playerChoice = 1
    randomNumber = round(random.random())
    
    if check_end_condition(stake, goal):
        print_results(stake, goal, number_of_bets, number_of_wins)
        return
    if randomNumber == 1:
        stake+=1 
        number_of_wins+=1
    else:
        stake-=1
    number_of_bets+=1
    play(stake, goal, number_of_bets, number_of_wins)

def check_end_condition(stake, goal):
    if(stake>=goal or stake==0):
        return True;    
  
def print_results(stake, goal, number_of_bets, number_of_wins):
    print("You won, Stake = "+str(stake) if stake!=0 else "You lost, Stake = "+str(stake))
    print(f'Total number of Bets: {number_of_bets}')
    print(f'Total number of Wins: {number_of_wins}')
    print(f'Average win rate: {(number_of_wins/number_of_bets)*100}')
  

main()