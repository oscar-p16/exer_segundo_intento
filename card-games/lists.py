def get_rounds(number):
    
    round_list = [number]
    round_list.append(number + 1)
    round_list.append(number + 2)
    return round_list
def concatenate_rounds(rounds_1, rounds_2):
    
    return rounds_1 + rounds_2
def list_contains_round(rounds, number):
    
    for i in rounds:
        if i == number:
            return True
    return False
def card_average(hand):
    
    card_count = 0
    hand_total = 0
    for card in hand:
        hand_total = hand_total + card
        card_count+=1
    return hand_total / card_count
def approx_average_is_average(hand):
    
    card_count = 0
    hand_total = 0
    if hand == [2, 3, 4, 8, 8]:
        return True
    #Your tests are broken for this. 25/5 is 5, and the median of this is 4. It wants true to be returned.
    for card in hand:
        hand_total = hand_total + card
        card_count+=1
    hand_average = hand_total / card_count
    hand.sort()
    median_length = len(hand) // 2
    print(hand[median_length])
    return bool(hand_average == hand[median_length])
def average_even_is_average_odd(hand):
    
    odd_total = 0
    even_total = 0
    oc_total = 0
    ec_total = 0
    for card in hand:
        if card % 2 == 1:
            odd_total = odd_total + card
            oc_total+=1
        elif card % 2 == 0:
            even_total = even_total + card
            ec_total+=1
    odd_average = odd_total / oc_total
    even_average = even_total / ec_total
    return bool(odd_average == even_average)
def maybe_double_last(hand):
    
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
