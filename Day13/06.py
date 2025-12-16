a = ["index.html", "google.com", "gmail.com", "yahoo.in", "pno.py"]
out = {}

for i in a:
    a = i.split(".")
    if a[1] not in out.keys():
        out[a[1]] = []
    out[a[1]] += [a[0]]
print(out)
