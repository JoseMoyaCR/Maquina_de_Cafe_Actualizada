

# Declaración de la Clase Máquina de Cafe
class MaquinadeCafe:

    # Consutructor de Clase: Código que se ejecuta cuando se "crea" la máquina de cafe
    def __init__(self, nombre : str = "Máquina de Café", version__sistema: float = 1.0):
        self.nombre                     = nombre
        self.version_sistema           = version__sistema
        self._tanque_de_agua            = 10000 # mililitros de agua
        self._recipiente_de_leche       = 4000  # gramos de leche en polvo
        self._recipiente_de_cafe        = 6000  # gramos de café
        self._recipiente_de_chocolate   = 4000  # gramos de chocolate
        self._tazas_servidas            = 0     # cantidad de tazas procesadas

        # recetas
        # Expreso       : _cafe_por_expreso +_agua_por_expreso
        # Cafe con Leche: _cafe_por_expreso +_agua_por_expreso + _agua_extra + _leche_por_taza
        # Moka          : _cafe_por_expreso +_agua_por_expreso + _agua_extra + _leche_por_taza + _chocolate_por_taza
        # Chocolate     : _leche_por_taza + _chocolate_por_taza + _agua_taza
        # Agua Caliente : _agua_taza

        self._cafe_por_expreso          = 18
        self._agua_por_expreso          = 40
        self._agua_taza                 = 250
        self._leche_por_taza            = 32
        self._chocolate_por_taza        = 32
        


    # Destructor de Clase: Código que se ejecuta cuando se "apaga" la máquinada de café
    def __del__(self,):
        print("La máquinde cafe %s está terminando su operación", self.nombre)


    # Estado de Máquina de cafe
    def estado(self,):
        print("Reporte de estado de máquina de café: %s", self.nombre)
        print("------------------------------------------------------")
        print("Materia Prima disponible:")
        print("       - Agua disponble:         %d", self._tanque_de_agua)
        print("       - Leche disponble:        %d", self._recipiente_de_leche)
        print("       - Cafe disponble:         %d", self._recipiente_de_cafe)
        print("       - Chocolate disponble:    %d", self._recipiente_de_chocolate)
        print("Cantidad de tazas procesadas:    %d",self._tazas_servidas)

    # Matenimiento de Máaquina para recarga de Materia Prima
    def mantenimiento(self, agua : int = 0, leche : int = 0, cafe : int = 0, chocolate : int = 0):
        self._tanque_de_agua            = agua
        self._recipiente_de_leche       = leche
        self._recipiente_de_cafe        = cafe
        self._recipiente_de_chocolate   = chocolate
    
    def check_agua(self, cantidad_de_agua_requerida : int):
        if (cantidad_de_agua_requerida == 0 or cantidad_de_agua_requerida < 0):
            print("Error - La cantidad de agua requerida no puede ser menor o igual que 0")
            return -1
        else:
            print()

    # Servir expresso
    def expreso(self, cantidad : int = 1): # por defecto hace un expresso
        print("Café Expreso Solicitado -> Cantidad de tazas: %d", cantidad)
        agua_necesaria = self._agua_por_expreso * cantidad
        cafe_necesario = self._cafe_por_expreso *cantidad
        # El expreso usa 18 g de café y 250 ml de agua
        if ((self._tanque_de_agua >= agua_necesaria) and (self._recipiente_de_cafe >= cafe_necesario)):
            print("Hay suficiente agua y café para la preparación. Comenzando preparación por favor espere...")
            self._tanque_de_agua       -= agua_necesaria
            self._recipiente_de_cafe   -= cafe_necesario
            self._tazas_servidas       += cantidad
            print("Cantidad de expresos preparados: %d", cantidad)
            return cantidad
        else:
            if (self._tanque_de_agua < agua_necesaria):
                expresos_disponibles = int(self._tanque_de_agua / self._agua_por_expreso)
                print("No Hay suficiente Agua para la preparación. Por favor recargue el sistema o solicite una cantidad menor de tazas. \
                      La cantidad de agua permitiría preparar %d", expresos_disponibles)
            if (self._recipiente_de_cafe < cafe_necesario):
                expressos_disponibles = int(self._recipiente_de_cafe / self._cafe_por_expreso)
                print("No Hay suficiente Agua para la preparación. Por favor recargue el sistema o solicite una cantidad menor de tazas. \
                      La cantidad de agua permitiría preparar %d", expresos_disponibles)
            return -1
        
    # Servir expresso
    def cafe_con_leche(self, cantidad : int = 1): # por defecto hace un expresso
        print("Café con Leche Solicitado -> Cantidad de tazas: %d", cantidad)
        agua_necesaria = self._agua_taza * cantidad
        cafe_necesario = 18 * cantidad
        leche_necesaria = 32 * cantidad
        # El cafe con leche usa 18 g de café, 32 g de leche y 250 ml de agua
        if ((self._tanque_de_agua >= agua_necesaria) and (self._recipiente_de_cafe >= cafe_necesario) and (self._recipiente_de_leche >= leche_necesaria)):
            print("Hay suficiente agua, leche y café para la preparación. Comenzando preparación por favor espere...")
            self._tanque_de_agua       -= agua_necesaria
            self._recipiente_de_cafe   -= cafe_necesario
            self._recipiente_de_leche  -= leche_necesaria
            self._tazas_servidas       += cantidad
            print("Cantidad de cafés con leche preparados: %d", cantidad)
            return cantidad
        else:
            if (self._tanque_de_agua < agua_necesaria):
                cafes_con_leche_disponibles = int(self._tanque_de_agua / 40)
                print("No Hay suficiente Agua para la preparación. Por favor recargue el sistema o solicite una cantidad menor de tazas. \
                      La cantidad de agua permitiría preparar %d", cafes_con_leche_disponibles)
            if (self._recipiente_de_cafe < cafe_necesario):
                expressos_disponibles = int(self._recipiente_de_cafe / 18)
                print("No Hay suficiente Agua para la preparación. Por favor recargue el sistema o solicite una cantidad menor de tazas. \
                      La cantidad de agua permitiría preparar %d", expresos_disponibles)
           if (self._recipiente_de_leche < leche_necesaria):
                expressos_disponibles = int(self._recipiente_de_cafe / 18)
                print("No Hay suficiente Agua para la preparación. Por favor recargue el sistema o solicite una cantidad menor de tazas. \
                      La cantidad de agua permitiría preparar %d", expresos_disponibles) 
            return -1

p1 = MaquinadeCafe("John", 1.2)
p1.myfunc()