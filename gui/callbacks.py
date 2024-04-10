import dearpygui.dearpygui as dpg

from functions import es_calculate

def calculate_callback():
    wires_count = dpg.get_value("input_wires_count")
    wires_length = dpg.get_value("input_wires_length")
    wires_radius = 1e-6 *dpg.get_value("input_wires_radius")
    wires_potential = 1000 * dpg.get_value("input_wires_potential")
    sc_mass = dpg.get_value("input_sc_mass")
    sw_density = dpg.get_value("input_sw_density")
    sw_velocity = dpg.get_value("input_sw_velocity")
    
    df_dz, f_w, f_sc, ac_sc = es_calculate(wires_count, wires_length, wires_radius, wires_potential, sc_mass, sw_density, sw_velocity)
    
    dpg.set_value("text_df_dz", "Удельная сила действующая на провод: " + str(df_dz))
    dpg.set_value("text_f_w", "Сила действующая на провод: " + str(f_w))
    dpg.set_value("text_f_sc", "Сила действующая на корабль: " + str(f_sc))
    dpg.set_value("text_ac_sc", "Ускорение корабля: " + str(ac_sc))