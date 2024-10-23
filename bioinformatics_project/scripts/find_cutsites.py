import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("--f", dest='file', type=str, help='specify FASTA file path')
parser.add_argument("--s", dest="cutsite", type=str, help='specify cutsite sequence')
args = parser.parse_args()
file_path = args.file
cutsite_seq = args.cutsite

def read_fasta_file(file):
    with open(file, 'r') as file:
        dna_sequence = file.read().replace('\n', '')
    return dna_sequence



def cutsite_pairs(cutsite_indices):
    pairs = []
    for i in range(len(cutsite_indices)):
        for j in range(i + 1, len(cutsite_indices)):
            d = cutsite_indices[j] - cutsite_indices[i]
            if d > 120000:
                break
            if 80000 <= d <= 120000:
                pairs.append((cutsite_indices[i], cutsite_indices[j]))
    return pairs


dna_sequence = read_fasta_file(file_path)
cutsite_indices = [x.start() for x in re.finditer(cutsite_seq.replace('|', ''), dna_sequence)]
cutsite_pairs = cutsite_pairs(cutsite_indices)

print("Analyzing cut site: ", cutsite_seq)
print("Total cut sites found: ", len(cutsite_indices))
print("Cut site pairs 80-120 kbp apart: ", len(cutsite_pairs))
print("First 5 pairs: ")

for i, pair in enumerate(cutsite_pairs[:5]):
    print(f"{i+1}. {pair[0]} - {pair[1]}")


# example usage
# python find_cutsites.py --f ../data/random_sequence.fasta --s "A|GAGTCC"

with open("../results/distant_cutsite_summary.txt", 'w') as file:
    file.write(f"Analyzing cut site: {cutsite_seq}\n")
    file.write(f"Total cut sites found: {len(cutsite_indices)}\n")
    file.write(f"Cut site pairs 80-120 kbp apart: {len(cutsite_pairs)}\n")
    file.write("First 5 pairs: \n")
    for i, pair in enumerate(cutsite_pairs[:5]):
        file.write(f"{i+1}. {pair[0]} - {pair[1]}\n")

print("Added to results folder")