import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe

class TestPreparacionExpreso(unittest.TestCase):
    def setUp(self):
        """Inicializar la maquina de cafe para cada prueba."""
        self.mc = MaquinadeCafe("Maquina de Cafe", 1.0)

    def test_preparar_expresso_simple(self):
        """CP-035-1: Validar preparacion de un expreso con cantidad correcta."""
        # Configuracion inicial
        receta_expresso = {"agua_ml": 30, "cafe_g": 7, "leche_g": 0, "chocolate_g": 0}
        nivel_agua_inicial = self.mc._tanque_de_agua
        nivel_cafe_inicial = self.mc._recipiente_de_cafe

        # Preparar la bebida
        respuesta = self.mc.preparar_bebida(receta_expresso, "Expreso", 0)

        # Validar la respuesta
        self.assertEqual(respuesta["Code"], 1, "Error al preparar el expreso.")

        # Verificar reduccion de ingredientes
        self.assertEqual(self.mc._tanque_de_agua, nivel_agua_inicial - receta_expresso["agua_ml"], "Error en consumo de agua.")
        self.assertEqual(self.mc._recipiente_de_cafe, nivel_cafe_inicial - receta_expresso["cafe_g"], "Error en consumo de cafe.")

if __name__ == "__main__":
    unittest.main()

