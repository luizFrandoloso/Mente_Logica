import json
import os
import datetime

#Carregar o arquivo, pegando os valores atuais da agenda#
def carregar_agenda():
    try:
        if os.path.exists("tarefas.json"):
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
        print(f"---> ID: {i['id']}")
        print(f"  Título: {i['titulo']}")
        print(f"  Descrição: {i['descricao']}")
        print(f"  Data: {i['data']}")
        print(f"  Status: {status}")
        print("-" * 30)

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
    try: 
        remover_id = int(input("Insira o id da tarefa que deseja excluir: "))
        agenda_filtrada = [tarefa for tarefa in agenda if tarefa['id'] != remover_id]
        if len(agenda_filtrada) < len(agenda):
            salvar_agenda(agenda_filtrada)
            print("Tarefa Excluida!!!")
        else:
            print("Não há uma tarefa correspondente ao ID fornecido.") 
    except ValueError:
        print("Valor invalido")
        
#Modificar o Status# 
def mudar_tarefa(agenda):
    try:
        id_tarefa = int(input("Insira o ID da tarefa que deseja modificar o status: "))
        for i in agenda:
            if i['id'] == id_tarefa:
                if i["concluida"]:
                    print("Tarefa ja esta concluida!!")
                else:
                    i["concluida"] = True
                    salvar_agenda(agenda)
                    print(f"tarefa --- {i["titulo"]} --- Atualizada !!")
                return
        print("ID inserido nao corresponde com uma tarefa.")
    except ValueError:
        print("ID inserido Invalido")

#Salvar as mudancas realizadas#
def salvar_agenda(agenda):
    try:
        with open("tarefas.json", 'w') as arquivo:
            json.dump(agenda, arquivo, indent = 4)
            print("Agenda salva com Sucesso!")
    except Exception as erro:
        print(f"Nao foi possivel salvar --> {erro} ")

#Pesquisa por termos#
def pesquisar_tarefa(agenda):
    pesquisa = (input("Insira o termo de pesquisa: "))
    pesquisa = pesquisa.lower()
    filtro = [tarefa for tarefa in agenda if pesquisa in tarefa['titulo'].lower() or pesquisa in tarefa['descricao'].lower()]
    tarefas_filtrada(filtro)
    
#Verifica se existe os termos filtrados#
def tarefas_filtrada(filtro):
    if filtro:
        for i, tarefa in enumerate(filtro,1):
            print(f"\nTarefa ID {i}")
            print(f"  Título: {tarefa['titulo']}")
            print(f"  Descrição: {tarefa['descricao']}")
            print(f"  Data: {tarefa['data']}")
            print(f"  Concluída: {'Sim' if tarefa['concluida'] else 'Não'}")
            print("-" * 30)  
    else:
        print("Nenhuma tarefa encontrada com o criterio informado")
    
#Menu#
def menu():
    largura = 25 #Variavel para indicar a funcao centro no print#
   
    print("\n" + "--- MENU AGENDA --- ".center(largura) + "\n")
    print("1 --> Listar Agenda.")
    print("2 --> Adicionar Tarefa.")
    print("3 --> Remover Tarefa.")
    print("4 --> Marcar Tarefa como Concluída.")
    print("5 --> Salvar Agenda.")
    print("6 --> Pesquisar Tarefa.")
    print("7 --> SAIR")
    print("-" * 30)
    return int(input("Selecione a ação que deseja "))

#Ordem das Execucoess#
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
                salvar_agenda(agenda)
            elif opcao == 6:
                pesquisar_tarefa(agenda)      
            elif opcao == 7:
                print("--- ENCERRANDO AGENDA ---")
                break
            else:
                print("Informe uma opção correspondente.")
        except ValueError:
            print("Digite um valor Valido!")

if __name__ == '__main__':
    main()