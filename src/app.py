from bs4 import BeautifulSoup
import requests
import time
import os
import threading
import csv
#def printit():
 #   threading.Timer(5.0,printit).start() 
 #   print("hola")

#printit()
def printit():
    # 5 en timer para probar, cambiar a 300.    
    threading.Timer(5.0,printit).start() 
    url = 'https://www.cronista.com/MercadosOnline/dolar.html'

    page_response = requests.get(url, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    monedaData=[]
    monedaAux=[]
    monedaAux2=[]
    monedaAux3= list()

    MonedaRows = page_content.find_all("tr")
    for row in MonedaRows[1: ]:
        valoresHtml = row.find_all("td")[1: 3]
        valoresArray =  list(map(lambda data: (data.text), valoresHtml))
        typesHtml = row.find_all()

        name = str(row.find("a").text).strip()
    
        #print(name,valoresArray)
       
        
        x=float(str(valoresArray[0][2:7]).replace(",","."))
        y=float(str(valoresArray[1][2:7]).replace(",","."))
        monedaData.append([name,str(x),str(y)])
        compra = str(x)
        venta = str(y)


    #for line in monedaData:
        # print(line)

    with open("dolar.csv", "a") as new_file:
     csv_writer  = csv.writer(new_file, delimiter=",")
     

     for line in monedaData:
         csv_writer.writerow(line)
        
    with open('dolar.csv', newline='') as File:  
     reader = csv.reader(File)
     
     for row in reader:  
         if not row:
             continue
         else:
             monedaAux.append(row[1])
             monedaAux2.append([row[0],row[1],row[2]])
                         
    monedaAux2.reverse()
    monedaAux.reverse()
    #CHANGE Balanz: 55.00 / 57.00 --> 56.00 / 58.00

    for i in range(0,3):
         #print(monedaAux[i])
         j = i+3
         if monedaAux[i]==monedaAux[j]:
             aux = monedaAux2[i]
             print(aux[0]+": "+aux[1]+" / "+aux[2])
         else:
             aux = monedaAux2[i]
             aux2= monedaAux2[j]
             print("CHANGE "+aux2[0]+": "+aux2[1]+" / "+aux2[2]+" --> "+" "+aux[1]+" / "+aux[2])
 
    print("Fecha: " + time.strftime("%y-%m-%d %H:%M"))
printit()