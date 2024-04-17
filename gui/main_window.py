import dearpygui.dearpygui as dpg
from callbacks import calculate_callback

def add_main_window():
    # Callback to handle dropdown menu change
    def dropdown_callback(sender, data):
        if data == "Manual":
            # Show all elements for manual input
            dpg.configure_item("input_wires_count", show=True)
            dpg.configure_item("input_wires_count_text", show=True)

            dpg.configure_item("input_wires_length", show=True)
            dpg.configure_item("input_wires_length_text", show=True)

            dpg.configure_item("input_wires_radius", show=True)
            dpg.configure_item("input_wires_radius_text", show=True)

            dpg.configure_item("input_wires_potential", show=True)
            dpg.configure_item("input_wires_potential_text", show=True)

            dpg.configure_item("input_sc_mass", show=True)
            dpg.configure_item("input_sc_mass_text", show=True)

            dpg.configure_item("input_sw_density", show=True)
            dpg.configure_item("input_sw_density_text", show=True)

            dpg.configure_item("input_sw_velocity", show=True)
            dpg.configure_item("input_sw_velocity_text", show=True)

            dpg.configure_item("input_file_path", show=False)
            dpg.configure_item("input_file_path_text", show=False)

        elif data == "File":
            # Show only the string input element for file input
            dpg.configure_item("input_wires_count", show=False)
            dpg.configure_item("input_wires_count_text", show=False)

            dpg.configure_item("input_wires_length", show=False)
            dpg.configure_item("input_wires_length_text", show=False)

            dpg.configure_item("input_wires_radius", show=False)
            dpg.configure_item("input_wires_radius_text", show=False)

            dpg.configure_item("input_wires_potential", show=False)
            dpg.configure_item("input_wires_potential_text", show=False)

            dpg.configure_item("input_sc_mass", show=False)
            dpg.configure_item("input_sc_mass_text", show=False)

            dpg.configure_item("input_sw_density", show=False)
            dpg.configure_item("input_sw_density_text", show=False)

            dpg.configure_item("input_sw_velocity", show=False)
            dpg.configure_item("input_sw_velocity_text", show=False)

            dpg.configure_item("input_file_path", show=True)
            dpg.configure_item("input_file_path_text", show=True)

    with dpg.window(label="Main", tag="window_main") as main_window:
        # Add dropdown menu
        dpg.add_combo(items=["Manual", "File"], callback=dropdown_callback, default_value="Manual", tag = 'input_type')

        # Elements for manual input
        with dpg.table(header_row=False):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                with dpg.table_cell():
                    dpg.add_text("Число проводов:", tag='input_wires_count_text')
                    dpg.add_input_int(tag="input_wires_count", default_value=4, min_clamped=True, min_value=0)

                    dpg.add_text("Длина провода, км:", tag = 'input_wires_length_text')
                    dpg.add_input_double(tag="input_wires_length", default_value=1, min_clamped=True, min_value=0, format = '%.1f')

                    dpg.add_text("Диаметр провода, мм:", tag = 'input_wires_radius_text')
                    dpg.add_input_double(tag="input_wires_radius", default_value=0.1, min_clamped=True, min_value=0, format = '%.1f')

                    dpg.add_text("Потенциал провода, кВ:", tag = 'input_wires_potential_text')
                    dpg.add_input_double(tag="input_wires_potential", default_value=20, min_clamped=True, min_value=0, format = '%.1f')

                    dpg.add_text("Масса корабля, кг:", tag = 'input_sc_mass_text')
                    dpg.add_input_double(tag="input_sc_mass", default_value=24, min_clamped=True, min_value=0, format = '%.1f')

                with dpg.table_cell():
                    dpg.add_text("Плотность протонов солнечного ветра, cm^-3:", tag = 'input_sw_density_text')
                    dpg.add_input_double(tag="input_sw_density", default_value=7.3, min_clamped=True, min_value=0, format = '%.1f')

                    dpg.add_text("Скорость солнечного ветра, км/с:", tag = 'input_sw_velocity_text')
                    dpg.add_input_double(tag="input_sw_velocity", default_value=400, min_clamped=True, min_value=0, format = '%.1f')

        # Element for file input
        dpg.add_text("Название файла:", tag ='input_file_path_text', show = False)
        dpg.add_input_text(tag="input_file_path", default_value= 'input.csv', show = False)







        dpg.add_button(label="Рассчитать", callback=calculate_callback)
        dpg.add_text(default_value="Погонная сила, Н/м: ", tag="text_df_dz")
        dpg.add_text(default_value="Сила действующая на провод, Н: ", tag="text_f_w")
        dpg.add_text(default_value="Сила действующая на корабль, Н: ", tag="text_f_sc")
        dpg.add_text(default_value="Тяговое ускорение, м/c^2: ", tag="text_ac_sc")

    dpg.set_primary_window(main_window, value=True)

                        
