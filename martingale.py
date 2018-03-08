from random import randint
from matplotlib import pyplot as plt


def binary_options():
    """
    This function selects a number between the random 
    range of 0 and 1. These numbers are used to simulate
    50/50 odds.
    
    :return: a boolean of True (if win) or False (if lose)
    """
    binary = randint(0, 1)
    if binary == 1:
        return True
    else:
        return False


def martingale(amount, initial_bet, total_bets):
    """
    This will run the martingale betting strategy against the 
    odds of the returned boolean from the binary_options() function. 
    
    :param amount: initial account balance
    :param initial_bet: initial bet amount
    :param total_bets: amount of bets to be made (if amount > 0)
    :return: two lists containing x values and y values
    """
    bet = initial_bet
    previous_bet_win = True
    previous_bet_amount = initial_bet

    x_axis = []
    y_axis = []

    for i in range(total_bets):

        win = binary_options()

        if amount > 0:
            if previous_bet_win:
                if win:
                    amount += bet
                    x_axis.append(i)
                    y_axis.append(amount)
                else:
                    amount -= bet
                    previous_bet_win = False
                    previous_bet_amount = bet
                    x_axis.append(i)
                    y_axis.append(amount)
            else:
                if win:
                    bet = previous_bet_amount * 2
                    amount += bet
                    bet = initial_bet
                    previous_bet_win = True
                    x_axis.append(i)
                    y_axis.append(amount)
                else:
                    bet = previous_bet_amount * 2
                    amount -= bet
                    x_axis.append(i)
                    y_axis.append(amount)
        else:
            x_axis.append(i)
            y_axis.append(amount)

    return x_axis, y_axis


def main():
    """
    This will request information from the user for the program
    to run. It will also compile the results and display a chart
    from PyPlot.
    
    :return: None
    """
    while True:
        try:
            amount = float(input("Initial Account Balance: "))
            if amount < 1:
                raise ValueError
            bet = float(input("Bet Amount: "))
            if bet > amount:
                raise ValueError
            num_of_bets = int(input("How Many Bets (Integers Only): "))
            num_of_people = int(input("How Many People (Integers Only): "))
            break
        except ValueError:
            print("Inputs are incorrect")

    num_of_losses = 0
    num_of_wins = 0
    num_of_busts = 0

    fig, ax = plt.subplots(num=None, figsize=(15, 7), dpi=80)
    plt.subplot(1, 2, 1)
    fig.canvas.set_window_title('Martingale Strategy Results')

    for _ in range(num_of_people):
        x, y = martingale(amount, bet, num_of_bets)
        if y[-1] > amount:
            num_of_wins += 1
        elif y[-1] <= 0:
            num_of_busts += 1
        else:
            num_of_losses += 1
        plt.plot(x, y)

    if num_of_busts > 0 and num_of_losses == 0:
        pie_chart_outcome = num_of_wins, num_of_losses, num_of_busts
        pie_chart_labels = "Profit", "Busts"
        enhance = (0.1, 0)
    elif num_of_busts > 0:
        pie_chart_outcome = num_of_wins, num_of_losses, num_of_busts
        pie_chart_labels = "Profit", "Loss", "Busts"
        enhance = (0.1, 0, 0)
    else:
        pie_chart_outcome = num_of_wins, num_of_losses
        pie_chart_labels = "Profit", "Loss"
        enhance = (0.1, 0)

    plt.ylabel("Account Value")
    plt.xlabel("Amount of Bets")

    plt.subplot(1, 2, 2)
    plt.pie(pie_chart_outcome, labels = pie_chart_labels, explode = enhance,
            autopct = '%.2f%%', shadow = True, startangle = 90)

    plt.tight_layout()
    plt.show()

main()
