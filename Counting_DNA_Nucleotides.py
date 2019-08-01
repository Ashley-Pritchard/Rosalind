file = open('DNA_seq.txt','r')
string = file.read()

A = string.count('A')
C = string.count('C')
G = string.count('G')
T = string.count('T')

print(A,C,G,T)

