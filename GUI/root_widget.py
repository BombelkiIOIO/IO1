from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

from matplotlib import style
from matplotlib import pyplot as plt
from matplotlib import use as mpl_use

mpl_use('module://kivy.garden.matplotlib.backend_kivy')
style.use('dark_background')


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class RootWidget(NavigationDrawer):
    loadfile = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

    def checkbox_change(self):

        self.ids.plots.clear_widgets()

        if self.ids.files_checkbox.active is True:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot([1, 23, 2, 4])
            self.ids.plots.add_widget(fig.canvas)

        if self.ids.functions_checkbox.active is True:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot([45, 32, 2, 4])
            self.ids.plots.add_widget(fig.canvas)
        if self.ids.modules_checkbox.active is True:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot([45, 554, 2, 1111])
            self.ids.plots.add_widget(fig.canvas)

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        print(path)
        print(filename)
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()
