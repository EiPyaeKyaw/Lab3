x = "h3ll0"
s = list(x)
for i,char in enumerate(s):
    if char.isdigit():
        s[i] = int(char)
print(type(s[1]))