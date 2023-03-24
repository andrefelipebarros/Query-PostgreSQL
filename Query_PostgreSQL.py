
#IMPORTAR A BLIBIOTECA DO BANCO DE DADOS:
import psycopg2

#GERAR VARIÁVEL COM INFORMAÇÕES PARA A CONEXÃO:
conn = psycopg2.connect(
    user='',
    host='',
    port='',
    database='',
    password=''
)
#AVISO DE CONEXÃO:
print("CONECTADO")

cur = conn.cursor()

#QUERY, CASO VOCÊ NÃO SAIBA DESENVOLVER UMA ESTUDE DML( Data Manipulation Language):
query = """select * from user;""" #EXEMPLO DE QUERY PARA PUXAR TODAS AS INFORMAÇÕES DA TABELA USER:

#EXECUTAR A QUERY:
cur.execute(query)

result = cur.fetchall()

for i in result:
    print(i)