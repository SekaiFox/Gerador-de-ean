import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import random
from io import BytesIO


# --- lógica EAN-13 ---
def calcular_digito_verificador(codigo12):
    soma = 0
    for i, num in enumerate(codigo12):
        n = int(num)
        if i % 2 == 0:
            soma += n
        else:
            soma += n * 3
    resto = soma % 10
    return str((10 - resto) % 10)


def gerar_ean13():
    prefixo = "789"
    corpo = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    codigo12 = prefixo + corpo
    digito = calcular_digito_verificador(codigo12)
    return codigo12 + digito


# --- interface Tkinter ---
class GeradorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerador de EAN-13")
        self.geometry("480x380")
        self.resizable(False, False)

        frm = ttk.Frame(self, padding=12)
        frm.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frm, text="Gerador de Códigos EAN-13 (iniciando com 789)").pack(pady=(0,10))

        row = ttk.Frame(frm)
        row.pack(fill=tk.X, pady=6)
        ttk.Label(row, text="Quantidade:").pack(side=tk.LEFT)
        self.spin = tk.Spinbox(row, from_=1, to=10000, width=8)
        self.spin.pack(side=tk.LEFT, padx=8)

        btn_frame = ttk.Frame(frm)
        btn_frame.pack(fill=tk.X, pady=8)
        self.gerar_btn = ttk.Button(btn_frame, text="Gerar EANs", command=self.gerar)
        self.gerar_btn.pack(side=tk.LEFT, padx=4)
        self.salvar_btn = ttk.Button(btn_frame, text="Salvar em Excel", command=self.salvar, state=tk.DISABLED)
        self.salvar_btn.pack(side=tk.LEFT, padx=4)

        ttk.Separator(frm, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=8)

        self.text = tk.Text(frm, height=12, wrap=tk.NONE)
        self.text.pack(fill=tk.BOTH, expand=True)

        self.status = ttk.Label(self, text="Pronto", relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(fill=tk.X, side=tk.BOTTOM)

        self.eans = []

    def gerar(self):
        try:
            qtd = int(self.spin.get())
        except Exception:
            messagebox.showerror("Erro", "Quantidade inválida")
            return
        if qtd < 1:
            messagebox.showerror("Erro", "Quantidade deve ser >= 1")
            return
        self.eans = [gerar_ean13() for _ in range(qtd)]
        self.text.delete("1.0", tk.END)
        for i, e in enumerate(self.eans, 1):
            self.text.insert(tk.END, f"{i:04d}: {e}\n")
        self.salvar_btn.config(state=tk.NORMAL)
        self.status.config(text=f"{qtd} códigos gerados")

    def salvar(self):
        if not self.eans:
            messagebox.showwarning("Nada para salvar", "Gere códigos antes de salvar.")
            return
        default_name = "codigos_ean13.xlsx"
        path = filedialog.asksaveasfilename(defaultextension=".xlsx", initialfile=default_name,
                                            filetypes=[("Excel files","*.xlsx"), ("All files","*.*")])
        if not path:
            return
        df = pd.DataFrame({"EAN-13": self.eans})
        try:
            df.to_excel(path, index=False)
            messagebox.showinfo("Salvo", f"Arquivo salvo em:\n{path}")
            self.status.config(text=f"Arquivo salvo: {path}")
        except Exception as e:
            messagebox.showerror("Erro ao salvar", str(e))


if __name__ == '__main__':
    app = GeradorApp()
    app.mainloop()
