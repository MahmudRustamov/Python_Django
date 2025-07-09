link = input('Enter your URL: ')

if link.startswith("http://") or link.startswith("https://"):
    print("You entered a correct link")
else:
    print("Please check your URL address")