#!/usr/bin/python3

import csv

file = open("TitanicSurvival.csv", "r")
data = list(csv.reader(file,delimiter=","))
file.close()

print(data[-1])
zimmer = data[-1]
zimmer[4] = '1st'
zimmer.append('good person')
print(data[-1])
