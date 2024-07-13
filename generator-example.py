def my_gen():
    n = 1
    print('First print, n is iqual a {}'.format(n))
    # Generator function contains yield statements
    yield n


    n += 1
    print('Second print, n is iqual a {}'.format(n))
    yield n

    n += 1
    print('third and last print, n is iqual a {}'.format(n))
    yield n
