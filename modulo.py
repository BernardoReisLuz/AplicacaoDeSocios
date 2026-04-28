import re
import sqlite3

conexao = sqlite3.connect("Registros.db") # link com banco
cursor = conexao.cursor() #obj que serve como mensageiro para o banco de dados

cursor.execute("""CREATE TABLE IF NOT EXISTS cadastro ( 
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               email TEXT NOT NULL UNIQUE,
               senha TEXT NOT NULL,
               nome_usuario TEXT NOT NULL
               )""")
conexao.commit()

def validacao_email(email):
      padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
      while not re.match(padrao, email):
        print("Email Invalido")
        print("O Email de usuario deve segir os exemplos" \
        "email@gmail.com , email@outlook.com e assim por diante")
        email = input("Digite o Email:")
      else:
        return(email)
      

def validacao_senha (senha):
    padrao = r'(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%*&"]).{8,}$'
    while not re.search(padrao, senha): #expressão regular para verificar se tem o que é necessario para a senha
                     print("Senha deve ter \n" \
                " -Ao menos 8 digitos \n" \
                " -Ao menos 1 caracter especial(!@#$%&*) \n" \
                " -Ao menos 1 numero \n" \
                " -Ao menos 1 letra maiúscula"
                )
                     print("Senha deve conter o requisitos informados a cima")
                     senha = input("Digite a Senha: ")
    
    return senha

def comparacao_senha(senha1 , senha2 ):
        while True:
                    if(senha1 != senha2):
                        print("A senha deve ser a mesma")
                        senha2 = input()   
                    else: 
                        return(senha1,senha2)
                    
def cadastro_realizado(email , senha, nome_usuario):
    try:
        cursor.execute("INSERT INTO cadastro (email,senha,nome_usuario) VALUES(?,?,?)", (email, senha, nome_usuario))
        conexao.commit()
        print("usuario cadastrado")
    except sqlite3.IntegrityError:
           print("Esse usuario já existe")

    
    return True

def login(email , senha ):
   try:
         cursor.execute("SELECT * FROM cadastro WHERE email = ?",(email,))
         usuario = cursor.fetchone()
         

         if usuario is None:
               raise ValueError("Conta não encontrada")
            
         else:
            if usuario:   
                cursor.execute("SELECT * FROM cadastro WHERE email = ? AND senha = ?", (email,senha))
                usuario = cursor.fetchone()

                if usuario:
                    nome = usuario[3]
                    print("Login realizado!")
                    print(f"Qual ação deseja realisar {nome}")
                    
                else:
                    print("email ou senha estão incorretos")
                    return False

   except ValueError:
         print("Você não possui uma conta , Crie uma e tente novamente")



# Dropa a db para conseguir limpar os dados 
def limpar():
      cursor.execute("DELETE FROM cadastro")
      cursor.execute("DELETE FROM sqlite_sequence WHERE name='cadastro'")
      conexao.commit()
    
def puxar_nome(email):
      cursor.execute("SELECT * FROM cadastro WHERE email = ?",(email))
      
      return