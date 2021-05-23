import re
import csv
import string

# Clean File
lista_acoes=[]
lista_jcp=[]


with open('../full.csv', encoding="utf8", errors="replace") as f, open('../fixed.csv', 'w', encoding="utf8", errors="replace") as out:
    reader = f.readlines()
    
    # Constrói a lista de ativos
    for line in reader:
        i=1
        colunas=line.split(";")
        ativo=colunas[2]
        #print(coluna)
        find_acoes=re.findall('ACOES ([A-Z]{4}[0-9]{1,2})',ativo)
        find_jcp=re.findall(' BR([A-Z]{9}[0-9]{1,2})',ativo)
        
        if find_acoes:
            lista_acoes.append(find_acoes[0])
        if find_jcp:
            lista_jcp.append(find_jcp[0])
    # Remove duplicados
    lista_acoes_u = list(dict.fromkeys(lista_acoes))
    lista_jcp_u = list(dict.fromkeys(lista_jcp))
    
    # Busca por dividendos (Acoes)
    for acoes in lista_acoes_u:
        lista_valores=[]
        for line in reader:
        
            if re.search(acoes,line):
                colunas=line.split(";")
                # print(colunas[5])
                if colunas[5] == "22":
                    valores=float(re.sub(",",".",colunas[3]))
                    # print("achou",acoes,valores)
                    lista_valores.append(valores)
                    # print(colunas[3])
        soma=sum(lista_valores)
        if soma > 0:
            print("Dividendos: ",acoes,sum(lista_valores))

    # Busca por proventos (FII)
    for acoes in lista_acoes_u:
        lista_valores=[]
        for line in reader:
        
            if re.search(acoes,line):
                colunas=line.split(";")
                # print(colunas[5])
                if colunas[5] == "200":
                    valores=float(re.sub(",",".",colunas[3]))
                    # print("achou",acoes,valores)
                    lista_valores.append(valores)
                    # print(colunas[3])
        soma=sum(lista_valores)
        if soma > 0:
            print("Proventos: ",acoes,sum(lista_valores))
   

f.close()


