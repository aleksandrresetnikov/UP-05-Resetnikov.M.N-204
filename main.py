from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text="Введите текст и нажмите кнопку")
        self.text_input = TextInput(hint_text="Введите что-то")
        button = Button(text="Нажми меня")

        button.bind(on_press=self.on_button_press)

        layout.add_widget(self.label)
        layout.add_widget(self.text_input)
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        self.label.text = f"Вы ввели: {self.text_input.text}"


if __name__ == "__main__":
    MyApp().run()