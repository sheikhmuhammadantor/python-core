# Python Loop (while, for) Like JavaScript Loop;
# break, continue keyword work like JS;

'''
# Q1. Print numbers from 100 to 1.
'''

# while:
i = 100;
while i >= 1:
    print(i);
    i -= 1;

# for & range(start?, stop, step?):
for num in range(100, 0, -1):
    print(num);

# else & pass:
# pass like JS function - "return" ;
age = 17
if age >= 18:
    print("Allowed")
else:
    pass  # Silently ignore underage users
