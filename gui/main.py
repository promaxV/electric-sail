import dearpygui.dearpygui as dpg

from fonts import *
from main_window import *

dpg.create_context()
dpg.create_viewport(title="ESCC: Electric Sail Configuration Calculator", width=800, height=500)
dpg.setup_dearpygui()

add_fonts()

add_main_window()

dpg.show_viewport()

while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
    
dpg.destroy_context()