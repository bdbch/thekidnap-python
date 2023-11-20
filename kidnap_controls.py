# A class that implements a controller for moving inside the "Kidnap" game

import keyboard
import mouse
import time
import win32api, win32con

class Kidnap_Controls:
  # constructor binds keyboard handlers for the game to specific messages
  def send_event(self, event):
    if (event == "w"):
      self.handle_key("w", .5)
    if (event == "s"):
      self.handle_key("s", .5)
    if (event == "a"):
      self.handle_key("a", .5)
    if (event == "d"):
      self.handle_key("d", .5)
    if (event == "shift"):
      self.handle_key("shift")
    if (event == "f"):
      self.handle_key("f")
    if (event == "click"):
      print("click left")
      mouse.click(mouse.LEFT)
    if (event == "ll"):
      print("mouse left")
      win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -20, 0, 0, 0)
    if (event == "ll+"):
      print("mouse left")
      win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -40, 0, 0, 0)
    if (event == "ll++"):
      print("mouse left")
      win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -100, 0, 0, 0)
    if (event == "lr"):
      print("mouse right")
      win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 20, 0, 0, 0)
    if (event == "lr+"):
      print("mouse right")
      win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 40, 0, 0, 0)
    if (event == "lr++"):
      print("mouse right")
      win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 100, 0, 0, 0)
    if (event == "lu"):
      print("mouse up")
      win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -20, 0, 0)
    if (event == "lu+"):
      print("mouse up")
      win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -40, 0, 0)
    if (event == "lu++"):
      print("mouse up")
      win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -100, 0, 0)
    if (event == "ld"):
      print("mouse down")
      win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 20, 0, 0)
    if (event == "ld+"):
      print("mouse down")
      win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 40, 0, 0)
    if (event == "ld++"):
      print("mouse down")
      win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 100, 0, 0)
  
  def handle_key(self, key, delay = .1):
    keyboard.press(key)
    print("press ", key)
    time.sleep(delay)
    print("release", key)
    keyboard.release(key)