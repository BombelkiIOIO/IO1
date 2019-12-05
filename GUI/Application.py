from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

class MyWidget(GridLayout):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)


    def checkbox_change(self):
        self.ids.plot.clear_widgets()
        if self.ids.files_checkbox.active is True:
            plt.plot([1, 23, 2, 4])
            plt.ylabel('some numbers')
            self.ids.plot.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        if self.ids.functions_checkbox.active is True:
            plt.plot([1, 23, 2, 24])
            plt.ylabel('some numbers')
            self.ids.plot.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        if self.ids.modules_checkbox.active is True:
            plt.plot([15, 23, 2, 4])
            plt.ylabel('some numbers')
            self.ids.plot.add_widget(FigureCanvasKivyAgg(plt.gcf()))




class Gui(App):
    def build(self):
        return MyWidget()


if __name__ == "__main__":
    Gui().run()


