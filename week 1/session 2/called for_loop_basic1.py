def countdown(x):
    output = []
    for i in range (x,-1,-1):
        output.append(i)
    return output 

print(countdown(5))


def print_and_return(x):
    print(x[0])
    return (x[1])
print(print_and_return([3,7]))


def first_plus_lenght(x):
    return x[0]+len(x)
print(first_plus_lenght([1,2,3,4,5,6]))

