import re
import csv
import string

# Clean File
lista_acoes=[]
lista_jcp=[]


with open('../full.csv', encoding="utf8", errors="replace") as f, open('../fixed.csv', 'w', encoding="utf8", errors="replace") as out:
    reader = f.readlines()
    
    for line in reader:
        i=1
        ACOES=line.split(";")
        coluna=ACOES[2]
        #print(coluna)
        find_acoes=re.findall('ACOES ([A-Z]{4}[0-9]{1,2})',coluna)
        find_jcp=re.findall(' BR([A-Z]{9}[0-9]{1,2})',coluna)
        
        if find_acoes:
            lista_acoes.append(find_acoes[0])
        if find_jcp:
            lista_jcp.append(find_jcp[0])
    # Remove duplicados
    lista_acoes_u = list(dict.fromkeys(lista_acoes))
    print(lista_acoes_u)
    lista_jcp_u = list(dict.fromkeys(lista_jcp))
    print(lista_jcp_u)
    

f.close()


