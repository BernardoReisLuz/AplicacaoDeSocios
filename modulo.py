import re

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
                        print("conta criada")
                        return(senha1,senha2)


        
