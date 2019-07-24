import tkinter as tk
import os
from tkinter import filedialog

__version__ = '1.0.0'


class Gui(tk.Frame):
    """Main program graphical user interface"""
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.build_interface()

    def build_interface(self):
        # craete frame
        frame = tk.Frame()
        frame.pack(expand=False, fill='x', anchor='n')

        # entry's variables
        str_folder = tk.StringVar()
        str_quote = tk.StringVar()
        str_delimiter = tk.StringVar()

        # create folder labelframe
        label_path = tk.LabelFrame(frame, text='Folder:', fg='brown')
        label_path.pack(side='top', expand='yes', fill='x', padx=2, pady=2, anchor='n')
        # entry path flder
        self.entry_folder = tk.Entry(label_path, textvariable=str_folder)
        self.entry_folder.pack(expand=True, fill='x', side='left', padx=2, pady=2)
        # btn to input files in folder on the list
        btn_folder = tk.Button(label_path, text='...', command=self.get_folder)
        btn_folder.pack(expand=False, fill='x', side='right', padx=2, pady=2)

        # LABELFRAME CONFIGS TO IMPORT
        label_config = tk.LabelFrame(frame, text='Config:', fg='brown')
        label_config.pack(side='top', expand='yes', fill='x', padx=2, pady=2, anchor='n')
        # labels
        label_quote = tk.Label(label_config, text='Quote string:')
        label_quote.pack(expand=False, fill='x', side='left', padx=2, pady=2)
        # entry quote string file
        self.entry_quote = tk.Entry(label_config, textvariable=str_quote)
        self.entry_quote .insert(tk.END, '"')
        self.entry_quote.pack(expand=False, fill='x', side='left', padx=2, pady=2)
        # labels
        label_delimiter = tk.Label(label_config, text='Delimiter:')
        label_delimiter.pack(expand=False, fill='x', side='left', padx=2, pady=2)
        # entry delimiter file
        self.entry_delimiter = tk.Entry(label_config, textvariable=str_delimiter)
        self.entry_delimiter.insert(tk.END, ';')
        self.entry_delimiter.pack(expand=False, fill='x', side='left', padx=2, pady=2)

        # create labelFrame to list files in folder selected
        label_folders = tk.LabelFrame(frame, text='Files to import:', fg='brown')
        label_folders.pack(side='top', expand='yes', fill='x', padx=2, pady=2, anchor='n')
        # craete listBox
        self.list_files = tk.Listbox(label_folders)
        self.list_files.bind('<<ListboxSelect>>', self.show_content)
        self.list_files.pack(expand=True, fill='x', side='left', padx=2, pady=2)

        # create labelFram to preview contet the file
        label_content = tk.LabelFrame(frame, text='File content:', fg='brown')
        label_content.pack(side='top', expand='yes', fill='x', padx=2, pady=2, anchor='n')
        # craete textBox to insert content the file and show
        self.content_text = tk.Text(label_content)
        self.content_text.pack(expand=True, fill='x', side='left', padx=2, pady=2)

    def get_folder(self):
        folder_path = filedialog.askdirectory()
        try:
            self.entry_folder.delete(0, tk.END)
            self.entry_folder.insert(tk.END, folder_path)
            self.list_folder(folder_path)
        except Exception as e:
            print(e)

    def list_folder(self, path_folder):
        file_list = os.listdir(path_folder)
        self.list_files.delete(0, tk.END)
        for item in file_list:
            file_extension = os.path.splitext(item)[1]
            if file_extension in ('.csv', '.txt'):  # load only files defined
                self.list_files.insert(tk.END, item)

    def show_content(self, event):
        x = self.list_files.curselection()[0]
        file = self.list_files.get(x)  # get name selected on list
        path_file = os.path.join(self.entry_folder.get(), file)  # concat path and file name
        with open(path_file, 'r', encoding="ISO-8859-1") as file:
            try:
                file = file.read()
                self.content_text.delete('1.0', tk.END)
                self.content_text.insert(tk.END, file)
            except Exception as e:
                print(e)

    @staticmethod
    def quit_program():
        """Quits main program window"""
        root.destroy()


if __name__ == '__main__':
    # create the application
    root = tk.Tk()
    importcsv = Gui(root)
    importcsv.pack(expand=False)

    # here are method calls windows manager class
    root.title("Import CSV v.{}".format(__version__))
    root.geometry('700x500')
    root.resizable(0, 0)  # don't allow resizing the window

    # start the program
    root.mainloop()
