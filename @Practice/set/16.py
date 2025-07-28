words = {"apple", "banana", "cherry", "kiwi"}

for i in list(words):
    if len(i) > 5:
        words.remove(i)

print(words)