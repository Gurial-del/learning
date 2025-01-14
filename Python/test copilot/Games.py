import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        self.root.geometry("600x400")

        self.file_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.file_listbox.pack(fill=tk.BOTH, expand=True)

        self.add_button = tk.Button(root, text="Add .exe File", command=self.add_file)
        self.add_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Selected File", command=self.delete_file)
        self.delete_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.load_files()

    def load_files(self):
        self.file_listbox.delete(0, tk.END)
        for file in os.listdir():
            if file.endswith(".exe"):
                self.file_listbox.insert(tk.END, file)

    def add_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe")])
        if file_path:
            file_name = os.path.basename(file_path)
            if not os.path.exists(file_name):
                os.rename(file_path, file_name)
                self.file_listbox.insert(tk.END, file_name)
            else:
                messagebox.showerror("Error", "File already exists")

    def delete_file(self):
        selected_file = self.file_listbox.get(tk.ACTIVE)
        if selected_file:
            os.remove(selected_file)
            self.file_listbox.delete(tk.ACTIVE)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()