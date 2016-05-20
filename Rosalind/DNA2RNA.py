data = open('rosalind_rna.txt','r')
string = data.read()
data.close()
new_string = ['U' if i =='T' else i for i in string  ]
string = ''.join(new_string)
data = open('rosalind_rna_output.txt','w')
data.write(string)
data.close()
#print(string)