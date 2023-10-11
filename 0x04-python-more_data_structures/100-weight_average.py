#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sums = 0
        con = 0
        for i in my_list:
            sums += (i[0] * i[1])
            con += i[1]
        return (sums / con)
    else:
        return 0
