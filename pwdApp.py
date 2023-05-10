# Import data libraries
import pandas as pd
import numpy as np
import random

# Import UI library
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Password Generation; dictionary loading
with open('dizionarioIta.txt', 'r') as file:
    lines = file.readlines()

# Remove newline character
def noNL(s):
    return s[:-1]

def pwdGen():
    # Convert the list into a DataFrame
    diz = pd.DataFrame({'word': lines})
    diz['word'] = diz['word'].apply(noNL).str.title()

    # Select 4 words randomly, and chain them together
    wordsList = diz['word'].sample(n=4)
    pwd = wordsList.str.cat(sep='')
    return pwd

#diz
#wordsList
#pwd

# App Layout
class pwdApp(App):
    def build(self):
        root_widget = BoxLayout(orientation = 'vertical')
        
        title_label = Label(
            font_size = 100,
            bold = True,
            italic = True,
            markup = True,
            text = '[color=#ff0000]Generate your password![/color]')
        
        self.label = Label(
            text='',
            font_size = 70,
            bold = True,
            )

        gen_button = Button(
            text = 'Generate',
            height = 100,
            size_hint_y = None
        )
        gen_button.bind(on_press=self.update_label_text)

        root_widget.add_widget(title_label)
        root_widget.add_widget(self.label)
        root_widget.add_widget(gen_button)
        return root_widget
    
    def update_label_text(self, instance):
        self.label.text = pwdGen()

if __name__ == "__main__":
    pwdApp().run()