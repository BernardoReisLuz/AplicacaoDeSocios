import re
import sqlite3

conexao = sqlite3.connect("banco.db") # link com banco
cursor = conexao.cursor() #obj que serve como mensageiro para o banco de dados

cursor.execute("""CREATE TABLE IF NOT EXISTS cadastro ( 
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               email TEXT NOT NULL UNIQUE,
               senha TEXT NOT NULL
               )""")
conexao.commit()

  



def validacao_senha (senha):
    while not(re.search(r'.{8,}',senha) and re.search(r'[A-Z]',senha) and re.search(r'[!@#$%&*"]',senha) and re.search(r'\d', senha)):
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
                    
def cadastro_realizado(email , senha):
    try:
        cursor.execute("INSERT INTO cadastro (email,senha) VALUES(?,?)", (email, senha))
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
                    print("Login realizado!")
                    return True
                else:
                    print("email ou senha estão incorretos")
                    return False

   except sqlite3.ValueError:
         print("Vc não possui uma conta")
              

