"""
Write a function expanded_form(number) that takes one argument and returns a string as shown in the example
'''
expanded_form(12); // Should return "10 + 2 "
expanded_form(42); // Should return "40 + 2"
expanded_form(5314); // Should return "5000 + 300 + 10 + 4"
expanded_form(70304); // Should return "70000 + 300 + 4"
'''
NOTE: all numbers are greater than 0.
"""

def expanded_form(num):
    total = []
    for index,digit in enumerate(str(num)[::-1]):  # [::-1] reverse of the list and enumerate(iterable,start) start = 0 is by default
    	if int(digit) != 0:
    		total.append(digit +('0' * index))
    return " + ".join(total[::-1])
