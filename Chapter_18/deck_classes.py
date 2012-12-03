__author__ = 'matt'

import random

class Card(object):
    """Represents a standard playing card."""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self, other):
        # Use tuple comparison to compare suite first, then rank.
        # See, suit is the first element in the tuple.
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1,t2)

class Deck(object):
    """Represents a deck of playing cards."""

    def __init__(self):
        self.cards = []
        # Loop through and add all standard cards to the deck.
        # Note that you don't need to place the Card class
        # definition above the Deck definition.
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        res = []
        for card in self.cards:
            # Here we're using the Card class' own __str__ representation
            # rather then storing the Card instance itself
            res.append(str(card))
        return '\n'.join(res)

    def sort(self):
        """
        Exercise 2
        Write a Deck method named sort that uses the list method sort
        to sort the cards in a Deck. sort uses the __cmp__ method
        we defined to determine sort order.
        """
        # Sort here actually uses the tuple comparison we defined in the Card class
        self.cards.sort()

    def pop_card(self):
        """return the last card on the list"""
        return self.cards.pop()

    def add_card(self, card):
        """Given a card instance, add it to the deck."""
        self.cards.append(card)

    def shuffle(self):
        """shuffle the list."""
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        """Pop cards from this deck to a hand."""
        # Good to place this method in the Deck class as it is inherited by hand.
        # Can be used by both Deck and Hand now.
        # If method were in Hand class, only would allow for method on Hand, not Deck.
        for i in range(num):
            hand.add_card(self.pop_card())

class Hand(Deck):
    """Represents a poker hand"""
    # NOTE: This does need to appear after Deck class definition,
    # as it is inheriting from Deck. This probably occurs before __main__ code.
    # where as in Deck composition example, that happens when object is instanciated,
    # e.g. after both Deck and Card class definitions have been parsed by interpreter.
    def __init__(self, label=''):
        self.cards = []
        self.label = label


if __name__ == '__main__':
#    newCard = Card(random.randint(0,3),random.randint(1,14))
#    print 'Test Card: %s' % newCard
#
#    newDeck = Deck()
#    print newDeck
#
#    print 'Pop pre-shuffle: %s' % newDeck.pop_card()
#    newDeck.shuffle()
#    print 'Pop post-shuffle: %s' % newDeck.pop_card()
#
#    deck2 = Deck()
#    deck2.shuffle()
#    print deck2
#    print '=====sorting====='
#    deck2.sort()
#    print deck2
#
#"""
#Wrenches will fail because tuple comparison in Card class __cmp__ method
#is expecting an object with attributes suit and rank.
#"""
#     print '=====Add Wrenches====='
#     deck2.cards.append(9999999)
#     deck2.cards.append('what is this text')
#     deck2.sort()
#     print deck2

    deck3 = Deck()
    print len(deck3.cards)
    mattHand = Hand('Matt\'s Hand')
    deck3.move_cards(mattHand,10)
    print len(deck3.cards)
    print len(mattHand.cards)


