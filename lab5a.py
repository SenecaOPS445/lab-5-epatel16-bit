#!/usr/bin/env python3
# Author ID:epatel

def read_file_string(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()  
    except Exception as e:
        return f"Error reading file: {e}"

def read_file_list(file_name):
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]  
    except Exception as e:
        return f"Error reading file: {e}"

if __name__ == '__main__':
    file_name = 'data.txt'
    
    print(read_file_string(file_name))
    
    print(read_file_list(file_name))

