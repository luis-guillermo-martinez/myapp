from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from utils.data_manager import DataManager
from utils.barcode_reader import read_barcode
import os

# Obtener la ruta absoluta del archivo CSV
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'assets', 'data', 'database.csv')

data_manager = DataManager(csv_path)

class MainScreen(Screen):
    pass

class SearchScreen(Screen):
    def search_item(self):
        search_query = self.ids.search_input.text
        search_by = 'barcode' if self.ids.search_by_barcode.active else 'name'
        result = data_manager.search_item(search_query, by=search_by)
        if not result.empty:
            self.ids.result_label.text = f"Precio: {result['precio'].values[0]}, Stock: {result['stock'].values[0]}"
        else:
            self.ids.result_label.text = "Artículo no encontrado"

class ModifyScreen(Screen):
    def modify_item(self):
        code = self.ids.barcode_input.text
        new_price = self.ids.price_input.text
        new_stock = self.ids.stock_input.text
        data_manager.modify_item(code, new_price, new_stock)
        self.ids.status_label.text = "Datos modificados y guardados"

class WindowManager(ScreenManager):
    pass

class MyApp(MDApp):
    def build(self):
        # Cargar el archivo .kv después de inicializar la aplicación
        kv = Builder.load_file("myapp.kv")
        return kv

if __name__ == "__main__":
    MyApp().run()
