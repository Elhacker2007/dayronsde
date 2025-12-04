import customtkinter as ctk
import subprocess
import sys
import os
import promedio_notas
import salario_simple
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FusionApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("FUSIÓN: Asistencia y Programas")
        self.geometry("980x560")
        self.configure(fg_color=("#f1f5f9", "#0D1117"))
        self.cards = []
        self.current_category = "Todos"
        header = ctk.CTkFrame(self, corner_radius=0, fg_color=("white", "#111827"))
        header.pack(side="top", fill="x")
        ctk.CTkLabel(header, text="Centro de Lanzamiento", font=("Segoe UI", 22, "bold")).pack(padx=20, pady=16)
        body = ctk.CTkFrame(self)
        body.pack(fill="both", expand=True, padx=20, pady=20)
        sidebar = ctk.CTkFrame(body, width=200, corner_radius=12)
        sidebar.pack(side="left", fill="y", padx=(0,20))
        ctk.CTkLabel(sidebar, text="Categorías", font=("Segoe UI", 16, "bold")).pack(pady=(16,8))
        ctk.CTkButton(sidebar, text="Todos", command=lambda: self.apply_filter("Todos")).pack(fill="x", padx=10, pady=4)
        ctk.CTkButton(sidebar, text="Académico", command=lambda: self.apply_filter("Académico")).pack(fill="x", padx=10, pady=4)
        ctk.CTkButton(sidebar, text="Sistemas", command=lambda: self.apply_filter("Sistemas")).pack(fill="x", padx=10, pady=4)
        ctk.CTkButton(sidebar, text="Ventas", command=lambda: self.apply_filter("Ventas")).pack(fill="x", padx=10, pady=4)
        ctk.CTkButton(sidebar, text="CLI", command=lambda: self.apply_filter("CLI")).pack(fill="x", padx=10, pady=4)
        ctk.CTkLabel(sidebar, text="Buscar", font=("Segoe UI", 12)).pack(pady=(16,4))
        self.search_var = ctk.StringVar()
        search = ctk.CTkEntry(sidebar, textvariable=self.search_var, placeholder_text="Nombre...")
        search.pack(fill="x", padx=10)
        search.bind("<KeyRelease>", lambda e: self.apply_filter(None))
        content = ctk.CTkFrame(body)
        content.pack(side="right", fill="both", expand=True)
        grid = ctk.CTkScrollableFrame(content, fg_color="transparent")
        grid.pack(fill="both", expand=True)
        card1 = ctk.CTkFrame(grid, corner_radius=12)
        card1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(card1, text="Asistencia", font=("Segoe UI", 18, "bold")).pack(pady=(20,6))
        ctk.CTkLabel(card1, text="Control y reporte de asistencias").pack()
        ctk.CTkButton(card1, text="Abrir Asistencia", height=40, command=self.run_asistencia).pack(fill="x", padx=20, pady=20)
        self.tag_card(card1, "Académico", "Asistencia")
        card2 = ctk.CTkFrame(grid, corner_radius=12)
        card2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(card2, text="Programas", font=("Segoe UI", 18, "bold")).pack(pady=(20,6))
        ctk.CTkLabel(card2, text="Gestión de programas y códigos").pack()
        ctk.CTkButton(card2, text="Abrir Programas", height=40, command=self.run_programas).pack(fill="x", padx=20, pady=20)
        self.tag_card(card2, "Académico", "Programas")
        card3 = ctk.CTkFrame(grid, corner_radius=12)
        card3.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(card3, text="Siga Integral", font=("Segoe UI", 18, "bold")).pack(pady=(20,6))
        ctk.CTkLabel(card3, text="Gestión integral académica").pack()
        ctk.CTkButton(card3, text="Abrir Siga", height=40, command=self.run_juan).pack(fill="x", padx=20, pady=20)
        self.tag_card(card3, "Académico", "Siga Integral")

        card4 = ctk.CTkFrame(grid, corner_radius=12)
        card4.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(card4, text="Venta / Salario", font=("Segoe UI", 18, "bold")).pack(pady=(20,6))
        ctk.CTkLabel(card4, text="Emisión de comprobantes").pack()
        ctk.CTkButton(card4, text="Abrir Venta", height=40, command=self.run_salario).pack(fill="x", padx=20, pady=20)
        self.tag_card(card4, "Ventas", "Venta / Salario")

        card5 = ctk.CTkFrame(grid, corner_radius=12)
        card5.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(card5, text="Super App V9", font=("Segoe UI", 18, "bold")).pack(pady=(20,6))
        ctk.CTkLabel(card5, text="Promedios, sumas y más").pack()
        ctk.CTkButton(card5, text="Abrir Super App", height=40, command=self.run_super_app).pack(fill="x", padx=20, pady=20)
        self.tag_card(card5, "Sistemas", "Super App V9")

        card7 = ctk.CTkFrame(grid, corner_radius=12)
        card7.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(card7, text="Instituto", font=("Segoe UI", 18, "bold")).pack(pady=(20,6))
        ctk.CTkLabel(card7, text="Sistema institucional").pack()
        ctk.CTkButton(card7, text="Abrir Instituto", height=40, command=self.run_instituto).pack(fill="x", padx=20, pady=20)
        self.tag_card(card7, "Sistemas", "Instituto")

        card8 = ctk.CTkFrame(grid, corner_radius=12)
        card8.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(card8, text="Promedio CLI", font=("Segoe UI", 18, "bold")).pack(pady=(20,6))
        ctk.CTkLabel(card8, text="Calculadora en consola").pack()
        ctk.CTkButton(card8, text="Abrir Promedio", height=40, command=self.run_promedio_cli).pack(fill="x", padx=20, pady=20)
        self.tag_card(card8, "CLI", "Promedio CLI")

        card9 = ctk.CTkFrame(grid, corner_radius=12)
        card9.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(card9, text="Salario CLI", font=("Segoe UI", 18, "bold")).pack(pady=(20,6))
        ctk.CTkLabel(card9, text="Calculadora en consola").pack()
        ctk.CTkButton(card9, text="Abrir Salario", height=40, command=self.run_salario_cli).pack(fill="x", padx=20, pady=20)
        self.tag_card(card9, "CLI", "Salario CLI")

        extra_row = 3
        card10 = ctk.CTkFrame(grid, corner_radius=12)
        card10.grid(row=extra_row, column=0, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(card10, text="Siga Final Pro", font=("Segoe UI", 18, "bold")).pack(pady=(20,6))
        ctk.CTkLabel(card10, text="Versión avanzada").pack()
        ctk.CTkButton(card10, text="Abrir Siga Final", height=40, command=self.run_siga_final_pro).pack(fill="x", padx=20, pady=20)
        self.tag_card(card10, "Sistemas", "Siga Final Pro")

        card11 = ctk.CTkFrame(grid, corner_radius=12)
        card11.grid(row=extra_row, column=1, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(card11, text="Sistema Permiti", font=("Segoe UI", 18, "bold")).pack(pady=(20,6))
        ctk.CTkLabel(card11, text="Permisos y gestión").pack()
        ctk.CTkButton(card11, text="Abrir Permiti", height=40, command=self.run_permitidi).pack(fill="x", padx=20, pady=20)
        self.tag_card(card11, "Sistemas", "Permiti")

        card12 = ctk.CTkFrame(grid, corner_radius=12)
        card12.grid(row=extra_row, column=2, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(card12, text="Certificación Modular", font=("Segoe UI", 18, "bold")).pack(pady=(20,6))
        ctk.CTkLabel(card12, text="Programas y módulos").pack()
        ctk.CTkButton(card12, text="Abrir Certificación", height=40, command=self.run_cert_modular).pack(fill="x", padx=20, pady=20)
        self.tag_card(card12, "Sistemas", "Certificación Modular")

        extra_row2 = 4
        card13 = ctk.CTkFrame(grid, corner_radius=12)
        card13.grid(row=extra_row2, column=0, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(card13, text="Tarifa GUI", font=("Segoe UI", 18, "bold")).pack(pady=(20,6))
        ctk.CTkLabel(card13, text="Cálculo de salario").pack()
        ctk.CTkButton(card13, text="Abrir Tarifa", height=40, command=self.run_tarifa).pack(fill="x", padx=20, pady=20)
        self.tag_card(card13, "Ventas", "Tarifa GUI")

        card14 = ctk.CTkFrame(grid, corner_radius=12)
        card14.grid(row=extra_row2, column=1, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(card14, text="Salario Simple", font=("Segoe UI", 18, "bold")).pack(pady=(20,6))
        ctk.CTkLabel(card14, text="CLI mejorado").pack()
        ctk.CTkButton(card14, text="Abrir Salario Simple", height=40, command=self.run_salario_simple).pack(fill="x", padx=20, pady=20)
        self.tag_card(card14, "CLI", "Salario Simple")

        card15 = ctk.CTkFrame(grid, corner_radius=12)
        card15.grid(row=extra_row2, column=2, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(card15, text="Código Maestro", font=("Segoe UI", 18, "bold")).pack(pady=(20,6))
        ctk.CTkLabel(card15, text="Fusión total").pack()
        ctk.CTkButton(card15, text="Abrir Maestro", height=40, command=self.run_codigo_maestro).pack(fill="x", padx=20, pady=20)
        self.tag_card(card15, "Sistemas", "Código Maestro")

        card6 = ctk.CTkFrame(grid, corner_radius=12)
        card6.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(card6, text="Acciones", font=("Segoe UI", 16, "bold")).pack(pady=(16,4))
        btn_row = ctk.CTkFrame(card6, fg_color="transparent")
        btn_row.pack(pady=10)
        ctk.CTkButton(btn_row, text="Abrir Todas", command=self.run_all, fg_color="#1f6aa5", hover_color="#144870").pack(side="left", padx=6)
        ctk.CTkButton(btn_row, text="Salir", command=self.destroy, fg_color="#ef4444", hover_color="#b91c1c").pack(side="left", padx=6)
        grid.columnconfigure(0, weight=1)
        grid.columnconfigure(1, weight=1)
        grid.columnconfigure(2, weight=1)
        self.status_label = ctk.CTkLabel(self, text="Listo", anchor="w")
        self.status_label.pack(side="bottom", fill="x", padx=20, pady=10)

    def run_asistencia(self):
        script = os.path.join(os.path.dirname(__file__), "cverdnideestudantes.py")
        subprocess.Popen([sys.executable, script])
        self.set_status("Abierto: Asistencia")

    def run_programas(self):
        script = os.path.join(os.path.dirname(__file__), "nuevotraabajo.py")
        subprocess.Popen([sys.executable, script])
        self.set_status("Abierto: Programas")

    def run_both(self):
        self.run_asistencia()
        self.run_programas()

    def run_juan(self):
        script = os.path.join(os.path.dirname(__file__), "JUAN.PY")
        subprocess.Popen([sys.executable, script])
        self.set_status("Abierto: Siga Integral")

    def run_salario(self):
        script = os.path.join(os.path.dirname(__file__), "salario.py")
        subprocess.Popen([sys.executable, script])
        self.set_status("Abierto: Venta/Salario")

    def run_super_app(self):
        script = os.path.join(os.path.dirname(__file__), "super_app_v9_pro.py")
        subprocess.Popen([sys.executable, script])
        self.set_status("Abierto: Super App V9")

    def run_all(self):
        self.run_asistencia()
        self.run_programas()
        self.run_juan()
        self.run_salario()
        self.run_super_app()
        self.run_instituto()
        self.run_promedio_cli()
        self.run_salario_cli()

    def run_siga_final_pro(self):
        script = os.path.join(os.path.dirname(__file__), "siga_final_pro.py")
        subprocess.Popen([sys.executable, script])
        self.set_status("Abierto: Siga Final Pro")

    def run_permitidi(self):
        script = os.path.join(os.path.dirname(__file__), "sisitemapermitidi.py")
        subprocess.Popen([sys.executable, script])
        self.set_status("Abierto: Permiti")

    def run_cert_modular(self):
        script = os.path.join(os.path.dirname(__file__), "sertificadomodular.py")
        subprocess.Popen([sys.executable, script])
        self.set_status("Abierto: Certificación Modular")

    def run_tarifa(self):
        script = os.path.join(os.path.dirname(__file__), "tarifa.py")
        subprocess.Popen([sys.executable, script])
        self.set_status("Abierto: Tarifa GUI")

    def run_salario_simple(self):
        script = os.path.join(os.path.dirname(__file__), "salario_simple.py")
        subprocess.Popen([sys.executable, script])
        self.set_status("Abierto: Salario Simple")

    def run_codigo_maestro(self):
        script = os.path.join(os.path.dirname(__file__), "CÓDIGO MAESTRO (FUSIÓN TOTAL).py")
        subprocess.Popen([sys.executable, script])
        self.set_status("Abierto: Código Maestro")

    def run_instituto(self):
        script = os.path.join(os.path.dirname(__file__), "app_instituto.py")
        subprocess.Popen([sys.executable, script])
        self.set_status("Abierto: Instituto")

    def run_promedio_cli(self):
        self.create_promedio_window()
        self.set_status("Abierto: Promedio GUI")

    def run_salario_cli(self):
        self.create_salario_window()
        self.set_status("Abierto: Salario GUI")

    def create_promedio_window(self):
        win = ctk.CTkToplevel(self)
        win.title("Promedio de Notas")
        win.geometry("420x360")
        f = ctk.CTkFrame(win)
        f.pack(fill="both", expand=True, padx=20, pady=20)
        ctk.CTkLabel(f, text="Nota 1").pack(anchor="w")
        e1 = ctk.CTkEntry(f)
        e1.pack(fill="x")
        ctk.CTkLabel(f, text="Nota 2").pack(anchor="w")
        e2 = ctk.CTkEntry(f)
        e2.pack(fill="x")
        ctk.CTkLabel(f, text="Nota 3").pack(anchor="w")
        e3 = ctk.CTkEntry(f)
        e3.pack(fill="x")
        res = ctk.CTkLabel(f, text="")
        res.pack(pady=10)
        def calc():
            try:
                notas = [float(e1.get()), float(e2.get()), float(e3.get())]
                prom = promedio_notas.calcular_promedio(notas)
                cond = promedio_notas.determinar_condicion(prom)
                res.configure(text=f"Promedio: {prom:.2f} | Estado: {cond}")
            except Exception as ex:
                res.configure(text=f"Error: {ex}")
        ctk.CTkButton(f, text="Calcular", command=calc).pack(fill="x")

    def create_salario_window(self):
        win = ctk.CTkToplevel(self)
        win.title("Calculadora de Salario")
        win.geometry("420x320")
        f = ctk.CTkFrame(win)
        f.pack(fill="both", expand=True, padx=20, pady=20)
        ctk.CTkLabel(f, text="Horas trabajadas").pack(anchor="w")
        eh = ctk.CTkEntry(f)
        eh.pack(fill="x")
        ctk.CTkLabel(f, text="Costo por hora").pack(anchor="w")
        ec = ctk.CTkEntry(f)
        ec.pack(fill="x")
        res = ctk.CTkLabel(f, text="")
        res.pack(pady=10)
        last = {"horas": None, "costo": None, "pago": None}
        def calc():
            try:
                horas = float(eh.get())
                costo = float(ec.get())
                pago = salario_simple.calcular_pago(horas, costo)
                last.update({"horas": horas, "costo": costo, "pago": pago})
                res.configure(text=f"Pago total: S/ {pago:.2f}")
            except Exception as ex:
                res.configure(text=f"Error: {ex}")
        btn_row = ctk.CTkFrame(f)
        btn_row.pack(fill="x", pady=6)
        ctk.CTkButton(btn_row, text="Calcular", command=calc).pack(side="left", expand=True, fill="x", padx=4)
        def exportar():
            if last["horas"] is None:
                res.configure(text="Primero calcule el salario")
                return
            ruta = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")], initialfile="salario_resultado.csv") or "salario_resultado.csv"
            try:
                salario_simple.exportar_a_csv(last["horas"], last["costo"], last["pago"], ruta)
                res.configure(text=f"Exportado: {ruta}")
            except Exception as ex:
                res.configure(text=f"Error exportando: {ex}")
        ctk.CTkButton(btn_row, text="Exportar CSV", command=exportar).pack(side="left", expand=True, fill="x", padx=4)

    def tag_card(self, frame, category, title):
        self.cards.append({"frame": frame, "category": category, "title": title})

    def apply_filter(self, category):
        if category:
            self.current_category = category
        query = (self.search_var.get() or "").lower()
        for item in self.cards:
            match_cat = (self.current_category == "Todos" or item["category"] == self.current_category)
            match_q = (query in item["title"].lower())
            if match_cat and match_q:
                item["frame"].grid()
            else:
                item["frame"].grid_remove()

    def set_status(self, text):
        self.status_label.configure(text=text)

if __name__ == "__main__":
    app = FusionApp()
    app.mainloop()