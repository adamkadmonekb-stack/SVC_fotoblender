[app]
title = FotoKvantum
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 0.2

requirements = python3, kivy, pillow, plyer, hostpython3


orientation = portrait
fullscreen = 1

android.api = 34
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.private_storage = True

android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

[buildozer]

log_level = 2
warn_on_root = 1
