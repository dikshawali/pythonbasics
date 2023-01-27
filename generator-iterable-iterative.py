#yield helps in storing the next value. It is useful in series output where we don't want to store the entire series

def print_square():
    i=1
    while True:           #infinite loop
        yield i*i
        i+=1

for num in print_square():
    if num > 100:
        break
    print(num)