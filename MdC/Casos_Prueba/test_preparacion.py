import unittest
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MaquinadeCafe import MaquinadeCafe


class TestPreparacionBebida(unittest.TestCase):
    def setUp(self):
        """Configurar la instancia de la maquina de cafe."""
        self.mc = MaquinadeCafe("Maquina de Cafe", version__sistema=1.0)

    def test_preparar_bebida_estandar(self):
        """CP-004-1: Medir el tiempo de preparacion de una bebida estandar."""
        receta = {"agua_ml": 60, "cafe_g": 14, "leche_g": 0, "chocolate_g": 0}
        inicio = time.time()
        resultado = self.mc.preparar_bebida(receta)
        fin = time.time()
        tiempo_transcurrido = fin - inicio

        self.assertEqual(resultado["Code"], 1, "La bebida no fue preparada exitosamente.")
        self.assertLessEqual(tiempo_transcurrido, 30, "El tiempo excede los 30 segundos.")
        print(f"Tiempo de preparacion estandar: {tiempo_transcurrido:.2f} segundos")

    def test_preparar_bebida_diferentes_tamanos(self):
        """CP-004-2: Validar tiempo para bebidas de diferentes tamanios."""
        tamanos = {
            "8oz": {"agua_ml": 240, "cafe_g": 20, "leche_g": 0, "chocolate_g": 0},
            "12oz": {"agua_ml": 360, "cafe_g": 30, "leche_g": 0, "chocolate_g": 0},
            "16oz": {"agua_ml": 480, "cafe_g": 40, "leche_g": 0, "chocolate_g": 0},
        }

        for tamano, receta in tamanos.items():
            inicio = time.time()
            resultado = self.mc.preparar_bebida(receta)
            fin = time.time()
            tiempo_transcurrido = fin - inicio

            self.assertEqual(resultado["Code"], 1, f"La bebida {tamano} no fue preparada exitosamente.")
            self.assertLessEqual(tiempo_transcurrido, 30, f"El tiempo para {tamano} excede los 30 segundos.")
            print(f"Tiempo de preparacion para {tamano}: {tiempo_transcurrido:.2f} segundos")

    def test_preparar_bebida_condiciones_de_carga(self):
        """CP-004-3: Verificar tiempos bajo diferentes condiciones de carga."""
        receta = {"agua_ml": 60, "cafe_g": 14, "leche_g": 0, "chocolate_g": 0}

        # Simular preparacion de bebidas en secuencia
        tiempos = []
        for i in range(5):
            inicio = time.time()
            resultado = self.mc.preparar_bebida(receta)
            fin = time.time()
            tiempo_transcurrido = fin - inicio
            tiempos.append(tiempo_transcurrido)

            self.assertEqual(resultado["Code"], 1, f"Fallo en la preparacion durante la carga en el intento {i+1}.")
            self.assertLessEqual(tiempo_transcurrido, 30, f"Tiempo excedido en la preparacion durante la carga en el intento {i+1}.")

        print(f"Tiempos de preparacion bajo carga: {[f'{t:.2f}' for t in tiempos]}")

if __name__ == "__main__":
    unittest.main()
