#!/bin/bash

ren=""
div=""
#Prepara a primeira linha do CSV
echo '"Liquid.";"Movim.";"Histrico";"Lanamento";"Saldo";"Cdigo";"StatementNumber"' > full.csv
#Concatena todos os CSV sem as 2 primeiras linhas

for FILE in Extrato_*.csv
    do
        #echo $FILE
        sed 1,2d $FILE >> full.csv
    done

#Extrai acoes e salva em arquivo
grep -oP 'ACOES \K\w+' full.csv | sort -u  > acoes.txt


#Busca as acoes no full.csv com base na lista de acoes.txt
while read p; do
    #Salva as ações por tipo em cada arquivo
    cat full.csv | grep $p | grep ";22;" | cut -d ";" -f4 | sed 's/,/./g' > $p"_div.csv"
    cat full.csv | grep $p | grep ";200;" | cut -d ";" -f4 | sed 's/,/./g' > $p"_ren.csv"
done <acoes.txt

#Soma as linhas
echo > div_total.csv
while read p
do
    echo $p
    sum=`awk '{s+=$1} END {print s}' $p"_div.csv" `
    echo $sum
    # filter=$(egrep "[0-9]{1,5}\.[0-9]{1,2}" $sum)
    # echo $filter
    # if (( $(egrep "[0-9]{1,5}\.[0-9]{1,2}" $sum) ))
    #     then
    #         echo "$p;"$sum";" >> div_total.csv
    #     else
    #         echo else
    #     fi

    #awk '{s+=$1} END {print s}' $p"_ren.csv" >> $p"_ren.csv"
done <acoes.txt





#Lista todos os ativos
#cat 