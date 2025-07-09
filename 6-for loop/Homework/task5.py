tags = input("Enter tags: ").split(' ')

for i in range(len(tags)):
    if not tags[i].startswith('#'):
        print("#"+tags[i], end=" ")
    else:
        print(tags[i], end=" ")
