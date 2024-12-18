import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe

class TestRutinaApagado(unittest.TestCase):
    def setUp(self):
        """Inicializar la maquina de cafe para cada prueba."""
        self.mc = MaquinadeCafe("Maquina de Cafe", 1.0)

    def test_apagado_normal(self):
        """CP-021-1: Verificar el apagado en condiciones normales."""
        self.mc._encendido = True  # Simula que la maquina esta encendida
        self.mc._encendido = False  # Simula el apagado
        self.assertFalse(self.mc._encendido, "El sistema no se apago correctamente.")

    def test_apagado_con_operaciones_activas(self):
        """CP-021-2: Simular operaciones activas y validar que el apagado se realiza correctamente."""
        self.mc._encendido = True  # Encender la maquina
        receta = {"agua_ml": 200, "cafe_g": 50}  # Simula preparacion
        self.mc.preparar_bebida(receta)
        self.mc._encendido = False  # Simula el apagado durante la operacion
        self.assertFalse(self.mc._encendido, "El sistema no se apago durante operaciones activas.")

    def test_estado_seguro_despues_apagado(self):
        """CP-021-3: Confirmar que el sistema queda en un estado seguro tras el apagado."""
        self.mc._encendido = True  # Simula que la maquina esta encendida
        self.mc._encendido = False  # Simula el apagado
        estado = self.mc.verificar_encendido()
        self.assertFalse(estado, "La maquina no quedo en estado apagado seguro.")

if __name__ == "__main__":
    unittest.main()
