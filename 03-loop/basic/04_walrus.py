# the walrus operator (:=) is an operator that allow you to assign values within
# an expression

# # Regular assignment - no return value
# x = 5  # This doesn't "become" 5

# # Walrus assignment - returns the value
# (x := 5)  # This expression evaluates to 5

# value = 10  (this is a statement or value)
# 4 + 8 is a expersions


# Traditional approch
lst_of_nums = [10, 20, 30, 52, 65, 68]

n = len(lst_of_nums)
print(n)
if n > 5:
    print("List length is greater than 5")


# using walrus operation
if (n := len(lst_of_nums) > 5):
    print("List length is greater than 5")
