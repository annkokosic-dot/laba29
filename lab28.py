# -*- coding: utf-8 -*-
"""
Лабораторная работа №29, Вариант 2
Задание 3: Сборка iOS-приложения с фиксированной ориентацией portrait
"""

# ============================================================
# ФИКСАЦИЯ ОРИЕНТАЦИИ PORTRAIT (для iOS и всех платформ)
# ВАЖНО: должно быть ДО импорта Window из kivy.core.window
# ============================================================
from kivy.config import Config
Config.set('graphics', 'orientation', 'portrait')
Config.set('graphics', 'resizable', False)  # Запрет изменения размера окна

# Стандартные импорты Kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import os
import sys
from datetime import datetime


def get_resource_path(relative_path):
    """Получить путь к ресурсу для PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        # Режим PyInstaller — временная папка _internal
        base_path = sys._MEIPASS
    else:
        # Режим разработки — папка проекта
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


class MainScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Путь к изображению
        self.image_path = get_resource_path('bg.png')
        
        # Фоновое изображение на весь экран
        bg = Image(
            source=self.image_path,
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0},
            allow_stretch=True,
            keep_ratio=False
        )
        self.add_widget(bg)
        
        # Заголовок
        title = Label(
            text='ЛАБА 29 - ВАРИАНТ 2',
            font_size='24sp',
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.1),
            pos_hint={'x': 0, 'top': 1}
        )
        self.add_widget(title)
        
        # Статусная метка
        self.status_label = Label(
            text='Готов к работе',
            font_size='16sp',
            color=(1, 1, 1, 1),
            size_hint=(1, 0.08),
            pos_hint={'x': 0, 'y': 0.15}
        )
        self.add_widget(self.status_label)
        
        # Кнопка "Проверить картинку"
        btn_check = Button(
            text='📷 Проверить картинку',
            font_size='18sp',
            size_hint=(0.45, 0.08),
            pos_hint={'x': 0.025, 'y': 0.05}
        )
        btn_check.bind(on_press=self.check_image)
        self.add_widget(btn_check)
        
        # Кнопка "Сохранить файл"
        btn_save = Button(
            text='💾 Сохранить файл',
            font_size='18sp',
            size_hint=(0.45, 0.08),
            pos_hint={'x': 0.525, 'y': 0.05}
        )
        btn_save.bind(on_press=self.save_file)
        self.add_widget(btn_save)
    
    def check_image(self, instance):
        """Проверить наличие и размер изображения."""
        if os.path.exists(self.image_path):
            size = os.path.getsize(self.image_path)
            self.status_label.text = f'✅ Картинка найдена ({size} байт)'
            print(f'✅ Картинка найдена: {self.image_path}')
            print(f'   Размер: {size} байт')
        else:
            self.status_label.text = '❌ Картинка не найдена!'
            print(f'❌ Картинка не найдена: {self.image_path}')
    
    def save_file(self, instance):
        """Сохранить лог-файл в папку data."""
        # Создаём папку data, если её нет
        data_dir = os.path.join(os.getcwd(), 'data')
        os.makedirs(data_dir, exist_ok=True)
        
        # Создаём лог-файл
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        log_file = os.path.join(data_dir, f'log_{timestamp}.txt')
        
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write('Лабораторная работа №29, Вариант 2\n')
            f.write(f'Время: {datetime.now()}\n')
            f.write(f'Ориентация: Portrait (375x812)\n')
            f.write(f'Изображение: {self.image_path}\n')
            if os.path.exists(self.image_path):
                size = os.path.getsize(self.image_path)
                f.write(f'Размер изображения: {size} байт\n')
        
        self.status_label.text = '✅ Сохранено!'
        print(f'✅ Файл сохранён: {log_file}')


class Lab29App(App):
    def build(self):
        # Размер окна как у iPhone (портретная ориентация)
        Window.size = (375, 812)
        Window.title = "Лабораторная 29 - Вариант 2"
        
        return MainScreen()
    
    def on_stop(self):
        print("📴 Приложение остановлено")


if __name__ == '__main__':
    Lab29App().run()