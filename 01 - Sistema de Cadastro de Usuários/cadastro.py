import re

class Usuario():
    def __init__(self, nome, username, e_mail, senha, confirmar_senha):
        self.nome = nome
        self.username = username
        self.e_mail = e_mail
        self.senha = senha
        self.confirmar_senha = confirmar_senha


class Sistema():
    def __init__(self):
        self.usuarios = []
        self.mensagem()
        self.menu()
    

    def mensagem(self):
        print()
        print('-' * 57)
        print('Bem vindo ao nosso sistema de gerenciamento de usuários.')
        print('-' * 57)
        print()

    def menu(self):
        # Escolhendo a opção desejada
        while True:
            try:
                escolha = int(input(''' Escolha uma opção: 
                                    
1 - Criar usuário
2 - Editar usuário
3 - Excluir usuário
4 - Realizar login
5 - Listar usuários
6 - Sair 
                                    
'''))
                break
            except ValueError:
                print()
                print("Erro: Você deve digitar um número inteiro. Tente novamente.")
        
        # Chamando a opção escolhida
        if escolha == 1:
            self.cadastro_usuario()
        elif escolha == 2:
            self.editar_usuario()
        elif escolha == 3:
            self.exclui_usuario()
        elif escolha == 4:
            self.login()
        elif escolha == 5:
            self.listagem_usuarios()
        elif escolha == 6:
            self.sair()
        else:
            print()
            print('Número incorreto, saindo...')

    
    def valida_nome(self, nome):
        if len(nome) < 3 or len(nome) > 55:
            return False
        elif not nome.replace(" ", "").isalpha():
            return False
        return True 
    

    def valida_username(self, username):
        if len(username) < 3 or len(username) > 20: 
            return False
        return True


    def valida_email(self, e_mail):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' 
        return bool(re.match(regex, e_mail))


    def valida_senha(self, senha, confirmar_senha):        
        if senha != confirmar_senha:
            return False
        return True


    def cadastro_usuario(self):
        # Validação do Nome
        while True:
            print()
            nome = str(input('Nome: ')).lower()
            if self.valida_nome(nome):
                break
            else:
                print()
                print("Erro: Nome inválido! Deve conter entre 3 e 55 caracteres e apenas letras.")

        # Validação do Username
        while True:
            username = str(input('Username: ')).strip().lower()
            if self.valida_username(username):
                break
            else:
                print()
                print("Erro: Username inválido! Deve conter entre 3 e 20 caracteres.")

        # Validação do E-mail
        while True:
            e_mail = str(input('E-mail: ')).strip().lower()
            if self.valida_email(e_mail):
                break
            else:
                print()
                print("Erro: E-mail inválido. Certifique-se de que o e-mail está no formato correto (ex: usuario@dominio.com).")

        # Validação da Senha
        while True:
            senha = str(input('Senha: '))
            confirmar_senha = str(input('Confirmar senha: '))
            if self.valida_senha(senha, confirmar_senha):
                break
            else:
                print()
                print("Erro: Senha inválida. A senha deve ter pelo menos 6 caracteres e as senhas digitadas devem coincidir.")
        
        # Criando um novo usuário e armazenando na lista
        novo_usuario = Usuario(nome, username, e_mail, senha, confirmar_senha)
        self.usuarios.append(novo_usuario)

        print()
        print('Cadastro realizado com sucesso... Voltando ao menu')
        print()
        self.menu()

    def editar_usuario(self):
        print()
        usuario = input('Qual usuário deseja editar? ').strip().lower()
        print('Buscando usuário...')

        usuario_encontrado = False  # Flag para verificar se o usuário foi encontrado

        for user in self.usuarios:
            if usuario == user.username.lower() or usuario == user.nome.lower():
                usuario_encontrado = True  

                while True:
                    try:
                        print()
                        edicao = int(input('''Qual informação deseja editar?
1 - Nome
2 - Username
3 - E-mail
4 - Senha
5 - Todas
 '''))
                        if edicao == 1:
                            novo_nome = input(f"Novo nome (atualmente: {user.nome}): ").strip()
                            if novo_nome:
                                user.nome = novo_nome
                            print()
                            print(f"Nome atualizado para: {user.nome}")
                            self.menu()
                        
                        elif edicao == 2:
                            novo_username = input(f"Novo username (atualmente: {user.username}): ").strip()
                            if novo_username:
                                user.username = novo_username
                            print()    
                            print(f"Username atualizado para: {user.username}")
                            self.menu()
                        
                        elif edicao == 3:
                            novo_email = input(f"Novo e-mail (atualmente: {user.e_mail}): ").strip()
                            if novo_email:
                                user.e_mail = novo_email
                            print()
                            print(f"E-mail atualizado para: {user.e_mail}")
                            self.menu()
                        
                        elif edicao == 4:
                            nova_senha = input(f"Nova senha: ").strip()
                            if nova_senha:
                                user.senha = nova_senha
                            print()
                            print(f"Senha atualizada.")
                            self.menu()
                        
                        elif edicao == 5:
                            novo_nome = input(f"Novo nome (atualmente: {user.nome}): ").strip()
                            novo_username = input(f"Novo username (atualmente: {user.username}): ").strip()
                            novo_email = input(f"Novo e-mail (atualmente: {user.e_mail}): ").strip()
                            nova_senha = input(f"Nova senha: ").strip()

                            if novo_nome:
                                user.nome = novo_nome
                            if novo_username:
                                user.username = novo_username
                            if novo_email:
                                user.e_mail = novo_email
                            if nova_senha:
                                user.senha = nova_senha
                            print()
                            print(f"Todas as informações foram atualizadas.")
                            self.menu()
                        
                        else:
                            print("Opção inválida. Tente novamente.")
                            continue  

                        break

                    except ValueError:
                        print("Erro: Você deve digitar um número inteiro. Tente novamente.")

        if not usuario_encontrado:
            print()
            print('Usuário não encontrado. Voltando ao menu...')
            self.menu()  


    def exclui_usuario(self):
        username = input('Digite o username do usuário que deseja excluir: ').strip().lower()

        # Verifica se o usuário existe na lista
        usuario_encontrado = None
        for usuario in self.usuarios:
            if usuario.username == username:
                usuario_encontrado = usuario
                break

        if usuario_encontrado:
            senha = input('Senha: ').strip()
            if usuario_encontrado.senha == senha:
                self.usuarios.remove(usuario_encontrado)
                print(f"Usuário '{username}' deletado com sucesso!")
            else:
                print('Senha inválida. A exclusão foi cancelada.')
        else:
            print()
            print(f"Erro: Usuário com username '{username}' não encontrado.")
        
        self.menu()


    def login(self):
        username = input('Username: ').strip().lower()
        senha = input('Senha: ')

        # Verifica se o usuário existe 
        usuario_encontrado = None
        for usuario in self.usuarios:
            if usuario.username == username:
                usuario_encontrado = usuario
                break
        
        if usuario_encontrado:
            if usuario.senha == senha:
                print('Login realizado com sucesso.')
            else:
                print('Senha incorreta.')
                self.menu()
        else:
            print(f"Erro: Usuário com username '{username}' não encontrado.")

    
    def listagem_usuarios(self):
        if len(self.usuarios) > 0:
            for user in self.usuarios:
                print()
                print(f'Nome: {user.nome}')
                print(f'Username: {user.username}')
                print(f'E-mail: {user.e_mail}')
                print()
                self.menu()
        else:
            print()
            print('Sem usuários cadastrados. Direcionando ao cadastro de usuários...')
            self.cadastro_usuario()
    

    def sair(self):
        print("Encerrando o programa...")
        exit()


sistema = Sistema()

