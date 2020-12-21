from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, ThreeLineListItem, ThreeLineIconListItem
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget

from kivy.uix.scrollview import ScrollView


class DemoApp(MDApp):

    def build(self):
        screen = Screen()

        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        for i in range(20):
            # icon = IconLeftWidget(icon='android')
            image = ImageLeftWidget(source='my.jpg')
            items = ThreeLineIconListItem(text=f'Item {str(i)}', secondary_text='hello wold',
                                          tertiary_text='Thertiary text')

            # items.add_widget(icon)
            items.add_widget(image)
            list_view.add_widget(items)

        screen.add_widget(scroll)

        return screen


if __name__ == '__main__':
    DemoApp().run()





