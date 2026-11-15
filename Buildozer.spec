[app]
title = TESS
package.name = tessapp
package.domain = com.pcdoc92.tess
source.dir = .
source.include_exts = py,png,jpg
version = 0.1
requirements = python3,kivy,requests
orientation = portrait
android.permissions = INTERNET,RECORD_AUDIO
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True

[buildozer]
log_level = 2
warn_on_root = 1
