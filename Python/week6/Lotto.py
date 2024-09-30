"""lotto"""
def lotto_calculator():
    """calcute the prize from the number"""
    prize = 0
    six_digit = input()
    two_last_digit = input()
    three_first_digit_1 = input()
    three_first_digit_2 = input()
    three_last_digit_1 = input()
    three_last_digit_2 = input()
    number = input()
    big_prize_1 = (six_digit=="000000") and (number == "999999")
    big_prize_2 = (six_digit=="999999") and (number == "000000")
    diff = abs(int(number)-int(six_digit))
    if number == six_digit:
        prize += 6_000_000
    if number[4:] == two_last_digit:
        prize += 2_000
    if number[:3] == three_first_digit_1:
        prize += 4_000
    if number[:3] == three_first_digit_2:
        prize += 4_000
    if number [3:] == three_last_digit_1:
        prize += 4_000
    if number [3:] == three_last_digit_2:
        prize += 4_000
    if diff == 1 or big_prize_1 or big_prize_2:
        prize += 100_000
    print(prize)
lotto_calculator()
