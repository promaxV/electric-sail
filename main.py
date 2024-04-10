import numpy as np

# Константы
K = 3.09 * 1e12  # Коэффициент, связанный с электрическим полем
M_P = 1.67262192e-27  # Масса протона, kg
N_0 = 12.4 * 10e-3  # Плотность солнечного ветра, km^-3
V = 576  # Скорость солнечного ветра, km/s
R_0 = 0.02  # Радиус электронного паруса, km
E = 1.6e-19  # Заряд электрона, K

def main():
    # Ввод данных
    wires_cnt = int(input("Введите число проводов: "))
    wire_length = float(input("Введите длину провода(в километрах): "))
    wire_radius = 1e-6 * float(input("Введите радиус провода(в миллиметрах): "))
    wire_potential = 1000 * float(input("Введите потенциал провода(в кВ): "))
    mass = float(input("Введите массу корабля (в кг): "))

    # Расчет удельной силы на провод
    under_exp = M_P * V**2 / (E * wire_potential) * np.log(R_0 / wire_radius)
    df_dz = 1000 * K * M_P * N_0 * V**2 * R_0 / (np.sqrt(np.exp(under_exp)) - 1)

    # Вывод результатов
    print("Удельная сила действующая на провод:", df_dz)
    print("Сила действующая на провод:", df_dz * wire_length)
    print("Сила действующая на корабль:", df_dz * wire_length * wires_cnt)
    print("Ускорение корабля:", df_dz * wire_length * wires_cnt / mass)

if __name__ == "__main__":
    main()
