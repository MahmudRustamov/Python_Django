"""1 dan N gacha bo`lgan sonlar kvadratlari summasi S ni xisoblang."""

N = int(input("Enter N= "))
summ = 0

if N > 0:
    for i in range(1, N+1):
        summ += i*i
    print("The result is -> ", summ) 
else:
    print("N should be higher than 0")