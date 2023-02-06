from tkinter import Label, Button, LabelFrame, Radiobutton, Tk, Text, Entry, IntVar, Menu
from tkinter import filedialog
from tkinter import messagebox
import os
import zipfile
import patoolib


def brows_file():
    filenmae = filedialog.askdirectory(initialdir="/", title="Select a File")
    address_entery.insert(0, filenmae)


def make():
    if (address_entery.get()):
        try:
            counter = add_info_label['text']
            pathI = os.path.join(address_entery.get(), "input")
            pathO = os.path.join(address_entery.get(), "output")
            os.makedirs(pathI)
            os.makedirs(pathO)

            with open(f"{pathI}/input{counter}.txt", 'w') as f:

                f.write(input_box.get("1.0", "end-1c"))

            with open(f"{pathO}/output{counter}.txt", 'w') as f:

                f.write(output_box.get("1.0", "end-1c"))
            add_info_label.config(text=str(int(counter)+1))
            input_box.delete("1.0", "end")
            output_box.delete("1.0", "end")

        except:
            with open(f"{pathI}/input{counter}.txt", 'w') as f:

                f.write(input_box.get("1.0", "end-1c"))

            with open(f"{pathO}/output{counter}.txt", 'w') as f:

                f.write(output_box.get("1.0", "end-1c"))
            add_info_label.config(text=str(int(counter)+1))
            input_box.delete("1.0", "end")
            output_box.delete("1.0", "end")
    else:

        messagebox.showerror(title="Error", message="Fill the address blank!!")


def make_archive_file(mode, name):
    files = ("input", "output")
    os.chdir(address_entery.get())
    if (mode == 1):
        patoolib.create_archive(f"{os.getcwd()}/{name}.rar", files)
        messagebox.showinfo(title="exporting", message="successfully done")
    elif (mode == 2):
        patoolib.create_archive(f"{os.getcwd()}/problem.rar", files)
        messagebox.showinfo(title="exporting", message="successfully done")
    else:
        messagebox.showerror(
            "Error", message="Choose one of these options!!")


def renameF(name,rooot):
    make_archive_file(radio_button.get(),name)
    rooot[0].quit
def export():

    try:
        make_archive_file(radio_button.get(), "problem")

    except:
        messagebox.showerror(
            "File exits", message="by defualt zip/rar file name is 'problem', for making new zip/rar file you must change its name or change its path!!")
        rename_root = Tk()
        rename_root.title('Rename')
        rf=[rename_root]
        new_name = Label(rename_root, text="New Name:", fg="red")
        rename = Entry(rename_root)
        rename.grid(row=0, column=1)
        new_name.grid(row=0, column=0)
        change_name = Button(rename_root, text="rename", fg="green",command=lambda:renameF(rename.get(),rf))
        change_name.grid(row=0, column=2)
        rename_root.mainloop()


def show_about():
    messagebox.showinfo(
        title="about", message="Programmer:Alireza Aramimehr\n----------\nLinkedin:www.linkedin.com/in/alireza-aramimehr\n----------\nDate:3/2/2023\nFriday, 3 February 2023")

# def go_to_the_next_entry(event):
#     output_box.focus_set()

root = Tk()
root.geometry('500x500')
root.title("Test Maker")
root.resizable(0, 0)


input_label = LabelFrame(root, text="Input", fg="blue", padx=10)
output_label = LabelFrame(root, text="Output", fg="red", padx=10)
address_label = LabelFrame(root, text="Address", fg='green', padx=10)
export_label = LabelFrame(root, text="export", fg="purple")

input_box = Text(input_label, width=40, height=10, relief="sunken", padx=5)
output_box = Text(output_label, width=40, height=10, relief="sunken", padx=5)

address_entery = Entry(address_label, width=46)
brows_button = Button(address_label, text="Brows", command=brows_file)

radio_button = IntVar()
rar = Radiobutton(export_label, text="Rar", variable=radio_button, value=1)
zip = Radiobutton(export_label, text="Zip", variable=radio_button, value=2)


export_button = Button(export_label, text="Export",
                       fg="#cc7a06", command=export)
creat_button = Button(root, text='Creat', fg='#07029c', command=make)
add_info_label = Label(root, text="1")

menubar = Menu(root)
fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label="about", command=show_about)
fileMenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=fileMenu)
root.config(menu=menubar)
# -----------------------------------------------------------

input_label.grid(row=0, column=0, padx=10)
input_box.grid(row=0, column=1, pady=15, rowspan=3)

output_label.grid(row=1, column=0)
output_box.grid(row=0, column=0, pady=15)

address_label.grid(row=2, column=0)
address_entery.grid(row=0, column=0, pady=5, padx=5)
brows_button.grid(row=0, column=1)

export_label.grid(row=0, column=1, columnspan=2)
rar.grid(row=0, column=0)
zip.grid(row=0, column=1)
export_button.grid(row=1, pady=5)

creat_button.grid(row=2, column=1)
add_info_label.grid(row=2, column=2)

#root.bind('<Return>',go_to_the_next_entry)
# -----------------------------------------------------------
root.mainloop()
