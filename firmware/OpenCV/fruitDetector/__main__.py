
# __main__.py

from __future__ import absolute_import, division, print_function, unicode_literals

import tkinter as win
import cv2
import numpy as np

import tensorflow as tf
import sys
import platform

import winApp

def main():
    """Read the Real Python article feed"""
    print(sys.argv) 
    winApp.config()
    winApp.run()

if __name__ == "__main__":
    main()
