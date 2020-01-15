from kivy.app import App
from kivy.lang import Builder

from GUI.root_widget import RootWidget


class Application(App):
    def build(self):
        self.title = "Dependency Tracker"
        return RootWidget()


if __name__ == "__main__":
    Builder.load_file('GUI/gui.kv')
    Application().run()


