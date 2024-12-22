#------------------------------------------------------------------------------------------------#
# Title: Powers Calci Demo (Presentation Classes Script)
# Description: Multi-line Textbox that displays results of arithmetic operations on two operands
# ChangeLog (Who, When, What)
# Rucha Nimbalkar, 12/21/2024, Created Script
# Rucha Nimbalkar, 12/21/2024, Created MainWindow class
# Rucha Nimbalkar, 12/21/2024, Added code in the MainWindow class
# Rucha Nimbalkar, 12/21/2024, Created MathIO class
# Rucha Nimbalkar, 12/21/2024, Added methods in the MathIO class
#------------------------------------------------------------------------------------------------#
import tkinter as tk
from tkinter import ttk
import processing_classes as proc

class MainWindow(object):
    """
        Description: Creates the following UI objects:
        window__root(tk.Tk)
        lbl_math_info(ttk.label)
        txt_first_number (ttk.entry)
        txt_second_number (ttk.entry)
        mtx_results(ttk.textbox)
        btn_add(ttk.button)
        btn_subtract(ttk.button)
        btn_multiply(ttk.button)
        btn_divide(ttk.button)
    """

    @staticmethod
    def create_main_window():
        """Create and configure a root node object"""
        application_window = tk.Tk()
        application_window.geometry("500x250")
        application_window.title("Powers")

        lbl_math_results = ttk.Label(application_window, text = "Exponential Results")
        lbl_math_results.grid(row=1, column=1, sticky = tk.NW, padx= 10, pady=5)

        lbl_base_number = ttk.Label(
            application_window,
            text="Base",
            width= 20,
            anchor= tk.E
        )
        lbl_base_number.grid(row=2,column=1, sticky = tk.E)
        txt_base_number = ttk.Entry(application_window, width=40)
        txt_base_number.grid(row=2, column=2, columnspan=3)
        txt_base_number.insert(0,"0.00")

           #Adding a multiline textbox
        power_results = tk.Text(width=50, height=5)
        power_results.grid(row=4,
                         column=1,
                         sticky=tk.N,
                         columnspan=4,
                         padx=10,
                         pady=10
                         )

        #Adding buttons
        #square button
        btn_square = ttk.Button(application_window, text ="SQUARE",width=8)
        btn_square.grid(row=5, column=1,sticky=tk.E, padx=15, pady=5)
        btn_square['command'] = lambda : MathIO.write_square_to_textbox(
            float(txt_base_number.get()),
            power_results
        )

        #cube button
        btn_subtract = ttk.Button(application_window, text="CUBE", width=8)
        btn_subtract.grid(row=5, column=2, sticky=tk.E, padx=15, pady=5)
        btn_subtract['command'] = lambda: MathIO.write_cube_to_textbox(
            float(txt_base_number.get()),
            power_results
        )

        #clear button
        btn_clear = ttk.Button(application_window, text="CLEAR", width=6)
        btn_clear.grid(row=5, column=5, sticky=tk.E, padx=15, pady=5)
        btn_clear['command'] = lambda: MathIO.clear_textbox(power_results)
        return application_window
#End class

class MathIO(object):

    @staticmethod
    def clear_textbox(textbox):
        textbox['state'] = 'normal'
        textbox.delete(1.0,tk.END)
        textbox['state'] = 'disabled'

    @staticmethod
    def write_square_to_textbox(n1,textbox):
        textbox['state']= 'normal'
        text = str.format('The square of {n1}  is {result}\n', n1=n1, result = proc.MathProcessor.square(n1))
        textbox.insert(tk.END,text)
        textbox['state'] = 'disabled'

    @staticmethod
    def write_cube_to_textbox(n1,textbox):
        textbox['state']= 'normal'
        text = str.format('The cube of {n1} is {result}\n', n1=n1, result = proc.MathProcessor.cube(n1))
        textbox.insert(tk.END,text)
        textbox['state'] = 'disabled'

#End class