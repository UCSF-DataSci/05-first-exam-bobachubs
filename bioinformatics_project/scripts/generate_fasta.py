import random

def generate_base_pairs(pairs, length):
    return ''.join(random.choice(pairs) for _ in range(length))


n = 1e6
length = 80
output = ''
for _ in range(int(n//length)):
    output += generate_base_pairs("ACGT", length)
    output += '\n'

# if there are leftovers
output += generate_base_pairs("ACGT", int(n%length))

with open('../data/random_sequence.fasta', 'w') as file:
    file.write(output)

print("Random DNA sequence generated and saved to bioinformatics_project/data/random_sequence.fasta")

