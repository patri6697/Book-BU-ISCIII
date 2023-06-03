# Ejercicio de programación en Python
# Este ejercicio consiste en desarrollar un programa en Python que realice las siguientes tareas:
# a) Crear un parámetro como para indicar el fichero FASTA a analizar o, si no se usa ningún parámetro, 
#    solicitar al usuario que ingrese el nombre del archivo por terminal.
# b) Leer el archivo FASTA y contar la frecuencia de cada nucleótido (A, C, G, T) en las secuencias.
# c) Mostrar los resultados por pantalla y guardar en un fichero, mostrando cada
#    nucleótido y su frecuencia.

# !pip install biopython
# First, we import the library biopython
from Bio import SeqIO 

# You can either directly introduce the path of your file  in the script or use the program to introduce it.
# seq = SeqIO.read("C:/Users/my_folder/file.fasta",'fasta')

file = input('Introduce the route of your file, please remove the quotation marks when copying ')
seq = SeqIO.read(file,'fasta')

print(f'FASTA content: {seq}')

# Create a dictionary to save the number of ocurrences of each nucleotide

nucleotide_freq = { 'A':seq.count('A'),
                    'T':seq.count('T'),
                    'C':seq.count('C'),
                    'G':seq.count('G') }

print (f'The frequence of nucleotides in your sequences are: {nucleotide_freq}')

# Finally to save our results, let's create a new file and write our results on it

gen = input('Please introduce the name of the gene ')
with open('nucleotide_freq_Gene.txt','w') as results:
    results.write(f'The gene {gen} has the following frequence of nucleotides: \n')
    results.write(str(nucleotide_freq))