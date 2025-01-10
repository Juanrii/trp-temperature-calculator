class TemperatureCalculator:
    def __init__(self, parametros, rtriple):
        self.parametros = parametros
        self.rtriple = rtriple
        self.promedio_rmedida = 0
        self.temperatura_data = []
        self.contador_data = []

    @staticmethod
    def desvio(x, b):
        return x * (b - 1)

    def calcular_temperatura(self):
        if not self.rtriple:
            raise ValueError("El valor Rtriple no está definido.")

        B = [self.parametros.get(f"B{i}", 0) for i in range(len(self.parametros))]
        Rtw = self.rtriple[-1]
        a = self.parametros.get("a", 0)

        wt = self.promedio_rmedida / Rtw
        wf = self.desvio(a, wt)
        wr = wt - wf

        temperatura = 0
        for i in range(len(B)):
            temperatura += B[i] * (((wr - 2.64) / 1.64) ** i)

        temperatura_final = temperatura + B[0]

        self.contador_data.append(len(self.contador_data))
        self.temperatura_data.append(temperatura_final)

        return temperatura_final

    def registrar_promedio_rmedida(self, promedio):
        self.promedio_rmedida = promedio

    def guardar_temperatura(self, filepath='../data/valores_medidos.txt'):
        temperatura = self.temperatura_data[-1] if self.temperatura_data else None
        if temperatura is not None:
            with open(filepath, 'a') as f:
                f.write("Temperatura calculada: {:.3f} °C\n".format(temperatura))

    def obtener_datos_grafica(self):
        return self.contador_data, self.temperatura_data
