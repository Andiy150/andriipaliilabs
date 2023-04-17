# pairs.py
# -*- coding: utf-8 -*-
import sys

def find_pairs(numbers, target):
    
    pairs = []
    seen = set()
    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

def print_pairs(pairs):
    
    for pair in pairs:
        print("{} + {} = {}".format(pair[0], pair[1], target))

if __name__ == '__main__':
    
    numbers = [int(num) for num in sys.argv[1:]]
    target = 10
    pairs = find_pairs(numbers, target)
    
    print_pairs(pairs)
