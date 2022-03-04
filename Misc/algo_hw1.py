import math
import random


def max_2(L: []) -> (int):
    max1 = 0
    max2 = 0
    for i in L:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i

    return max2


def find_max_first_second_max(L: []) -> (int, int):
    """

    Recursively finds max1, and max2, assume n >= 2

    :param L: list to be searched
    :return: max1, max2
    """
    n = len(L)  # Array length

    L_winner = []
    L_loser = []

    for i in range(math.ceil(n/2)):  # C style for loop
        if L[i] > L[(n-1)-i]:  # Compare first and last
            L_winner.append(L[i])
            L_loser.append(L[(n-1)-i])
        elif i == (n-1)-i:  # Check if cursor is on same element, move onto winner bracket
            L_winner.append(L[i])
        else:  # L[(n-1)-i] > L[i]
            L_winner.append(L[(n-1)-i])
            L_loser.append(L[i])

    if n > 2:  # Recursive condition
        (max1, max2) = find_max_first_second_max(L_winner)
        (L_max2, _) = find_max_first_second_max(L_loser)
    elif n == 2:  # Even end condition
        return L_winner[0], L_loser[0]
    elif n == 1:  # Odd end condition
        return L_winner[0], -1
    else:  # error
        return -1, -1

    if L_max2 > max2:
        max2 = L_max2

    return max1, max2


if __name__ == '__main__':
    L = [random.randrange(0, 100) for _ in range(0, 101)]  # Create array of odd number of elements
    print(L)
    print(find_max_first_second_max(L))
    print(max(L))
    print(max_2(L))
