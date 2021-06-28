print("Welcome to the airline ticket rating system.")
name=input("What is your name?")
print("Welcome "+name+" it is nice to meet you! ")
answer=input("So, tell us. what would you rate our ticket system out of 5 stars?")
if answer=="1":
    print("What a bummer! We apologize sincerely and will definitely look into it to fix the issues")
elif answer=="2":
    print("We apologize for the inconvenience, we hope the next time will be better")
elif answer=="3":
    print("Thank you for your honest response, we look forward to improving your upcoming experiences ")
elif answer=="4":
    print("We are happy to hear that. However, we will gladly aim to improve your exprenience even more for your utmost satisfaction!")
elif answer=="5":
    print("Wonderful! Thank you for your support and great feedback, we look forward to seeing you again")
else:
    print("invalid rating")