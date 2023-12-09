brackets = input()

first_condition = brackets.count('(') == brackets.count(')')
second_condition = True

while brackets:
    opening = brackets.find('(')
    closing = brackets.find(')')
    if opening > closing:
        second_condition = False
        break
    brackets = brackets.replace('(', '', 1).replace(')', '', 1)

answer = first_condition and second_condition

print(answer)
