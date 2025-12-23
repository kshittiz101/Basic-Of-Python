# 1. What Are Loops?
# A loop is a control flow structure that repeats a block of code until a certain condition is met.
# Instead of writing the same line 10 times, you write it once and let the loop handle the repetition.
for i in range(4):  # 0,1,2,3
    print(i)


# range()- function of python it generate the sequnces of number, commanly use with for loop
for i in range(1, 11):
    print(i)


# above code loop though the range from 1 to 10 because 11 is exclusive it will not include in the range
# range syntax:
# range(start, end, step)
# start: start from 0
# end: end - 1
# step: skip pattern
