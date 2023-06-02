# Ejercicio ISCIII

# # Ejercicio de programación en python
# Este ejercicio consiste en desarrollar un programa en Python que realice las siguientes tareas:
# a) Crear un parámetro como para indicar el fichero FASTA a analizar o, si no se usa ningún parámetro, solicitar al usuario que ingrese el nombre del archivo por terminal.
# b) Leer el archivo FASTA y contar la frecuencia de cada nucleótido (A, C, G, T) en las secuencias.
# c) Mostrar los resultados por pantalla y guardar en un fichero, mostrando cada
# nucleótido y su frecuencia.

#!pip install biopython
# First we import our sequence usin the library biopython
from Bio import SeqIO
#You can either directly introduce the path of your file  in the script or use the program to introduce it.
#seq1 = SeqIO.read("C:/Users/my_/my_folder/file.fasta",'fasta')'''

file = input('Introduce the route of your file, please remove the quotation marks when copying ')
seq1 = SeqIO.read (file,'fasta')

print(f'FASTA content: {seq1}')

#Or using biopython library you can make a dictionary to obtain in one line the number nucleotides

nucleotide_freq = {'A':seq1.count('A'),'T':seq1.count('T'),
                    'C':seq1.count('C'),'G':seq1.count('G')}

print (f'The frequence of nucleotides in your sequences are: {nucleotide_freq}')


#Finally to save our results, let's create a new file and write our results in it

results = open('nucleotide_freq_Gene.txt','w')
gen = input('Please introduce the name of the gene ')
texto_exp = str(f'The gene {gen} has the following frequence of nucleotides: \n')
results.write(texto_exp)
results.write(str(nucleotide_freq))
results.close()


