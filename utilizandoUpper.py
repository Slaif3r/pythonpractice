#programa que recibe como parametro un valor y en minuscula y lo devuelve en mayuscula y viceversa
var = raw_input('type in something: ')
if var.islower() == True:
    print var.upper()
elif var.isupper() == True:
    print var.lower()
else:
    print('\n'"it's not a letter")
