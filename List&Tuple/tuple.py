# Tuple Like JS Array But Immutable;
# Once created, they cannot be modified (no changes to elements, no appending, no deleting).
# Tuple:
tup = (55, 63, 83, 47, 39, 23);
s_tup = (5,) # way to make a single element tuple;

# Length:
len_tup = len(tup);
print(len_tup);

# Indexing:
idx = tup[5];
print(idx);

# Slicing:
sl = tup[2:5];
Nsl = tup[-6:-3];
print(sl);
print(Nsl);

# [M, u, h, a, m, m, a, d]
#  0  1  2  3  4  5  6  7 
# -8 -7 -6 -5 -4 -3 -2 -1

# Tuple Functions: ...more;
"""
Tuple.index(el) # returns index of first occurrence;
Tuple.count(el) # counts total occurrences;
"""
