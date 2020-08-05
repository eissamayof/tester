from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
class MyClass1(Widget):
    pass


class MyClass(BoxLayout):

    def __init__(self, **kwargs):
        super(MyClass, self).__init__(**kwargs)
        self.rows = 4
        self.cols = 4
        self.size_hint = 1, 1
        self.padding = 10
        self.background_color = [0,4,3,3]
        button = Button(text='hello1  ', font_size=15, size_hint=(.1, .1), pos_hint={'x': .2, 'y': .2})
        self.add_widget(button)


        self.layout2 = FloatLayout()
        self.layout2.add_widget(Label(text='allah akber',pos_hint={'x': .2, 'y': .2}))
        self.layout2.add_widget(CheckBox(pos_hint={'x': .35, 'y': .2}))
        self.add_widget(self.layout2)
        self.layout2.add_widget(Button(size_hint=(.3,.3),text='ACMILAN',pos_hint={'x': .35, 'y': .2}))


        ahmed = CheckBox()
        self.add_widget(ahmed)


        button1 = Button(text='hello2  ', font_size=15, size_hint=(.1, .1), pos_hint={'x': .2, 'y': .1})
        self.add_widget(button1)


        button2 = Button(text='hello3  ', font_size=15, size_hint=(.1, .1))
        self.add_widget(button2)

        self.layout1 = GridLayout(rows=4, size_hint_y=None, pos_hint={'x': .3, 'y': .6})
        self.layout1.add_widget(Label(text='Iw:'))
        self.layout1.add_widget(Button(text='Is:'))
        self.layout1.add_widget(Label(text='Ir:'))
        self.layout1.add_widget(TextInput(width=Window.size[0] * 0.4,size_hint_x=None, multiline=False))

        self.add_widget(self.layout1)




        self.layout3 = GridLayout(rows=4, size_hint_y=None)
        self.layout3.add_widget(Label(text='cr7:'))
        self.layout3.add_widget(Button(text='messi:'))
        self.layout3.add_widget(Label(text='kaka'))
        self.layout3.add_widget(Button(text='nymar'))

        self.add_widget(self.layout3)


        self.layout4 = FloatLayout()

        self.layout4.add_widget(Label(text=' this is us  ', font_size=15, size_hint=(.2, .2), pos_hint={'x': .2, 'y': .1} ,color=[0,4,3,3]))

        self.add_widget(self.layout4)


        





class ClassName2(App):

    # noinspection PyUnreachableCode
    def build(self):
        return MyClass()
        return MyClass2()


if __name__ == '__main__':
    myapp = ClassName2()
    myapp.run()
