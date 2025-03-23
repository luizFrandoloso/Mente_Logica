import json
import os
import datetime

#Carregar o arquivo, pegando os valores atuais da agenda#
def carregar_agenda():
    try:
        if os.path.exists('tarefas.json'):
            with open("tarefas.json", 'r') as agenda:
                agenda = json.load(agenda)
                return agenda
        return []
    except FileNotFoundError:
        print("Arquivo nao encontrado!")

#Lista os valores da agenda ja carregada#
def listar_agenda(agenda):
    print("--- TAREFAS ---\n")
    for i in agenda:
        status = "Concluida" if i['concluida'] else "Pendente"
        print(f"---> ID: {i['id']}\nTitulo: {i['titulo']}.\nDescricao: {i['descricao']}.\nData: {i['data']}.\nStatus: {status}.\n")

#Adiciona a tarefa#
def adicionar_tarefa(agenda):
    print("Adicionar nova Tarefa!")
    titulo = input("Titulo: ")
    desc = input("Descricao:")
    data = datetime.datetime.now()
    data_str = data.strftime("%Y-%m-%d")
    tarefa = {
        'id' : incrementar_id(agenda),
        'titulo' : titulo,
        'descricao' : desc,
        'data' : data_str,
        'concluida' : False
    }

    agenda.append(tarefa)
    salvar_agenda(agenda)
    print("Tarefa inserida com Sucesso!")

#Incrementa o ID da tarefa que esta sendo adicionada#
def incrementar_id(agenda):
    if agenda:
        return agenda[-1]['id'] + 1
    else:
        return 1

#Remove a tarefa extritamente pelo ID#
def remover_tarefa(agenda):
    remover_id = int(input("Insira o id da tarefa que deseja excluir "))
    agenda = [tarefa for tarefa in agenda if tarefa['id'] != remover_id]
    salvar_agenda(agenda)
    print("Tarefa Excluida!")        

def mudar_tarefa():
    return 0

#Salvar as mudancas realizadas#
def salvar_agenda(agenda):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(agenda, arquivo, indent = 4)
    return 0

def pesquisar_tarefa():
    return 0

def menu():
    print("\n--- BEM VINDO A AGENDA --- ")
    print("1 --> Listar Agenda. \n2 --> Adicionar Tarefa \n3 --> Remover Tarefa \n4 --> Marcar Tarefa como Concluida. "
    "\n5 --> Salvar Agenda \n6 --> Pesquisar Tarefa \n7 --> SAIR")
    return int(input("Selecione a ação que deseja "))


def main():
    while True:   
        try:
            agenda = carregar_agenda()
            opcao = menu()
            if opcao == 1:
                listar_agenda(agenda)   
            elif opcao == 2:
                adicionar_tarefa(agenda)
            elif opcao == 3:
                remover_tarefa(agenda)
            elif opcao == 4:
                mudar_tarefa(agenda)
            elif opcao == 5:
                pesquisar_tarefa(agenda)
            elif opcao == 6:    
                salvar_agenda(agenda)
            elif opcao == 7:
                print("--- ENCERRANDO AGENDA ---")
                break
            else:
                print("Informe uma opção correspondente.")
        except ValueError:
            print("Digite um valor Valido!")

if __name__ == '__main__':
    main()