#!/usr/bin/env python3
# Author ID:epatel16

def add(number1, number2):
    try:
        number1 = int(number1)
        number2 = int(number2)
        
        result = number1 + number2
        return result
    except:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                        
    print(add('10', 5))                      
    print(add('abc', 5))                     
    print(add('5', '5'))            

    print(read_file('seneca2.txt'))         
    print(read_file('file10000.txt'))       

