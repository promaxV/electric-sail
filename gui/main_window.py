import dearpygui.dearpygui as dpg

from callbacks import calculate_callback

def add_main_window():
    with dpg.window(label="Main", tag="window_main") as main_window:
        with dpg.table(header_row=False):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                with dpg.table_cell():
                    dpg.add_text("Введите число проводов:")
                    dpg.add_input_int(tag="input_wires_count", default_value=4, min_clamped=True, min_value=0)
                    dpg.add_text("Введите длину провода (в километрах):")
                    dpg.add_input_double(tag="input_wires_length", default_value=1, min_clamped=True, min_value=0)
                    dpg.add_text("Введите радиус провода (в микрометрах):")
                    dpg.add_input_double(tag="input_wires_radius", default_value=10, min_clamped=True, min_value=0)
                    dpg.add_text("Введите потенциал провода (в кВ):")
                    dpg.add_input_double(tag="input_wires_potential", default_value=20, min_clamped=True, min_value=0)
                    dpg.add_text("Введите массу корабля (в кг):")
                    dpg.add_input_double(tag="input_sc_mass", default_value=24, min_clamped=True, min_value=0)
                    
                with dpg.table_cell():
                    dpg.add_text("Введите плотность протонов солнечного ветра (в cm^-3):")
                    dpg.add_input_double(tag="input_sw_density", default_value=7.3, min_clamped=True, min_value=0)
                    dpg.add_text("Введите скорость солнечного ветра (в км/с):")
                    dpg.add_input_double(tag="input_sw_velocity", default_value=400,min_clamped=True, min_value=0)
                    
        dpg.add_button(label="Рассчитать", callback=calculate_callback)
        dpg.add_text(default_value="Удельная сила действующая на провод: ", tag="text_df_dz")
        dpg.add_text(default_value="Сила действующая на провод: ", tag="text_f_w")
        dpg.add_text(default_value="Сила действующая на корабль: ", tag="text_f_sc")
        dpg.add_text(default_value="Ускорение корабля: ", tag="text_ac_sc")
            
    dpg.set_primary_window(main_window, value=True)