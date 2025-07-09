"""1 dan 500 gacha bo'lgan sonlar orasidan toq sonlar yig'indisini topib, usha son polindrom ekanligini aniqlovchi dastur tuzing."""


counter = 1
polindrom = 0
while counter <= 500:
    if counter % 2 == 1:
        polindrom += counter
    counter += 1

if str(polindrom) == str(polindrom)[-1]:
    print("The sum is polindrome number: ", polindrom)
else:
    print("The sum is not a polindrome number: ", polindrom)