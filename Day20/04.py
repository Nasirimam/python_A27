# find the greatest number among list collection
def maxim():
    a = [1, 45, 3, 54, 34, 5, 65, 5]
    max = 0
    for i in a:
        if i > max:
            max = i
    return max


print(maxim())
