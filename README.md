# Martingale Binary Betting System

## Introduction

When I was 17, I traded with a martingale betting strategy for binary options with foreign currencies. I started with an account balance of $2,000 dollars and traded $1 bets. After extremely lucky success, I was able to withdraw a balance of $2,500 after a few days.

I have always wondered what my odds were, so I built this simulation to test them.

**Binary Option:**
> a financial option in which the payoff is either some fixed monetary amount or nothing at all.

If the price of a currency pair, such as EUR/USD, is at 1.1, a person can either "put" or "call" depending on if they think the price will go up or down. For instance, if a person speculates that the currency will rise above 1.1 in the next 15 minutes, they can place a "call" bet with a 15 minute expiry. Once the time expires, if the price is above 1.1, the better receives their betted amount.

## What is the Martingale Betting Strategy?

Originating in 18th century France, the martingale betting strategy is a simplistic approach that will double a bet if a loss has occured. For example if a better places a $5 bet, they will receive $5 if they win; however, if they lose, they will double their previous bet to recuperate the loss. 

Going from the previous example, lets say the better lost their initial bet. Now, they place a bet for $10. If they win, they receive a net profit of $5.

**Ex:**

Simulation #1 | Simulation #2
--- | ---
Balance: $10 | Balance: $10
Bet #1: $1 [LOSS] | Bet #1: $1 [LOSS]
Bet #2: $2 [LOSS] | Bet #2: $2 [LOSS]
Bet #3: $4 [LOSS] | Bet #3: $4 [Win]
Profit: $-7 | Net Profit: $1

## What type of martingale does this program simulate?

This program will utilize the martingale betting strategy to simulate the binary options strategy I personally used:

1. Start out with an intial balance - $2,000
2. Start Initial bet - $1
   - Win: Place another bet for $1
   - Lose: Place a new trade for $2 (and double for each loss)
3. If the player finally wins after a losing streak:
   - Then, reset the next bet back to $1 and start over

## How to Use

**To run, the necessary library of pyplot will need to be installed.**

After executing the program, it will ask for a series of prompt requests from the user:

1. Initial Account Balance
   - Must be greater than or equal to 1.00
     - Ex. 1 | 20,000 | 1,000,000.01
2. Bet Amount:
   - Must be less than account balance.
     - Ex. 10.5 | 1,000 | 0.20
3. How Many Bets (Integers Only):
   - Must be an integer
   - Represents how many times each player will bet
4. How Many People (Integers Only):
   - Must be an integer
   - Represents how many players will participate in the simulation
