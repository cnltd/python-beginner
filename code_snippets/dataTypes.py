# Working with text
"""
String is the datatype that deals with text in python
"""
my_str = "this is a string"
print(f"Data type of variable with value {my_str} is {type(my_str)}")

# Working with numbers
"""
Integer - zero, positive or negative whole numbers without a fractional part
Float - integer with a fractional part
"""
my_int = 123456
my_float = 123.456

print(f"Data type of variable with value {my_int} is {type(my_int)}")
print(f"Data type of variable with value {my_float} is {type(my_float)}")

# working with collections
"""
# list
# tuple
# set
"""

my_list = ["abc",123,"def"]
my_tuple = ("abc",123,"def")
my_set = set((1,2,3))
my_frozenset = frozenset((1,2,3))

print(f"Data type of variable with value {my_list} is {type(my_list)}")
print(f"Data type of variable with value {my_tuple} is {type(my_tuple)}")
print(f"Data type of variable with value {my_set} is {type(my_set)}")
print(f"Data type of variable with value {my_frozenset} is {type(my_frozenset)}")

# working with key value paired data
my_dict = {"name": "firstname lastname",
           "phone": 1234567890,
           "address": "address line 1",
           "pincode": 123456}

print(f"Data type of variable with value {my_dict} is {type(my_dict)}")

# Boolean
my_boolean = True

print(f"Data type of variable with value {my_boolean} is {type(my_boolean)}")