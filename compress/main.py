import tkinter as tk
from tkinter import filedialog
import zipfile
import os
import pathlib
from tkinter.messagebox import showerror, showwarning, showinfo


root = tk.Tk()


def files_to_zip(files_to_zipp, zip_name):
    zip_filename = pathlib.Path(zip_name, "compressed.zip")
    if files_to_zip and zip_name:
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for file in files_to_zipp:
                file = pathlib.Path(file)
                zipf.write(file, arcname=os.path.basename(file))
        tk.messagebox.showinfo("Success", "Files have been compressed successfully!")
        entry_var_file.set("")
        entry_var.set("")
    else:
        tk.messagebox.showwarning("Warning", "Please select files and a destination folder.")


def select_filepath():
    file_path = filedialog.askopenfilenames(
        title="Select a file",
        filetypes=[("All files", "*.*")]
    )
    if file_path:
        entry_var_file.set(";".join(file_path))


def select_folder():
    # Open a directory dialog and store the selected folder path
    folder_path = filedialog.askdirectory(title="Select a folder")

    # If a folder was selected, set the folder path in the Entry widget
    if folder_path:
        entry_var.set(folder_path)


entry_var_file = tk.StringVar()
entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var_file, font=("Calibri", 16), width=30)
entry.pack(padx=10, pady=40)

entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 16), width=30)
entry.pack(padx=10, pady=10)

select_button = tk.Button(root, text="Select Filepath", command=lambda: select_filepath())
select_button.place(x=650, y=40)


select_button = tk.Button(root, text="Select Folder", command=lambda: select_folder())
select_button.place(x=650, y=120)

select_button = tk.Button(root, text="Compress",
                          command=lambda: files_to_zip(files_to_zipp=list(entry_var_file.get().split(";")),
                                                       zip_name=entry_var.get()))

select_button.place(x=650, y=320)


root.title("To-Do App")
root.geometry("800x400+50+50")
root.mainloop()