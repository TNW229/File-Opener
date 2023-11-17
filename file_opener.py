import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import os
import pickle

def open_file(file_path):
    if os.path.exists(file_path):
        os.startfile(file_path)
    else:
        print(f"File not found: {file_path}")

def create_button():
    file_paths = [entry.get()] + [additional_entry.get() for additional_entry in additional_entries]
    button_name = button_name_entry.get()

    if all(file_paths) and button_name:
        for file_path in file_paths:
            button = ttk.Button(sidebar_frame, text=button_name, command=lambda path=file_path: open_file(path))
            buttons.append((button, button_name, file_path))
            button_listbox.insert("", "end", values=(button_name, file_path))
            button.pack(pady=5, fill=tk.X)

def update_button(event):
    selected_item = button_listbox.selection()
    if selected_item:
        selected_index = int(selected_item[0])
        button_info = buttons[selected_index]
        button, button_name, file_path = button_info
        new_button_name = button_name_entry.get()
        if new_button_name and file_path:
            button.config(text=new_button_name)
            buttons[selected_index] = (button, new_button_name, file_path)
            button_listbox.item(selected_item, values=(new_button_name, file_path))

def delete_button():
    selected_item = button_listbox.selection()
    if selected_item:
        selected_index = int(selected_item[0])
        button_info = buttons[selected_index]
        button, _, _ = button_info
        button.destroy()
        buttons.remove(button_info)
        button_listbox.delete(selected_item)

def save_buttons():
    save_data = []
    for button_info in buttons:
        _, button_name, file_path = button_info
        save_data.append((button_name, file_path))

    desktop_path = os.path.expanduser("~/Desktop")
    save_file_path = os.path.join(desktop_path, "button_data.pickle")

    os.makedirs(os.path.dirname(save_file_path), exist_ok=True)

    with open(save_file_path, "wb") as file:
        pickle.dump(save_data, file)

def load_buttons():
    desktop_path = os.path.expanduser("~/Desktop")
    save_file_path = os.path.join(desktop_path, "button_data.pickle")

    if os.path.exists(save_file_path):
        with open(save_file_path, "rb") as file:
            save_data = pickle.load(file)

        for button_name, file_path in save_data:
            button = ttk.Button(sidebar_frame, text=button_name, command=lambda path=file_path: open_file(path))
            buttons.append((button, button_name, file_path))
            button_listbox.insert("", "end", values=(button_name, file_path))
            button.pack(pady=5, fill=tk.X)

def change_theme(theme_name):
    style.theme_use(theme_name)

def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")

    themes_button = ttk.Button(settings_window, text="Themes", command=open_theme_settings)
    themes_button.pack(pady=10)

def open_theme_settings():
    theme_settings_window = tk.Toplevel(root)
    theme_settings_window.title("Theme Settings")

    dark_button = ttk.Button(theme_settings_window, text="Dark Theme", command=lambda: change_theme("equilux"))
    dark_button.pack(pady=5)

    light_button = ttk.Button(theme_settings_window, text="Light Theme", command=lambda: change_theme("default"))
    light_button.pack(pady=5)

    windows_button = ttk.Button(theme_settings_window, text="Windows Default Theme", command=lambda: change_theme("vista"))
    windows_button.pack(pady=5)

root = ThemedTk(theme="equilux")
root.title("File Opener")

icon_path = r"C:\Users\ASUS\OneDrive\Desktop\Other\Profile.ico"
root.iconbitmap('Profile.ico')

style = ttk.Style()
style.theme_use("equilux")
style.configure("TFrame", background="#2e2e2e")
style.configure("TLabel", foreground="#ffffff", background="#2e2e2e")
style.configure("TEntry", fieldbackground="#000000", foreground="#ffffff")
style.configure("TButton", background="#383838", foreground="#ffffff")
style.configure("Treeview", background="#2e2e2e", fieldbackground="#2e2e2e", foreground="#ffffff")
sidebar_frame = ttk.Frame(root, width=200, style="TFrame")
sidebar_frame.pack(side=tk.LEFT, fill=tk.Y, padx=3, pady=3)

frame = ttk.Frame(root, style="TFrame")
frame.pack(pady=3)

entry_label = ttk.Label(frame, text="File Location:", style="TLabel")
entry_label.pack()
entry = ttk.Entry(frame, width=50, style="TEntry")
entry.pack(pady=3)

additional_entries_frame = ttk.Frame(frame, style="TFrame")
additional_entries_frame.pack()

additional_entries = []

def add_entry():
    additional_entry = ttk.Entry(additional_entries_frame, width=50, style="TEntry")
    additional_entry.pack(pady=3)
    additional_entries.append(additional_entry)

add_entry_button = ttk.Button(frame, text="Add Location Entry", command=add_entry, style="TButton")
add_entry_button.pack(pady=3)

button_name_label = ttk.Label(frame, text="Button Name:", style="TLabel")
button_name_label.pack()
button_name_entry = ttk.Entry(frame, width=30, style="TEntry")
button_name_entry.pack(padx=3, pady=3)

create_button = ttk.Button(frame, text="Create Button", command=create_button, style="TButton")
create_button.pack(padx=3, pady=3)

columns = ("Button Name", "File Path")
button_listbox = ttk.Treeview(frame, columns=columns, show="headings", style="Treeview")
button_listbox.heading("Button Name", text="Button Name")
button_listbox.heading("File Path", text="File Path")
button_listbox.pack(padx=3, pady=3)
button_listbox.bind('<<TreeviewSelect>>', update_button)

delete_button_button = ttk.Button(frame, text="Delete", command=delete_button, style="TButton")
delete_button_button.pack(padx=3, pady=3)

save_button_button = ttk.Button(frame, text="Save Buttons", command=save_buttons, style="TButton")
save_button_button.pack(padx=3, pady=3)

settings_button = ttk.Button(frame, text="⚙️", command=open_settings, style="TButton")
settings_button.pack(padx=3, pady=3)

buttons = []

load_buttons()

root.mainloop()
