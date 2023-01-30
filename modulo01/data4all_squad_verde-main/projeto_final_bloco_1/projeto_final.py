# Integrantes do Grupo:
# Aline Carvalho
# Eduardo Vitor
# Felipe Cunha
# Thalita Silva



menu = '''
\nBoas vindas ao nosso sistema:

1 - Inserir usuário
2 - Excluir usuário
3 - Atualizar usuário
4 - Informações de um usuário
5 - Informações de todos os usuários
6 - Sair\n
'''

sub_menu = '''
\nQual informação deseja alterar?
1 - Nome
2 - Tefone
3 - Endereço\n
'''

users = [
    [1,"Ciclano Sauro",'2345678',"Rua Boa",True],
    [2,"Fulano Silva",'3478358235',"Rua Top",True],
    [3,"John Doe",'3853385267',"MAIOBÃO",True],
    [4, "Aline Carvalho", '32988427689', "Rua Roberto Thomazeli", True],
    [5, "Felipe Cunha", '81998057401', "Rua General Polidoro", True],
    [6, "Eduardo Vitor", '12988723166', "Rua Maria Pereira", True],
    [7, "Thalita Silva", '11937523634', "Rua Domingos Maciel", True]
]

#Busca de dados iguais em id (0), nome(1), telefone(2)...
def procura_no_sistema(data, index):
    for user in users:
        if data == user[index]: return True
    return False

while(True): 
    print(menu)
    opcao = input('')
    
    if(opcao=='1'):
        
         #Inserindo as informações do novo usuário
         while True:
            new_user_nome = input('Insira o nome do usuário: ')
            if not procura_no_sistema(new_user_nome, 1): break  
            else: print('Usuário já cadastrado.\n ')
    
         while True:
            new_user_telefone = input('Insira o telefone do usuário: ')
            if not procura_no_sistema(new_user_telefone, 2): 
                if not new_user_telefone.isnumeric():
                    print('Telefone Inválido.')
                else: break
            else: print('Telefone já cadastrado.\n')

         new_user_endereco = input('Insira o endereço do usuário: ')
       
         #Adicionando novo usuário em users 
         new_user_full = [len(users)+1, new_user_nome, new_user_telefone, new_user_endereco, True]
         users.append(new_user_full)
         
    elif(opcao=='2'):
        while True:   
            id_user_excluir = input('Por favor, digite o ID do usuário que deseja excluir: ')
            if not id_user_excluir.isnumeric(): print('Digite um ID válido')
            else:        
                id_user_excluir = int(id_user_excluir)
                if id_user_excluir < 1 or id_user_excluir > len(users) or not users[id_user_excluir-1][4]: print('Usuário não encontrado')
                else:
                    users[id_user_excluir-1][4] = False
                    print('Usuário excluído!') 
                    break

    elif(opcao=='3'):
        # Recebendo o ID do Usuário
        while(True):
            user_id = input('Insira o ID do Usuário: ')
            if(not user_id.isnumeric()): print("Insira um ID válido!")
            else: 
                user_id = int(user_id)
                if(user_id < 1 or user_id > len(users)): print("Insira um ID válido!")
                elif(not users[user_id-1][4]): print("Usuário não encontrado!\n")
                else: break
    
        
        
        # Alterando as informacoes
        opcao = input(sub_menu)
        if(opcao == '1'):
            while True:
                new_user_nome= input('Insira o nome: ')
                if not procura_no_sistema(new_user_nome, 1):
                    users[user_id-1][1] = new_user_nome  
                    break
                else: print('Usuário já cadastrado.\n ')
        elif(opcao == '2'):
            while True:
                new_user_telefone = input('Insira o telefone: ')
                if not procura_no_sistema(new_user_telefone, 2): 
                    if not new_user_telefone.isnumeric():
                        print('Telefone Inválido.')
                    else: 
                        users[user_id-1][2] = new_user_telefone
                        break        
                else: print('Telefone já cadastrado.\n')
            
        elif(opcao == '3'):
            users[user_id-1][3] = input('Insira o endereço: ')
        else: 
            print('Digite uma opção válida!')
    
    elif(opcao=='4'):
        while True:
            id = input('Digite o ID do usuário: ')
            if id.isnumeric():
                id = int(id)
                if id < 1 or id > len(users) or not users[id-1][4]: print('Usuário não encontrado.')
                else: 
                    print(f'Nome: {users[id-1][1]}')
                    print(f'Telefone: {users[id-1][2]}')  
                    print(f'Endereço: {users[id-1][3]}')
                    break   
        

    elif(opcao=='5'):
        print('\nUsuários cadastrados\n')
        for user in users:
            if(user[4]):
                print(f'ID: {user[0]}\nNome: {user[1]}\nTelefone: {user[2]}\nEndereço: {user[3]}\n\n')
    elif (opcao=='6'): break
    else:
        print('Digite uma opção válida!')