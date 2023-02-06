#!/usr/bin/python3

percent_float = float(input("What is your percentage? "))

if 90 <= percent_float < 100:
    print("you received an A")
elif 80 <= percent_float < 90:
    print("you received an B")
elif 70 <= percent_float < 80:
    print("you received an C")
elif 60 <= percent_float < 70:
    print("you received an d")
else:
    print("oops, not good")
