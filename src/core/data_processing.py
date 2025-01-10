import re
from tkinter import messagebox

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.rtriple = []
        self.subrangos = []

    def buscar_rtriple_y_subrangos(self, trp_numero):
        self.rtriple.clear()
        self.subrangos.clear()

        try:
            with open(self.file_path, 'r') as archivo:
                trp_encontrado = False
                subrango_info = None
                encontrado_rtriple = False

                for linea in archivo:
                    if f"..........TRP {trp_numero}:" in linea:
                        trp_encontrado = True
                        continue

                    if trp_encontrado and not encontrado_rtriple and "--------------------------------------------------------------------------------" in linea:
                        siguiente_linea = next(archivo).strip()
                        valor = re.match(r'[-+]?\d*\.\d+|\d+', siguiente_linea)
                        if valor:
                            self.rtriple.append(float(valor.group()))
                            encontrado_rtriple = True
                        continue

                    if trp_encontrado and "SubRango" in linea:
                        subrango_info = {'nombre': linea.strip()}
                        for siguiente_linea in archivo:
                            siguiente_linea = siguiente_linea.strip()
                            if "Puntos de calibracion:" in siguiente_linea:
                                subrango_info['calibracion'] = siguiente_linea.replace("Puntos de calibracion:", "").strip()
                            elif "Parametros:" in siguiente_linea:
                                subrango_info['parametros'] = siguiente_linea.replace("Parametros:", "").strip()
                            elif "Ecuacion" in siguiente_linea:
                                subrango_info['ecuacion'] = siguiente_linea.strip()
                            elif "--------------------------------------------------------------------------------" in siguiente_linea:
                                siguiente_linea = next(archivo).strip()
                                numeros = re.findall(r'[-+]?\d*\.\d+|\d+', siguiente_linea)
                                if numeros:
                                    subrango_info['valores'] = numeros
                                break

                        if subrango_info:
                            self.subrangos.append(subrango_info)

                    if trp_encontrado and "..........TRP" in linea and f"..........TRP {trp_numero}:" not in linea:
                        break

            if not self.rtriple:
                messagebox.showinfo("Sin resultados", f"No se encontró valor Rtriple para el TRP {trp_numero}.")
            if not self.subrangos:
                messagebox.showinfo("Sin resultados", f"No se encontraron subrangos para el TRP {trp_numero}.")

        except FileNotFoundError:
            messagebox.showerror("Error", f"No se encontró el archivo '{self.file_path}'.")
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error: {e}")

    def get_rtriple(self):
        return self.rtriple

    def get_subrangos(self):
        return self.subrangos
