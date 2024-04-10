import numpy as np

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
    
    under_exp = m_p * V**2 / (e * wire_potential) * np.log(r_0 / wire_radius)

    r_0 = 2/e * np.sqrt((eps_0 * T_e)/(n_0))
    df_dz = K * m_p * n_0 * V**2 * r_0 / (np.sqrt(np.exp(under_exp)) - 1)
    print("Удельная сила действующая на провод:", df_dz)
    print("Сила действующая на провод:", df_dz * wire_length)
    print("Сила действующая на корабль:", df_dz * wire_length * wires_cnt)
    print("Ускорение корабля:", df_dz * wire_length * wires_cnt / mass)


if __name__ == "__main__":
    main()
