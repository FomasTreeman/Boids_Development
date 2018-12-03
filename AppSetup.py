#https://www.python-course.eu/tkinter_canvas.php
#canvas

import tkinter as tk
import os
import subprocess
import platform


class App(tk.Canvas):
    def __init__(self, title: str, my_model, master=None, app_width=1000, app_height=600):
        tk.Canvas.__init__(self, master, width=app_width, height=app_height)
        self.master.title(title)
        self.model = my_model
        self.grid()
        self.model.setup(self)
        self.raise_app()
        self.update()
        self.move()

    def move(self):
        self.model.draw(self)
        self.update()
        self.after(10, self.move)

    def raise_app(self):
        self._root().attributes("-topmost", True)
        if platform.system() == 'Darwin':
            script_text = 'tell application "System Events" to set frontmost of every process whose unix id is {} to ' \
                          'true'
            script = script_text.format(os.getpid())
            subprocess.check_call(['/usr/bin/osascript', '-e', script])
        self._root().after(0, lambda: self._root().attributes("-topmost", False))
