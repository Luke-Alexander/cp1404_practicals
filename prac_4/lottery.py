lottery_numbers_hold = []
quick_pick_count = 0
import random

quick_picks = int(input("How many quick picks? "))
for quick_pick in range(0, quick_picks):
    while quick_pick_count < 5:
        number = random.randint(1, 45)
        lottery_numbers_hold.append(number)
        quick_pick_count = quick_pick_count + 1
        lottery_numbers_hold.sort()
    lottery_numbers_hold.sort()
    print(*lottery_numbers_hold)
