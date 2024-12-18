import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe

class TestEncendidoSistema(unittest.TestCase):
    def setUp(self):
        """Inicializar la maquina de cafe para cada prueba."""
        self.mc = MaquinadeCafe("Maquina de Cafe", 1.0)

    def test_encendido_normal(self):
        """CP-020-1: Verificar el flujo de encendido en condiciones normales."""
        resultado = self.mc.encender_máquina()
        self.assertTrue(resultado["Code"], "La rutina de encendido fallo.")
        estado = self.mc.estado()
        self.assertGreaterEqual(estado["Agua disponible"], 0, "El nivel de agua no es valido despues del encendido.")
        self.assertGreaterEqual(estado["Leche disponible"], 0, "El nivel de leche no es valido despues del encendido.")

    def test_encendido_inicializa_funciones(self):
        """CP-020-2: Confirmar que la rutina de encendido inicia todas las funciones del sistema."""
        self.mc.encender_máquina()
        estado = self.mc.estado()
        self.assertEqual(estado["Temperatura de la caldera"], 98, "La caldera no se inicializo correctamente.")
        self.assertGreaterEqual(estado["Agua disponible"], 0, "El nivel de agua no es valido despues del encendido.")
        self.assertGreaterEqual(estado["Cafe disponible"], 0, "El nivel de cafe no es valido despues del encendido.")

if __name__ == "__main__":
    unittest.main()

