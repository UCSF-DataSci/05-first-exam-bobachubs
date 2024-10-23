import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--s", dest='seq', type=str, help='specify DNA sequence')
args = parser.parse_args()
sequence = args.seq.upper()

seq_dict = dict()
seq_dict['A'] = 'T'
seq_dict['C'] = 'G'
seq_dict['G'] = 'C'
seq_dict['T'] = 'A'

def complement(sequence):
    output = ''
    for c in sequence:
        output += seq_dict[c]
    return output

def reverse(sequence):
    return sequence[::-1]

def reverse_complement(sequence):
    return reverse(complement(sequence))

print("Original Sequence: ", sequence)
print("Complement: ", complement(sequence))
print("Reverse: ", reverse(sequence))
print("Reverse complement: ", reverse_complement(sequence))
