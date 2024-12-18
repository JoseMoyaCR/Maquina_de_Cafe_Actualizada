
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe

class TestPreparacionChocolateCaliente(unittest.TestCase):
    def setUp(self):
        """Inicializar la maquina de cafe para cada prueba."""
        self.mc = MaquinadeCafe("Maquina de Cafe", 1.0)

    def test_preparar_chocolate_tamano_8oz(self):
        """CP-040-1: Validar preparacion de chocolate caliente de 8 oz."""
        receta = {"agua_ml": 236, "cafe_g": 0, "leche_g": 10, "chocolate_g": 10}
        self._verificar_preparacion(receta, "Chocolate caliente", 8)

    def test_preparar_chocolate_tamano_12oz(self):
        """CP-040-2: Validar preparacion de chocolate caliente de 12 oz."""
        receta = {"agua_ml": 355, "cafe_g": 0, "leche_g": 20, "chocolate_g": 20}
        self._verificar_preparacion(receta, "Chocolate caliente", 12)

    def test_preparar_chocolate_tamano_16oz(self):
        """CP-040-3: Validar preparacion de chocolate caliente de 16 oz."""
        receta = {"agua_ml": 473, "cafe_g": 0, "leche_g": 30, "chocolate_g": 30}
        self._verificar_preparacion(receta, "Chocolate caliente", 16)

    def _verificar_preparacion(self, receta, bebida, tamano):
        """Funcion para validar reduccion correcta de ingredientes."""
        # Configuracion inicial
        nivel_agua_inicial = self.mc._tanque_de_agua
        nivel_leche_inicial = self.mc._recipiente_de_leche
        nivel_chocolate_inicial = self.mc._recipiente_de_chocolate

        # Preparar la bebida
        respuesta = self.mc.preparar_bebida(receta, bebida, tamano)

        # Validar la respuesta
        self.assertEqual(respuesta["Code"], 1, f"Error al preparar {bebida} de {tamano} oz.")

        # Verificar reduccion de ingredientes
        self.assertEqual(self.mc._tanque_de_agua, nivel_agua_inicial - receta["agua_ml"], "Error en consumo de agua.")
        self.assertEqual(self.mc._recipiente_de_leche, nivel_leche_inicial - receta["leche_g"], "Error en consumo de leche.")
        self.assertEqual(self.mc._recipiente_de_chocolate, nivel_chocolate_inicial - receta["chocolate_g"], "Error en consumo de chocolate.")

if __name__ == "__main__":
    unittest.main()
