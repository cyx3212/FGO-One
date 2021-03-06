__metaclass__ = type

from util.filter import get_filtered
from util.anti import basic_tap
from util.cvs import analyze
import cv2


class Basic:
    def __init__(self):
        self.scene = []
        self.sh = []
        self.btn_crd = [0, 0]
        self.end = []

    def get_button(self):
        position = get_filtered(self.sh, self.scene, 0.9)
        self.btn_crd[0] = position[0][0]
        self.btn_crd[1] = position[0][1]
        basic_tap(self.btn_crd[0], self.btn_crd[1])

        if analyze(self.sh, cv2.imread("./assets/scene/win2.png", 0), 0.9) == 1:
            self.end = "end"
