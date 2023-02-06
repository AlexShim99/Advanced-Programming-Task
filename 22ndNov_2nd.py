#!/usr/bin/python3

my_str = 'This is a test'
string_elements = my_str.split()
print (string_elements)

reversed_elements = []
for element in string_elements:
	reversed_elements.append(element[::-1])

print (reversed_elements)
new_str = ' '.join(reversed_elements)
print (new_str)
