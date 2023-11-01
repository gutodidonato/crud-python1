import cx_Oracle
import json

# Pegando o usuário e senha do arquivo

path = r"login.json"
with open(path, "r") as arquivo:
    dados = json.load(arquivo)

login = dados["user"]
pswd = dados["password"]

# ESQUELETO BANCO DE DADOS #

# Cria a String de conexão com informações do Host, Porta e SID
print('Apontando biblioteca Oracle...')
cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\Mr Random\Desktop\Python\CRUD\instantclient-basic-windows.x64-21.12.0.0.0dbru\instantclient_21_12")
print('...feito!\n')

print('Criando DSN...')
dsn = cx_Oracle.makedsn(host="oracle.fiap.com.br", port=1521, sid="orcl")
print('...DSN criado!\n')

print('abrindo conexão')
conn = cx_Oracle.connect(user=login, password=pswd, dsn=dsn)
print('...conexão estabelecida!\n')

# Criando cursor
print('Criando cursor...')
cursor = conn.cursor()
print('...cursor criado!\n')

# CREATE
def criar_tabela(nome_tabela, coluna1, tipo1, coluna2, tipo2, coluna3, tipo3):
    sql = f'CREATE TABLE {nome_tabela} ({coluna1} {tipo1}, {coluna2} {tipo2}, {coluna3} {tipo3})'
    cursor.execute(sql)
    print(f"tabela {nome_tabela} criada")
    conn.commit()

# INSERT
def inserir_tabela(nome_tabela, valor1, valor2, valor3):
    cursor.execute(f'INSERT INTO {nome_tabela} VALUES (:valor1, :valor2, :valor3)', valor1=valor1, valor2=valor2, valor3=valor3)
    print("Valores inseridos")
    conn.commit()


# # SELECT
def consulta_geral(nome_tabela):
    cursor.execute(f'SELECT * FROM {nome_tabela}')
    linhas = cursor.fetchall()
    for i in linhas:
        print(i) 
    print()
    
def atualizar_tabela(nome_tabela, coluna_desejada, valor_alterado, coluna_parametro, valor_parametro):
    sql = f'UPDATE {nome_tabela} SET {coluna_desejada} = :valor_alterado WHERE {coluna_parametro} = :valor_parametro'
    cursor.execute(sql, valor_alterado=valor_alterado, valor_parametro=valor_parametro)
    print("Valores alterados")
    conn.commit()

def apagar_elemento(nome_tabela, coluna_parametro, valor_parametro):
    cursor.execute(f'DELETE FROM {nome_tabela} WHERE {coluna_parametro}={valor_parametro}')
    conn.commit()

'''inserir_tabela(nome_tabela="vinhos", valor1="seco", valor2="15%", valor3="1990")'''
'''inserir_tabela(nome_tabela="vinhos", valor1="tinto", valor2="20%", valor3="1995")'''
atualizar_tabela(nome_tabela="vinhos", coluna_desejada="safra", valor_alterado="1900", coluna_parametro="tipo", valor_parametro="seco")
consulta_geral("vinhos")


'''criar_tabela(nome_tabela="vinhos", coluna1="tipo", tipo1="VARCHAR2(50)", coluna2="teor", tipo2="VARCHAR2(50)", coluna3="Safra", tipo3="VARCHAR2(50)")'''


# UPDATE
# cursor.execute('UPDATE TB_USUARIO SET COLUMN1=:valor1 WHERE COLUMN2=:valor2', valor1 = 'Kaique', valor2 = 1)
# conn.commit()

# DELETE
'''print('Deletando uma entrada da tabela')
cursor.execute('DELETE FROM DAN1 WHERE COLUMN1=:valor1', valor1=1)
conn.commit()
print('...Entrada removida!\n')'''

#CRIAR METODOS DE PESQUISA NO BD
#ALTERAR PESQUISAS

print('Encerrando cursor...')
cursor.close()
print('...cursor encerrada!\n')

print('Encerrando conexão...')
conn.close()
print('...conexão encerrada!\n')
