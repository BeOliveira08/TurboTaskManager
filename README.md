# Turbo Task Manager CLI (Python)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Version-2.0-brightgreen)

**Um gerenciador de tarefas avançado para terminal** com prioridades, prazos, buscas inteligentes e sistema de backups.

## Features Premium

**Prioridades** (Alta/Média/Baixa)  
**Prazos com alertas** (Atrasadas/Hoje)  
**Busca inteligente** por palavras-chave  
**Backup automático** das tarefas  
**Estatísticas completas**  
**Filtros avançados** (Todas/Concluídas/Pendentes)  
**Interface colorida** intuitiva  

##  Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/super-task-manager.git
cd super-task-manager

# Instale as dependências
pip install -r requirements.txt
```

 **Requisitos**: Python 3.8+ | Colorama (instalado automaticamente)

##  Como Usar

```bash
python super_task_manager.py
```

**Menu Principal:**
```
1. Adicionar tarefa
2. Listar todas
3. Listar concluídas
4. Listar pendentes
5. Buscar tarefas
6. Concluir tarefa
7. Remover tarefa
8. Estatísticas
9. Sair
```

##  Estrutura do Projeto

```
super-task-manager/
├── super_task_manager.py  # Código principal
├── tasks.json            # Banco de dados das tarefas
├── backups/              # Pasta de backups automáticos
│   └── tasks_backup_*.json
├── requirements.txt      # Dependências
└── README.md            # Este arquivo
```

##  Funcionalidades Detalhadas

###  Sistema de Prazos
- Visualização de dias restantes
- Alertas coloridos para tarefas:
  -  `[ATRASADA]`
  -  `[HOJE]`
  -  `(3d)` - dias restantes

###  Prioridades
```python
PRIORITIES = {
    "1": {"name": "Alta", "color": Fore.RED},
    "2": {"name": "Média", "color": Fore.YELLOW},
    "3": {"name": "Baixa", "color": Fore.GREEN}
}
```

###  Busca Inteligente
```bash
[Buscar tarefas]
Termo de busca: estudar
```

###  Estatísticas
```
 Estatísticas:
• Total: 5 tarefas
• Concluídas: 2
• Pendentes: 3
• Alta: 1
• Média: 2
• Baixa: 2
```

## Sistema de Backup
Backups automáticos são salvos em:
```bash
backups/
├── tasks_backup_20230815_143022.json
└── tasks_backup_20230816_101512.json
```

## Como Contribuir
1. Faça um Fork
2. Crie uma Branch (`git checkout -b feature/nova-feature`)
3. Commit (`git commit -m 'Add nova feature'`)
4. Push (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença
MIT - Distribuído livremente

##  Contato
Bernardo Oliveira - bernardocher22@gmail.com

--- 

** Link do Projeto**: https://github.com/BeOliveira08/TurboTaskManager

>**Dica**: Execute com `python -i super_task_manager.py` para modo interativo!

---

### Capturas de Tela (Adicione URLs reais)
1. **Menu Principal**: `![Menu](url-da-imagem)`
2. **Lista de Tarefas**: `![Tasks](url-da-imagem)`
3. **Estatísticas**: `![Stats](url-da-imagem)`

---

Este README está otimizado para:
- SEO com palavras-chave relevantes
- Visualização perfeita no GitHub
- Facilidade de compreensão
- Atração de contribuidores
