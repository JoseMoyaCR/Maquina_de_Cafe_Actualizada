import unittest
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe

class TestDiagnosticoInicial(unittest.TestCase):
    def setUp(self):
        """Inicializar la maquina de cafe para cada prueba."""
        self.mc = MaquinadeCafe("Maquina de Cafe", 1.0)

    def test_diagnostico_inicial_completo(self):
        """CP-019-1: Validar diagnostico con todos los sensores y actuadores operativos."""
        resultado = self.mc.encender_máquina()
        self.assertTrue(resultado["Code"], "La maquina no se encendio correctamente.")
        estado = self.mc.estado()
        self.assertGreaterEqual(estado["Agua disponible"], 0, "El nivel de agua no es valido.")
        self.assertGreaterEqual(estado["Leche disponible"], 0, "El nivel de leche no es valido.")
        self.assertGreaterEqual(estado["Cafe disponible"], 0, "El nivel de cafe no es valido.")
        self.assertGreaterEqual(estado["Chocolate disponible"], 0, "El nivel de chocolate no es valido.")
        self.assertEqual(estado["Temperatura de la caldera"], 98, 
						 "La temperatura de la caldera no se inicializo correctamente.")

    def test_diagnostico_inicial_falla_sensor(self):
        """CP-019-2: Simular fallos en un sensor y validar el reporte."""
        # Simula fallo en sensor de agua
        self.mc._tanque_de_agua = -1
        estado = self.mc.estado()
        self.assertLess(estado["Agua disponible"], 0, "El fallo del sensor de agua no se reporto correctamente.")

    def test_tiempo_diagnostico_inicial(self):
        """CP-019-3: Confirmar que el diagnostico inicial no exceda un tiempo razonable."""
        inicio = time.time()
        self.mc.encender_máquina()
        tiempo_total = time.time() - inicio
        self.assertLessEqual(tiempo_total, 3, "El diagnostico inicial tardo demasiado tiempo.")

if __name__ == "__main__":
    unittest.main()
