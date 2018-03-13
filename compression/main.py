#!/usr/bin/env python2
from sys import argv
from os.path import join
from run_length import RunLength

TEST_DIR = 'test_files'

def test_path(file_path):
    return file_path
    return join(TEST_DIR,file_path)
    
def process(input_file_name, encode):
    # '10-digits.txt'
    input_file_path = test_path(input_file_name)
    
    # 'test_files/10-digits.txt'
    input_file = open(input_file_path, 'rb')
    
    split_file_name = input_file_name.split('.')
    
    ext = split_file_name[-1]
    
    # Add 'out' to file name.
    split_file_name[-1] = 'out'
    
    split_file_name.append(ext)    
    
    # '10-digits.out.txt'
    output_file_name = '.'.join(split_file_name)
    output_file_path = test_path(output_file_name)
    
    output_file = open(output_file_path, 'w')
    
    bytes = input_file.read()
    
    compressor = RunLength()
    
    if(encode):
        output_bytes = compressor.encode(bytes)
    else:
        output_bytes = compressor.decode(bytes)
    
    
    
    #print(output_bytes)
    
    output_file.write(output_bytes)
    

def main():
    if(len(argv) < 3):
        print("Invalid Command")
        return
    commands = ['encode', 'decode']
    command = argv[1]
    if(command not in commands):
        print("Invalid Command")
        return
    encode = (command == 'encode')
    
    
    
    input_file_name = argv[2]
    
    if(encode):
        print("Encoding {}".format(input_file_name))
    else:
        print("Decoding {}".format(input_file_name))
    #input_file_name = '10-digits.out.txt'
    process(input_file_name, encode)

if(__name__ == '__main__'):
    main()
