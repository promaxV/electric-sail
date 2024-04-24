import dearpygui.dearpygui as dpg

from functions import es_calculate
import pandas as pd
import numpy as np

def calculate_callback():
    input_type = dpg.get_value("input_type")

    if input_type == 'Manual':
        wires_count = dpg.get_value("input_wires_count")
        wires_length = dpg.get_value("input_wires_length")
        wires_radius = 1e-3 *dpg.get_value("input_wires_radius") / 2
        wires_material_density = dpg.get_value("input_wires_material_density")
        wires_potential = 1000 * dpg.get_value("input_wires_potential")
        sc_mass = dpg.get_value("input_sc_mass")
        sw_density = dpg.get_value("input_sw_density")
        sw_velocity = dpg.get_value("input_sw_velocity")

        df_dz, f_w, f_sc, ac_sc = es_calculate(wires_count, wires_length, wires_radius, wires_potential, sc_mass, wires_material_density, sw_density, sw_velocity)

        dpg.set_value("text_df_dz", "Погонная сила, Н/м: " + str(round(df_dz,2)))
        dpg.set_value("text_f_w", "Сила действующая на провод, Н: " + str(round(f_w,2)))
        dpg.set_value("text_f_sc", "Сила действующая на корабль, Н: " + str(round(f_sc,2)))
        dpg.set_value("text_ac_sc", "Тяговое ускорение, м/c^2: " + str(round(ac_sc,2)))

    elif input_type == 'File':
        file_name = dpg.get_value('input_file_path')
        data = pd.read_csv('./' + file_name)

        data['input_wires_radius'] = 1e-3 * data['input_wires_radius'] /2
        data['input_wires_potential'] = 1000 * data['input_wires_potential']

        
        data_values = data.values
        output_values = es_calculate(data_values[:,0], data_values[:,1], data_values[:,2], 
                                     data_values[:,3],data_values[:,4], data_values[:,5], data_values[:,6])
        output_values = np.round(np.array(output_values).T, 2)

        output = pd.DataFrame(columns=['Погонная сила Н/м', 'Сила действующая на провод Н', 'Сила действующая на корабль Н', 'Тяговое ускорение м/c^2'], 
                              data = output_values)

        
        output.to_csv('output.csv', index = False)