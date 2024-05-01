import numpy as np

K = 3.09
M_P = 1.67262192 *10e-27 #кг
E = 1.6 *10e-19
T_E = 12 # 1.5 * 10e5
EPS_0 = 8.85 * 10e-12


def es_calculate(wires_count: int, 
                 wires_length: float, 
                 wires_radius: float, 
                 wires_potential: float, 
                 sc_mass: float,
                 wire_material_density: float,
                 sw_density: float,
                 sw_velocity:float) -> tuple[float]:
    """Calculates unit force, force per wire, total force and
        total acceleration by electric sail configuration."""
        
    r_0 = 2/E * np.sqrt((EPS_0 * T_E)/(sw_density))
    under_exp = M_P * sw_velocity**2 / (E * wires_potential) * np.log(r_0 / wires_radius)
    df_dz = K * M_P * sw_density * sw_velocity**2 * r_0 / (np.sqrt(np.exp(under_exp)) - 1)
    
    wires_mass = 1000*wires_length*np.pi*wires_radius**2 * wire_material_density * wires_count
    
    print(wires_mass/(wires_mass+sc_mass))
    
    return df_dz, df_dz * wires_length, df_dz * wires_length * wires_count, df_dz * wires_length * wires_count / (sc_mass + wires_mass)