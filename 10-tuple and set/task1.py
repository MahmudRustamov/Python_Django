
week_days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday') 

day = input("Enter the name of the day: ").strip().lower()

if day in week_days:
    if not week_days[-1]:
        print(week_days[week_days.index(day)- 1],'', week_days[week_days.index(day) + 1] )
    else:
        print(week_days[week_days.index(day)- 1],'', week_days[0] )
else:
    print("Error")