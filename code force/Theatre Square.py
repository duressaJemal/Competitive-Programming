num = input()
ar = num.split()
 
a = int(ar[0])
b = int(ar[1])
c = int(ar[2])
 
if a % c != 0:
    
    hr = a//c + 1
else:
    
    hr = a//c
    
 
if b % c != 0:
    
    vr = b//c + 1
else:
    
    vr = b//c
    
 
print(hr * vr)
