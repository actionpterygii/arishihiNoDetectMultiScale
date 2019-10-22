#-*- coding:utf-8 -*-
import cv2
import numpy as np

def main():
    # 入力画像を読み込み
    img = cv2.imread("a.png")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 方法2(OpenCVで実装)
    dst2 = cv2.equalizeHist(img)
    
    # 結果の出力
    cv2.imwrite("output.png", dst2)


if __name__ == "__main__":
    main()
