import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe

class TestDispensarAguaCaliente(unittest.TestCase):
    def setUp(self):
        """Inicializar la maquina de cafe para cada prueba."""
        self.mc = MaquinadeCafe("Maquina de Cafe", 1.0)

    def test_dispensar_agua_tamano_8oz(self):
        """CP-041-1: Validar dispensado de agua caliente de 8 oz."""
        receta = {"agua_ml": 236, "cafe_g": 0, "leche_g": 0, "chocolate_g": 0}
        self._verificar_dispensado_agua(receta, "Agua caliente", 8)

    def test_dispensar_agua_tamano_12oz(self):
        """CP-041-2: Validar dispensado de agua caliente de 12 oz."""
        receta = {"agua_ml": 355, "cafe_g": 0, "leche_g": 0, "chocolate_g": 0}
        self._verificar_dispensado_agua(receta, "Agua caliente", 12)

    def test_dispensar_agua_tamano_16oz(self):
        """CP-041-3: Validar dispensado de agua caliente de 16 oz."""
        receta = {"agua_ml": 473, "cafe_g": 0, "leche_g": 0, "chocolate_g": 0}
        self._verificar_dispensado_agua(receta, "Agua caliente", 16)

    def _verificar_dispensado_agua(self, receta, bebida, tamano):
        """Funcion auxiliar para validar dispensado de agua caliente."""
        self.mc.encender_máquina()
        # Configuracion inicial
        nivel_agua_inicial = self.mc._tanque_de_agua
        temperatura_inicial = self.mc._temperatura_caldera

        # Preparar la bebida
        respuesta = self.mc.preparar_bebida(receta, bebida, tamano)

        # Validar la respuesta
        self.assertEqual(respuesta["Code"], 1, f"Error al dispensar {bebida} de {tamano} oz.")

        # Verificar reduccion del agua
        self.assertEqual(self.mc._tanque_de_agua, nivel_agua_inicial - receta["agua_ml"], "Error en consumo de agua.")

        # Validar la temperatura
        self.assertGreaterEqual(self.mc._temperatura_caldera, 94, "La temperatura esta por debajo de 94C.")
        self.assertLessEqual(self.mc._temperatura_caldera, 96, "La temperatura supera los 96C.")

if __name__ == "__main__":
    unittest.main()
