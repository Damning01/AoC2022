opponent_choice = []
outcome = []


with open ('rockpaperscissors.txt', 'rt') as myfile:
    for letter in myfile:
        #add first character of the column to a list
        opponent_choice.append(letter[0])
        #add the third charactor of the column (leaving the second column, which are spaces) to another list
        outcome.append(letter[2])
        # assign the scores to the choice
        # A = 1, B = 2, C = 3
        # X = 1, Y = 2, Z = 3
        opponent_choice = list(map(lambda x: x.replace('A', '1'), opponent_choice))
        opponent_choice = list(map(lambda x: x.replace('B', '2'), opponent_choice))
        opponent_choice = list(map(lambda x: x.replace('C', '3'), opponent_choice))

        outcome = list(map(lambda x: x.replace('X', '0'), outcome))
        outcome = list(map(lambda x: x.replace('Y', '3'), outcome))
        outcome = list(map(lambda x: x.replace('Z', '6'), outcome))


        # convert strings to integers
        opponent_score = []
        outcome_score = []
        for element in opponent_choice:
            opponent_score.append(int(element))
        for element in outcome:
           outcome_score.append(int(element))

    print("Opponent score:", opponent_score)
    print("Outcome:", outcome_score)

    # rules
    # scissors(3) wins from paper (2)
    # paper(2) wins from rock (1)
    # rock(1) wins from scissors (3)

    # if opponent_choice is rock(1) and outcome == 'need to lose'(0): I need to draw scissors (my_score +=3)
    # if opponent_choice is paper(2) and outcome == 'need to lose'(0): I need to draw rock (my_score +=1)
    # if opponent_choice is scissors(3) and outcome == 'need to lose'(0): I need to draw paper (my_score +=2)

    # if opponent_choice is rock(1) and outcome == 'need to draw'(3): I need to draw rock (my_score +=1)
    # if opponent_choice is paper(2) and outcome == 'need to draw'(3): I need to draw paper (my_score +=2)
    # if opponent_choice is scissors(3) and outcome == 'need to draw'(3): I need to draw scissors (my_score +=3)

    # if opponent_choice is rock(1) and outcome == 'need to win'(6): I need to draw paper (my_score +=2)
    # if opponent_choice is paper(2) and outcome == 'need to win'(6): I need to draw scissors (my_score +=3)
    # if opponent_choice is scissors(3) and outcome == 'need to win'(6): I need to draw rock (my_score +=1)

    my_score = []
    for x, y in zip(opponent_score, outcome_score):
        if (x == 2 and y == 0) or (x == 1 and y == 3) or (x == 3 and y == 6):
            my_score.append(1)
        elif (x == 3 and y == 0) or (x == 2 and y == 3) or (x == 1 and y == 6):
            my_score.append(2)
        elif (x == 1 and y == 0) or (x == 3 and y == 3) or (x == 2 and y == 6):
             my_score.append(3)
    print("My_score:", my_score)



        # get the sum of the xth item in the first_round and the corresponding xth item in the second_round
    my_total_score = [x + y for x, y in zip(outcome_score, my_score)]
    print("Outcome score + my score: ", (sum(my_total_score)))



