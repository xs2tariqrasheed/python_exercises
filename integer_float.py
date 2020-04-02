_ = print

# NOTE: don't compare floating number with ==
# A better way to compare floating point numbers is to assume that two
# numbers are equal if the difference between them is less than ε , where ε is a
# small number.
# In practice, the numbers can be compared as follows ( ε = 10 − 9 )
# if abs(a - b) < 1e-9: # a and b are equal

# _(0.3*3+0.1)
# x = 4.66668
# _(round(x, 2))
# c = 4 + 2j  # complex
# print(type(c))
# i = 9999999999999999999999999999999999
# f = 0.00000000000000000001
# print(f)
# print(45.1e-2)
# _(0.1 + 0.2)  # TODO: reading https://docs.python.org/3.6/tutorial/floatingpoint.html
# _(16 ** -2 == 1 / 16 ** 2)  # True
# _(17 / 3)  # 5.666666666666667
# _(17 // 3)  # 5
# _(17 % 3)  # 2
