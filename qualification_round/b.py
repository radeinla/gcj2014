#!/usr/bin/python

import sys

memo = {}

def get_file(argv):
    if len(argv) == 1:
        return "b.in"
    else:
        return "b_%s.in" % (argv[1])

def get_file_out(argv):
    if len(argv) == 1:
        return "b.out"
    else:
        return "b_%s.out" % (argv[1])

def print_answer(t, answer, f):
    answer = "Case #%d: %s" % (t, answer)
    print answer
    f.write(answer)
    f.write("\n")

def get_min(c, r, t, C, F, X, curr_min):
    """c = current cookies
    r = current rate
    t = time spent
    C = cookies per farm
    F = additional rate per farm
    X = target
    """
    # get
    # if (C-c)/r < X-c/r:
    #     return get_min()
    # next_farm_cost = 
    # print (c, r, t, C, F, X, curr_min)
    # print (c, r, t)
    try:
        memo[(c, r, t)]
        # print 'using memoized!'
        return memo[(c, r, t)]
    except:
        if c == X:
            ans = t
        elif t > curr_min:
            ans = curr_min
        else:
            to_target = (X-c)/r
            # print to_target
            a = get_min(X, r, t+to_target, C, F, X, t+to_target)
            next_farm_cost = (C-c)/r
            # print next_farm_cost
            b = get_min(0, r+F, t+next_farm_cost, C, F, X, min(t+to_target, curr_min))
            ans = min(a, b)
        memo[(c, r, t)] = ans
        return ans

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for t in xrange(1, T+1):
        arr = f.readline().split(" ")
        C = float(arr[0])
        F = float(arr[1])
        X = float(arr[2])
        memo.clear()
        print_answer(t, "%.7f" % get_min(0, 2, 0, C, F, X, X/2), f_out)

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main(sys.argv)