from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton


class DemoApp(MDApp):
    def build(self):
        screen = Screen()

        label = MDLabel(text='hello', halign='center', theme_text_color='Custom',
                        text_color=(190 / 255, 19 / 255, 148 / 255, 1),
                        font_style='Caption')
        icon_label = MDIcon(icon='flash-red-eye', pos_hint={'center_x': 0.5})
        return label


if __name__ == '__main__':
    DemoApp().run()





