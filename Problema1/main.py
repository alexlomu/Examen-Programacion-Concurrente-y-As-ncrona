from multiprocessing import Pool

# Creamos la clase cuenta
class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo
        self.saldo_inicial = saldo

    def hacer_movimiento(self, cantidad):
        self.saldo += cantidad

    def es_simulacion_correcta(self):
        return self.saldo == self.saldo_inicial

    def get_saldo(self):
        return self.saldo

# Creamos una función para hacer operaciones con las cuentas
def hacer_operaciones(cuenta, cantidad, num_ops):
    for _ in range(num_ops):
        cuenta.hacer_movimiento(cantidad)
        print(f"La cuenta tiene: {cuenta.get_saldo()}")
        

# Creamos el lanzador
if __name__ == '__main__':
    cuenta = Cuenta(100)

    num_ops_con_100 = 40
    num_ops_con_50 = 20
    num_ops_con_20 = 60

# Con el Pool y la función definida antes realizamos las operaciones
    with Pool() as p:
        p.starmap(hacer_operaciones, [(cuenta, 100, num_ops_con_100)])
        p.starmap(hacer_operaciones, [(cuenta, 50, num_ops_con_50)])
        p.starmap(hacer_operaciones, [(cuenta, 20, num_ops_con_20)])
        p.starmap(hacer_operaciones, [(cuenta, -100, num_ops_con_100)])
        p.starmap(hacer_operaciones, [(cuenta, -50, num_ops_con_50)])
        p.starmap(hacer_operaciones, [(cuenta, -20, num_ops_con_20)])

# Comprobamos si ha salido bien la simulación
    if cuenta.es_simulacion_correcta():
        print("La simulación fue correcta")
    else:
        print("La simulación falló")
        print(f"La cuenta tiene: {cuenta.get_saldo()}")
        print("Revise sus synchronized")
