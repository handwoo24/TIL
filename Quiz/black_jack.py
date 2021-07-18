from __future__ import annotations
from typing import List
import random

class Dealer:
    def shuffle(self, number_cards: int) -> List[int]:
        card_list: list = []
        for i in range(0, number_cards):
            card_number = random.randrange(0, 100000)
            card_list.append(card_number)
        
        return card_list
        
    @property
    def max(self) -> int:
        sum_of_card_number = random.randrange(10, 300000)
        return sum_of_card_number
    
    @property
    def number(self) -> int:
        return random.randrange(3, 100)

class BlackJackMachine:
    pass

def main():
    dealer = Dealer()
    number_cards: int = dealer.number
    sum_of_card_number: int = dealer.max
    card_list: List[int] = dealer.shuffle(number_cards)

    black_jack_machine = BlackJackMachine()
    pass

if __name__ == "__main__":
    main()