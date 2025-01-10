# **TRP Temperature Calculator**

TRP Temperature Calculator es una herramienta interactiva para procesar datos de calibración TRP (Triple Point Resistance), calcular temperaturas basadas en esos datos, y visualizar los resultados en gráficos dinámicos. La aplicación combina cálculos precisos y una interfaz gráfica personalizable para facilitar el análisis de datos.

---

### **Cómo funciona**

#### **Inicio del programa**
Al ejecutar el programa, se carga la interfaz gráfica que incluye controles para personalizar la visualización, como escala del eje Y y color de la gráfica. También aparece un cuadro de diálogo para ingresar el número de TRP a procesar.

#### **Inicio del programa**
![trp-1](https://github.com/user-attachments/assets/a3f79c73-e5c4-4a62-a2b7-b36f43417f55)

En este ejemplo:
- Se solicitó el número de TRP a procesar.
- Se ingresó **1**.

![trp-2](https://github.com/user-attachments/assets/9115f364-4abc-43c9-b73f-4ba7b3e90aea)

#### **Selección del TRP y subrango**
Después de ingresar el número de TRP, el programa busca los datos relacionados, muestra el valor Rtriple y los subrangos disponibles.

- En este caso, se seleccionó el subrango **1**.
- Se calculó la temperatura correspondiente (**1.6479681385144485 °C**) y se registró en el archivo de salida.

**Nota:** También se generó un gráfico dinámico con el resultado calculado. Los controles permiten:
- Pausar la gráfica.
- Cambiar el color de la curva.
- Ajustar los límites mínimo y máximo del eje Y.

---

### **Cómo usar**
1. Ejecuta el programa:
   ```bash
   python3 src/main.py   
2. Ingresa el número de TRP que deseas procesar en el cuadro de diálogo.
3. Selecciona un subrango de los listados.
4. Observa la gráfica y utiliza los controles para personalizar la visualización.

### **Requisitos**
- **Python 3.8 o superior**
- **Dependencias necesarias**:
  Instálalas ejecutando el siguiente comando:
  ```bash
  pip install matplotlib
