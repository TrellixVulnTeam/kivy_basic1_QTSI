from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import ImageLeftWidget


list_helper = """
Screen: 
    ScrollView:
        MDList:
            id: container     
"""


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper)
        return screen

    def on_start(self):
        for i in range(20):
            items = OneLineListItem(text=f'Item {str(i)}')
            self.root.ids.container.add_widget(items)


if __name__ == '__main__':
    DemoApp().run()





