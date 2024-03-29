from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

class DemoApp(MDApp):


    def build(self):
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text="hello", pos_hint={'center_x':0.5, 'center_y': 0.5})
        screen.add_widget(btn_flat)
        return screen


if __name__ == '__main__':
    DemoApp().run()





