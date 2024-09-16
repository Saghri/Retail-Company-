import tkinter as tk
from tkinter import filedialog, messagebox
import os
from order_processor import process_order
from file_manager import list_files, move_file, create_directory
from logger import setup_logger
from config_handler import get_config_value

# Setup logger
setup_logger()

def process_selected_order():
    file_path = filedialog.askopenfilename(
        title="Select Order File",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*"))
    )
    if file_path:
        process_order(file_path)
        messagebox.showinfo("Success", f"Orders processed from {file_path}")

def move_file_gui():
    source = filedialog.askopenfilename(title="Select File to Move")
    destination = filedialog.askdirectory(title="Select Destination Directory")
    
    if source and destination:
        move_file(source, destination)
        messagebox.showinfo("Success", f"File moved to {destination}")

def setup_directories():
    data_dir = get_config_value('Paths', 'DataDirectory')
    logs_dir = get_config_value('Paths', 'LogsDirectory')
    create_directory(data_dir)
    create_directory(logs_dir)
    messagebox.showinfo("Success", "Directories created")

# GUI Setup
root = tk.Tk()
root.title("Retail System")

# Buttons
process_button = tk.Button(root, text="Process Orders", command=process_selected_order)
process_button.pack(pady=10)

move_button = tk.Button(root, text="Move Files", command=move_file_gui)
move_button.pack(pady=10)

setup_button = tk.Button(root, text="Setup Directories", command=setup_directories)
setup_button.pack(pady=10)

# Run the application
root.mainloop()
