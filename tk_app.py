import tkinter as tk
from tkinter import ttk, messagebox
from calculos import calcular_risco_total

def calcular():
    try:
        dados = {
            "tipo_estrutura": tipo_estrutura.get(),
            "area": float(area_entry.get()),
            "altura": float(altura_entry.get()),
            "numero_pessoas": int(pessoas_entry.get()),
            "isoceraunico": float(isoceraunico_entry.get()),
            "tipo_solo": tipo_solo.get()
        }

        resultado = calcular_risco_total(dados)

        resultado_text.set(
            f"Risco Total: {resultado['R_total']:.2e}\n"
            f"Risco Tolerável: {resultado['R_toleravel']:.1e}\n"
            f"Nível de Proteção: {resultado['nivel_protecao']}\n"
            f"SPDA: {'OBRIGATÓRIO' if resultado['necessita_spda'] else 'NÃO OBRIGATÓRIO'}"
        )
    except Exception as e:
        messagebox.showerror("Erro", f"Verifique os dados de entrada.\n{e}")

app = tk.Tk()
app.title("Análise de Risco SPDA (NBR 5419)")
app.geometry("450x500")
app.resizable(False, False)

frame = ttk.Frame(app, padding="10")
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Tipo da Estrutura:").pack()
tipo_estrutura = ttk.Combobox(frame, values=["Residencial", "Hospital", "Escola", "Indústria", "Comercial", "Outro"])
tipo_estrutura.set("Residencial")
tipo_estrutura.pack()

ttk.Label(frame, text="Área da Edificação (m²):").pack()
area_entry = ttk.Entry(frame)
area_entry.insert(0, "100")
area_entry.pack()

ttk.Label(frame, text="Altura da Estrutura (m):").pack()
altura_entry = ttk.Entry(frame)
altura_entry.insert(0, "10")
altura_entry.pack()

ttk.Label(frame, text="Número Médio de Pessoas:").pack()
pessoas_entry = ttk.Entry(frame)
pessoas_entry.insert(0, "5")
pessoas_entry.pack()

ttk.Label(frame, text="Número de Tempestades por Ano (N_g):").pack()
isoceraunico_entry = ttk.Entry(frame)
isoceraunico_entry.insert(0, "30")
isoceraunico_entry.pack()

ttk.Label(frame, text="Tipo de Solo:").pack()
tipo_solo = ttk.Combobox(frame, values=["Alta Resistividade", "Baixa Resistividade"])
tipo_solo.set("Baixa Resistividade")
tipo_solo.pack()

ttk.Button(frame, text="Calcular Risco", command=calcular).pack(pady=10)

resultado_text = tk.StringVar()
resultado_label = ttk.Label(frame, textvariable=resultado_text, justify="left", foreground="blue")
resultado_label.pack(pady=10)

app.mainloop()