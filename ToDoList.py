import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List Application")
        self.root.geometry("400x400")
        self.root.configure(bg="#f5f5f5")  # Light gray background

        self.tasks = []

        # Frame for Listbox and Scrollbar
        self.frame = tk.Frame(self.root, bg="#ffffff", padx=10, pady=10, borderwidth=2, relief=tk.SUNKEN)
        self.frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Listbox for tasks
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, bg="#ffffff", fg="#333333", font=('Helvetica', 12), selectmode=tk.SINGLE, borderwidth=1, relief=tk.SOLID)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Menu Button
        self.menu_button = tk.Button(self.root, text="Menu", command=self.show_menu, bg="#4CAF50", fg="#ffffff", font=('Helvetica', 12, 'bold'), borderwidth=0, padx=10, pady=5)
        self.menu_button.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, bg="#f44336", fg="#ffffff", font=('Helvetica', 12, 'bold'), borderwidth=0, padx=10, pady=5)
        self.exit_button.pack(pady=5)

    def show_menu(self):
        choice = simpledialog.askstring("Menu", "Enter your choice:\n1. Add Task\n2. Delete Task\n3. View Tasks")

        if choice == '1':
            self.add_task()
        elif choice == '2':
            self.delete_task()
        elif choice == '3':
            self.view_tasks()
        else:
            messagebox.showwarning("Invalid Choice", "Please enter a valid choice (1, 2, or 3).")

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.task_listbox.insert(tk.END, task)
            self.tasks.append(task)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        self.view_tasks()
        task_id = simpledialog.askinteger("Delete Task", "Enter the task ID to delete:")
        if task_id is not None and 0 <= task_id < len(self.tasks):
            self.task_listbox.delete(task_id)
            del self.tasks[task_id]
        else:
            messagebox.showwarning("Invalid ID", "Please enter a valid task ID.")

    def view_tasks(self):
        tasks = '\n'.join(f"{idx}: {task}" for idx, task in enumerate(self.tasks))
        if not tasks:
            tasks = "No tasks found."
        messagebox.showinfo("View Tasks", tasks)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
