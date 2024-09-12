#!/usr/bin/env python3

def return_evens(num_list):
    return[num for num in num_list if num % 2 == 0]
numbers = [1,2,3,4,5,6,7,8]
even_numbers = return_evens(numbers)
print(even_numbers)
    

def make_exclamation(sentence_strings):
    return[string + "!" for string in sentence_strings]
string = "Hello" "I'm doing great" "Python is fun"
new_string = make_exclamation(string)
print(new_string)