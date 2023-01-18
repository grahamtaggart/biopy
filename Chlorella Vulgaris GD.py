from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
gn = (r"C:\Users\graha\Downloads\GCA_023343905.1\ncbi_dataset\data\GCA_023343905.1\GCA_023343905.1_cvul_genomic.fna")
for record in SeqIO.parse(gn, "fasta"):
    print("%s %i" % (record.id, len(record)))
gnd = SeqIO.parse(gn, "fasta")
gnd.id = "Chlorella Vulgaris Reference Genome"
gnd.description = "The entire genome of this Algae"
gnd.seq = (gnd)
print(gnd.id)
print(gnd.description)
