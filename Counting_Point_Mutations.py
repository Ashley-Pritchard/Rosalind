f = open('rosalind.txt', 'r')
lines = f.readlines()
seq1 = lines[0]
seq2 = lines[1]

def hamming(seq1, seq2):
	difference = 0
	length = len(seq1)
	for i in range(length):
		if seq1[i] != seq2[i]:
			difference += 1
	print(difference)

hamming(seq1, seq2)
