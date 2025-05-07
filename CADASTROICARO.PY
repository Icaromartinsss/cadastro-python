def main ():
    nome=""
    idade=0
    opcao=0
    while True :
        print("**MENU PRINCIPAL**")
        print("1. Cadastrar usúario")
        print("2.Ver dados cadastrados")
        print("3.Sair do sistema")
        print("*****************")
        opcao=int(input("Escolha uma opção"))
        
        if opcao == 1:
            nome=input("Digite o seu nome")
            idade=int(input("Digite a sua idade"))
            print("Dados cadastrados com sucesso!")
        elif opcao == 2:
            if  nome == "" or idade == 0:
                print("Nenhum dados cadastrado")
            else:
                print("Dados cadastrados com sucesso!")
                print(f"nome:{nome}")
                print(f"Idade:{idade}")
       
        elif opcao == 3:
            print("Encerrando o sitema...")
            break
        else:
            print("Opção Inválida")
            
            
if  __name__ == "__main__":
     main()