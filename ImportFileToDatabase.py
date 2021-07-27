import datetime as dt
import pandas as pd
import dateutil
import pyodbc
import os
import shutil
import time

# Connection variables
server = 'DESKTOP-NUKLK9D'
database = 'AdventureWorks2019'
username = 'Administrator'
password = 'Acesso@2021'

#insert table
table = 'AFDFILE'

#Database connection
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                  server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';Trusted_Connection=yes')
#Path files
path = "C://AFD"
target_dir = 'C://AFD//Lido'
dir_list = os.listdir(path)
#list and variables
nsr = []
cod = []
data = []
hora = []
pis = []
nfr = []
idrelogio = []
a_month = dateutil.relativedelta.relativedelta(months=1)
filter = dt.date.today() - a_month
#list files in the directory
for x in os.listdir(path):
    #get only .txt files in the directory
    if x.endswith(".txt"):
        ref_archive = open(path + '/'+x, "r", encoding='ISO-8859-1')
        line = ref_archive.readline()
        while line:
            line = ref_archive.readline()
            try:
                if (line[9:10]) == '1' and len(line.replace('\n', '')) == 232:
                    print(line[188:204])
                if (len(line.replace('\n','')) == 34 and (line[9:10]) == '3'):
                    nsr.append(line[0:9])
                    nfr.append('')
                    idrelogio.append('')
                    data.append(dt.datetime.strptime(line[10:18],'%d%m%Y').strftime('%Y-%m-%d'))
                    hora.append(dt.datetime.strptime(line[18:22],'%H%M').strftime('%H:%M'))
                    pis.append(line[22:34])
                else:
                    pass
            except Exception as e:
                print(e)
        ref_archive.close()
        timestr = time.strftime("%Y%m%d-%H%M%S")
        shutil.move(os.path.join(path, x), target_dir + '/' + x.replace('.txt', '') + '_' + timestr + '.txt')
try:
    df = pd.DataFrame({'CARTAO': pis, 'DATA' : data, 'HORA' : hora,'IDRELOGIO' : idrelogio,'NSR' : nsr, 'NFR': nfr})
    #df = df[(df['DATA'] > str(filter))]
except Exception as e:
    print(e)

#sql stetament
sql = ("INSERT INTO {} (CARTAO, DATA, HORA, IDRELOGIO, NSR, NFR) values(?,?,?,?,?,?)")
cursor = conn.cursor()
for index, row in df.iterrows():
  try:
    cursor.execute(sql.format(table), row.CARTAO, row.DATA, row.HORA, row.IDRELOGIO, row.NSR, row.NFR)
  except Exception as e:
    print(e)
conn.commit()
cursor.close()