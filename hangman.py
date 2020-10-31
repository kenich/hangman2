# Answer P.69

# definition function
def input_f():
    """
    Input number & Print square 1number
    """
    x = input("type number:")
    x = int(x)
    print(x**2)

def print_str(x):
    print(x)

def sum3num(x, y, z=5):
    return x + y + z

def div2num(x, y):
    return int(x)/int(y)

def multi4(x):
    return 4*x

def str2float(x):
    try:
        return float(x)
    except(ValueError):
        return "invalid input"

# end

input_f()

print_str("Hello, World!")

print(sum3num(1,2))

print(div2num(6,2))

print(multi4(3))

print(str2float("num"))

