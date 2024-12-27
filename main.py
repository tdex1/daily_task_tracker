from rich.console import Console
from rich.table import Table
import os
import json

# Console for output
console = Console()

# File to store tasks
TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add a task
def add_task(tasks):
    task = console.input("[bold cyan]Enter your task:[/bold cyan] ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    console.print("[green]Task added successfully![/green]")

# View tasks
def view_tasks(tasks):
    table = Table(title="Daily Task Tracker")
    table.add_column("No.", style="cyan", justify="center")
    table.add_column("Task", style="magenta")
    table.add_column("Completed", style="green", justify="center")

    for i, task in enumerate(tasks, 1):
        completed = "✅" if task["completed"] else "❌"
        table.add_row(str(i), task["task"], completed)

    console.print(table)

# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)
    task_num = console.input("[bold cyan]Enter the task number to mark as completed:[/bold cyan] ")
    try:
        task_num = int(task_num)
        tasks[task_num - 1]["completed"] = True
        save_tasks(tasks)
        console.print("[green]Task marked as completed![/green]")
    except (ValueError, IndexError):
        console.print("[red]Invalid task number![/red]")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        console.print("\n[bold yellow]1. Add Task[/bold yellow]")
        console.print("[bold yellow]2. View Tasks[/bold yellow]")
        console.print("[bold yellow]3. Complete Task[/bold yellow]")
        console.print("[bold yellow]4. Exit[/bold yellow]")

        choice = console.input("[bold cyan]Enter your choice:[/bold cyan] ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            console.print("[bold green]Goodbye![/bold green]")
            break
        else:
            console.print("[red]Invalid choice![/red]")

if __name__ == "__main__":
    main()