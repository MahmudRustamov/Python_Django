gmail = input("Enter your email address: ").strip()

# gmail = gmail.strip()

if ' ' not in gmail and gmail.endswith("@gmail.com") and gmail.count("@") == 1:
    print("You have a good gmail")
else:
    print("Enter your email again")

