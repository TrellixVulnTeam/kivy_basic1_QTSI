from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton


class DemoApp(MDApp):


    def build(self):
        screen = Screen()

        btn_flat = MDRectangleFlatButton(text="hello", pos_hint={'center_x':0.5, 'center_y': 0.5})

        icon_btn = MDIconButton(icon='format-wrap-tight', pos_hint={'center_x':0.5, 'center_y': 0.5})

        floating_btn = MDFloatingActionButton(icon='format-wrap-tight', pos_hint={'center_x':0.5, 'center_y': 0.5})

        screen.add_widget(floating_btn)

        return screen


if __name__ == '__main__':
    DemoApp().run()





