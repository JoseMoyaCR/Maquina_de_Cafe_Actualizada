import tkinter as tk
from tkinter import font
from MaquinadeCafe import MaquinadeCafe


class InterfazUsuario:
    def __init__(self):
        self.textos_bebidas = [
            "Expreso",
            "Doble expreso",
            "Americano",
            "Cappuccino",
            "Mokaccino",
            "Chocolate caliente",
            "Leche caliente",
            "Agua caliente",
        ]
        self.textos_tamanos = ["Tamaño 1", "Tamaño 2", "Tamaño 3"]

        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("Máquina de Café")
        self.root.geometry("1000x600")
        self.button_font = font.Font(size=10, weight="bold")

        # Inicializar variables de selección
        # Otras inicializaciones
        self.bebida_seleccionada = None
        self.tamano_seleccionado = None
        self.receta = None  # Inicializa la variable receta

        # Crear Maquina de cafe
        self.McD = MaquinadeCafe("Máquina de Café", 1.0)

        # Crear botones, LEDs y área de visualización
        self.create_display()
        self.create_buttons()
        self.create_leds()

        # Configurar pesos de la cuadrícula para diseño responsivo
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1)

        # Mensaje de inicio
        self.mensaje_inicio = f"{self.McD.nombre} \n versión {self.McD.version_sistema:.1f} \n inicializada"
        self.update_display(self.mensaje_inicio)

        # Iniciar el bucle principal
        self.root.mainloop()

    def create_display(self):
        # Crear el área de visualización con tamaño fijo
        self.display = tk.Label(
            self.root,
            text="DISPLAY",
            font=("Arial", 12),
            borderwidth=2,
            relief="solid",
            anchor="center",
            width=40,  # Fijar ancho en caracteres
            height=10,  # Fijar altura en líneas
            wraplength=300,  # Limitar ancho del texto en píxeles
        )
        self.display.grid(row=0, column=1, rowspan=4, padx=10, pady=5, sticky="nsew")

    def create_leds(self):
        # LED de bebida seleccionada
        self.led_bebida = tk.Label(self.root, text="Bebida", bg="gray", width=15, height=2)
        self.led_bebida.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        # LED de tamaño seleccionado
        self.led_tamano = tk.Label(self.root, text="Tamaño", bg="gray", width=15, height=2)
        self.led_tamano.grid(row=6, column=1, padx=5, pady=5, sticky="e")

    def update_leds(self):
        # Actualizar LED de bebida
        if self.bebida_seleccionada:
            self.led_bebida.config(bg="green")
        else:
            self.led_bebida.config(bg="gray")

        # Actualizar LED de tamaño
        if self.tamano_seleccionado:
            self.led_tamano.config(bg="green")
        else:
            self.led_tamano.config(bg="gray")

    def update_display(self, message):
        # Actualizar el texto del display
        self.display.config(text=message)

    def create_buttons(self):
        # Botones laterales izquierdos
        for i in range(4):
            button = tk.Button(
                self.root,
                text=self.textos_bebidas[i],
                font=self.button_font,
                command=lambda i=i: self.button_action(self.textos_bebidas[i]),
            )
            button.grid(row=i, column=0, padx=10, pady=5, sticky="nsew")

        # Botones laterales derechos
        for i in range(4):
            button = tk.Button(
                self.root,
                text=self.textos_bebidas[i + 4],
                font=self.button_font,
                command=lambda i=i: self.button_action(self.textos_bebidas[i + 4]),
            )
            button.grid(row=i, column=2, padx=10, pady=5, sticky="nsew")

        # Botones inferiores
        tk.Button(
            self.root,
            text="Encender",
            bg="green",
            fg="white",
            font=self.button_font,
            command=lambda: self.button_action("Encender"),
            height=2,
            width=15,
        ).grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
        tk.Button(
            self.root,
            text="8 oz",
            font=self.button_font,
            command=lambda: self.button_action("Tamaño 1"),
            height=2,
            width=5,
        ).grid(row=4, column=1, padx=5, pady=5, sticky="w")
        tk.Button(
            self.root,
            text="12 oz",
            font=self.button_font,
            command=lambda: self.button_action("Tamaño 2"),
            height=2,
            width=5,
        ).grid(row=4, column=1, padx=5, pady=5)
        tk.Button(
            self.root,
            text="16 oz",
            font=self.button_font,
            command=lambda: self.button_action("Tamaño 3"),
            height=2,
            width=5,
        ).grid(row=4, column=1, padx=5, pady=5, sticky="e")
        tk.Button(
            self.root,
            text="Apagar",
            bg="red",
            fg="white",
            font=self.button_font,
            command=lambda: self.button_action("Apagar"),
            height=2,
            width=15,
        ).grid(row=4, column=2, padx=10, pady=5, sticky="nsew")
        tk.Button(
            self.root,
            text="Reporte",
            bg="blue",
            fg="white",
            font=self.button_font,
            command=lambda: self.button_action("Reporte"),
            height=1,
            width=15,
        ).grid(row=5, column=2, padx=10, pady=5, sticky="nsew")
        tk.Button(
            self.root,
            text="Mantenimiento",
            bg="orange",
            fg="white",
            font=self.button_font,
            command=lambda: self.button_action("Mantenimiento"),
            height=1,
            width=15,
        ).grid(row=5, column=0, padx=5, pady=10, sticky="nsew")
        tk.Button(
            self.root,
            text="Reiniciar",
            bg="gray",
            fg="white",
            font=self.button_font,
            command=self.reiniciar_seleccion,
            height=1,
            width=10,
        ).grid(row=5, column=1, padx=3, pady=5, sticky="nsew")

    def mostrar_progreso(self, proceso: str, tiempo_espera: int):
        progreso_total = 100
        pasos = 20
        tiempo_por_paso = tiempo_espera // pasos
        progreso_actual = 0

        def actualizar_progreso():
            nonlocal progreso_actual
            if progreso_actual <= progreso_total:
                self.update_display(f"{proceso}: {progreso_actual}% completado")
                progreso_actual += progreso_total // pasos
                self.root.after(tiempo_por_paso, actualizar_progreso)
            else:
                self.update_display(f"{proceso}: ¡Completado!")

        actualizar_progreso()


    def button_action(self, button_name):
        if not self.McD.verificar_encendido():
            if button_name == "Encender":
                resultado = self.McD.encender_máquina()
                self.mostrar_progreso(resultado["Message"], resultado["Tiempo_Proceso"])  # Mostrar progreso
            else:
                self.update_display(
                    f"{self.McD.nombre} no ha sido encendida. \n Por favor, encienda la máquina antes \n de realizar cualquier acción."
                )
        else:
            if button_name in self.textos_bebidas:
                self.bebida_seleccionada = button_name
                self.update_display(f"Has seleccionado: {button_name}")
                self.update_leds()

            # Preparación automática si es Expreso o Doble expreso
            if button_name in ["Expreso", "Doble expreso"]:
                self.update_leds()
                tamano = 0 if button_name == "Expreso" else 1  # 0 para Expreso, 1 para Doble expreso
                self.receta = self.McD.obtener_receta("Expreso", tamano)  # Obtener receta
                if "error" in self.receta:
                    self.update_display(self.receta["error"])
                if self.McD.verificar_reservas(self.receta)["Code"]:
                    self.mostrar_progreso(f"Preparando {button_name}", 5000)  # Simula 5 segundos de progreso
                    resultado = self.McD.preparar_bebida(self.receta, "Expreso", tamano)
                    self.update_display(resultado["Message"])
                    self.receta = None
                    self.bebida_seleccionada = None
                    self.tamano_seleccionado = None
                    self.reiniciar_seleccion()  # Reiniciar automáticamente después de la preparación
                else:
                    self.update_display(self.McD.verificar_reservas(self.receta)["Message"])
                
            elif button_name in self.textos_tamanos and self.bebida_seleccionada:
                tamano_index = self.textos_tamanos.index(button_name)
                self.tamano_seleccionado = [8, 12, 16][tamano_index]
                self.update_display(
                    f"Tamaño seleccionado: {self.tamano_seleccionado} oz"
                )
            elif button_name == "Reporte":
                reporte_imprimir = self.McD.mostrar_reporte()
                resultado = self.McD.guardar_reporte()
                self.update_display(reporte_imprimir + f"\n" + resultado["Message"])
            elif button_name == "Mantenimiento":
                self.mostrar_progreso("Realizando mantenimiento", 7000)  # Simula 7 segundos de progreso
                resultado = self.McD.mantenimiento(
                    agua=10000, leche=2500, cafe=5000, chocolate=2500
                )
                self.update_display(resultado["Message"])
            elif button_name == "Apagar":
                self.update_display(f"{self.McD.nombre} se está apagando...")
                self.mostrar_progreso("Apagando máquina", 3000)  # Simula 3 segundos de apagado
                self.McD._encendido = False
            else:
                self.update_display("Por favor, seleccione \n una acción válida.")

        # Lógica para preparar bebida si bebida, tamaño y receta están seleccionados
        if self.bebida_seleccionada != None and self.tamano_seleccionado != None:
            self.receta = self.McD.obtener_receta(self.bebida_seleccionada, self.tamano_seleccionado)
            if self.McD.verificar_reservas(self.receta)["Code"]:
                self.mostrar_progreso(f"Preparando {self.bebida_seleccionada} de \n {self.tamano_seleccionado} oz", 5000)  # Simula 5 segundos de preparación
                resultado = self.McD.preparar_bebida(self.receta, self.bebida_seleccionada, self.tamano_seleccionado)
                self.update_display(resultado["Message"])

                # Reiniciar variables después de preparar la bebida
                self.bebida_seleccionada = None
                self.tamano_seleccionado = None
                self.receta = None
                self.reiniciar_seleccion()
            else:
                self.update_display(self.McD.verificar_reservas(self.receta)["Message"])

    def reiniciar_seleccion(self):
        # Reiniciar la selección de bebida y tamaño
        self.bebida_seleccionada = None
        self.tamano_seleccionado = None
        self.update_display(self.mensaje_inicio)
        self.update_leds()


# Crear e iniciar la interfaz
InterfazUsuario()







'''
import tkinter as tk
from tkinter import font
from MaquinadeCafe import MaquinadeCafe
from time import sleep

class InterfazUsuario:
    def __init__(self):
        self.textos_bebidas = [
        "Expreso",
        "Doble expreso",
        "Americano",
        "Cappuccino",
        "Mokaccino",
        "Chocolate caliente",
        "Leche caliente",
        "Agua caliente",
        ]

        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("Máquina de Café")
        self.root.geometry("800x400")  # Ajustar tamaño según sea necesario

        # Definir fuentes
        self.button_font = font.Font(size=10, weight="bold")

        # Inicializar variables de selección
        self.bebida_seleccionada = None
        self.tamano_seleccionado = None

        # Crear botones y área de visualización
        self.create_display()
        self.create_buttons()

        # Crear Maquina de cafe
        self.McD = MaquinadeCafe("Máquina de Café", 1.0)

        # Configurar pesos de la cuadrícula para diseño responsivo
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1)
        
        self.mensaje_inicio = f"{self.McD.nombre} \n versión {self.McD.version_sistema:.1f} \n inicializada"

        self.update_display(self.mensaje_inicio)

        # Iniciar el bucle principal
        self.root.mainloop()



    def create_display(self):
        # Área de visualización
        self.display = tk.Label(
            self.root,
            text="DISPLAY",
            font=("Arial", 14),
            borderwidth=2,
            relief="solid",
            anchor="center",
        )
        self.display.grid(row=0, column=1, rowspan=4, padx=10, pady=5, sticky="nsew")

    def update_display(self, message):
        # Actualizar el texto del display
        self.display.config(text=message)

    def create_buttons(self):
        
        # Botones laterales izquierdos
        for i in range(4):
            button = tk.Button(self.root, text=self.textos_bebidas[i], font=self.button_font,
                               command=lambda i=i: self.button_action(self.textos_bebidas[i]))
            button.grid(row=i, column=0, padx=10, pady=5, sticky="nsew")

        # Botones laterales derechos
        for i in range(4):
            button = tk.Button(self.root, text=self.textos_bebidas[i+4], font=self.button_font,
                               command=lambda i=i: self.button_action(self.textos_bebidas[i+4]))
            button.grid(row=i, column=2, padx=10, pady=5, sticky="nsew")

        # Botones inferiores
        encender_button = tk.Button(self.root, text="Encender", bg="green", fg="white", font=self.button_font, command=lambda: self.button_action("Encender"))
        encender_button.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")

        tamaño1_button = tk.Button(self.root, text="8 oz", font=self.button_font, command=lambda: self.button_action("Tamaño 1"))
        tamaño1_button.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        tamaño2_button = tk.Button(self.root, text="12 oz", font=self.button_font, command=lambda: self.button_action("Tamaño 2"))
        tamaño2_button.grid(row=4, column=1, padx=5, pady=5)

        tamaño3_button = tk.Button(self.root, text="16 oz", font=self.button_font, command=lambda: self.button_action("Tamaño 3"))
        tamaño3_button.grid(row=4, column=1, padx=5, pady=5, sticky="e")

        apagar_button = tk.Button(self.root, text="Apagar", bg="red", fg="white", font=self.button_font, command=lambda: self.button_action("Apagar"))
        apagar_button.grid(row=4, column=2, padx=10, pady=5, sticky="nsew")

        mantenimiento_button = tk.Button(self.root, text="Mantenimiento", bg="orange", font=self.button_font, command=lambda: self.button_action("Mantenimiento"))
        mantenimiento_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
    
    def mostrar_progreso_bloqueante(self, proceso: str, tiempo_espera: int):
        progreso_total = 100
        pasos = 20
        tiempo_por_paso = tiempo_espera // pasos

        for progreso_actual in range(0, progreso_total + 1, progreso_total // pasos):
            self.update_display(f"{proceso}: {progreso_actual}% completado")
            sleep(tiempo_por_paso / 1000)  # Detiene la ejecución (bloquea la GUI)

        self.update_display(f"{proceso}: ¡Completado!")


    def button_action(self, button_name):
        # Verificar si la máquina está encendida
        if not self.McD.verificar_encendido():
            if button_name == "Encender":
                # Encender la máquina
                resultado = self.McD.encender_máquina()
                self.mostrar_progreso_bloqueante(resultado["Message"], resultado["Tiempo_Proceso"])
            else:
                # Mostrar mensaje si la máquina no está encendida
                self.update_display(f"{self.McD.nombre} no ha sido encendida. Por favor, encienda la máquina antes de realizar cualquier acción.")
                sleep(2)
                self.update_display(self.mensaje_inicio)
        else:
            # Acciones cuando la máquina está encendida
            if button_name in self.textos_bebidas and self.bebida_seleccionada is None:
                # Seleccionar bebida
                self.bebida_seleccionada = button_name
                self.update_display(f"Has seleccionado: {button_name}")
            elif button_name in self.textos_tamanos and self.bebida_seleccionada:
                # Seleccionar tamaño
                tamano_index = self.textos_tamanos.index(button_name)
                self.tamano_seleccionado = [8, 12, 16][tamano_index]
                self.update_display(f"Tamaño seleccionado: {self.tamano_seleccionado} oz")
            elif button_name == "Preparar" and self.bebida_seleccionada and self.tamano_seleccionado:
                # Preparar bebida
                self.receta = self.McD._obtener_self.receta(self.bebida_seleccionada, self.tamano_seleccionado)
                if "error" in self.receta:
                    self.update_display(self.receta["error"])
                else:
                    resultado = self.McD.preparar_bebida(self.receta)
                    self.mostrar_progreso_bloqueante(resultado["Message"], 5000)  # Simula 5 segundos de preparación
                    self.bebida_seleccionada = None
                    self.tamano_seleccionado = None
            elif button_name == "Mantenimiento":
                # Realizar mantenimiento
                resultado = self.McD.mantenimiento(agua=10000, leche=4000, cafe=6000, chocolate=4000)
                self.update_display(resultado["Message"])
            elif button_name == "Apagar":
                # Apagar la máquina
                self.update_display(f"{self.McD.nombre} se está apagando...")
                sleep(2)
                self.McD.__del__()
            else:
                # Mensaje predeterminado para acciones no válidas
                self.update_display("Por favor, seleccione una acción válida.")

# Crear e iniciar la interfaz
InterfazUsuario()
'''
