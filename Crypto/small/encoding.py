from Crypto.Util.number import getPrime, bytes_to_long , long_to_bytes 

flag = b"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

pt = bytes_to_long(flag)

p = getPrime(512)
q = getPrime(512)

n = p * q

e = 3

ct = pow(pt,e,n)

print(f"N = {n}")
print(f"e = {e}")
print(f"CT = {ct}")