import time

import cv2
import pyautogui
import pygetwindow


class ScreenShotter:
    def __init__(self):
        self.count = 0
        self.scale = self.get_window_size()[0] / 1728

    def get_window(self):
        return pygetwindow.getWindowsWithTitle('阴阳师-网易游戏')[0]

    def get_window_top_left(self):
        window = self.get_window()
        return window.topleft[0], window.topleft[1]

    def get_window_bottom_right(self):
        window = self.get_window()
        return window.bottomright[0], window.bottomright[1]

    def get_window_size(self):
        window = self.get_window()
        return window.width, window.height

    def screenshot(self):
        window = self.get_window()
        window.activate()
        time.sleep(1)
        topleft = self.get_window_top_left()
        fullscreen = pyautogui.screenshot()
        fullscreen.save('tmp/fullscreen' + str(self.count) + '.png')

        im = cv2.imread('tmp/fullscreen' + str(self.count) + '.png')
        im_crop = im[topleft[1]: topleft[1] + window.height, topleft[0]:topleft[0] + window.width]
        self.count += 1

        return im_crop

    def crop(self, height_start=0.0, height_end=1.0, width_start=0.0, width_end=1.0):
        img = self.screenshot()
        shape = img.shape
        return shape, img[int(height_start * shape[0]):int(height_end * shape[0]),
                      int(width_start * shape[1]):int(width_end * shape[1])]

    def match_template(self, img, template):
        template = cv2.resize(template, (0, 0), fx=self.scale, fy=self.scale)
        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        return cv2.minMaxLoc(result)
