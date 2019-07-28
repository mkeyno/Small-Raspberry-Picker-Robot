
# __main__.py

from __future__ import absolute_import, division, print_function, unicode_literals

import tkinter as win
import cv2
import numpy as np

import tensorflow as tf
import sys
import platform


def main():
    """Read the Real Python article feed"""
    print(sys.argv) 
    windows=win.Tk()
    windows.title(__version__)
    windows.mainloop()

if __name__ == "__main__":
    main()
