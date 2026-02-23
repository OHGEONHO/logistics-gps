# main.py
from kivy.app import App
from kivy.uix.label import Label
from plyer import gps

class TestApp(App):
    def build(self):
        return Label(text="GPS 앱 테스트 시작!")

    def on_start(self):
        try:
            gps.configure(on_location=self.print_location)
            gps.start()
        except:
            pass

    def print_location(self, **kwargs):
        print(f"위치 수신: {kwargs}")

if __name__ == '__main__':
    TestApp().run()