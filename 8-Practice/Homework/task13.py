"""1 dan N gacha bo`lgan juft sonlar kvadratlari va toq sonlar kublari
summasi S ni xisoblang."""

N = int(input("Enter N= "))
summ_even = 0
summ_odd = 0

if N > 0:
    for i in range(1, N+1):
        if i % 2 == 0:
            summ_even += i*i
        else:
            summ_odd += i*i*i
    print(f"The sum of squares of even numbers -> {summ_even} \
          \nThe sum of cubes of odd numbers -> {summ_odd}") 
else:
    print("N should be higher than 0")