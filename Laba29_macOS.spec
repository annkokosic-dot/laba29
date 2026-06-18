# -*- mode: python ; coding: utf-8 -*-
# ============================================================
# Конфигурация сборки macOS-приложения Laba29
# Лабораторная работа №29, Вариант 2, Задание 2
# ============================================================
# Параметры сборки:
# - Имя приложения: Laba29_macOS
# - Версия: 1.0.0
# - Bundle Identifier: org.test.laba29
# - Режим: windowed (без консоли)
# - Ресурсы: bg.png (фоновое изображение)
# ============================================================

import sys
import os

# Блок анализа зависимостей
a = Analysis(
    ['lab28.py'],                          # Исходный файл приложения
    pathex=[],                             # Дополнительные пути поиска
    binaries=[],                           # Бинарные зависимости
    datas=[('bg.png', '.')],               # ✅ Включаем картинку в сборку
    hiddenimports=[],                      # Скрытые импорты
    hookspath=[],                          # Пути к хукам
    hooksconfig={},                        # Конфигурация хуков
    runtime_hooks=[],                      # Рантайм-хуки
    excludes=[],                           # Исключаемые модули
    noarchive=False,                       # Архивирование PYZ
    optimize=0,                            # Уровень оптимизации
)

# Создание PYZ-архива (сжатые Python-модули)
pyz = PYZ(a.pure)

# Создание исполняемого файла
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,                 # Бинарники выносятся отдельно
    name='Laba29_macOS',                   # Имя приложения
    debug=False,                           # Без отладочной информации
    bootloader_ignore_signals=False,
    strip=False,                           # Не удалять символы
    upx=True,                              # Сжатие UPX
    console=False,                         # ✅ Графическое приложение (без консоли)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # ============================================================
    # ПАРАМЕТРЫ ДЛЯ MACOS (активируются при сборке на macOS)
    # ============================================================
    icon=None,                             # Иконка приложения (если есть)
    version='1.0.0',                       # ✅ Версия приложения (Задание 2)
)

# Создание папки с файлами (COLLECT для режима onedir)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Laba29_macOS',
)