
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print (hash(t))

# map:- Return an iterator that applies function to every item of iterable, yielding the # results
