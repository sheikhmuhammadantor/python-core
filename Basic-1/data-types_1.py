# Data Types in Python & Examples;
# Predefined Data Types in Python;
# 1. integers
# 2. float
# 3. string
# 4. boolean
# 5. none

# ###

# 1. integers
# An integer is a whole number (i.e. without any decimal point).
# Examples: 5, 10, -15, 1000, 1000000, -1000000
num_int = 5;
num_int_negative = -5;
num_int_large = 1000000;
print(num_int, num_int_negative, num_int_large);

# 2. float
# A float is a number with a decimal point.
# Examples: 5.0, 10.0, -15.0, 1000.0, 1000000.0, -1000000.0
num_float = 5.0;
num_float_negative = -5.0;
num_float_large = 1000000.0;
print(num_float, num_float_negative, num_float_large);

# 3. string
# A string is a sequence of characters enclosed within single quotes (' ') or double quotes (" ").
# Examples: 'Hello', "World", '5', "5.0"
name_single_quotes = 'Muhammad';
name_double_quotes = "Muhammad";
name_triple_quotes = '''Muhammad''';
name_triple_double_quotes = """Muhammad""";
print(name_single_quotes, name_double_quotes, name_triple_quotes, name_triple_double_quotes);

# 4. boolean
# A boolean data type is either True or False.
# Examples: True, False
is_true = True;
is_false = False;
print(is_true, is_false);

# 5. none
# None is a special constant in Python that represents the absence of a value or a null value.
# Examples: None
null_value = None;
print(null_value);

# Type: type()
# The type() function is used to get the data type of an object.
print(type(num_int));
print(type(num_float));
print(type(name_single_quotes));
print(type(is_true));
print(type(null_value));
