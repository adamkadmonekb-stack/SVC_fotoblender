[app]

# (str) Название приложения на экране вашего планшета
title = rnakhz

# (str) Имя пакета БЕЗ точек и пробелов (только латиница!)
package.name = rnakhz

# (str) Домен (уникальное слово латиницей)
package.domain = com.rna

# (str) Папка исходного кода
source.dir = .

# (list) Включаем расширения файлов картинок, чтобы все фото упаковались внутрь APK
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Версия вашего приложения
version = 0.3

# === 🏆 ИСПРАВЛЕННАЯ И ЗАЩИЩЕННАЯ СТРОКА ЗАВИСИМОСТЕЙ: ===
requirements = python3, kivy, pillow, android

# (str) Ориентация экрана
orientation = portrait

# (bool) Приложение во весь экран
fullscreen = 1

# ==============================================================================
# НАСТРОЙКИ ANDROID (Идеальные для вашего Android 10)
# ==============================================================================

# (list) Разрешения для работы с галереей и фото
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# ПРАВИЛЬНЫЙ СПОСОБ ВКЛЮЧИТЬ LEGACY-ДОСТУП К ПАМЯТИ НА ANDROID 10:
android.manifest.xml_attribute = android:requestLegacyExternalStorage="true"

# (int) Целевой Android API. Оставляем стабильный 33
android.api = 33

android.python_version = 3.11

# (int) Минимальная поддерживаемая версия (Android 7.0)
android.minapi = 24

# (int) Версия NDK-API, чтобы не было конфликта Mismatch
android.ndk_api = 24

# (str) Версия Android NDK, проверенная с Kivy
android.ndk = 25b

# (bool) Принять лицензии автоматически
android.accept_sdk_license = True

# (bool) Использовать private директорию
android.private_storage = True

# (list) Архитектуры процессоров под ваш планшет Lenovo и другие телефоны
android.archs = arm64-v8a, armeabi-v7a

# ==============================================================================
# НАСТРОЙКИ СБОРЩИКА
# ==============================================================================

[buildozer]

# (int) Уровень логирования
log_level = 2

# (int) Предупреждение о root
warn_on_root = 0
