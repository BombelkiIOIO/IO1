import pathlib

from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

from matplotlib import style
from matplotlib import pyplot as plt
from matplotlib import use as mpl_use

from data import graphs
from objects import module, project

mpl_use('module://kivy.garden.matplotlib.backend_kivy')
style.use('dark_background')


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class RootWidget(NavigationDrawer):
    loadfile = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.ids.image.source = str(pathlib.Path(__file__).parent.absolute()) + "/hamburger.png"
        self.proj = None
        self.fig_modules = None
        self.fig_files = None
        self.fig_function = None


    def modules_graph(self):
        if self.ids.modules_checkbox.active is True:
            self.ids.plots.add_widget(self.fig_modules.canvas)

        if self.ids.modules_checkbox.active is False:
            self.ids.plots.remove_widget(self.fig_modules.canvas)

    def functions_graph(self):
        if self.ids.functions_checkbox.active is True:
            self.ids.plots.add_widget(self.fig_function.canvas)

        if self.ids.functions_checkbox.active is False:
            self.ids.plots.remove_widget(self.fig_function.canvas)

    def files_graph(self):
        if self.ids.files_checkbox.active is True:
            self.ids.plots.add_widget(self.fig_files.canvas)

        if self.ids.files_checkbox.active is False:
            self.ids.plots.remove_widget(self.fig_files.canvas)

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, dir_root_path):

        print(dir_root_path)
        self.proj = project.Project("elo", dir_root_path[0])
        self.fig_modules = graphs.draw_modules_graph(self.proj)
        self.fig_files = graphs.draw_files_graph(self.proj)
        self.fig_function = graphs.draw_modules_graph(self.proj)
        self.ids.files_checkbox.disabled = False
        self.ids.modules_checkbox.disabled = False
        self.ids.functions_checkbox.disabled = False
        self.toggle_state()
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()
