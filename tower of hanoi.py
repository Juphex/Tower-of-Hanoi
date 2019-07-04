#a = source
#b=middle/stack
#c=destination
def move(a, b=0, c=0, n=0):
    if n==1:    
        #a to c (a can be tower b)
        global counter
        print(counter)
        counter += 1
    else:
        move(a,c,b,n-1)
        #move(a,b,c,n-1)
        move(a,b,c,1)
        move(b,a,c,n-1)

if __name__ == "__main__":    
    counter = 0

    move(5,n=5)
    print(counter)