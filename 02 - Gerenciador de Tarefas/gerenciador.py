from datetime import datetime 

class Tarefa():
    def __init__(self, nome, descricao, data_prazo, categoria, status):
        self.nome = nome
        self.descricao = descricao
        self.data_cadastro = datetime.now().strftime('%d/%m/%Y') # Data de quando foi criado
        self.data_prazo = data_prazo
        self.categoria = categoria
        self.status = status


class Gerenciador():
    def __init__(self):
        self.tarefas = []
        self.mensagem() # Mensagem de inicio
        self.menu() # Opções do menu


    def mensagem(self):
        print()
        print('-' * 57)
        print('Bem vindo ao nosso sistema de Gerenciador de Tarefas.')
        print('-' * 57)
        print()


    def menu(self):
        print()
        while True:
            try: 
                # Opções de entrada
                escolha = int(input('''O que deseja realizar?
                                     
1 - Criar uma nova Tarefa
2 - Editar uma tarefa
3 - Excluir uma tarefa
4 - Listar tarefas por categoria
5 - Listar tarefas por status
6 - Sair do sistema 
                                                              
'''))
                break
            except ValueError:
                print()
                print('Erro: Você deve digitar um número inteiro. Tente novamente.')
        
        # Definindo a requisição do usuário
        if escolha == 1:
            self.criar_tarefa()
        elif escolha == 2:
            self.editar_tarefa()
        elif escolha == 3:
            self.excluir_tarefa()
        elif escolha == 4:
            self.listar_tarefas_categoria()
        elif escolha == 5:
            self.listar_tarefas_status()
        elif escolha == 6:
            self.sair()
        else:
            print('Número incorreto. Encerrando...')
            exit()
            

    def criar_tarefa(self):
        # Coletando o nome da tarefa
        while True:
            nome = input('\nNome da tarefa: ').strip()
            if nome:  # Verifica se há conteúdo
                break
            else:
                print('Erro: O nome da tarefa não pode estar vazio.')
                print('Tente novamente...')
        
        # Coletando a descrição da tarefa
        while True:
            descricao = input('Descrição da tarefa: ').lower().strip()
            if descricao: # Verifica se há conteúdo
                break
            else:
                print('Erro: A descrição da tarefa não pode estar vazio.')
        
        # Coletando a data da tarefa
        while True:
            data_prazo = input("Digite o prazo para finalizar a tarefa (DD/MM/AAAA): ").lower().strip()
            try:
                data_formatada = datetime.strptime(data_prazo, "%d/%m/%Y")  # Converte para datetime
                if data_formatada < datetime.now():
                    print('Erro: A data informada deve ser no futuro.')
                    continue
                data_formatada = data_prazo
                break
            except ValueError:
                print("Erro: Formato inválido. Use o formato DD/MM/AAAA.")
                print()
        
        # Coletando a categoria da tarefa
        while True:
            categoria = input('Categoria da tarefa: ').lower().strip()
            if categoria: # Verifica se há conteúdo
                break 
            else:
                print('Erro: A categoria da tarefa não pode estar vazio.')
            
        # Coletando o status da tarefa
        while True:
            status = input('Status da tarefa: ').lower().strip()
            if status: # Verifica se há conteúdo
                break
            else:
                print('Erro: O status da tarefa não pode estar vazio.')
        

        nova_tarefa = Tarefa(nome, descricao, data_prazo, categoria, status) # Criando uma tarefa
        self.tarefas.append(nova_tarefa) # Adicionando a tarefa na lista

        print('Tarefa cadastrada com sucesso.')

        self.menu()
    

    def editar_tarefa(self):
        if len(self.tarefas) == 0:  # Verifica se há tarefas cadastradas
            print('Nenhuma tarefa cadastrada. Voltando ao menu...')
            print()
            self.menu()  # Voltando ao menu

        editar = input('Digite o nome da tarefa que deseja editar: ').lower().strip()
        tarefa_encontrada = False  # Flag para verificar se a tarefa foi encontrada

        for task in self.tarefas:
            if editar == task.nome.lower():  # Verifica se a tarefa existe
                print()
                print('É permitido apenas a edição do status da tarefa.')
                novo_status = input('Qual novo status da tarefa? ').strip()
                task.status = novo_status  # Atualiza o status da tarefa
                print(f'Status da tarefa "{task.nome}" atualizado para "{novo_status}".')
                print()
                tarefa_encontrada = True
                break  # Sai do loop após encontrar a tarefa

        if not tarefa_encontrada:
            print('Tarefa não encontrada. Voltando ao menu...')
            print()
        
        self.menu()  # Voltando ao menu

    
    def excluir_tarefa(self):
        if len(self.tarefas) == 0: # Verifica se há tarefas cadastradas
            print('Nenhuma tarefa cadastrada. Voltando ao menu...')
            print()
            self.menu() # Voltando ao menu
        
        excluir = input('Digite o nome da tarefa que deseja excluir: ').lower().strip()
        tarefa_encontrada = False # Flag para verificar se a tarefa foi encontrada

        for task in self.tarefas:
            if excluir == task.nome.lower(): # Verifica se existe alguma tarefa com o nome inserido
                print()
                print('Tarefa excluída com sucesso')
                self.tarefas.remove(task) # Removendo a tarefa
                tarefa_encontrada = True
                break # Sai do loop após encontrar a tarefa
        
        if not tarefa_encontrada:
            print('Tarefa não encontrada. Voltando ao menu...')
            print()
        
        self.menu() # Voltando ao menu


    def listar_tarefas_categoria(self):
        if len(self.tarefas) == 0: # Verifica se há tarefas cadastradas
            print('Nenhuma tarefa cadastrada. Voltando ao menu...')
            print()
            self.menu()
        
        tarefa_categoria = input('Digite o nome da categoria da tarefa: ').lower().strip()
        tarefa_encontrada = False # Flag para verificar se a tarefa foi encontrada

        for task in self.tarefas:
            if tarefa_categoria == task.categoria.lower().strip(): # Verifica se existe alguma tarefa com o nome inserido
                print("\nTarefa Encontrada:")
                print(f"Nome: {task.nome}")
                print(f"Descrição: {task.descricao}")
                print(f"Categoria: {task.categoria}")
                print(f"Data de Vencimento: {task.data_prazo}")
                print(f"Status: {task.status}")
                tarefa_encontrada = True

        if not tarefa_encontrada:
            print("Nenhuma tarefa encontrada para essa categoria.")
        
        self.menu() # Voltando ao menu
        
    
    def listar_tarefas_status(self):
        if len(self.tarefas) == 0: # Verifica se há tarefas cadastradas
            print('Nenhuma tarefa cadastrada. Voltando ao menu...')
            print()
            self.menu()
        
        tarefa_status = input('Digite o nome do status da tarefa: ').lower().strip()
        tarefa_encontrada = False # Flag para verificar se a tarefa foi encontrada

        for task in self.tarefas:
            if tarefa_status == task.status.lower().strip(): # Verifica se existe alguma status com o nome inserido
                print("\nTarefa Encontrada")
                print('-' * 15)
                print(f"Nome: {task.nome}")
                print(f"Descrição: {task.descricao}")
                print(f"Categoria: {task.categoria}")
                print(f"Data de Vencimento: {task.data_prazo}")
                print(f"Status: {task.status}")
                tarefa_encontrada = True

        if not tarefa_encontrada:
            print("Nenhuma tarefa encontrada para esse status.")
        
        self.menu() # Voltando ao menu
        
    
    def sair(self):
        print('Encerrando o sistema...')
        exit()


sistema = Gerenciador()
