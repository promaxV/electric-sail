import numpy as np

from functions import es_calculate


K = 3.09
m_p = 1.67262192 *10e-27 #кг
n_0 = 7.3 #cm^-3
V = 400
e = 1.6 *10e-19
T_e = 12 # 1.5 * 10e5
eps_0 = 8.85 * 10e-12



def main():
    wires_cnt = int(input("Введите число проводов: "))
    wire_length = float(input("Введите длину провода(в километрах): "))
    wire_radius = 1e-6 * float(input("Введите радиус провода(в микрометрах): "))
    wire_potential = 1000 * float(input("Введите потенциал провода(в кВ): "))

    mass = float(input("Введите массу корабля (в кг): "))
    
    df_dz, f_w, f_sc, ac_sc = es_calculate(wires_cnt, wire_length, wire_radius, wire_potential, mass, n_0, V)
    
    print("Удельная сила действующая на провод:", df_dz)
    print("Сила действующая на провод:", f_w)
    print("Сила действующая на корабль:", f_sc)
    print("Ускорение корабля:", ac_sc)


if __name__ == "__main__":
    main()
