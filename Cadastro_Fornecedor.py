import tkinter as tk
import sqlite3


#Criando Janela:

janela = tk.Tk()
janela.title('Cadastro de Fornecedor')
janela.geometry("700x420")



def cadastrar_fornecedor():
    conexao = sqlite3.connect('LojaMatriz.db')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO fornecedores VALUES (:ID,:nome,:telefone,:email,:cnpj,:expediente)",
                {
                  'ID': entry_ID.get(),
                  'nome': entry_nome.get(),
                  'telefone': entry_telefone.get(),
                  'email': entry_email.get(),
                  'cnpj': entry_cnpj.get(),
                  'expediente': entry_expediente.get()

              })
    

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_ID.delete(0,"end")
    entry_nome.delete(0,"end")
    entry_telefone.delete(0,"end")
    entry_email.delete(0,"end")
    entry_cnpj.delete(0,"end")
    entry_expediente.delete(0,"end")
    
    


#Titulo Entradas:
label_ID = tk.Label(janela, text='ID')
label_ID.grid(row=0,column=0, padx=10, pady=10)

label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=1, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=2, column=0 , padx=10, pady=10)

label_email = tk.Label(janela, text='Email')
label_email.grid(row=3, column=0, padx=10, pady=10)

label_cnpj = tk.Label(janela, text='CNPJ')
label_cnpj.grid(row=4,column=0, padx=10, pady=10)

label_expediente = tk.Label(janela, text='Expediente')
label_expediente.grid(row=5,column=0, padx=10, pady=10)






#Caixas Entradas:
entry_ID = tk.Entry(janela , width =35)
entry_ID.grid(row=0,column=1, padx=10, pady=10)

entry_nome = tk.Entry(janela, width =35)
entry_nome.grid(row=1, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, width =35)
entry_telefone.grid(row=2, column=1 , padx=10, pady=10)

entry_email = tk.Entry(janela, width =35)
entry_email.grid(row=3, column=1, padx=10, pady=10)

entry_cnpj = tk.Entry(janela, width =35)
entry_cnpj.grid(row=4,column=1, padx=10, pady=10)

entry_expediente = tk.Entry(janela, width =35)
entry_expediente.grid(row=5,column=1, padx=10, pady=10)







# Botão de Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar Fornecedor', command=cadastrar_fornecedor)
botao_cadastrar.grid(row=10, column=1,columnspan=2, padx=10, pady=10 , ipadx = 80)



janela.mainloop()
