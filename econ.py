import sys
def menu():
    #print what options you have
    print ("Welcome to econ calc your options are:")
    print ("1) F/P")
    print ("2) P/F")
    print ("3) P/A")
    print ("4) A/P")
    print ("5) F/A")
    print ("6) A/F")
    print ("7) P/G")
    print ("8) A/G")
    print ("9) P/A Geometric")
    print ("0) Quit")
    return int(input("Choose your option: "))

def f_p(i,n): #1
    x = (1+(i/100))**n
    print (x)    
    input("Press any key")
    print (" ")
    
def p_f(i,n): #2
    x = 1/((1+(i/100))**n)
    print (x)
    input("Press any key")
    print (" ")

def p_a(i,n): #3
    x = (((1+(i/100))**n)-1)/((i/100)*((1+(i/100))**n))
    print (x)
    input("Press any key")
    print (" ")

def a_p(i,n): #4
    x = ((i/100)*((1+(i/100))**n))/(((1+(i/100))**n)-1)
    print (x)
    input("Press any key")
    print (" ")

def f_a(i,n): #5
    x = (((1+(i/100))**n)-1)/(i/100)
    print (x)
    input("Press any key")
    print (" ")

def a_f(i,n): #6
    x = (i/100)/(((1+(i/100))**n)-1)
    print (x)
    input("Press any key")
    print (" ")

def p_g(i,n): #7
    x = (((1+(i/100))**n)-(i/100)*n-1)/(((i/100)**2)*((1+(i/100))**n))
    print (x)
    input("Press any key")
    print (" ")

def a_g(i,n): #8 
    x = (i/100)
    y = (((1+x)**n)-1)
    z = ((1/x)-(n/y))
    print (z)
    input("Press any key")
    print (" ")

def p_aG(i,n,g): #9
    i = (i/100)
    g = (g/100)
    if i != g:
        x = ((1+g)/(1+i))
        y = (1-x**n)
        z = (y/(i-g))
        print (z)
        input("Press any key")
        print (" ")
    else:
        x = (n/(1+i))
        print (x)
        input("Press any key")
        print (" ")
    
loop = 1
choice = 0
x = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        f_p(int(input("i=")),int(input("n=")))
    elif choice == 2:
        p_f(int(input("i=")),int(input("n=")))
    elif choice == 3:
        p_a(int(input("i=")),int(input("n=")))
    elif choice == 4:
        a_p(int(input("i=")),int(input("n=")))
    elif choice == 5:
        f_a(int(input("i=")),int(input("n=")))
    elif choice == 6:
        a_f(int(input("i=")),int(input("n=")))
    elif choice == 7:
        p_g(int(input("i=")),int(input("n=")))
    elif choice == 8:
        a_g(int(input("i=")),int(input("n=")))
    elif choice == 9:
        p_aG(int(input("i=")),int(input("n=")),int(input("g=")))
    elif choice == 0:
        loop = 0
        sys.exit(1)
