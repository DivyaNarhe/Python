import ctypes

my_var = 'Python rocks'
another_var = my_var
yet_another_var = another_var
print(ctypes.c_long.from_address(id(my_var)).value)
