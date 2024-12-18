
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe

class TestPreparacionAmericano(unittest.TestCase):
    def setUp(self):
        """Inicializar la maquina de cafe para cada prueba."""
        self.mc = MaquinadeCafe("Maquina de Cafe", 1.0)

    def test_preparar_americano_tamano_8oz(self):
        """CP-039-1: Validar preparacion de americano de 8 oz."""
        receta = {"agua_ml": 236, "cafe_g": 7, "leche_g": 0, "chocolate_g": 0}
        self._verificar_preparacion(receta, "Americano", 8)

    def test_preparar_americano_tamano_12oz(self):
        """CP-039-2: Validar preparacion de americano de 12 oz."""
        receta = {"agua_ml": 355, "cafe_g": 14, "leche_g": 0, "chocolate_g": 0}
        self._verificar_preparacion(receta, "Americano", 12)

    def test_preparar_americano_tamano_16oz(self):
        """CP-039-3: Validar preparacion de americano de 16 oz."""
        receta = {"agua_ml": 473, "cafe_g": 14, "leche_g": 0, "chocolate_g": 0}
        self._verificar_preparacion(receta, "Americano", 16)

    def _verificar_preparacion(self, receta, bebida, tamano):
        """Funcion para validar reduccion correcta de ingredientes."""
        # Configuracion inicial
        nivel_agua_inicial = self.mc._tanque_de_agua
        nivel_cafe_inicial = self.mc._recipiente_de_cafe

        # Preparar la bebida
        respuesta = self.mc.preparar_bebida(receta, bebida, tamano)

        # Validar la respuesta
        self.assertEqual(respuesta["Code"], 1, f"Error al preparar {bebida} de {tamano} oz.")

        # Verificar reduccion de ingredientes
        self.assertEqual(self.mc._tanque_de_agua, nivel_agua_inicial - receta["agua_ml"], "Error en consumo de agua.")
        self.assertEqual(self.mc._recipiente_de_cafe, nivel_cafe_inicial - receta["cafe_g"], "Error en consumo de cafe.")

if __name__ == "__main__":
    unittest.main()
