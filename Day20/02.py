# WAP to extract All the uppercase alphabet from a given string at even index and its ascii value
# should be divisible by 3


def prob():
    a = "HTkjdHtJHfdbHJDGKdwifgLJDBGjgbfwbkJCHGFDhx"
    out = ""
    for i in range(0, len(a), 2):
        if "A" <= a[i] <= "Z" and ord(a[i]) % 3 == 0:
            out += a[i]
    return out


print(prob())
