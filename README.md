# ☕ Máquina de Café - Proyecto Final de Validación de Sistemas Embebidos

Este repositorio contiene la implementación y validación del sistema de **Máquina de Café**, desarrollado como parte del proyecto final del curso **Validación de Sistemas Embebidos (TSEV-008)** de la Universidad Fidélitas. 

---
## 🛠️ Descripción del Proyecto
El sistema emula una **máquina de café** con capacidades de:

- Preparación de bebidas (éxpresso, cappuccino, mokaccino, chocolate caliente, etc.).
- Monitoreo de niveles de materia prima (agua, café, leche en polvo, chocolate).
- Diagnóstico automático del sistema y generación de reportes.
- Control de temperaturas durante la preparación.

Este proyecto **implementa validaciones exhaustivas** mediante un **plan de pruebas estructurado** y mejoras funcionales en el sistema original.

---
## 📊 Características Principales
1. **Control de Materia Prima**: Monitoreo y alerta sobre niveles bajos.
2. **Preparación de Bebidas**: Validación de proporciones y volúmenes correctos.
3. **Diagnóstico del Sistema**: Rutinas de autodiagnóstico de sensores y componentes.
4. **Reportes Generados**:
   - 📃 Reporte de bebidas preparadas.
   - 📃 Reporte de mantenimiento.
   - 📃 Reporte del sistema en formato JSON y CSV.
5. **Interfaz Gráfica (Tkinter)**: 
   - 💡 Panel de control intuitivo.
   - 🔢 Visualización de estados del sistema (encendido, apagado, inicialización).

---
## 🔧 Mejoras Realizadas
- **Plan de validación**: Creación de un plan estructurado con pruebas unitarias (usando **unittest**) y funcionales.
- **Rutinas implementadas**:
   - Diagnóstico de sensores (🛡️).
   - Registro automático de bebidas preparadas y eventos de mantenimiento.
- **Código simplificado**: Refactorización del código original para mejorar legibilidad y modularidad.

---
## ✅ Validaciones Realizadas
| **Requerimiento** | **Criterio de Éxito** | **Estado** |
|-------------------|--------------------------|------------|
| REQ1  | Validar el funcionamiento general de la máquina. | 👍 Cumplido |
| REQ2  | Confirmar la operación en Raspberry Pi 5. | 👍 Cumplido |
| REQ3  | Validar el uso de Tkinter para la interfaz gráfica. | 👍 Cumplido |
| REQ4  | Asegurar tiempos de preparación inferiores a 30 segundos. | 👍 Cumplido |
| REQ5  | Confirmar que el uso del CPU no alcanza el 100%. | 👍 Cumplido |
| REQ7  | Validar sensor de nivel de agua y alertas. | 👍 Cumplido |
| REQ8  | Simulación del sensor de nivel de agua. | 👍 Cumplido |
| REQ9  | Validar sensor de temperatura (0-110°C). | 👍 Cumplido |
| REQ10 | Simulación del sensor de temperatura. | 👍 Cumplido |
| REQ11 | Validar sensor de peso del café (0-5000 g). | 👍 Cumplido |
| REQ12 | Simulación del sensor de peso del café. | 👍 Cumplido |
| REQ13 | Validar sensor de peso de leche en polvo (0-2500 g). | 👍 Cumplido |
| REQ15 | Validar sensor de peso de chocolate en polvo (0-2500 g). | 👍 Cumplido |
| REQ16 | Validar la visualización en pantalla LCD. | 👍 Cumplido |
| REQ17 | Verificar la funcionalidad del tablero de control. | 👍 Cumplido |
| REQ18 | Validar los niveles y alertas de materia prima. | 👍 Cumplido |
| REQ19 | Implementar y validar rutina de autodiagnóstico. | 👍 Cumplido |
| REQ20 | Simular la rutina de encendido del sistema. | 👍 Cumplido |
| REQ21 | Validar la rutina de apagado seguro del sistema. | 👍 Cumplido |
| REQ22 | Verificar el estado visual del sistema (encendido/apagado/inicialización). | 👍 Cumplido |
| REQ23 | Validar autodiagnóstico completo del sistema. | 👍 Cumplido |
| REQ24 | Generar reporte del estado general del sistema. | 👍 Cumplido |
| REQ25 | Mostrar el reporte en la pantalla LCD. | 👍 Cumplido |
| REQ26 | Guardar reportes del sistema en una carpeta de logs. | 👍 Cumplido |
| REQ29 | Registrar bebidas preparadas con hora y tipo. | 👍 Cumplido |
| REQ31 | Validar registro de eventos de mantenimiento. | 👍 Cumplido |
| REQ32 | Generar reporte de mantenimiento en formato CSV. | 👍 Cumplido |
| REQ33 | Implementar y cargar recetario de bebidas en formato JSON. | 👍 Cumplido |
| REQ34 | Validar temperatura de operación de la caldera (95 ± 1.0°C). | 👍 Cumplido |
| REQ35 | Preparar expreso simple (1 oz). | 👍 Cumplido |
| REQ36 | Preparar doble expreso (2 oz). | 👍 Cumplido |
| REQ37 | Preparar cappuccino en sus 3 tamaños. | 👍 Cumplido |
| REQ38 | Preparar mokaccino en sus 3 tamaños. | 👍 Cumplido |
| REQ39 | Preparar americano en sus 3 tamaños. | 👍 Cumplido |
| REQ40 | Preparar chocolate caliente en sus 3 tamaños. | 👍 Cumplido |
| REQ41 | Dispensar agua caliente a la temperatura adecuada. | 👍 Cumplido |
| REQ42 | Preparar bebidas con un volumen exacto de 8 oz. | 👍 Cumplido |

Las validaciones fueron implementadas con **unittest**, asegurando que cada requisito específico sea verificado de manera rigurosa.

---
## 📊 Resultados Obtenidos
- **Confiabilidad del sistema**: Validación exitosa de todos los requerimientos funcionales y de rendimiento.
- **Automatización de pruebas**: Implementación de casos de prueba automáticos con **unittest**, reduciendo el tiempo de validación manual.
- **Organización con matriz de trazabilidad**: Cada prueba corresponde a un requisito específico, garantizando cobertura completa.

---
## 📊 Documentación Adicional
- **Especificación de Requerimientos**: Incluida en la carpeta `Documentos`.
- **Reportes Generados**: Almacenados en carpetas `logs/` y `reportes/`.

---
## 🌟 Agradecimientos
Este proyecto fue desarrollado como parte del curso **Validación de Sistemas Embebidos** en la Universidad Fidélitas. 

