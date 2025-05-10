todo = []

while True:
    task = input("Enter a task (or 'quit' to exit, 'list' to show tasks): ")
    if task.lower() == 'quit':
        break
    elif task.lower() == 'list':
        for i, t in enumerate(todo, 1):
            print(f"{i}. {t}")
    else:
        todo.append(task)
        print("Task added.")
