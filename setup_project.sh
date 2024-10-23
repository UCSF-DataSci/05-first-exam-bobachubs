#!/bin/bash
mkdir -p "bioinformatics_project"
cd bioinformatics_project

mkdir -p data scripts results

cd scripts
touch generate_fasta.py
touch dna_operations.py
touch find_cutsites.py

cd ..

cd results

touch cutsite_summary.txt
cd ..

cd data

touch random_sequence.fast

cd ..

cat <<EOL > README.md 

midterm project for DATASCI 217

EOL

echo "success"
