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
    _selection: int = 3


    def game(self, sum_of_card_number: int, card_list: List[int]) -> int:
        cards: List[int] = []
        print("input list: ", card_list)
        print("input sum: ", sum_of_card_number)
        play_number = self._combination(len(card_list))
        print("play numer: ", play_number)
        result: int = sum_of_card_number
        for i in range(0, play_number):
            copy_list = list(card_list)
            for j in range(0, 3):
                index = random.randrange(0, len(copy_list))
                card = copy_list[index]
                copy_list.remove(card)
                cards.append(card)
            
            card_sum = sum(cards)
            print(card_sum)
            current_result = sum_of_card_number - card_sum
            if current_result < result and card_sum <= sum_of_card_number:
                result = current_result
                sum_result = card_sum

            cards = []
        
        return result, sum_result

    def _combination(self, length) -> int:
        denominator = length * (length - 1) * (length - 2)
        numerator = 6
        situation = int(denominator / numerator)
        return situation * 10

def main():
    dealer = Dealer()
    number_cards: int = dealer.number
    sum_of_card_number: int = dealer.max
    card_list: List[int] = dealer.shuffle(number_cards)

    black_jack_machine = BlackJackMachine()
    result, sum = black_jack_machine.game(sum_of_card_number, card_list)
    print(result, sum)

if __name__ == "__main__":
    main()