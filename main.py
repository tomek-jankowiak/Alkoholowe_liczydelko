from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import ScreenManager, Screen
from liczenie import Licznik
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')


class SexSlider(FloatLayout):
    def __init__(self, body_parameters, **kwargs):
        super(SexSlider, self).__init__(**kwargs)
        y_pos = .92
        self.sex_slider = Slider(min=0,
                                 max=1,
                                 value=0,
                                 step=1,
                                 size_hint=(.18, .1),
                                 pos_hint={'center_x': .5, 'center_y': y_pos})

        self.sex_text = Label(text="Płeć",
                              size_hint=(.3, .1),
                              pos_hint={'center_x': .2, 'center_y': y_pos})
        self.sex1 = Label(text="Mężczyzna",
                          size_hint=(.3, .1),
                          pos_hint={'center_x': .35, 'center_y': y_pos})
        self.sex2 = Label(text="Kobieta",
                          size_hint=(.3, .1),
                          pos_hint={'center_x': .65, 'center_y': y_pos})
        self.sex_slider.bind(value=self.on_value)

        self.add_widget(self.sex_text)
        self.add_widget(self.sex_slider)
        self.add_widget(self.sex1)
        self.add_widget(self.sex2)

        body_parameters[0] = self.sex_slider.value

    def on_value(self, instance, sex):
        param1.body_parameters[0] = sex


class AgeSlider(FloatLayout):
    def __init__(self, body_parameters, **kwargs):
        super(AgeSlider, self).__init__(**kwargs)
        y_pos = .82
        self.gramarr = " lat"
        self.age_slider = Slider(min=18,
                                 max=100,
                                 value=30,
                                 step=1,
                                 size_hint=(.5, .1),
                                 pos_hint={'center_x': .5, 'center_y': y_pos})

        self.age_text = Label(text="Wiek",
                              size_hint=(.3, .1),
                              pos_hint={'center_x': .2, 'center_y': y_pos})

        self.age_value = Label(text=str(self.age_slider.value) + self.gramarr,
                               size_hint=(.3, .1),
                               pos_hint={'center_x': .8, 'center_y': y_pos})
        self.age_slider.bind(value=self.on_value)

        self.add_widget(self.age_text)
        self.add_widget(self.age_slider)
        self.add_widget(self.age_value)

        body_parameters[1] = self.age_slider.value

    def on_value(self, instance, age):
        if age%10 in [2, 3, 4]:
            self.gramarr = " lata"
        else:
            self.gramarr = " lat"
        param1.body_parameters[1] = age
        self.age_value.text = str(age) + self.gramarr


class WeightSlider(FloatLayout):
    def __init__(self, body_parameters, **kwargs):
        super(WeightSlider, self).__init__(**kwargs)
        y_pos = .72
        self.weight_slider = Slider(min=40,
                                    max=200,
                                    value=60,
                                    step=1,
                                    size_hint=(.5, .1),
                                    pos_hint={'center_x': .5, 'center_y': y_pos})

        self.weight_text = Label(text="Waga",
                                 size_hint=(.3, .1),
                                 pos_hint={'center_x': .2, 'center_y': y_pos})

        self.weight_value = Label(text=str(self.weight_slider.value) + " kg",
                                  size_hint=(.3, .1),
                                  pos_hint={'center_x': .8, 'center_y': y_pos})
        self.weight_slider.bind(value=self.on_value)

        self.add_widget(self.weight_text)
        self.add_widget(self.weight_slider)
        self.add_widget(self.weight_value)

        body_parameters[2] = self.weight_slider.value

    def on_value(self, instance, weight):
        param1.body_parameters[2] = weight
        self.weight_value.text = "%d" % weight


class HeightSlider(FloatLayout):
    def __init__(self, body_parameters, **kwargs):
        super(HeightSlider, self).__init__(**kwargs)
        y_pos = .62
        self.height_slider = Slider(min=120,
                                    max=230,
                                    value=170,
                                    step=1,
                                    size_hint=(.5, .1),
                                    pos_hint={'center_x': .5, 'center_y': y_pos})

        self.height_text = Label(text="Wzrost",
                                 size_hint=(.3, .1),
                                 pos_hint={'center_x': .2, 'center_y': y_pos})

        self.height_value = Label(text=str(self.height_slider.value) + " cm",
                                  size_hint=(.3, .1),
                                  pos_hint={'center_x': .8, 'center_y': y_pos})
        self.height_slider.bind(value=self.on_value)

        self.add_widget(self.height_text)
        self.add_widget(self.height_slider)
        self.add_widget(self.height_value)

        body_parameters[3] = self.height_slider.value

    def on_value(self, instance, height):
        param1.body_parameters[3] = height
        self.height_value.text = "%d" % height


class FoodSlider(FloatLayout):
    def __init__(self, body_parameters, **kwargs):
        super(FoodSlider, self).__init__(**kwargs)
        y_pos = .47
        self.food_text = Label(text="Podczas spożycia alkoholu jadłeś:",
                               size_hint=(.3, .1),
                               pos_hint={'center_x': .5, 'center_y': y_pos + 0.05})
        self.food_slider = Slider(min=0,
                                  max=2,
                                  value=1,
                                  step=1,
                                  size_hint=(.5, .1),
                                  pos_hint={'center_x': .5, 'center_y': y_pos})
        self.food_option0 = Label(text="mało/wcale",
                                  size_hint=(.3, .1),
                                  pos_hint={'center_x': .28, 'center_y': y_pos - 0.05})
        self.food_option1 = Label(text="normalnie",
                                  size_hint=(.3, .1),
                                  pos_hint={'center_x': .5, 'center_y': y_pos - 0.05})
        self.food_option2 = Label(text="dużo",
                                  size_hint=(.3, .1),
                                  pos_hint={'center_x': .72, 'center_y': y_pos - 0.05})
        self.food_slider.bind(value=self.on_value)

        self.add_widget(self.food_text)
        self.add_widget(self.food_slider)
        self.add_widget(self.food_option0)
        self.add_widget(self.food_option1)
        self.add_widget(self.food_option2)

        body_parameters[4] = self.food_slider.value

    def on_value(self, instance, food):
        param1.body_parameters[4] = food


class MetabolismSlider(FloatLayout):
    def __init__(self, body_parameters, **kwargs):
        super(MetabolismSlider, self).__init__(**kwargs)
        y_pos = .27
        self.metabolism_text = Label(text="Z doświadczenia wiesz, że alkohol spalasz:",
                                     size_hint=(.3, .1),
                                     pos_hint={'center_x': .5, 'center_y': y_pos + 0.05})
        self.metabolism_slider = Slider(min=0,
                                        max=4,
                                        value=2,
                                        step=1,
                                        size_hint=(.75, .1),
                                        pos_hint={'center_x': .5, 'center_y': y_pos})
        self.metabolism_option0 = Label(text="bardzo wolno",
                                        size_hint=(.3, .1),
                                        pos_hint={'center_x': .15, 'center_y': y_pos - 0.05})
        self.metabolism_option1 = Label(text="wolno",
                                        size_hint=(.3, .1),
                                        pos_hint={'center_x': .325, 'center_y': y_pos - 0.05})
        self.metabolism_option2 = Label(text="normalnie",
                                        size_hint=(.3, .1),
                                        pos_hint={'center_x': .5, 'center_y': y_pos - 0.05})
        self.metabolism_option3 = Label(text="szybko",
                                        size_hint=(.3, .1),
                                        pos_hint={'center_x': .675, 'center_y': y_pos - 0.05})
        self.metabolism_option4 = Label(text="bardzo szybko",
                                        size_hint=(.3, .1),
                                        pos_hint={'center_x': .85, 'center_y': y_pos - 0.05})
        self.metabolism_slider.bind(value=self.on_value)

        self.add_widget(self.metabolism_text)
        self.add_widget(self.metabolism_slider)
        self.add_widget(self.metabolism_option0)
        self.add_widget(self.metabolism_option1)
        self.add_widget(self.metabolism_option2)
        self.add_widget(self.metabolism_option3)
        self.add_widget(self.metabolism_option4)

        body_parameters[5] = self.metabolism_slider.value

    def on_value(self, instance, metabolism):
        param1.body_parameters[5] = metabolism


class Alcohol(FloatLayout):
    def __init__(self, name, volume, num, **kwargs):
        super(Alcohol, self).__init__(**kwargs)
        self.amount = 0
        self.volume = volume
        self.alcohol_name = Label(text=str(name),
                                  size_hint=(.4, .1),
                                  pos_hint={'center_x': .2, 'center_y': (.8 - num/15)})
        self.alcohol_minusbutton = Button(text="-",
                                          size_hint=(.05, .05),
                                          pos_hint={'center_x': .625, 'center_y': (.8 - num/15)})
        self.alcohol_plusbutton = Button(text='+',
                                         size_hint=(.05, .05),
                                         pos_hint={'center_x': .675, 'center_y': (.8 - num/15)})
        self.alcohol_value = Label(text=str(self.amount),
                                   size_hint=(.1, .1),
                                   pos_hint={'center_x': .8, 'center_y': (.8 - num/15)})
        self.alcohol_plusbutton.bind(on_press=self.on_press_plusbutton)
        self.alcohol_minusbutton.bind(on_press=self.on_press_minusbutton)

        self.add_widget(self.alcohol_name)
        self.add_widget(self.alcohol_plusbutton)
        self.add_widget(self.alcohol_minusbutton)
        self.add_widget(self.alcohol_value)

    def on_press_plusbutton(self, instance):
        self.amount = self.amount + 1
        self.alcohol_value.text = str(self.amount)

    def on_press_minusbutton(self, instance):
        if self.amount > 0:
            self.amount = self.amount - 1
            self.alcohol_value.text = str(self.amount)


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        screen_layout = FloatLayout()

        title = Label(text="Alkoholowe Liczydełko",
                      font_size=55,
                      size_hint=(.7, .2),
                      pos_hint={'center_x': .5, 'center_y': .7})
        screen_layout.add_widget(title)

        next_button = Button(text="START",
                             size_hint=(.3, .1),
                             pos_hint={'center_x': .5, 'center_y': .3})
        next_button.bind(on_press=self.on_press_button)
        screen_layout.add_widget(next_button)

        self.add_widget(screen_layout)

    def on_press_button(self, instance):
        sm.transition.direction = 'left'
        sm.current = 'param1'


class ParameterScreen1(Screen):
    def __init__(self, **kwargs):
        super(ParameterScreen1, self).__init__(**kwargs)
        screen_layout = FloatLayout()
        # parametry:
        # 0 - sex, 1 - age, 2 - weight, 3 - height, 4 - food, 5 - metabolism
        self.body_parameters = [0, 0, 0, 0, 0, 0]

        screen_layout.add_widget(SexSlider(self.body_parameters))
        screen_layout.add_widget(AgeSlider(self.body_parameters))
        screen_layout.add_widget(WeightSlider(self.body_parameters))
        screen_layout.add_widget(HeightSlider(self.body_parameters))
        screen_layout.add_widget(MetabolismSlider(self.body_parameters))
        screen_layout.add_widget(FoodSlider(self.body_parameters))

        next_button = Button(text='Następny krok',
                             size_hint=(.3, .1),
                             pos_hint={'center_x': .5, 'center_y': .1})
        next_button.bind(on_press=self.on_press_button)
        screen_layout.add_widget(next_button)

        self.add_widget(screen_layout)

    def on_press_button(self, instance):
        sm.transition.direction = 'left'
        sm.current = 'param2'


class ParameterScreen2(Screen):
    def __init__(self, **kwargs):
        super(ParameterScreen2, self).__init__(**kwargs)
        screen_layout = FloatLayout()
        names = ["małe piwo(5%, 330ml)", "duże piwo(5%, 500ml)", "kieliszek wina(12%, 150ml)",
                 "mocny alkohol(40%, 50ml)"]
        volumes = [330, 500, 150, 50]
        self.alcohols = []
        # wypite, w każdej podliście: 0 - procent, 1 - ilość
        self.drunk = [[5.0, 0], [5.0, 0], [12.0, 0], [40.0, 0]]
        self.time = 0.0

        for i in range(len(names)):
            self.alcohols.append(Alcohol(names[i], volumes[i], i))
            screen_layout.add_widget(self.alcohols[i])

        self.another_label = Label(text="Inne:",
                                   size_hint=(.4, .1),
                                   pos_hint={'center_x': .2, 'center_y': .53})
        self.another_percent = TextInput(text='',
                                         hint_text="Procent alkoholu",
                                         multiline=False,
                                         size_hint=(.2, .06),
                                         pos_hint={'center_x': .5, 'center_y': .53})
        self.another_amount = TextInput(text='',
                                        hint_text="Ilość [ml]",
                                        multiline=False,
                                        size_hint=(.2, .06),
                                        pos_hint={'center_x': .7, 'center_y': .53})

        self.time_label = Label(text="Czas spożywania alkoholu (w godzinach):",
                                size_hint=(.3, .1),
                                pos_hint={'center_x': .25, 'center_y': .4})
        self.time_value = Label(text=str(self.time),
                                size_hint=(.3, .1),
                                pos_hint={'center_x': .8, 'center_y': .4})
        self.time_minusbutton = Button(text="-",
                                       size_hint=(.05, .05),
                                       pos_hint={'center_x': .625, 'center_y': .4})
        self.time_plusbutton = Button(text="+",
                                      size_hint=(.05, .05),
                                      pos_hint={'center_x': .675, 'center_y': .4})
        self.time_plusbutton.bind(on_press=self.on_press_time_plusbutton)
        self.time_minusbutton.bind(on_press=self.on_press_time_minusbutton)

        screen_layout.add_widget(self.another_label)
        screen_layout.add_widget(self.another_percent)
        screen_layout.add_widget(self.another_amount)
        screen_layout.add_widget(self.time_label)
        screen_layout.add_widget(self.time_value)
        screen_layout.add_widget(self.time_plusbutton)
        screen_layout.add_widget(self.time_minusbutton)

        back_button = Button(text='Wróć',
                             size_hint=(.3, .1),
                             pos_hint={'center_x': .5, 'center_y': .2})
        back_button.bind(on_press=self.on_press_backbutton)
        next_button = Button(text='Oblicz',
                             size_hint=(.3, .1),
                             pos_hint={'center_x': .5, 'center_y': .1})
        next_button.bind(on_press=self.on_press_button)

        screen_layout.add_widget(back_button)
        screen_layout.add_widget(next_button)

        self.add_widget(screen_layout)

    def check_another_alcohol(self):
        if any(c.isalpha() for c in self.another_amount.text) or any(c.isalpha() for c in self.another_percent.text):
            return False
        if self.another_amount.text == '' or self.another_percent.text == '':
            return False
        return True

    def on_press_time_plusbutton(self, isntance):
        self.time += .25
        self.time_value.text = str(self.time)

    def on_press_time_minusbutton(self, instance):
        if self.time > 0:
            self.time -= .25
            self.time_value.text = str(self.time)

    def on_press_backbutton(self, instance):
        sm.transition.direction = 'right'
        sm.current = 'param1'

    def on_press_button(self, isntance):
        for i in range(len(self.alcohols)):
            self.drunk[i][1] = self.alcohols[i].amount * self.alcohols[i].volume
        if self.check_another_alcohol():
            self.drunk.append([float(self.another_percent.text.replace(',', '.')), int(self.another_amount.text)])
        sm.transition.direction = 'left'
        sm.current = 'plot'


class PlotScreen(Screen):
    def __init__(self, **kwargs):
        super(PlotScreen, self).__init__(**kwargs)
        screen_layout = FloatLayout()
        self.alc = 0
        self.peak = 0

        self.alc_text = Label(text="Spożyto " + str(self.alc) + "g czystego alkoholu",
                              size_hint=(.3, .1),
                              pos_hint={'center_x': .42, 'center_y': .95})
        self.peak_text = Label(text="Szczytowa ilość alkoholu we krwi wyniosła: " + str(self.peak) + "‰",
                               size_hint=(.3, .1),
                               pos_hint={'center_x': .49, 'center_y': .91})
        screen_layout.add_widget(self.alc_text)
        screen_layout.add_widget(self.peak_text)

        again_button = Button(text="Oblicz jeszcze raz",
                              size_hint=(.3, .1),
                              pos_hint={'center_x': .5, 'center_y': .2})
        again_button.bind(on_press=self.on_press_againbutton)
        screen_layout.add_widget(again_button)

        stop_button = Button(text="Zakończ",
                             size_hint=(.3, .1),
                             pos_hint={'center_x': .5, 'center_y': .1})
        stop_button.bind(on_press=self.on_press_stopbutton)
        screen_layout.add_widget(stop_button)

        self.add_widget(screen_layout)

    def draw_plot(self, data):
        x_axis = data[1]
        y_axis = data[0]

        plt.close()
        indy = np.arange(len(y_axis))
        indx = [i for i in range(0, len(x_axis), 4)]
        colors = []
        for y in y_axis:
            if y < .2:
                colors.append('green')
            else:
                colors.append('red')

        plt.bar(indy, y_axis, color=colors)
        plt.xticks(indx, [int(x_axis[i]) for i in range(0, len(x_axis), 4)], size=8)
        plt.ylim(min(y_axis), 1.1 * max(y_axis))
        plt.grid(True, which='both', axis='y')
        plt.xlabel('czas od rozpoczęcia picia [h]')
        plt.ylabel('zawartość alkoholu we krwi [promil]')

        return FigureCanvas(plt.gcf())

    def on_pre_plot_enter(self, instance):
        plot_layout = BoxLayout()
        liczydelko = Licznik(param1.body_parameters[0], param1.body_parameters[1], param1.body_parameters[2],
                             param1.body_parameters[3], param1.body_parameters[5], param1.body_parameters[4],
                             param2.time, param2.drunk)
        plot_data = liczydelko.calculate()
        plot_layout.add_widget(self.draw_plot(plot_data))
        plot_layout.size_hint = (.8, .6)
        plot_layout.pos_hint = {'center_x': .5, 'center_y': 0.57}

        self.add_widget(plot_layout)
        self.alc = liczydelko.alcoholAmount
        self.peak = round(max(plot_data[0]), 2)
        self.alc_text.text = "Spożyto " + str(self.alc) + "g czystego alkoholu"
        self.peak_text.text = "Szczytowa ilość alkoholu we krwi wyniosła: " + str(self.peak) + "‰"

    def on_press_againbutton(self, instance):
        param2.drunk = [[5, 0], [5, 0], [12, 0], [40, 0]]
        sm.transition.direction = 'right'
        sm.current = 'param2'
        sm.current = 'param1'

    def on_press_stopbutton(self, instance):
        app.stop()


sm = ScreenManager()
mainscr = MainScreen(name='mainscr')
param1 = ParameterScreen1(name='param1')
param2 = ParameterScreen2(name='param2')
plot = PlotScreen(name='plot')
plot.bind(on_pre_enter=plot.on_pre_plot_enter)
sm.add_widget(mainscr)
sm.add_widget(param1)
sm.add_widget(param2)
sm.add_widget(plot)


class MainApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    app = MainApp()
    app.run()
