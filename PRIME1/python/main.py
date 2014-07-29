#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys

class Solver(object):

    def __init__(self):
        self.prime_list = [2]
        pass

    def is_prime(self, v):
        if v in prime_list:
            return True
        elif v < prime_list[-1]
            return False
        else:
            while v < prime_list[-1]:
                self._add_next_prime()
            if v == prime_list[-1]:
                return True
            else:
                return False

    def _add_next_prime(self):
        i = prime_list[-1] + 1
        while True:
            if fold((lambda x y: x and y),
                    (map (lambda x: i % x == 0),
                     prime_list)):
                prime_list.add(i)
                break
            else:
                i++

def main():
    """
    """
    num = int(sys.stdin.readline())

    solver = Solver()

    for i in range(0, num):
        
        solver.do_solve()

if __name__ == '__main__':
    main()
