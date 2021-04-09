import tkinter as tk
from tkinter import filedialog
import functools
from lugReader import lugHTML
from lugWriter import lugInput


class run_GUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Hola")
        self.master.resizable(False, False)
        self.master.update()

        # Botones selección caso
        self.case= tk.IntVar()
        self.case_create = tk.Radiobutton(self.master, text='Create ISAMI input', variable=self.case, value=1)
        self.case_create.grid(row = 0, column = 0, padx = 10, pady = (10,0), sticky=tk.W)
        self.case_read = tk.Radiobutton(self.master, text='Read HTML or CZM', variable=self.case, value=2)
        self.case_read.grid(row=1, column=0, padx = 10, pady = 0, sticky=tk.W)

        # Bloques de entrada
        self.label_dic, self.button_dic, self.entry_dic  = {}, {}, {}
        self.count = 0
        self.create_block('input_file','file', 'Input file:', 2, 0)
        self.create_block('output_folder','folder', 'Output folder:', 3, 0)
        self.create_block('output_name','entry', 'Output filename:', 4, 0)

        # Botón de generar
        self.generate_button = tk.Button(self.master, text='Generate', command=self.generate)
        self.generate_button.grid(row=5, column=0, columnspan = 2, sticky = tk.W+tk.E, padx = (10,0), pady = (10,10))

        # Texto de salida y barra
        self.scrollbar = tk.Scrollbar(orient="vertical")
        self.output_print = tk.Text(self.master, yscrollcommand=self.scrollbar.set,  height=3, width = 10)
        self.output_print.grid(row=6, column=0, columnspan=2, sticky=tk.W + tk.E, padx = 10, pady = (10,20))
        self.scrollbar.config(command=self.output_print.yview)
        self.scrollbar.grid(row=6, column=2, sticky=tk.N + tk.S + tk.W, padx = 10)


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
        label.grid(row=row, column=column, sticky=tk.W, padx = 10)
        self.label_dic.update({id:label})
        if type == 'file':
            button = tk.Button(self.master, text="...", command=functools.partial(self.askfilename, entry=id))
            button.grid(row=row, column=column + 2, sticky=tk.W, padx = 10)
            self.button_dic.update({id:button})
        elif type == 'folder':
            button = tk.Button(self.master, text="...", command=functools.partial(self.askdirectory, entry=id))
            button.grid(row=row, column=column + 2, sticky=tk.W, padx = 10)
            self.button_dic.update({id:button})
        if type == 'entry':
            entry = tk.Entry(self.master)
        else:
            entry = tk.Entry(self.master, state="disabled")
        entry.grid(row=row, column=column+1, sticky=tk.W)
        self.entry_dic.update({id:entry})
        self.count = self.count +1

    def generate(self):

        self.warning_print = ""
        self.output_print.configure(state='normal')
        self.output_print.delete(1.0, tk.END)

        for i in self.entry_dic.keys():
            warning = self.check_empty(self.entry_dic[i].get(), i)
            if warning:
                self.warning_print = self.warning_print + warning + "\n"

        self.write_in_txt(self.warning_print, self.output_print)

        file_name = self.entry_dic['input_file'].get()
        dir_path = self.entry_dic['output_folder'].get()
        output_name = self.entry_dic['output_name'].get()

        if self.warning_print == "":

            if self.case.get() == 1:
                try:
                    ISAMI = lugInput(input_file=file_name)
                    ISAMI.write_output(output_path=dir_path, output_filename=output_name)
                    ISAMI.write_bach(output_path=dir_path, output_filename=output_name)
                    self.write_in_txt("The ISAMI file has been generated.", self.output_print)
                except:
                    self.write_in_txt("Error: ISAMI input file not compatible.", self.output_print)

            elif self.case.get() == 2:
                try:
                    HTML = lugHTML(input_file=file_name)
                    HTML.write_output(output_path=dir_path, output_filename=output_name)
                    self.write_in_txt("The HTML file has been read: Kt has been extracted.",self.output_print)
                except:
                    self.write_in_txt("Error: HTML or CZM file not compatible.", self.output_print)

            else:
                self.output_print.delete(1.0, tk.END)
                self.output_print.insert(tk.END, "Error: Select one of the program options.")

        self.warning_print = ""

    def write_in_txt(self, txt, object):
        object.configure(state='normal')
        object.delete(1.0, tk.END)
        object.insert(tk.END, txt)
        object.configure(state='disabled')

    def check_empty(self, input, field):
        warning = ""
        if not input:
            self.write_in_txt("Error: The %s field is empty.", self.output_print)
        return warning

if __name__ == '__main__':

    root = tk.Tk()
    app = run_GUI(root)
    root.mainloop()