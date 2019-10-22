#-*- coding:utf-8 -*-
import cv2
import numpy as np

def main():
    # ���͉摜��ǂݍ���
    img = cv2.imread("a.png")

    # �O���[�X�P�[���ϊ�
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # ���@2(OpenCV�Ŏ���)
    dst2 = cv2.equalizeHist(img)
    
    # ���ʂ̏o��
    cv2.imwrite("output.png", dst2)


if __name__ == "__main__":
    main()
