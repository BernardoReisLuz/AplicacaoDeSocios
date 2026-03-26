# Falta : Parte dos dois fatores , parte de liberar a atividade , parte do anexo ao banco de dados , otimizar, validações(email)
# Feito: A base do codigo da parte do login ja esta encaminhada 
#bonus : talvez tenhamos que fazer uma interface mesmo ela nao sendo obrigatoria 
#Falta tmb os levatamentos de requisitos , funcionais e nao funcionais , fluxo que vemos no treco do rubem , diagrama de classe(todos que nos sabemos) , descrisao do escopo,arquitetura do sistema 
#detalhamento de FrameWorks 
import re #comparar se vai ter os caracters que foram pedidos dentro da requisição re
import modulo 


username_start = None
senha_account= None

while (True ):
    print("Qual operacao deseja realizar ")
    print("1- Logar 2- Criar 3-Sair ")
    selecao = input()
    
    match (selecao):

        case "1" :
         
            if(username_start == None or username_start == ""):
                print("Voce nao possui uma conta ")
            else:
                email_cheak = str(input("Informe o email de acesso:"))
                password_cheak = str(input("Informe a senha de acesso:"))
                if(email_cheak == username_start and  password_cheak == senha_account):
                    print("Acesso liberado")
                elif(email_cheak == username_start and senha_account != password_cheak ):
                    print("A senha esta incorreta")
                else:
                    print("Usuario e Senha ambos estão incorreto ")
        
        case "2" :
            #Gostaria de fazer isso em poo , mas estou com um pouco de dificuldade na sintaxe e me perdendo pelo padrao que me recordo no Java
           
            if(username_start == None and senha_account == None):
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
                modulo.comparacao_senha(senha1 , senha2 , username_start)
                
            else:
                print("Ja exite um usuario com esse email ")
        case _ :
            print("Sistema fechado")
            break