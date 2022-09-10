import csv

my_string = "-What is pepsin? Pepsin is an endopeptidase that breaks down proteins into smaller peptides.-What is the proenzyme of pepsin? Pepsin's proenzyme is pepsinogen."

with open('people.csv', 'w') as out :
    my_string = my_string.replace("? ", "?,")
    lines = [line for line in my_string.split('-')]
    #setiap kali jumpa '-' kita akan split the string to multiple string
    my_string = '\n'.join(lines)
    #Kita akan join line2 tersebut dengan '\n', menyebabkan dia break line
    out.write(my_string)
