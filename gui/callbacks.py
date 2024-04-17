import dearpygui.dearpygui as dpg

from functions import es_calculate
import pandas as pd
import numpy as np

def calculate_callback():
    input_type = dpg.get_value("input_type")

    if input_type == 'Manual':
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

    elif input_type == 'File':
        file_name = dpg.get_value('input_file_path')
        data = pd.read_csv('./' + file_name)

        data['input_wires_radius'] = 1e-6 * data['input_wires_radius']
        data['input_wires_potential'] = 1000 * data['input_wires_potential']

        
        data_values = data.values
        output_values = es_calculate(data_values[:,0], data_values[:,1], data_values[:,2], 
                                     data_values[:,3],data_values[:,4], data_values[:,5], data_values[:,6])
        output_values = np.array(output_values).T

        output = pd.DataFrame(columns=['Удельная сила действующая на провод', 'Сила действующая на провод', 'Сила действующая на корабль', 'Ускорение корабля'], 
                              data = output_values)

        
        output.to_csv('output.csv', index = False)