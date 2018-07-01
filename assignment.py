import cards
import collections
from operator import methodcaller

def less_than(c1, c2):
    """Return
           True if c1 is smaller in rank,
           True if ranks are equal and c1 has a 'smaller' suit
           False otherwise"""
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False


def min_in_list(L):
    """Return the index of the mininmum card in L"""
    min_card = L[0]  # first card
    min_index = 0
    for i, c in enumerate(L):
        if less_than(c, min_card):  # found a smaller card, c
            min_card = c
            min_index = i
    return min_index


def cannonical(H):
    """ Selection Sort: find smallest and swap with first in H,
        then find second smallest (smallest of rest) and swap with second in H,
        and so on..."""
    for i, c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        min_index = min_in_list(H[i:]) + i
        H[i], H[min_index] = H[min_index], c  # swap
    return H


def flush_7(H):
    """Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards,
       False otherwise."""
    suit_cards_dict = collections.defaultdict(list)
    for card in H:
        suit_cards_dict[card.suit()].append(card)

    for suit, card_list in suit_cards_dict.iteritems():
        if len(card_list) >= 5:
            return card_list[:5]

    return False

def straight_7(H):
    """Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards,
       False otherwise."""
    sorted_hand = sorted(H, key=methodcaller('rank'))
    sorted_hand_tuples = [(sorted_hand[i], sorted_hand[i+1], sorted_hand[i+2], sorted_hand[i+3], sorted_hand[i+4]) for i in range(3)]
    for hand in sorted_hand_tuples:
        if is_straight(hand):
            return list(hand)
    return False

def is_straight(H):
    """ Returns True if the given 5 card hand is a straight."""
    for i in range(4):
        if H[i].rank() != H[i+1].rank() - 1:
            return False
    return True

def is_flush(hand):
    """Return True if the given 5 card hand is a flush"""
    # suit_set = set([card.suit() for card in hand])
    # return len(suit_set) == 1
    return all(card.suit() == hand[0].suit() for card in hand)


def straight_flush_7(H):
    """Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards,
       False otherwise."""
    sorted_hand = sorted(H, key=methodcaller('value'))
    sorted_hand_tuples = [(sorted_hand[i], sorted_hand[i+1], sorted_hand[i+2], sorted_hand[i+3], sorted_hand[i+4]) for i in range(3)]
    for hand in sorted_hand_tuples:
        if is_straight(hand) and is_flush(hand):
            return list(hand)

    return False

def four_7(H):
    """Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards,
       False otherwise."""
    card_dict = {}
    for card in H:
        if card.rank() in card_dict:
            card_dict[card.rank()] = card_dict.get(card.rank()) + 1
        else:
            card_dict[card.rank()] = 1

    for rank in card_dict.keys():
        if card_dict.get(rank) == 4:
            return filter(lambda c: c.rank() == rank, H)
    return False


def three_7(H):
    """Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H) is False."""
    pass


def two_pair_7(H):
    """Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H) and three_7(H) are both False."""
    pass


def one_pair_7(H):
    """Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H), three_7(H) and two_pair(H) are False."""
    pass


def full_house_7(H):
    """Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H) is False."""
    pass


def main():

    for i in range(2000):
        D = cards.Deck()
        D.shuffle()
        hand = [D.deal() for i in range(1, 8)]
        if straight_7(hand) is not False:
            print 'Found straight'
            print straight_7(hand)
        # if four_7(hand) is not False:
        #     print 'Found 4 of a kind'
        #     print four_7(hand)

    # while True:
    #     # create community cards
    #     # create Player 1 hand
    #     # create Player 2 hand
    #
    #     print("-" * 40)
    #     print("Let's play poker!\n")
    #     print("Community cards:", community_list)
    #     print("Player 1:", hand_1_list)
    #     print("Player 2:", hand_2_list)
    #     print()


if __name__ == "__main__":
    main()
