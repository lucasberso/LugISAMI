import tkinter as tk
from tkinter import filedialog
from lugReader import lugHTML

window_main = tk.Tk(className='Lug ISAMI')
window_main.geometry('800x400')
window_main.option_add('*Font', '18')

# file_name_var = tk.StringVar()

#Función que llama al archivo que se desea leer
def askfilename():
    global file_name
    window_main.file_name = filedialog.askopenfilename()
    e1.configure(state=tk.NORMAL)
    e1.insert(0, window_main.file_name)
    e1.configure(state=tk.DISABLED)

#Función que llama al directorio donde se desea guardar la carpeta
def askdirectory():
    global dir_path
    window_main.dir_path = filedialog.askdirectory()
    e3.configure(state=tk.NORMAL)
    e3.insert(0, window_main.dir_path)
    e3.configure(state=tk.DISABLED)

def generate():
    output_name = e2.get()
    file_name=e1.get()
    dir_path=e3.get()
    if gender.get() == 1:
        print('HOLAAAAA')
    elif gender.get()==2:
        HTML=lugHTML(input_file=file_name)
        HTML.write_output(output_path=dir_path, output_filename=output_name)



gender = tk.IntVar()
radiobutton_1 = tk.Radiobutton(window_main, text='Create ISAMI input', variable=gender, value=1)# .grid(row = 1, column = 1)
radiobutton_1.place(x = 10, y = 10)
#radiobutton_1.pack(align = "w")



radiobutton_2 = tk.Radiobutton(window_main, text='Read HTML output file', variable=gender, value=2)
radiobutton_2.place(x = 10, y = 50)
#radiobutton_2.pack(align = "w")

Label1 = tk.Label(window_main, text = "Input Filename")
Label1.place(x = 10, y = 130)
e1 = tk.Entry(window_main, width = 35, borderwidth = 5, state='disabled')
e1.place(x = 180, y = 130)



Label2 = tk.Label(window_main, text = "Output Filename")
Label2.place(x = 10, y = 180)
e2 = tk.Entry(window_main, width = 35, borderwidth = 5)
e2.place(x = 180, y = 180)


Label3 = tk.Label(window_main, text = "Output directory")
Label3.place(x = 10, y = 230)
e3 = tk.Entry(window_main, width = 35, borderwidth = 5, state='disabled')
e3.place(x = 180, y = 230)

e4= tk.Entry(window_main, width = 70, borderwidth = 1, state='disabled')
e4.place(x = 10, y = 280, height=70)

bot1 = tk.Button(window_main, text = '...', command = askfilename, height = 1, width = 2)
bot1.place(x = 580, y = 125)


bot3 = tk.Button(window_main, text = '...', command = askdirectory, height = 1, width = 2)
bot3.place(x = 580, y = 225)


bot4 = tk.Button(window_main, text = 'Generate', command=generate) #FALTA METER EL COMMAND  LLAMANDO A LO QUE QUERAMOS HACER
bot4.place(x = 680, y = 295)




window_main.mainloop()

print("Hola")