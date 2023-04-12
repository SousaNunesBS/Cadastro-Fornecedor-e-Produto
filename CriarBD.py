import sqlite3

conexao = sqlite3.connect('LojaMatriz.db')

c = conexao.cursor()

c.execute("""CREATE TABLE  fornecedores (
    ID int,
    nome text,
    telefone int,
    email text,
    cnpj int,
    expediente float
    )
""")
   

conexao.commit()

conexao.close()

