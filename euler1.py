def sum_mod(modulus):
    n = num / modulus
    return modulus * n * (n+1) / 2

num = 999
sum = sum_mod(3) + sum_mod(5) - sum_mod(15)
print sum
