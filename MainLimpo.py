# Falta : Parte dos dois fatores , parte de liberar a atividade , parte do anexo ao banco de dados , otimizar, validações(email)
# Feito: A base do codigo da parte do login ja esta encaminhada 
#bonus : talvez tenhamos que fazer uma interface mesmo ela nao sendo obrigatoria 
#Falta tmb os levatamentos de requisitos , funcionais e nao funcionais , fluxo que vemos no treco do rubem , diagrama de classe(todos que nos sabemos) , descrisao do escopo,arquitetura do sistema 
#detalhamento de FrameWorks 
 #comparar se vai ter os caracters que foram pedidos dentro da requisição re
import modulo 
import sqlite3

conexao = sqlite3.connect("banco.db") # link com banco
cursor = conexao.cursor() #obj que serve como mensageiro para o banco de dados

cursor.execute("""CREATE TABLE IF NOT EXISTS cadastro ( 
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               email TEXT NOT NULL UNIQUE,
               senha TEXT NOT NULL
               )""")
conexao.commit()
#tabela já esta criada


while (True ):
    print("Qual operacao deseja realizar ")
    print("1- Logar 2- Criar 3-Sair ")
    selecao = input()
    
    match (selecao):

        case "1" :
                username_start = input("escreva ou o usuario da conta:")
                senha_account = input("escreva a senha da conta:")
                modulo.login(username_start,senha_account)
        
        case "2" :
            #Gostaria de fazer isso em poo , mas estou com um pouco de dificuldade na sintaxe e me perdendo pelo padrao que me recordo no Java
           #ainda precisa ser melhorada
            
                username_start = str(input("Digite o email de acesso do usuario:"))
                while True: #vai que nao preenche o email, ainda tenho que fazer uma verificação sobre o email para nao recer a sem gmail.com
                    if(username_start == None or username_start == "") : 
                        username_start = str(input("Preecha com um email:"))
                    else:
                     break 
                
                print("Senha deve ter \n" \
                " -Ao menos 8 digitos \n" \
                " -Ao menos 1 caracter especial(!@#$%&*) \n" \
                " -Ao menos 1 numero \n" \
                " -Ao menos 1 letra maiúscula"
                )
                senha1 = input("Digite a senha:")
                modulo.validacao_senha(senha1)

                senha2 = input("Digite novamente a mesma senha:")
                modulo.comparacao_senha(senha1,senha2)
                senha_account = senha2
                modulo.cadastro_realizado(username_start,senha_account)
                
                
            
        case _ :
            print("Sistema fechado")
            break