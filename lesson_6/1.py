def args_function(a, b, *args):
    print("I got a", a)
    print("I got a", b)
    if args:
        print(' I also get args: ', args)

def bad_function(list_to_process[], symbol="*", n=5)):
if __name__ = "__main__":
    l0 = bad_function()

    print('First call: with a,b')
    args_function(1, 2)

    print('Second call: with a,b, ...')
    args_function(1, 2, 3, 4, 5)

    print('Third call: no arguments')
    args_function()
