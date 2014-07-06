# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 11:19:38 2014

@author: S G.
"""

import sys
    
def f():
    r = 0
    result = None
    step = 0
    g = lambda x:(12-x)*(x**3)
    print "Running program with numbers 0 to 12"
    for i in xrange(13):
#        print i
        if r<g(i):
            r = g(i)
#            print "result", r
        else:
            if result == r:
                print "Expression maxed. Result %s" %result
                """
                in the next step, if the result is lesser in this step,
                the previous step is where the result maxed out, so adjust
                variable accordingly.
                """
                print "The numbers are %s & %s" %(12-(step-1), (step-1))
                break
            else:
#                print "else result", r
#                print "x=%s" %i
                result = r
                step = i
#                print step
            
if __name__ == "__main__":
    sys.exit(f())