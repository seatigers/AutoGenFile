#! /usr/bin/env python
# author jianghua@baidu.com
# coding utf-8
# according size and path generate appointed file

import argparse

def gen_file(path, size, unit):
    # TODO  filename is correct 
    if(int(size) <=0):
        print "size should > 0"
        return 
    file = open(path, 'w')
    if unit == 'B':
        realSize = int(size)
    elif unit == 'KB':
        realSize = int(size) * 1024
    elif unit == 'MB':
        realSize = int(size) * 1024 * 1024
    elif unit == 'GB':
        realSize = int(size) * 1024 * 1024
    file.seek(realSize-1)
    file.write('a')
    file.close()

def main():
    parser = argparse.ArgumentParser(description="auto create file")
    parser.add_argument('--unit', choices= ['B','KB', 'MB', 'GB'], help='unit of created file, eg:KB,MB,GB')
    parser.add_argument('--size', help='size of created file, eg:1')
    parser.add_argument('--path', help='path of create file, eg: 1.txt')

    args = parser.parse_args()
    if (args.path and args.unit and args.size) :
        gen_file(args.path, args.size, args.unit)

    elif args.size and args.path:
        gen_file(args.path, args.size, "B") # default unit B
        
    elif args.size and args.unit:
        gen_file("a.txt", args.size, args.unit)

    elif args.size:
        gen_file("a.txt", args.size, "B")

    else:
        print "Usage: AutoGenFile.py -h"

if __name__ == "__main__":
    main()
    
    
