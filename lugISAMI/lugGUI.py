import tkinter as tk
from tkinter import filedialog
import functools
from lugReader import lugHTML
from lugWriter import lugInput
import os

class run_GUI:

    def __init__(self, master):
        self.master = master
        self.master.title("ISAMI LUG")
        self.master.resizable(False, False)
        self.master.update()

        # Botones selección caso
        self.case= tk.IntVar()
        self.case_create = tk.Radiobutton(self.master, text='Create ISAMI input', variable=self.case, value=1)
        self.case_create.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.case_read = tk.Radiobutton(self.master, text='Read HTML or CZM', variable=self.case, value=2)
        self.case_read.grid(row=1, column=2, padx = 10, pady = 10 )

        #Boton de ayuda
        self.help = tk.Button(self.master, text="How It Works", command=self.open_help)
        self.help.grid(row=1, column=3, padx=10, pady = 10)

        # Bloques de entrada
        self.label_dic, self.button_dic, self.entry_dic  = {}, {}, {}
        self.count = 0
        self.create_block('input_file','file', 'INPUT FILE:', 2, 1)
        self.create_block('output_folder','folder', 'OUTPUT FOLDER:', 3, 1)
        self.create_block('output_name','entry', 'OUTPUT FILENAME:', 4, 1)

        self.generate_button = tk.Button(self.master, text='Generate', command=self.generate)
        self.generate_button.grid(row=5, column=1, columnspan = 3, sticky = tk.W+tk.E, padx = 10, pady = 10)

        self.scrollbar = tk.Scrollbar(orient="vertical")
        self.output_print = tk.Text(self.master, yscrollcommand=self.scrollbar.set,  height=3)
        self.output_print.grid(row=6, column=1, columnspan=3, rowspan = 1, sticky=tk.W + tk.E, pady = 10, padx = 10)
        self.scrollbar.config(command=self.output_print.yview)
        self.scrollbar.grid(row=6, column=6,  rowspan=2, sticky=tk.N + tk.S + tk.W)

    def askfilename(self, entry):

        file_name = filedialog.askopenfilename()
        self.entry_dic[entry].configure(state=tk.NORMAL)
        self.entry_dic[entry].delete(0, "end")
        self.entry_dic[entry].insert(0, file_name)
        self.entry_dic[entry].configure(state=tk.DISABLED)

    def askdirectory(self, entry):

        dir_path = filedialog.askdirectory()
        self.entry_dic[entry].configure(state=tk.NORMAL)
        self.entry_dic[entry].delete(0, "end")
        self.entry_dic[entry].insert(0, dir_path)
        self.entry_dic[entry].configure(state=tk.DISABLED)

    def create_block(self, id, type, label_text, row, column):

        label = tk.Label(self.master, text= label_text)
        label.grid(row=row, column=column)
        self.label_dic.update({id:label})
        if type == 'file':
            button = tk.Button(self.master, text="...", command=functools.partial(self.askfilename, entry=id))
            button.grid(row=row, column=column + 2, padx = (0, 10))
            self.button_dic.update({id:button})
        elif type == 'folder':
            button = tk.Button(self.master, text="...", command=functools.partial(self.askdirectory, entry=id))
            button.grid(row=row, column=column + 2, padx = (0, 10))
            self.button_dic.update({id:button})
        if type == 'entry':
            entry = tk.Entry(self.master)
        else:
            entry = tk.Entry(self.master, state="disabled")
        entry.grid(row=row, column=column+1)
        self.entry_dic.update({id:entry})
        self.count = self.count +1

    def generate(self):
        file_name = self.entry_dic['input_file'].get()
        dir_path = self.entry_dic['output_folder'].get()
        output_name = self.entry_dic['output_name'].get()
        self.warning_print = ""
        self.output_print.delete(1.0, tk.END)
        for i in self.entry_dic.keys():
            warning = self.check_empty(self.entry_dic[i].get(), i)
            if warning:
                self.warning_print = self.warning_print + warning + "\n"

        self.output_print.insert(tk.END, self.warning_print)

        if self.warning_print == "":
            if self.case.get() == 1:
                ISAMI = lugInput(input_file=file_name)
                ISAMI.write_output(output_path=dir_path, output_filename=output_name)
                self.output_print.delete(1.0, tk.END)
                self.output_print.insert(tk.END, "The ISAMI file has been generated.")

            elif self.case.get() == 2:
                HTML = lugHTML(input_file=file_name)
                HTML.write_output(output_path=dir_path, output_filename=output_name)
                self.output_print.delete(1.0, tk.END)
                self.output_print.insert(tk.END, "The HTML file has been read: Kt has been extracted.")
                # kt_info = os.path.join(dir_path, output_name)
                # os.system(kt_info + ".txt")
            else:
                self.output_print.delete(1.0, tk.END)
                self.output_print.insert(tk.END, "Select one of the given options.")

        self.warning_print = ""

    def open_help(self):
        os.system("HELP.docx")

    def check_empty(self, input, field):
        warning = None
        if not input:
            warning = 'The %s field is empty.' % (field)
        return warning

if __name__ == '__main__':

    root = tk.Tk()
    app = run_GUI(root)
    root.mainloop()