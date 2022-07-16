import time

import cv2
import pyautogui
import screenshot
import ocr
import logging


class Control:
    def __init__(self):
        self.sshot = screenshot.ScreenShotter()

    def __click(self, top_left, bottom_right):
        """
        Click the center of the given rectangle on the screen.
        :param top_left: with respect to the window
        :param bottom_right: with respect to the window
        """
        window_pos = self.sshot.get_window_top_left()
        click_pos = (
            (top_left[0] + bottom_right[0]) // 2 + window_pos[0], (top_left[1] + bottom_right[1]) // 2 + window_pos[1])
        pyautogui.click(click_pos)

    def __find_text(self, text, height_start=0.0, height_end=1.0, width_start=0.0, width_end=1.0):
        """
        Find the position of the text in the bounded portion of the window.
        :return: top_left and bottom_right corner of the text with respect to the window.
        """
        shape, img = self.sshot.crop(height_start, height_end, width_start, width_end)
        top_left, bottom_right = ocr.get_position(img, text)
        top_left = (top_left[0] + int(width_start * shape[1]), top_left[1] + int(height_start * shape[0]))
        bottom_right = (bottom_right[0] + int(width_start * shape[1]), bottom_right[1] + int(height_start * shape[0]))
        return top_left, bottom_right

    def __find_img(self, template_path, height_start=0.0, height_end=1.0, width_start=0.0, width_end=1.0):
        """
        Find the position of the image in the bounded portion of the window.
        :return: top_left and bottom_right corner of the image with respect to the window.
        Returns None, None if not found.
        """
        shape, img = self.sshot.crop(height_start, height_end, width_start, width_end)
        template = cv2.imread(template_path, cv2.IMREAD_COLOR)
        min_val, max_val, min_loc, max_loc = self.sshot.match_template(img, template)
        if max_val > 0.90:
            top_left = max_loc[0] + int(width_start * shape[1]), max_loc[1] + int(height_start * shape[0])
            bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
            return top_left, bottom_right
        else:
            return None, None

    def start_game(self):
        """
        Start the game.
        """
        time.sleep(5)
        self.quit_notice()
        time.sleep(3)
        self.enter_game()
        time.sleep(3)
        self.wait_for_entering()
        time.sleep(3)

    def quit_notice(self):
        top_left, bottom_right = self.__find_img('resources/quit_notice.png')
        if top_left is not None:
            self.__click(top_left, bottom_right)
        else:
            try:
                time.sleep(3)
                self.__find_text('进入游戏')
                time.sleep(3)
                self.enter_game()
            except ocr.NotFound:
                time.sleep(3)
                self.quit_notice()

    def enter_game(self):
        try:
            top_left, bottom_right = self.__find_text('进入游戏', 0.5, 1.0)
            self.__click(top_left, bottom_right)
        except ocr.NotFound:
            time.sleep(3)
            self.enter_game()

    def wait_for_entering(self):
        try:
            self.__find_text('数据加载中', 0.75, 1.0)
            time.sleep(3)
            self.wait_for_entering()
        except ocr.NotFound:
            try:
                self.__find_text('加载进度', 0.75, 1.0)
                time.sleep(3)
                self.wait_for_entering()
            except ocr.NotFound:
                pass

    def explore(self):
        try:
            top_left, bottom_right = self.__find_text('探索', 0.0, 0.5)
            self.__click(top_left, bottom_right)
            time.sleep(3)
        except ocr.NotFound:
            time.sleep(3)
            self.explore()

    def __dungeon_select(self, dungeon, recur, height_start=0.0, height_end=1.0, width_start=0.0, width_end=1.0):
        try:
            top_left, bottom_right = self.__find_text(dungeon, height_start, height_end, width_start, width_end)
            self.__click(top_left, bottom_right)
        except ocr.NotFound:
            time.sleep(3)
            recur()

    def soul(self):
        self.__dungeon_select('御魂', self.soul, 0.95, 1.0, 0.0, 0.5)

    def __soul_select(self, im_path, recur):
        top_left, bottom_right = self.__find_img(im_path)
        if top_left is not None:
            self.__click(top_left, bottom_right)
        else:
            time.sleep(3)
            recur()

    def soul_snake(self):
        self.__soul_select('resources/soul_snake.png', self.soul_snake)

    def soul_fire(self):
        self.__soul_select('resources/soul_fire.png', self.soul_fire)

    def soul_sun(self):
        self.__soul_select('resources/soul_sun.png', self.soul_sun)

    def soul_sea(self):
        self.__soul_select('resources/soul_sea.png', self.soul_sea)

    def kirin(self):
        self.__dungeon_select('觉醒材料', self.kirin, 0.95, 1.0, 0.0, 0.5)

    def kirin_fire(self):
        self.__dungeon_select('业火轮', self.kirin_fire, 0.75,1.0)

    def kirin_wind(self):
        self.__dungeon_select('风转符', self.kirin_wind, 0.75,1.0)

    def kirin_water(self):
        self.__dungeon_select('水灵鲤', self.kirin_water, 0.75,1.0)

    def kirin_thunder(self):
        self.__dungeon_select('天雷鼓', self.kirin_thunder, 0.75,1.0)

    def log_battle(self, total, level, name):
        self.scroll_to_highest_level()
        self.select_level(level)
        self.lock_team()
        count = 1
        while count != total + 1:
            logging.info("开始：刷第{}次{}".format(count, name))
            self.start_battle()
            logging.info("完成：刷第{}次{}".format(count, name))
            count += 1

    def scroll_to_highest_level(self):
        time.sleep(3)
        window_size = self.sshot.get_window_size()
        top_left = self.sshot.get_window_top_left()
        pyautogui.moveTo(top_left[0] + window_size[0] // 4, top_left[1] + window_size[1] // 2)
        pyautogui.scroll(-10000)

    def select_level(self, name):
        try:
            top_left, bottom_right = self.__find_text(name, 0.0, 1.0, 0.0, 0.5)
            self.__click(top_left, bottom_right)
        except ocr.NotFound:
            time.sleep(3)
            self.select_level(name)

    def lock_team(self):
        top_left, bottom_right = self.__find_img('resources/unlock_team.png')
        if top_left is not None:
            self.__click(top_left, bottom_right)

    def start_battle(self):
        try:
            top_left, bottom_right = self.__find_text('挑战', 0.5, 1.0, 0.75, 1.0)
            self.__click(top_left, bottom_right)
            time.sleep(5)
            self.continue_next()
        except ocr.NotFound:
            time.sleep(3)
            self.start_battle()

    def continue_next(self):
        clicked = False
        try:
            while True:
                top_left, bottom_right = self.__find_text('点击屏幕继续', 6 / 7, 1.0)
                self.__click(top_left, bottom_right)
                clicked = True
                time.sleep(0.5)
        except ocr.NotFound:
            if not clicked:
                time.sleep(3)
                self.continue_next()

    def realm(self):
        self.__dungeon_select('结界突破', self.realm, 0.95, 1.0, 0.0, 0.5)

    def realm_raid(self, total):
        heights = [0.2, 0.4, 0.6, 0.8]
        widths = [0.1, 0.43, 0.77, 0.9]
        self.lock_team()
        count = 1
        while True:
            for h in range(3):
                for w in range(3):
                    time.sleep(3)
                    if count == total+1:
                        return
                    shape = self.sshot.get_window_size()
                    top_left = widths[w]*shape[0], heights[h]*shape[1]
                    bottom_right = widths[w+1]*shape[0], heights[h+1]*shape[1]
                    self.__click(top_left, bottom_right)
                    time.sleep(3)
                    try:
                        top_left, bottom_right = self.__find_text('进攻')
                        logging.info("开始：刷第{}次结界突破".format(count))
                        self.__click(top_left, bottom_right)
                        self.continue_next()
                        logging.info("完成：刷第{}次结界突破".format(count))

                        time.sleep(3)
                        try:
                            top_left, bottom_right = self.__find_text('点击屏幕继续')
                            self.__click(top_left, bottom_right)
                            time.sleep(3)
                        except ocr.NotFound:
                            pass
                        count += 1
                    except ocr.NotFound:
                        continue

    def back(self):
        top_left, bottom_right = self.__find_img('resources/back_0.png', 0.0, 0.5)
        if top_left is not None:
            self.__click(top_left, bottom_right)
        else:
            top_left, bottom_right = self.__find_img('resources/back_1.png', 0.0, 0.5)
            if top_left is not None:
                self.__click(top_left, bottom_right)
            else:
                top_left, bottom_right = self.__find_img('resources/back_2.png', 0.0, 0.5)
                if top_left is not None:
                    self.__click(top_left, bottom_right)

    def is_home(self):
        try:
            self.__find_text('探索', 0.0, 0.5)
            return True
        except ocr.NotFound:
            return False

    def home(self):
        while not self.is_home():
            self.back()

    def __buff(self, buff_im_path, status_im_path):
        window_size = self.sshot.get_window_size()
        buff_loc = (window_size[0]*0.305, window_size[1]*0.05), (window_size[0]*0.38, window_size[1]*0.15)
        self.__click(buff_loc[0], buff_loc[1])
        time.sleep(2)
        top_left, bottom_right = self.__find_img(buff_im_path)
        height_start = top_left[1]/window_size[1]
        height_end = bottom_right[1]/window_size[1]
        time.sleep(2)
        tl, br = self.__find_img(status_im_path, height_start, height_end)
        if tl is not None:
            self.__click(tl, br)
            time.sleep(2)
        self.__click(buff_loc[0], buff_loc[1])

    def start_buff(self, buff_im_path):
        self.__buff(buff_im_path, 'resources/buff_off.png')
        time.sleep(3)

    def stop_buff(self, buff_im_path):
        time.sleep(3)
        self.back()
        time.sleep(3)
        self.__buff(buff_im_path, 'resources/buff_on.png')
        time.sleep(3)

