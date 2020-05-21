A = b'ABC'
B = b'DEF'

C = [A, B]

C.append(3)
print(C)
print(type(C))


for i in range(2):
    C.append(A)

print(C)