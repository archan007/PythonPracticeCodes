str1 = str(input())
length = len(str1) - 1
finalName = ''
while length >= 0 :
    finalName += str1[length]
    length = length -1
if str1 == finalName :
    print('YES')
else:
    print('NO')