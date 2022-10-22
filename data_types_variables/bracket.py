number_of_lines = int(input())
opening_brackets = 0
closing_brackets: int = 0
false_opening = False

for _ in range(number_of_lines):
    current_char = input()
    if current_char != "(" or current_char != ")":
        pass
    if current_char == "(":
        opening_brackets += 1
    if current_char == ")":
        closing_brackets += 1
    if closing_brackets > 0 and opening_brackets == 0:
        false_opening = True

if closing_brackets != opening_brackets or false_opening:
    print('UNBALANCED')
else:
    print("BALANCED")