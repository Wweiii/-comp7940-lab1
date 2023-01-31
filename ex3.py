# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]


def print_factor(x):
    if x == 0: return [0]
    if x == 1: return [1]
    rlist = []
    for j in x:
        for i in range(1, j + 1):
            if j % i == 0:
                rlist.append(i)

    return rlist


if __name__ == '__main__':
    print(print_factor(l))
