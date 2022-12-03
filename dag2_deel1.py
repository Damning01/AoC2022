opponent_choice = []
my_choice = []


with open ('rockpaperscissors.txt', 'rt') as myfile:
    for letter in myfile:
        #add first character of the column to a list
        opponent_choice.append(letter[0])
        #add the third charactor of the column (leaving the second column, which are spaces) to another list
        my_choice.append(letter[2])
        # assign the scores to the choice
        # A = 1, B = 2, C = 3
        # X = 1, Y = 2, Z = 3
        opponent_choice = list(map(lambda x: x.replace('A', '1'), opponent_choice))
        opponent_choice = list(map(lambda x: x.replace('B', '2'), opponent_choice))
        opponent_choice = list(map(lambda x: x.replace('C', '3'), opponent_choice))

        my_choice = list(map(lambda x: x.replace('X', '1'), my_choice))
        my_choice = list(map(lambda x: x.replace('Y', '2'), my_choice))
        my_choice = list(map(lambda x: x.replace('Z', '3'), my_choice))

        # convert strings to integers
        opponent_score = []
        my_score = []
        for element in opponent_choice:
            opponent_score.append(int(element))
        for element in my_choice:
            my_score.append(int(element))

    print("Opponent score:", opponent_score)
    print("My score:", my_score)

    # rules
    # scissors(3) wins from paper (2)
    # paper(2) wins from rock (1)
    # rock(1) wins from scissors (3)

    # assign scores based on the choices
    # if opponent_choice == 3 and my_choice = 2: I get outcome_score += 0
    # if opponent_choice == 2 and my_choice = 1: I get outcome_score += 0
    # if opponent_choice == 1 and my_choice = 3: I get outcome_score += 0

    # if opponent_choice = 1 and my_choice = 1: I get outcome_score += 3
    # if opponent_choice = 2 and my_choice = 2: I get outcome_score += 3
    # if opponent_choice = 3 and my_choice = 3: I get outcome_score += 3

    # if opponent_choice = 1 and my_choice = 2: I get outcome_score += 6
    # if opponent_choice = 2 and my_choice = 3: I get outcome_score += 6
    # if opponent_choice = 3 and my_choice = 1: I get outcome_score += 6

    outcome_score = []
    for x, y in zip(opponent_score, my_score):
        if x == 3 and y == 2 or x == 2 and y == 1 or x == 1 and y == 3:
            outcome_score.append(0)
        elif x == 1 and y == 1 or x == 2 and y == 2 or x == 3 and y == 3:
            outcome_score.append(3)
        elif x == 1 and y == 2 or x == 2 and y == 3 or x == 3 and y == 1:
            outcome_score.append(6)
    print(outcome_score)



        # get the sum of the xth item in the first_round and the corresponding xth item in the second_round
    my_total_score = [x + y for x, y in zip(my_score, outcome_score)]
    print("First + Second round: ",(sum(my_total_score)))



