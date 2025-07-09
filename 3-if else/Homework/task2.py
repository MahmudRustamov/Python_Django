battery_lvl= int(input("Enter your battery level: "))

if battery_lvl < 0 or battery_lvl > 100:
    print('Error, try again.....')
elif battery_lvl <= 20:
    print('Charge your phone') 
elif battery_lvl <= 50:
    print('Your phone has average battery life but it needs to be charged')
else:
    print("You do not have to charge your device!")