import pyttsx3

engine = pyttsx3.init()

# 设置语言为中文
engine.setProperty(
    "voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0")

msg="Hello，欢迎进入Python的世界！"

engine.say(msg)

engine.runAndWait()
