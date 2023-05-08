#!/usr/bin/env python3

# Quick way to convert Google Chrome base time to a readable time format
# Useful for dirt digging on a user's browser history...

from time import strftime, localtime
import argparse


# 11644473600 is the seconds differential between epoch (01/01/1970 00:00:00) and chrome's base time (01/01/1601 00:00:00)
def calc_time(given_time):
    chrome_time = int(given_time)
    new_time = int((chrome_time/1000000) - 11644473600)
    print(strftime('%Y-%m-%d %H:%M:%S', localtime(new_time)))
    

def main():
    parser = argparse.ArgumentParser(prog='convert-time.py', description='Convert Google Chrome time to readable time format')
    parser.add_argument('-t', '--time', dest='_time', help='Single Google Chrome timestamp to convert')
    parser.add_argument('-f', '--file', dest='_file', help='Pass a file of Google Chrome timestamps to convert')
    args = parser.parse_args()

    if args._time:
        calc_time(args._time)
    elif args._file:
        with open(args._file, 'r') as f:
            lines = f.readlines()
        
            for line in lines:
                calc_time(line)


if __name__ == "__main__":
    main()
