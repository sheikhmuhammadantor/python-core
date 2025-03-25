# Expression Execution:
# 1. String & Number values can operate together with *
A,B=2,3
Tex="@"
print(2*Tex*3) # Output: @@@@@@

# 2. String & String can operate with +
C,D="2", 3
Tex2="@"
print((C+Tex2)*D) # Output: 2@2@2@

# 3. Numeric values can operate with all arithmetic operators
E,F=2,3
G=4
print(E+F*G) # Output: 14

# 4. Arithmetic expressions with integer and float will result in float
H,I=10, 5.0
J=H*I
print(J) # Output: 50.0

# 5. Result of division operator with two integers will be float
K,L=10, 5
M=K/L
print(M) # Output: 2.0

# 6. Integer division with float and int will give int displayed as float
# # Result of (A//B) is same as floor(A/B); Result of (A/B) is float
N,O=1.5, 3
P=N//O
print(P, N/O) # Output: 0 0.5

# 7. Remainder is negative when denominator is negative
Q,R=10, -3
S=Q%R
print(S) # Output: -2
