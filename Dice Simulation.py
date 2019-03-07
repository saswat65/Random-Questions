from random import choice

die = [1, 2, 3, 4, 5, 6]

print('This program rolls two 6-sided dice until their sum is a given target.')
target = 0
while target not in range(2, 13):
    try:
        target = int(input('Enter the target sum to roll (2- 12): '))
    except ValueError:
        print('Please enter a target between 2 and 12')

roll_sum = 0
roll_count = 0

while target != roll_sum:

    die_1 = choice(die)
    die_2 = choice(die)
    roll_sum = die_1 + die_2
    roll_count += 1
    print('You rolled a total of {}'.format(roll_sum))

print('You hit your target {} in {} rolls'.format(target, roll_count))