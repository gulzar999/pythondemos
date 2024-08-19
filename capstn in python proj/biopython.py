DNA = "ATTCGAATCGAATCGACTGCATCGATCGATCGATTCGAACTGAATCGATGCATTGCAATTGCATGACACTGAC"
print(len(DNA))
length_of_sequence=len(DNA)
print(length_of_sequence)

#normal version
asma="gulzar"
name =len(asma)
print(asma)

#true or false
mystring ="asma gulzar"
'a'in mystring
print('c'in mystring)
mystring.find('a')
print(mystring.find('a'))

DNA = 'ATAGGGCGA'
DNA.count('A')
print(DNA.count('A'))
gc=DNA.count('G')+DNA.count('c')
print(gc)
#lenth
length =len(DNA)
gc/length * 100
#percentage
percentage_gc=(gc/length)*100
print(percentage_gc)
print('percentage gc is',percentage_gc)
#replace
mystring='PROgraminG'
mystring.replace('G','g')
print(mystring.replace('G','g'))
mystring.replace('pro','PRO') 
print(mystring.replace('PRO','pro'))          
#capitalize
myname ="asma gulzar"
capitalize_myname = myname.capitalize()
print(capitalize_myname)
#combine string/sequences
DNA='AGT'
DNA1='TTA'
combined=DNA+DNA1
print(combined)
