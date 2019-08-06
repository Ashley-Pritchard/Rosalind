from Bio import SeqIO
from Bio.SeqUtils import GC
import operator 

fasta_sequences = SeqIO.parse(open('rosalind.txt'), 'fasta')

GC_content = {}

for fasta in fasta_sequences:
	name, sequence = fasta.id, str(fasta.seq)
	GC_content.update({name: GC(sequence)})

max_id = max(GC_content, key=GC_content.get)
max_value = max(GC_content.values())
print(max_id, max_value, sep='\n')

