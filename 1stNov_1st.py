#!/usr/bin/python3

age = int(input('Enter your age in years: '))
max_hear_rate = 206.9 - (0.67 * age)
target = 0.65 * max_hear_rate
print ("Your target fat-burning heart", \
"rate is", target)

