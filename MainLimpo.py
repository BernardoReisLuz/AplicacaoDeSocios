# Falta : Parte dos dois fatores , parte de liberar a atividade , otimizar,
#bonus : talvez tenhamos que fazer uma interface mesmo ela nao sendo obrigatoria 
#Falta tmb os levatamentos de requisitos , funcionais e nao funcionais , fluxo que vemos no treco do rubem , diagrama de classe(todos que nos sabemos) , descrisao do escopo,arquitetura do sistema 
#detalhamento de FrameWorks 
#comparar se vai ter os caracters que foram pedidos dentro da requisição re
import modulo 
import sqlite3

conexao = sqlite3.connect("Registros.db") # link com banco
cursor = conexao.cursor() #obj que serve como mensageiro para o banco de dados

# Vai criar a tabela para a entrada de dados , se ela já existir so vai add direto nela
cursor.execute("""CREATE TABLE IF NOT EXISTS cadastro ( 
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               email TEXT NOT NULL UNIQUE,
               senha TEXT NOT NULL,
               nome_usuario TEXT NOT NULL
               )""")


conexao.commit()


#tabela já esta criada

#While que vai fazer as ações 
while (True ):
    print("Qual operacao deseja realizar ")
    print("1- Logar 2- Criar 3-Sair ")
    selecao = input()
    
    match (selecao):

        case "1" : 
                # Tentar checar se tem uma conta com o usuario colocado
                username_start = input("escreva o usuario da conta:")
                senha_account = input("escreva a senha da conta:")
                #Entra os inputs e faz a validação que esta no modulo
                modulo.login(username_start,senha_account)
                ## Tem que fazer para puxar o nome que o usuario salvou
                ##dar um jeito de fazer esperar a conta logar
                while(True):
                    print("1 2 3")
                    selecao_acao = input()
                    match(selecao_acao):
                         
                         case "1":
                              ##
                              print("Socios")
                              #Tabela para os socios que possa armazenar arquivos
                         case "2":
                              ##
                              print("Realizar/Aprovar compra")
                         case "3":
                              ## 
                              print("Documentos Recursos")
                              
                         case "4":
                              print()
                    
                         case _ :
                              print("Nao existe essa opção escolha dentro dessas")
                    
                
        
        case "2" :
            #Gostaria de fazer isso em poo , mas estou com um pouco de dificuldade na sintaxe e me perdendo pelo padrao que me recordo no Java
           #ainda precisa ser melhorada
            
                username_start = str(input("Digite o email de acesso do usuario:"))
                #vai passar pela validacao do email criada
                modulo.validacao_email(username_start)
                
                print("Senha deve ter \n" \
                " -Ao menos 8 digitos \n" \
                " -Ao menos 1 caracter especial(!@#$%&*) \n" \
                " -Ao menos 1 numero \n" \
                " -Ao menos 1 letra maiúscula"
                )
                #Vai validar a senha depois fazer uma comparação se as senhas forem iguais 
                senha1 = input("Digite a senha:")
                modulo.validacao_senha(senha1)

                senha2 = input("Digite novamente a mesma senha:")
                modulo.comparacao_senha(senha1,senha2)
                senha_account = senha2
                nome_usuario = input("Agora informe o seu nome:")
                modulo.cadastro_realizado(username_start,senha_account, nome_usuario)
                #Conta criada
                
                
            
        case "3":
            print("Sistema fechado")
            break
          
        case _ :
            print("Selecione uma das 3 opções o selecionado não apresenta dentro dessas opções")