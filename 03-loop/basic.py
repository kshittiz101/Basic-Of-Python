#loop---it is used to repeat again and again until some condition match
#it is usrd repeat instruction
#two type
#for loop ---it is used to repeat predetermine number
#it is used in sequeence traversal Eg:list,tuple,set,dict,range

# for i in range(4): #0,1,2,3
#     print("sujan",i)

# a=["sujan","ram","manoj"]
# for i in a:
#     print(i,end=' ')

# a={"sujan","ram","manoj","deepak"}
# for abc in a:
#     print(abc)


# a={'a':2,'b':43,'c':98}

# for i in a:
#     print(i)

# num=int(input("enter your nnumber : "))
# for i in range(1,11):
    
#     print(f"{num} x {i} = {num*i}")

# a=[1,2,3,4]
# for i in range(10,5,-1): #range(start,end,step)
#     print("sujan",i)


# a=["sujan","ram","safal","deepak"]
# for i in a:
#     print(i)#sujan 0
#     for j in i:
#         print(j)

# a=[1,2,9,5]
# # b=[3,4,11,7]
# # print(a)
# b=[]
# for i in a:
#     b.append(i+2)
# print(b)

a=[1,2,3,4]
b=[2,3,4,5]
c=[]


for i in range(4):#range(4) 0,1,2,3
    c.append(a[i]+b[i])
   
print(c)






