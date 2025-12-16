a = ["index.html", "google.com", "gmail.com", "yahoo.in", "pno.py"]
out = {}

for i in a:
    a = i.split(".")
    out[a[0]] = a[1]
print(out)
