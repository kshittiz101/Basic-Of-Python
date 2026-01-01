# def show(a,b):
#     print(a+b)

# show(2,3)

#type of argument
# 1 postitional argument

# def show(name,age):
#     print(f"my name is {name}\n my age is {age}")

# show(44,"sujan")

#keyword argument

# def show(name,age):
#     print(f"my name is {name}\n my age is {age}")

# show(age=44,name="sujan")

#default argument
# def show(name,price,age=44):
#     print(f"my name is {name}\n my age is {age} and our price is {price}")

# show("sujan",10000)


#variable-length argument/arbitary argument
#positional arbitary argument: it is prefix with single *

# def show(a,*n,v):
#     print(a)
#     # n[0]=6
#     s=0
#     for i in n:
#         s+=i
#     print(s)


# show(1,2,3,4,v=5)

#keyword aribtary argument : it is prefix with double **

# def show(*a,**n):
#     print(a[0])
#     for key,value in n.items():
#         print(f"{key}:{value}")

# show(1,2,3,4,5,name="sujan",age=44)



