import click  # CLI commands banane ke liye
import json   # Tasks ko JSON file me store karne ke liye
import os     # File existence check karne ke liye

# JSON file jisme tasks save honge
Todo_file = "todo.json"


def load_tasks():
    """Yeh function tasks ko JSON file se load karta hai.
       Agar file nahi mili toh ek empty list return karega."""
    if not os.path.exists(Todo_file):
        return []  # Agar file nahi mili toh empty list return karega
    with open(Todo_file, "r") as file:
        return json.load(file)  # JSON file ko read karke Python list me convert karega


def save_tasks(tasks):
    """Yeh function tasks ko JSON file me save karega."""
    with open(Todo_file, "w") as file:
        json.dump(tasks, file, indent=4)  # Tasks ko formatted JSON format me save karega


@click.group()
def cli():
    """CLI commands ka main group, jisme sub-commands add honge"""
    pass


@click.command()
@click.argument("task")  # Command line se ek task argument lega
def add(task):
    """Naya task add karne ka command"""
    tasks = load_tasks()  # Pehle se majood tasks load karega
    tasks.append({"task": task, "done": False})  # Naya task add karega (By default 'done' False hoga)
    save_tasks(tasks)  # Update file me save karega
    click.echo(f"Task Added Successfully: {task}")  # Confirmation message print karega


@click.command()
def list_tasks():
    """Yeh command sare tasks ko list karegi"""
    tasks = load_tasks()  # Tasks load karega
    if not tasks:
        click.echo("No tasks Found")  # Agar list empty hai toh yeh message show hoga
        return
    # Task list ko formatted tarike se print karega
    for index, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"  # Agar task complete hai toh ✅ warna ❌
        click.echo(f"{index}. {task['task']} [{status}]")  # Example output: 1. Wake up Early [❌]


@click.command()
@click.argument("tasks_number", type=int)  # Command line se task number lega
def complete(tasks_number):
    """Task ko complete mark karne ka command"""
    tasks = load_tasks()  # Pehle se majood tasks load karega
    if 1 <= tasks_number <= len(tasks):  # Check karega ke given task number valid hai ya nahi
        tasks[tasks_number - 1]["done"] = True  # Task ko 'done' mark karega
        save_tasks(tasks)  # Updated list ko save karega
        click.echo(f"Task {tasks_number} marked as Complete. ✅")  # Confirmation message print karega
    else:
        click.echo(f"Invalid Task Number: {tasks_number}")  # Agar number invalid hai toh error show karega


@click.command()
@click.argument("task_number", type=int)  # Command line se task number lega
def delete(task_number):
    """Task delete karne ka command"""
    tasks = load_tasks()  # Pehle se majood tasks load karega
    if 1 <= task_number <= len(tasks):  # Check karega ke given task number valid hai ya nahi
        delete_task = tasks.pop(task_number - 1)  # Task ko remove karega
        save_tasks(tasks)  # Updated list ko save karega
        click.echo(f"Removed task: {delete_task['task']}")  # Confirmation message print karega
    else:
        click.echo("Invalid Task Number")  # Agar invalid number hai toh error show karega


# CLI commands ko group ke saath register karna
cli.add_command(add)
cli.add_command(list_tasks)
cli.add_command(complete)
cli.add_command(delete)

if __name__ == "__main__":
    cli()  # CLI ko execute karega
