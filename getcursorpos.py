import win32api

x, y = win32api.GetCursorPos()
print("X =", x)
print("Y =", y)
