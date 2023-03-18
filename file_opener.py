import tkinter as tk
from tkinter import filedialog
import os
import sys

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path.endswith((".jpg", ".png", ".jpeg")):
        os.system(f"start {file_path}")
    else:
        print("Selected file is not a jpg file.")
    print("Selected file 1:", file_path)

def open_directory():
    directory_path = filedialog.askdirectory()
    print("Selected directory:", directory_path)
    os.system(f"start {directory_path}")

root = tk.Tk()

# Title of the window
root.title("File Opener")

# Size and position of the window
root.geometry("300x150+{}+{}".format(int(root.winfo_screenwidth()/2 - 400), int(root.winfo_screenheight()/2 - 300)))

# Icon of the window
root.iconbitmap('profile.ico')

# Title
msg = tk.Label(root, text="File Opener", font=("Comic Sans MS", 24), fg=("blue"))

x = root.winfo_width() // 2
y = root.winfo_height() // 2
msg.place(relx=0.5, rely=0.12, anchor="center")

# Buttons that open a file dialog or close the program
directory_button = tk.Button(root, text="Open Directory", command=open_directory)
directory_button.pack()
directory_button.place(relx=0.5, rely=0.40, anchor="center")

open_button = tk.Button(root, text="Open JPG/PNG", command=open_file)
open_button.pack()
open_button.place(relx=0.5, rely=0.60, anchor="center")

exit_button = tk.Button(root, text="Close", command=sys.exit)
exit_button.pack()
exit_button.place(relx=0.5, rely=0.80, anchor="center")

root.mainloop()