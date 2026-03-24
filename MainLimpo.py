# Falta : Parte dos dois fatores , parte de liberar a atividade , parte do anexo ao banco de dados , otimizar, validações
# Feito: A base do codigo da parte do login ja esta encaminhada 
#bonus : talvez tenhamos que fazer uma interface mesmo ela nao sendo obrigatoria 
#Falta tmb os levatamentos de requisitos , funcionais e nao funcionais , fluxo que vemos no treco do rubem , diagrama de classe(todos que nos sabemos) , descrisao do escopo,arquitetura do sistema 
#detalhamento de FrameWorks 
print("Qual operacao deseja realizar ")
opcao = 0 
username_start = None
senha_account= None
while (opcao !=3 ):
    print("1- Logar 2- Criar 3-Sair ")
    selecao = input()
    match (selecao):

        case "1" :
            if(username_start == None):
                print("Voce nao possui uma conta ")
            else:
                print("Informe o email do login")
                email_cheak = input()
                print("Informe a senha da conta")
                password_cheak = input()
                if(email_cheak == username_start and  password_cheak == senha_account):
                    print("Acesso liberado")
                elif(email_cheak == username_start and password_cheak != senha_account ):
                    print("A senha esta incorreta")
                else:
                    print("Usuario e Senha ambos estão incorreto ")
        case "2" :
            #Precisa fazer uma validacao da senha para ser no minimo 8 digitos e com ao menos 1 letra em caps , 1 caracter especial 
            #Gostaria de fazer isso em poo , mas estou com um pouco de dificuldade na sintaxe e me perdendo pelo padrao que me recordo no Java
            if(username_start == None and senha_account == None):
                print("Qual sera o email de acesso ao usuario")
                username_start= input()
                while True: #vai que nao preenche o email, ainda tenho que fazer uma verificação sobre o email para nao recer a sem gmail.com
                    if(username_start == None or username_start == "") : 
                        print("Preecha com um email:")
                        username_start = input()
                    else:
                     break 
                print("Digite a senha dessa conta")
                senha1 = input()
                print("Escreva novamente a mesma")
                senha2 = input()
                if(senha1 != senha2):
                    print("A senha deve ser a mesma")
                else: 
                    senha_account = senha2
                    print("conta criada")
                    print(f"Usuario:{username_start} senha: {senha_account}")
            else:
                print("Ja exite um usuario com esse email ")
        case _ :
            print("Sistema fechado")
            opcao = 3