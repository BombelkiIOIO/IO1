from kivy.app import App
from kivy.lang import Builder

from GUI import root_widget


class Application(App):
    def build(self):
        self.title = "Dependency Tracker"
        return root_widget.RootWidget()


if __name__ == "__main__":
    Builder.load_file('GUI/gui.kv')
    Application().run()


