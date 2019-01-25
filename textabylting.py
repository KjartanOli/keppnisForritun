N = int(input())

texts = []
longest = 0

for i in range(N):
    text = input()
    texts.append(text)
    if len(text) > longest:
        longest = len(text)

for i in range(longest):
    for x in range(len(texts)):
        if i > len(texts[x]) - 1:
            print(" ", end = "")
        else:
            print(texts[x][i], end = "")
    print()

"""
6
This is some example text
and here is even more text
wow such text
many text
much text
alright this is enough
"""






