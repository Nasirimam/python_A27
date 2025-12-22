# Write a program to extract all the numbers from a given list and they should palindrome and at even inext

a = [1, 121, 232, 434, 656]


def palCheck(li):
    out = []
    for i in range(0, len(a), 2):
        if str(li[i]) == str(li[i])[::-1] and type(li[i]) == int:
            out.append(li[i])


palCheck(a)
