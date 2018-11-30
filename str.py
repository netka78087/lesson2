def test(str1, str2):
    if not isinstance(str1, str):
        return 0
    if not isinstance(str2, str):
        return 0
    if str1 == str2:
        return 1
    if str2 == "learn":
        return 3
    if len(str1) > len(str2):
        return 2

str1 = 1
str2 = "learn"
print(test(str1, str2))

str1 = "ghfg"
str2 = 2
print(test(str1, str2))

str1 = "learn"
str2 = "learn"
print(test(str1, str2))

str1 = "learn11"
str2 = "tree"
print(test(str1, str2))

str1 = "fghhghgfhgfgfj"
str2 = "learn"
print(test(str1, str2))