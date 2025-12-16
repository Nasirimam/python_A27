a = "DAta SCiNCe"
out = ""
n = len(a)
i = 0

while i < n:
    if "A" <= a[i] <= "Z":
        out += a[i]
    i += 1
print(out + str(len(out)))
