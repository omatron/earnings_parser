import re
import csv
import string

# Clean File
lista=[]


with open('full.csv', encoding="utf8", errors="replace") as f, open('fixed.csv', 'w', encoding="utf8", errors="replace") as out:
    reader = f.readlines()
    
    for line in reader:
        i=1
        ACOES=line.split(";")
        coluna=ACOES[2]
        #print(coluna)
        find=re.findall('ACOES ([A-Z]{4}[0-9]{1,2})',coluna)
        if find:
            lista.append(find[0])
    # Remove duplicados
    mylist = list(dict.fromkeys(lista))
    print(mylist)
        # out.writelines(line)

f.close()


