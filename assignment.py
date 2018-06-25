
import cards

def less_than(c1 ,c2):
    '''Return
           True if c1 is smaller in rank,
           True if ranks are equal and c1 has a 'smaller' suit
           False otherwise'''
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False

def min_in_list(L):
    '''Return the index of the mininmum card in L'''
    min_card = L[0]  # first card
    min_index = 0
    for i ,c in enumerate(L):
        if less_than(c ,min_card):  # found a smaller card, c
            min_card = c
            min_index = i
    return min_index

def cannonical(H):
    ''' Selection Sort: find smallest and swap with first in H,
        then find second smallest (smallest of rest) and swap with second in H,
        and so on...'''
    for i ,c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        min_index = min_in_list(H[i:]) + i
        H[i], H[min_index] = H[min_index], c  # swap
    return H

def flush_7(H):
    '''Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards,
       False otherwise.'''
    pass

def straight_7(H):
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards,
       False otherwise.'''
    pass

def straight_flush_7(H):
    '''Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards,
       False otherwise.'''
    pass

def four_7(H):
    '''Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards,
       False otherwise.'''
    pass

def three_7(H):
    '''Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H) is False.'''
    pass

def two_pair_7(H):
    '''Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H) and three_7(H) are both False.'''
    pass

def one_pair_7(H):
    '''Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H), three_7(H) and two_pair(H) are False.'''
    pass

def full_house_7(H):
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H) is False.'''
    pass

def main():
    D = cards.Deck()
    D.shuffle()

    while True:
        # create community cards
        # create Player 1 hand
        # create Player 2 hand

        print( "-" *40)
        print("Let's play poker!\n")
        print("Community cards:" ,community_list)
        print("Player 1:" ,hand_1_list)
        print("Player 2:" ,hand_2_list)
        print()



if __name__ == "__main__":
    main()