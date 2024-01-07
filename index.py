import tkinter as tk
from tkinter import ttk, messagebox

class CalculadoraPromedioGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Promedio")
        self.root.title("Calculadora de Promedio")

        self.notas = []
        self.porcentajes = []
      
        self.label_notas = ttk.Label(root, text="Notas (ejemplo: 5.5 ingresar 55):")
        self.label_porcentajes = ttk.Label(root, text="Porcentajes:")

        self.entry_notas = ttk.Entry(root)
        self.entry_porcentajes = ttk.Entry(root)

        self.btn_agregar = ttk.Button(root, text="Agregar", command=self.agregar_nota_porcentaje)
        self.btn_calcular = ttk.Button(root, text="Calcular Promedio", command=self.calcular_promedio)
        self.btn_limpiar = ttk.Button(root, text="Limpiar", command=self.limpiar_datos)


        self.table_frame = ttk.Frame(root)
        self.table = ttk.Treeview(self.table_frame, columns=("Nota", "Porcentaje"), show="headings")
        self.table.heading("Nota", text="Nota")
        self.table.heading("Porcentaje", text="Porcentaje")

        self.label_notas.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.label_porcentajes.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_notas.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        self.entry_porcentajes.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        self.btn_agregar.grid(row=2, column=1, pady=10)
        self.btn_calcular.grid(row=3, column=1, pady=10)
        self.btn_limpiar.grid(row=5, column=1, pady=10)

        self.table_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.table.pack(side="left", fill="both")

    def agregar_nota_porcentaje(self):
        nota_str = self.entry_notas.get()
        porcentaje_str = self.entry_porcentajes.get()

   
        try:
            nota = float(nota_str.replace(",", ".")) / 10  
            porcentaje = float(porcentaje_str)
        except ValueError:
            messagebox.showwarning("Error", "Ingrese valores numéricos válidos.")
            return

        if not (1.0 <= nota <= 7.0):
            messagebox.showwarning("Error", "La nota debe estar en el rango de 1.0 a 7.0.")
            return

        if sum(self.porcentajes) + porcentaje > 100:
            messagebox.showwarning("Error", "La suma de porcentajes no puede exceder el 100%.")
            return

        self.notas.append(nota)
        self.porcentajes.append(porcentaje)

        self.entry_notas.delete(0, tk.END)
        self.entry_porcentajes.delete(0, tk.END)


        self.actualizar_tabla()

    def calcular_promedio(self):
        if not self.notas or not self.porcentajes:
            return

        if len(self.notas) != len(self.porcentajes):
            return


        if sum(self.porcentajes) != 100:
            messagebox.showwarning("Error", "La suma de porcentajes debe ser igual a 100%.")
            return

        promedio_ponderado = sum(nota * (porcentaje / 100) for nota, porcentaje in zip(self.notas, self.porcentajes))

        if promedio_ponderado < 5:

            notas_necesarias = max(0, (4.0 - promedio_ponderado * 0.75) / 0.25)

            mensaje = f"Tu promedio ponderado es: {promedio_ponderado:.1f}.\n"
            mensaje += f"No te has eximido. Necesitas sacar al menos {notas_necesarias:.1f} en el examen para aprobar."
        else:
            mensaje = f"Felicidades, te has eximido. Tu promedio ponderado es: {promedio_ponderado:.1f}."

        messagebox.showinfo("Resultado", mensaje)

    def limpiar_datos(self):
        self.notas = []
        self.porcentajes = []
        self.entry_notas.delete(0, tk.END)
        self.entry_porcentajes.delete(0, tk.END)
        self.actualizar_tabla()

    def actualizar_tabla(self):

        for row in self.table.get_children():
            self.table.delete(row)

        for nota, porcentaje in zip(self.notas, self.porcentajes):
            self.table.insert("", "end", values=(nota, porcentaje))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraPromedioGUI(root)
    root.mainloop()
