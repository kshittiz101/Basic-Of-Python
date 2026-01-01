#lamda ---anonymous function---which name is not define and oneline function

# syntax:
# lambda argument: expression

# def show(n):
#     return n+2

# print(show(2))

# var=lambda n:n+2
# print(var(2))

#argument can be more than one,but should be one

# var=lambda x,y,z:(x*x+y*y+z*z)/2
# print(var(3,5,3))



# iterator--it is object contain countable number of value eg:list,string set dict,tuple

#map(),filter(),reduce()
# def show(n):
#     return n+2

# n=[1,2,3,4,5]
# show(n)

#map() it is inbuilt function which is used to process and transform on all item in that iterator

def show(n):
    return n*n

# n=[1,5,9,4,8]
n=[1,2,3,4,5]
var=map(show,n)
print(list(var))



# var=lambda n:n*n
# a=map(var,n)
# print(list(a))

# a=list(map(lambda n:n*n,n))



# filter() --it is inbuilt function which is used to process only satisfy condition

# a=[1,2,3,4,5,6,7]
# def show(n):
#     if n%2==0:
#         return n

# var=filter(show,a)
# print(list(var))


from functools import reduce
a=[1,2,3,4,5]
def show(a,b):
    return a+b

var=reduce(show,a)
print(var)


