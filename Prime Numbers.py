size = int(input())
s = str(input())
numbers = list(map(int, s.split(' ')))
answer = 1
a = 0
while a < size :
    answer = (answer * numbers[a]) % (1000000007)
    a = a + 1

print(answer)
