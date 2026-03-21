from Bio.Seq import Seq

def process_dna(sequence):
    dna = Seq(sequence)
    print(f"Original Sequence: {dna}")
    print(f"Complement: {dna.complement()}")
    print(f"GC Content: {100 * (dna.count('G') + dna.count('C')) / len(dna):.2f}%")

if __name__ == "__main__":
    test_seq = "ATGCGATCGTAGCTAGCTACGATCAG"
    process_dna(test_seq)
