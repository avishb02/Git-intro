def  new(a,b):
    print("Id for a is %d and for b is %d" % (id(a),id(b)))
    return(a+b)
x= int(input("enter 2 numbers: "))
y= int(input("enter 2 numbers: "))
z=new(x,y)
print (z)
print("Id for x is %d, for y is %d and new unc is %d" % (id(x),id(y),id(new)))
