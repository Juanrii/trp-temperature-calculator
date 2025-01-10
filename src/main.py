from src.core.data_processing import DataProcessor
from src.core.calculation import TemperatureCalculator
from src.ui.gui import GraphController

def main():
    file_path = 'data/its90trp+2.txt'

    data_processor = DataProcessor(file_path)
    temperature_calculator = TemperatureCalculator({}, [])

    def obtener_datos_grafica():
        return temperature_calculator.obtener_datos_grafica()

    graph_controller = GraphController(obtener_datos_grafica)

    def buscar_trp_y_calcular():
        import tkinter.simpledialog as simpledialog
        trp_numero = simpledialog.askstring("Buscar TRP", "Ingrese el número de TRP que desea buscar:")

        if trp_numero:
            data_processor.buscar_rtriple_y_subrangos(trp_numero)

            rtriple = data_processor.get_rtriple()
            subrangos = data_processor.get_subrangos()

            if rtriple:
                print(f"\nValor Rtriple del TRP {trp_numero}: {rtriple[-1]}")
                temperature_calculator.rtriple = rtriple

            if subrangos:
                print("Subrangos disponibles:")
                for i, subrango in enumerate(subrangos):
                    print(f"({i + 1}) {subrango['nombre']}")

                seleccion = int(input("Seleccione el número del subrango que desea (0 para cancelar): "))

                if seleccion > 0 and seleccion <= len(subrangos):
                    parametros = subrangos[seleccion - 1].get('parametros', '').split(',')
                    valores = subrangos[seleccion - 1].get('valores', [])

                    parametros_seleccionados = {
                        parametro.strip(): float(valores[i]) if i < len(valores) else None
                        for i, parametro in enumerate(parametros)
                    }

                    temperature_calculator.parametros = parametros_seleccionados

                    temperature_calculator.registrar_promedio_rmedida(1.0)

                    temperatura = temperature_calculator.calcular_temperatura()
                    print(f"Temperatura calculada: {temperatura} °C")

                    temperature_calculator.guardar_temperatura()

    # Ejecutar en el thread principal
    buscar_trp_y_calcular()
    graph_controller.run()

if __name__ == "__main__":
    main()
