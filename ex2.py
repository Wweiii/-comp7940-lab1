# Write a function that prints all factors of the given parameter x
def print_factor(x):
    if x == 0: return [0]
    if x == 1: return [1]
    rlist = []
    for i in range(1, x + 1):
        if x % i == 0:
            rlist.append(i)

    return rlist

if __name__ == '__main__':
    print(print_factor(100))