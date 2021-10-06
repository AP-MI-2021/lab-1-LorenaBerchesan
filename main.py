'prob 1-numar prim'
'''nr=int(input('nr:'))
e_prim= True
for i in range (2, nr//2+1):
        if nr%i==0 or nr==1 or nr==0:
            print('nu e prim')
            e_prim=False

if e_prim:
    print ('e prim')'''


'prob 2-produsul a n numere'
'''n=int(input('numar:'))
p=1
for i in range(0, n):
    nr=int(input('Numere:'))
    p=p*nr
print(p)'''


'prob 3-cmmdc'
a = int(input('primul numar:'))
b = int(input('al doilea numar:'))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print('cmmdc=', a)


