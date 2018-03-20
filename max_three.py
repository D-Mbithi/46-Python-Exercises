def max_of_three(a, b, c):
    if a > b and a > c:
        print("{0} is greater than {1} or {2}".format(a, b, c))
    elif(b > a and b > c):
        print("{0} is greater than {1} and {2}".format(b, a, c))
    else:
        print("{} is greater than {} or {}".format(c, a, b))


max_of_three(3, 2, 1)
max_of_three(2, 3, 1)
max_of_three(1, 2, 3)
