def display(n):
    while True:
        try:
            n= n+1
            if n==21:
                raise StopIteration("its are infinite numbers")
        except StopIteration as e:
            print(e)
            break
        else:
            print(n,end=" ")

display(0)