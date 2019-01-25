amount = int(input())

prizes = []
for i in range(amount):
    prize = int(input())
    prizes.append(prize)

print(sum(prizes))