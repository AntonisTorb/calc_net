import tkinter as tk
from tkinter import ttk


class Calc:

    def __init__(self):
        ("")

        self.previous_evt = ""


    def reset(self):
        
        self.entry_gross.delete(0,tk.END)
        self.entry_gross.insert(0,"0")
        self.entry_bins.delete(0,tk.END)
        self.entry_bins.insert(0,"0")
        self.entry_kl.delete(0,tk.END)
        self.entry_kl.insert(0,"0")

        self.mat_val.configure(state="normal")
        self.mat_val.delete(0, tk.END)
        self.mat_val.insert(0, "0")
        self.mat_val.configure(state="readonly")

        self.fyr_val.configure(state="normal")
        self.fyr_val.delete(0, tk.END)
        self.fyr_val.insert(0, "0")
        self.fyr_val.configure(state="readonly")

        self.net_val.configure(state="normal")
        self.net_val.delete(0, tk.END)
        self.net_val.insert(0, "0")
        self.net_val.configure(state="readonly")

    
    def calculate(self, event=None):

        if event.keysym == 'Control_L' or event.keysym == 'Control_R':
            self.previous_evt = "ctrl"
            return
        else:
            self.previous_evt = ""

        if event.keysym == "c" and self.previous_evt == "ctrl":
            return

        self.gross_value = self.entry_gross.get()
        self.bins = self.entry_bins.get()
        self.kl = self.entry_kl.get()

        try:
            bins_mass = 30 * int(self.bins)
            kl_mass = 2 * int(self.kl)
            mat_mass = bins_mass + kl_mass

            self.mat_val.configure(state="normal")
            self.mat_val.delete(0, tk.END)
            self.mat_val.insert(0, str(mat_mass))
            self.mat_val.configure(state="readonly")

            mid_mass = float(self.gross_value) - mat_mass

            fyr = 0.05 * mid_mass
            self.fyr_val.configure(state="normal")
            self.fyr_val.delete(0, tk.END)
            self.fyr_val.insert(0, str(round(fyr, 2)))
            self.fyr_val.configure(state="readonly")

            net_mass = mid_mass - fyr
            self.net_val.configure(state="normal")
            self.net_val.delete(0, tk.END)
            self.net_val.insert(0, str(round(net_mass, 2)))
            self.net_val.configure(state="readonly")

        except ValueError:

            self.mat_val.configure(state="normal")
            self.mat_val.delete(0, tk.END)
            self.mat_val.insert(0,"ERROR")
            self.mat_val.configure(state="readonly")

            self.fyr_val.configure(state="normal")
            self.fyr_val.delete(0, tk.END)
            self.fyr_val.insert(0,"ERROR")
            self.fyr_val.configure(state="readonly")

            self.net_val.configure(state="normal")
            self.net_val.delete(0, tk.END)
            self.net_val.insert(0,"ERROR")
            self.net_val.configure(state="readonly")


    def context_menu(self, event):

        try:
            self.menu.tk_popup(event.x_root,event.y_root) # Pop the menu up in the given coordinates
        finally:
            self.menu.grab_release()


    def copy_cmd(self):

        net_val = self.net_val.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(net_val)


    def main_gui(self):

        self.root = tk.Tk()
        self.root.configure(background="lightblue")
        self.root.geometry("800x600")
        self.root.title("ΥΠΟΛΟΓΙΣΜΟΣ ΚΑΘΑΡΟΥ ΒΑΡΟΥΣ")
        self.root.bind("<Key>", self.calculate)

        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Copy", command=self.copy_cmd)

        self.frame = tk.Frame(self.root)
        self.frame.configure(background="lightblue")
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)

        self.label_gross = tk.Label(self.frame, text="ΜΙΚΤΟ ΒΑΡΟΣ:", font=("Arial", 20), anchor="w")
        self.label_gross.configure(background="lightblue")
        self.label_gross.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=20, pady=20)
        self.entry_gross = tk.Entry(self.frame, font=("Arial", 20))
        self.entry_gross.insert(1, "0")
        self.entry_gross.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=20, pady=20, columnspan=3)

        self.label_bins = tk.Label(self.frame, text="BINS (30KG):", font=("Arial", 20), anchor="w")
        self.label_bins.configure(background="lightblue")
        self.label_bins.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=20, pady=20)
        self.entry_bins = tk.Entry(self.frame, font=("Arial", 20))
        self.entry_bins.insert(1, "0")
        self.entry_bins.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=20, pady=20, columnspan=3)

        self.label_kl = tk.Label(self.frame, text="ΚΛΟΥΒΕΣ (2KG):", font=("Arial", 20), anchor="w")
        self.label_kl.configure(background="lightblue")
        self.label_kl.grid(row=2, column=0, sticky=(tk.W, tk.E), padx=20, pady=20)
        self.entry_kl = tk.Entry(self.frame, font=("Arial", 20))
        self.entry_kl.insert(1, "0")
        self.entry_kl.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=20, pady=20, columnspan=3)

        self.seperator_1 = ttk.Separator(self.frame, orient="horizontal")
        self.seperator_1.grid(row=3, column=0, sticky=(tk.W, tk.E), columnspan=3)

        self.label_mat = tk.Label(self.frame, text="BΑΡΟΣ ΥΛΙΚΟΥ (BINS):", font=("Arial", 20), wraplength=120)
        self.label_mat.configure(background="lightblue")
        self.label_mat.grid(row=4, column=0, sticky=(tk.W, tk.E), padx=20)
        self.label_fyr = tk.Label(self.frame, text="BΑΡΟΣ ΑΠΟΜΕΙΩΣΗΣ / ΦΥΡΑ (5%):", font=("Arial", 20), wraplength=200)
        self.label_fyr.configure(background="lightblue")
        self.label_fyr.grid(row=4, column=1, sticky=(tk.W, tk.E), padx=20)
        self.label_net = tk.Label(self.frame, text="ΚΑΘΑΡΟ ΒΑΡΟΣ:", font=("Arial", 20, "bold"), wraplength=200, background="limegreen")
        self.label_net.configure(background="lightblue")
        self.label_net.grid(row=4, column=2, sticky=(tk.W, tk.E), padx=20)

        self.mat_val = tk.Entry(self.frame, font=("Arial", 20), justify="right")
        self.mat_val.insert(0, "0")
        self.mat_val.configure(state="readonly")
        self.mat_val.grid(row=5, column=0, sticky=(tk.W, tk.E), padx=20)

        self.fyr_val = tk.Entry(self.frame, font=("Arial", 20), justify="right")
        self.fyr_val.insert(0, "0")
        self.fyr_val.configure(state="readonly")
        self.fyr_val.grid(row=5, column=1, sticky=(tk.W, tk.E), padx=20)

        self.net_val = tk.Entry(self.frame, font=("Arial", 20, "bold"), justify="right")
        self.net_val.insert(0, "0")
        self.net_val.configure(state="readonly")
        self.net_val.grid(row=5, column=2, sticky=(tk.W, tk.E), padx=20)
        self.net_val.bind("<Button-3>", self.context_menu)

        self.seperator_2 = ttk.Separator(self.frame, orient="horizontal")
        self.seperator_2.grid(row=6, column=0, sticky=(tk.W, tk.E), columnspan=3, pady=20)

        self.calc_btn = tk.Button(self.frame, text="RESET", font=("Arial", 20, "bold"), background="orange", command=self.reset, anchor="w")
        self.calc_btn.grid(row=7, column=1)

        self.frame.pack()

        self.looping = True
        self.root.mainloop()


def main_gui():
    calc = Calc()
    calc.main_gui()
