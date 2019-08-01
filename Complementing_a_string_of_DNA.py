from Bio.Seq import Seq

file = open('DNA_seq.txt','r')
seq = Seq(file.read())

print(seq.reverse_complement())

