fname = "words.txt"
infile = open(fname, "r")

for s in infile:
    if s[0] == "A" or s[0] == "a":
        print(s)
