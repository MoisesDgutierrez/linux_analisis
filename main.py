from kivy.uix.boxlayout import BoxLayout
from librerias.sysinfo import Sysinfo
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

class Linux_practice(App):
    def build(self):
        self.milibreria = Sysinfo()
        self.bl1 = BoxLayout(orientation="vertical")
        self.bl2 = BoxLayout(orientation="horizontal")
        self.lbl1 = Label(text="my linux analitics app")
        self.btn1 = Button(text="Sys info")
        self.btn2 = Button(text="temperatura")
        self.btn3 = Button(text="about me")
        self.lbl2 = Label(text=" ")
        self.bl2.add_widget(self.btn1)
        self.bl2.add_widget(self.btn2)
        self.bl2.add_widget(self.btn3)
        self.bl1.add_widget(self.lbl1)
        self.bl1.add_widget(self.bl2)
        self.bl1.add_widget(self.lbl2)
        self.btn1.bind(on_press=self.acciones_btn1)
        return self.bl1

    def acciones_btn1(self, *args):
        textoSalida = self.milibreria.fecha_hora() + "\n" + self.milibreria.operative_system() + "\n" + self.milibreria.host_name() self.lbl2.text = textoSalida
        

if __name__ == "__main__":
    Linux_practice().run()