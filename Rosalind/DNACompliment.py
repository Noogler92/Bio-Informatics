
data = open('rosalind_revc.txt','r')
string = data.read()
data.close()

new_string = ['T' if i == 'A' else 'A' if i == 'T' else 'C' if i == 'G' else 'G' if i == 'C' else i  for i in string]

compliment = ''.join(new_string)[::-1]

data = open("rosalind_revc_out.txt", 'w')
data.write(compliment)
data.close()
#print(new)