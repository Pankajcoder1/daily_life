#to generate one time password of required length.
import numpy as np
print("How many digit of otp you want:")
n=int(input())
print(np.random.randint(10**(n-1),10**n))