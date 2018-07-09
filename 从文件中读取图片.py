#你可以轻松的使用cv2.imread函数读取图像，该函数采用图像路径和可选标记。
import argparse
import cv2
parser = argparse.ArgumentParser()
parser.add_argument('--path',default='../data/Lena.png', help='Imgae path.')
