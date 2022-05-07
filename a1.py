# Problem: I want to play Blackjack with my friend/against a computer, but I can't find my deck of cards anywhere!
# This program solves this problem by being able to simulate a deck of cards and convert drawn cards into a score value.
# The associated output.txt file should contain the results of 10 games run with this program, 5 with one player and 5
# with two players.

# The "reshuffle" function fully resets the deck to be filled with all 52 cards from a standard deck.
def reshuffle(deck):
    del deck[:]
    heartsuit = ['Ace of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts',
                 '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts',
                 'King of Hearts']
    spadesuit = ['Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades',
                 '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades',
                 'King of Spades']
    diamondsuit = ['Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds',
                   '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds',
                   'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds']
    clubsuit = ['Ace of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs',
                '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs']
    deck.extend(heartsuit)
    deck.extend(spadesuit)
    deck.extend(diamondsuit)
    deck.extend(clubsuit)
    print('The deck has been shuffled.')
    return deck


# Function for drawing a card from the deck, automatically subtracting the drawn card from the deck, and returning
# a new score value. Meant for player input.
def draw(stack, currentScore):
    drawNum = randint(0, (len(stack)))
    if drawNum >= (len(stack)):
        drawNum = len(stack) - 1
    print(f"Player drew the {stack[drawNum]}.")
    newScore = cardCheck(stack[drawNum], currentScore)
    stack.pop(drawNum)
    return stack, newScore


# Function used to convert the drawn card into an integer value between 1 and 11.
def cardCheck(cardDrawn, currentScore):
    if "2" in cardDrawn:
        newScore = currentScore + 2
    elif "3" in cardDrawn:
        newScore = currentScore + 3
    elif "4" in cardDrawn:
        newScore = currentScore + 4
    elif "5" in cardDrawn:
        newScore = currentScore + 5
    elif "6" in cardDrawn:
        newScore = currentScore + 6
    elif "7" in cardDrawn:
        newScore = currentScore + 7
    elif "8" in cardDrawn:
        newScore = currentScore + 8
    elif "9" in cardDrawn:
        newScore = currentScore + 9
    elif ("King" in cardDrawn) or ("Queen" in cardDrawn) or ("Jack" in cardDrawn) or ("10" in cardDrawn):
        newScore = currentScore + 10
    else:
        aceInput = (input(f'Choose what value you want the ace to be at, 1 or 11 (Defaults to 1 if input is invalid)'
                          f': '))
        if aceInput == "11":
            newScore = currentScore + 11
        else:
            newScore = currentScore + 1
    return newScore


# Function used by the computer opponent to draw cards.
def aiDraw(stack, aiCurrentScore):
    drawNum = randint(0, (len(stack)))
    if drawNum >= (len(stack)):
        drawNum = len(stack) - 1
    print(f"Your opponent drew the {stack[drawNum]}.")
    aiNewScore = aiCardCheck(stack[drawNum], aiCurrentScore)
    stack.pop(drawNum)
    return stack, aiNewScore


# Function for the computer opponent to use to convert their drawn card into an integer value. Only difference between
# this and the playerCardCheck function is that the choice for the ace value is done automatically.
def aiCardCheck(cardDrawn, currentScore):
    if "2" in cardDrawn:
        newScore = currentScore + 2
    elif "3" in cardDrawn:
        newScore = currentScore + 3
    elif "4" in cardDrawn:
        newScore = currentScore + 4
    elif "5" in cardDrawn:
        newScore = currentScore + 5
    elif "6" in cardDrawn:
        newScore = currentScore + 6
    elif "7" in cardDrawn:
        newScore = currentScore + 7
    elif "8" in cardDrawn:
        newScore = currentScore + 8
    elif "9" in cardDrawn:
        newScore = currentScore + 9
    elif ("King" in cardDrawn) or ("Queen" in cardDrawn) or ("Jack" in cardDrawn) or ("10" in cardDrawn):
        newScore = currentScore + 10
    else:
        if currentScore <= 10:
            print(f'Your opponent has chosen their ace value to be 11.')
            newScore = currentScore + 11
        else:
            print(f'Your opponent has chosen their ace value to be 1.')
            newScore = currentScore + 1
    return newScore


# Used to check if the player got Blackjack (21 points with only 2 cards.)
def blackJackCheck(playerScoreTemp):
    if playerScoreTemp == 21:
        return True
    else:
        return False


# Used to check if the player's score goes over 21.
def bustCheck(playerScoreTemp):
    if playerScoreTemp > 21:
        return True
    else:
        return False


# Used to check if the ai achieves BlackJack.
def aiBlackJackCheck(aiScoreTemp):
    if aiScoreTemp == 21:
        return True
    else:
        return False


# Used to check if the ai's score goes over 21.
def aiBustCheck(aiScoreTemp):
    if aiScoreTemp > 21:
        return True
    else:
        return False


# Decides randomly if they ai will choose to draw a third card.
# If the ai's score is less or equal to 11, it has a 4 in 5 chance to draw.
# If the ai's score is between 11 and 16, it has a 3 in 5 chance to draw.
# The ai will not draw another card if their score is 17 or higher.
def aiCoinFlip(stack, score):
    aiChoice = randint(0, 5)
    score = score
    if score <= 11:
        if aiChoice < 4:
            print(f'Your opponent is drawing another card.')
            hold = aiDraw(stack, score)
            score = hold[1]
        else:
            print(f'Your opponent has decided to not draw another card.')
    elif 11 < score <= 16:
        if aiChoice < 3:
            print(f'Your opponent is drawing another card.')
            hold = aiDraw(stack, score)
            score = hold[1]
        else:
            print(f'Your opponent has decided to not draw another card.')
    elif score > 16:
        print(f'Your opponent has decided to not draw another card.')
    return stack, score


# The main function, holds the rules and will call the other functions when necessary.
def startup(deck, player1Score, player2Score, aiScore):
    print(f'Welcome to Blackjack!')
    ruleOpt = input(f'Would you like to view the rules? ')
    if (ruleOpt == "yes") or (ruleOpt == "Yes"):
        print(f'This is a game meant for 1 to 2 players.')
        print(f'Players draw cards to see who can get closer to 21 points without going over.')
        print(f'Cards are valued purely by face number, so a 2 of hearts is worth 2 points, a 7 of clubs is worth 7 '
              f'points, etc.')
        print(
            f'Jacks, Queens, and Kings are all worth 10 points each while an Ace\'s value can either 1 or 11, depending'
            f' on the choice of the drawer.')
        print(f'A player can choose when to stop drawing cards whenever they wish and can draw as many as they want, '
              f'assuming they do not go over 21 points.')
        print(f'If a player\'s score does go over 21, they immediately lose the round.')
        print(
            f'If a player gets 21 in two cards (i.e, an Ace and a Queen), they achieve Blackjack and immediately win '
            f'the round.')

    playerNum = 0
    while (playerNum != "1") or (playerNum != "2"):
        playerNum = (input(f'How many players are there? '))
        if playerNum == "1":
            singlePlayer(deck, player1Score, aiScore)
            break
        elif playerNum == "2":
            versus(deck, player1Score, player2Score)
            break
        else:
            print(f'{playerNum} is not a valid input. Please enter 1 or 2.')


# Function for when it's one player playing against an ai.
def singlePlayer(deck, playerScore, aiScore):
    print(f'There is one player.')
    print(f'You will be playing against an AI. The AI will go first.')
    reshuffle(deck)
    temp = aiDraw(deck, aiScore)
    deck = temp[0]
    aiScore = temp[1]
    print(f'Their score is now {aiScore}.')
    temp = aiDraw(deck, aiScore)
    deck = temp[0]
    aiScore = temp[1]
    print(f'Their score is now {aiScore}.')
    if aiBlackJackCheck(aiScore):
        print(f'Your opponent got Blackjack! They win!', file=open('output.txt', 'a'))
    else:
        temp = aiCoinFlip(deck, aiScore)
        aiScore = temp[1]
        print(f'Their final score is {aiScore}.')
        if aiBustCheck(aiScore):
            print(f'Your opponent has gone over 21! You win!', file=open('output.txt', 'a'))
        else:
            print(f'Your opponent has finished drawing. It is now your turn.')
            print(f'Your first two cards will be drawn automatically.')
            reshuffle(deck)
            temp = draw(deck, playerScore)
            playerScore = temp[1]
            print(f'Your score is now {playerScore}.')
            temp = draw(deck, playerScore)
            playerScore = temp[1]
            print(f'Your score is now {playerScore}.')
            if blackJackCheck(playerScore):
                print(f'You got Blackjack! You win!', file=open('output.txt', 'a'))
            else:
                while not bustCheck(playerScore):
                    playerChoice = input(f'Would you like to draw another card? (Yes or No):')
                    if (playerChoice == "Yes") or (playerChoice == "yes"):
                        temp = draw(deck, playerScore)
                        playerScore = temp[1]
                        print(f'Your score is now {playerScore}.')
                    else:
                        print(f'You have decided to stop drawing cards. Your final score is {playerScore}.')
                        break
                if bustCheck(playerScore):
                    print(f'You\'ve gone over 21! Your opponent wins!', file=open('output.txt', 'a'))
                else:
                    if aiScore > playerScore:
                        print(f'Your opponent\'s score of {aiScore} is greater than your score of '
                              f'{playerScore}. They win!', file=open('output.txt', 'a'))
                    elif aiScore == playerScore:
                        print(f'Both of your scores are equal. It\'s a draw!', file=open('output.txt', 'a'))
                    else:
                        print(
                            f'Your score of {playerScore} is greater than your opponent\'s score of {aiScore}. You\'ve'
                            f' won!', file=open('output.txt', 'a'))


# Function for when there's 2 players playing against each other.
def versus(deck, player1Score, player2Score):
    print(f'There are 2 players.')
    print(f'Player 1 will go first. Their first two cards are being drawn automatically.')
    reshuffle(deck)
    temp = draw(deck, player1Score)
    player1Score = temp[1]
    print(f'Player 1\'s score is now {player1Score}.')
    temp = draw(deck, player1Score)
    player1Score = temp[1]
    print(f'Player 1\'s score is now {player1Score}.')
    if blackJackCheck(player1Score):
        print(f'Player 1 got Blackjack! They win!', file=open('output.txt', 'a'))
    else:
        while not bustCheck(player1Score):
            playerChoice = input(f'Player 1, would you like to draw another card? (Yes or No):')
            if (playerChoice == "Yes") or (playerChoice == "yes"):
                temp = draw(deck, player1Score)
                player1Score = temp[1]
                print(f'Player 1\'s score is now {player1Score}.')
            else:
                print(f'Player 1 has decided to stop drawing cards. Their final score is {player1Score}.')
                break
        if bustCheck(player1Score):
            print(f'Player 1 has gone over 21! Player 2 wins!', file=open('output.txt', 'a'))
        else:
            print(f'Player 1 has finished drawing. It is now player 2\'s turn.')
            print(f'Player 2\'s first two cards will be drawn automatically.')
            reshuffle(deck)
            temp = draw(deck, player2Score)
            player2Score = temp[1]
            print(f'Player 2\'s score is now {player2Score}.')
            temp = draw(deck, player2Score)
            player2Score = temp[1]
            print(f'Player 2\'s score is now {player2Score}.')
            if blackJackCheck(player2Score):
                print(f'Player 2 got Blackjack! They win!', file=open('output.txt', 'a'))
            else:
                while not bustCheck(player2Score):
                    playerChoice = input(f'Player 2, would you like to draw another card? (Yes or No):')
                    if (playerChoice == "Yes") or (playerChoice == "yes"):
                        temp = draw(deck, player2Score)
                        player2Score = temp[1]
                        print(f'Player 2\'s score is now {player2Score}.')
                    else:
                        print(f'Player 2 has decided to stop drawing cards. Their final score is {player2Score}.')
                        break
                if bustCheck(player2Score):
                    print(f'Player 2 has gone over 21! Player 1 wins!', file=open('output.txt', 'a'))
                else:
                    if player1Score > player2Score:
                        print(f'Player 1\'s score of {player1Score} is greater than player 2\'s score of '
                              f'{player2Score}. Player 1 wins!', file=open('output.txt', 'a'))
                    elif player1Score == player2Score:
                        print(f'Both of your scores are equal. It\'s a draw!', file=open('output.txt', 'a'))
                    else:
                        print(f'Player 2\'s score of {player2Score} is greater than player 1\'s score of {player1Score}'
                              f'. Player 2 wins!.', file=open('output.txt', 'a'))


# Main block
if __name__ == "__main__":
    from random import randint

    # Initialized variables
    firstDeck = []
    # Player 1 variables:
    p1Score = 0
    # player 2 variables
    p2Score = 0
    # ai variables
    firstAiScore = 0

    # Starts the game. The variables can be replaced by integer values if the user wishes.
    startup(firstDeck, p1Score, p2Score, firstAiScore)
