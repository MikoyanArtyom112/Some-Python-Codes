apple_three = int(input())
apple_two = int(input())
apple_one = int(input())

banana_three = int(input())
banana_two = int(input())
banana_one = int(input())


apple_score = apple_three * 3 + apple_two * 2 + apple_one
banana_score = banana_three*3 + banana_two*2 + banana_one

if apple_score < banana_score:
    print('Team Banana Wins!')

elif banana_score < apple_score:
    print('Team Apple Wins!')

else:
    print('It is a Tie')
