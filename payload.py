import ctypes

# 0x40 = Info-Icon
ctypes.windll.user32.MessageBoxW(
    0,
    "Be more careful!\nThis could've been malware.",
    "Info",
    0x40
)
