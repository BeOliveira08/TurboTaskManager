import json
import os
from datetime import datetime
from colorama import init, Fore, Style
import shutil

init(autoreset=True)

# Constantes
TASKS_FILE = "tasks.json"
BACKUP_DIR = "backups"

# Prioridades
PRIORITIES = {
    "1": {"name": "Alta", "color": Fore.RED},
    "2": {"name": "Média", "color": Fore.YELLOW},
    "3": {"name": "Baixa", "color": Fore.GREEN}
}

def load_tasks():
    """Carrega tarefas com tratamento de erros robusto"""
    try:
        if not os.path.exists(TASKS_FILE):
            return []
        
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
            
            # Converter strings de data para objetos datetime
            for task in tasks:
                if "deadline" in task and task["deadline"]:
                    task["deadline"] = datetime.strptime(task["deadline"], "%Y-%m-%d").date()
            return tasks
            
    except (json.JSONDecodeError, IOError) as e:
        print(Fore.RED + f"Erro ao carregar tarefas: {e}")
        return []

def save_tasks(tasks):
    """Salva tarefas com backup automático"""
    try:
        # Criar backup
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
        backup_file = os.path.join(BACKUP_DIR, f"tasks_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        shutil.copy2(TASKS_FILE, backup_file) if os.path.exists(TASKS_FILE) else None
        
        # Serializar datas antes de salvar
        tasks_to_save = []
        for task in tasks:
            task_copy = task.copy()
            if "deadline" in task_copy and isinstance(task_copy["deadline"], datetime.date):
                task_copy["deadline"] = task_copy["deadline"].strftime("%Y-%m-%d")
            tasks_to_save.append(task_copy)
            
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks_to_save, file, indent=2)
            
    except Exception as e:
        print(Fore.RED + f"Erro ao salvar tarefas: {e}")

def add_task(tasks):
    """Adiciona tarefa com prioridade e prazo"""
    title = input(Fore.CYAN + "Título da tarefa: ").strip()
    if not title:
        print(Fore.YELLOW + "O título não pode estar vazio!")
        return
    
    print(Fore.CYAN + "Prioridade (1-Alta, 2-Média, 3-Baixa): ", end="")
    priority = input().strip() or "2"
    
    deadline = None
    if input("Adicionar prazo? (s/n): ").lower() == "s":
        try:
            deadline_str = input("Data (YYYY-MM-DD): ")
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
        except ValueError:
            print(Fore.RED + "Formato de data inválido!")
    
    tasks.append({
        "title": title,
        "completed": False,
        "priority": priority,
        "deadline": deadline.strftime("%Y-%m-%d") if deadline else None
    })
    save_tasks(tasks)
    print(Fore.GREEN + "✓ Tarefa adicionada!")

def list_tasks(tasks, filter_type="all"):
    """Lista tarefas com filtros avançados"""
    if not tasks:
        print(Fore.YELLOW + "Nenhuma tarefa encontrada.")
        return
    
    # Aplicar filtros
    filtered_tasks = []
    for task in tasks:
        if filter_type == "completed" and not task["completed"]:
            continue
        if filter_type == "pending" and task["completed"]:
            continue
        filtered_tasks.append(task)
    
    # Ordenar por prioridade e prazo
    filtered_tasks.sort(key=lambda x: (
        x["priority"], 
        x["deadline"] if x["deadline"] else "9999-99-99"
    ))
    
    # Exibir
    for idx, task in enumerate(filtered_tasks, 1):
        status = Fore.GREEN + "[✓]" if task["completed"] else Fore.RED + "[ ]"
        priority = PRIORITIES.get(task["priority"], PRIORITIES["2"])
        priority_display = priority["color"] + f"[{priority['name']}]"
        
        deadline = ""
        if task["deadline"]:
            deadline_date = datetime.strptime(task["deadline"], "%Y-%m-%d").date()
            days_left = (deadline_date - datetime.now().date()).days
            deadline = Fore.BLUE + f" (Prazo: {task['deadline']}"
            if days_left < 0:
                deadline += Fore.RED + " [ATRASADA]"
            elif days_left == 0:
                deadline += Fore.YELLOW + " [HOJE]"
            else:
                deadline += f", {days_left}d"
            deadline += ")"
        
        print(f"{idx}. {status} {priority_display} {task['title']}{deadline}")

def search_tasks(tasks):
    """Busca por palavras-chave"""
    term = input(Fore.CYAN + "Termo de busca: ").lower()
    results = [t for t in tasks if term in t["title"].lower()]
    list_tasks(results)

def manage_task(tasks, action):
    """Gerencia conclusão/remoção com tratamento de erros"""
    list_tasks(tasks)
    try:
        task_num = int(input(Fore.CYAN + f"Número da tarefa para {action}: "))
        if 1 <= task_num <= len(tasks):
            if action == "concluir":
                tasks[task_num-1]["completed"] = True
                save_tasks(tasks)
                print(Fore.GREEN + "✓ Tarefa concluída!")
            elif action == "remover":
                removed = tasks.pop(task_num-1)
                save_tasks(tasks)
                print(Fore.GREEN + f"✗ Tarefa '{removed['title']}' removida!")
        else:
            print(Fore.YELLOW + "Número inválido.")
    except ValueError:
        print(Fore.RED + "Por favor, insira um número válido.")

def show_stats(tasks):
    """Exibe estatísticas"""
    completed = sum(1 for t in tasks if t["completed"])
    pending = len(tasks) - completed
    
    print(Fore.MAGENTA + "\n📊 Estatísticas:")
    print(f"• Total: {len(tasks)} tarefas")
    print(Fore.GREEN + f"• Concluídas: {completed}")
    print(Fore.RED + f"• Pendentes: {pending}")
    
    # Contar por prioridade
    for level, info in PRIORITIES.items():
        count = sum(1 for t in tasks if t["priority"] == level)
        print(f"{info['color']}• {info['name']}: {count}")

def main():
    tasks = load_tasks()
    
    while True:
        print(Fore.BLUE + "\n--- SUPER TASK MANAGER ---")
        print("1. Adicionar tarefa")
        print("2. Listar todas")
        print("3. Listar concluídas")
        print("4. Listar pendentes")
        print("5. Buscar tarefas")
        print("6. Concluir tarefa")
        print("7. Remover tarefa")
        print("8. Estatísticas")
        print("9. Sair")
        
        choice = input(Fore.CYAN + "Escolha: ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            list_tasks(tasks, "completed")
        elif choice == "4":
            list_tasks(tasks, "pending")
        elif choice == "5":
            search_tasks(tasks)
        elif choice == "6":
            manage_task(tasks, "concluir")
        elif choice == "7":
            manage_task(tasks, "remover")
        elif choice == "8":
            show_stats(tasks)
        elif choice == "9":
            print(Fore.MAGENTA + "Até logo! 👋")
            break
        else:
            print(Fore.RED + "Opção inválida!")

if __name__ == "__main__":
    main()