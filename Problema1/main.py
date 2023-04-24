from multiprocessing import Pool

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

def hacer_operaciones(cuenta, cantidad, num_ops):
    for _ in range(num_ops):
        cuenta.hacer_movimiento(cantidad)

if __name__ == '__main__':
    cuenta = Cuenta(100)

    num_ops_con_100 = 40
    num_ops_con_50 = 20
    num_ops_con_20 = 60

    with Pool() as p:
        p.starmap(hacer_operaciones, [(cuenta, 100, num_ops_con_100)] * 2)
        p.starmap(hacer_operaciones, [(cuenta, -100, num_ops_con_100)] * 2)
        p.starmap(hacer_operaciones, [(cuenta, 50, num_ops_con_50)] * 2)
        p.starmap(hacer_operaciones, [(cuenta, -50, num_ops_con_50)] * 2)
        p.starmap(hacer_operaciones, [(cuenta, 20, num_ops_con_20)] * 2)
        p.starmap(hacer_operaciones, [(cuenta, -20, num_ops_con_20)] * 2)

    if cuenta.es_simulacion_correcta():
        print("La simulación fue correcta")
    else:
        print("La simulación falló")
        print(f"La cuenta tiene: {cuenta.get_saldo()}")
        print("Revise sus synchronized")
