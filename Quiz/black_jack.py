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
        
    pass

def main():
    dealer = Dealer()
    pass

if __name__ == "__main__":
    main()