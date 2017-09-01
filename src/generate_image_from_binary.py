# -*- coding: UTF-8 -*-

import numpy
from PIL import Image
import binascii
from os import listdir
from os.path import isfile, join

def getMatrixfrom_bin(filename,  width):
    with open(filename, 'rb') as f:
        content = f.read()
    hexst = binascii.hexlify(content)  #将二进制文件转换为十六进制字符串
    fh = numpy.array([int(hexst[i:i+2], 16) for i in range(0, len(hexst), 2)])  #按字节分割
    rn = len(fh)/width
    fh = numpy.reshape(fh[:rn*width], (-1, width))  #根据设定的宽度生成矩阵
    fh = numpy.uint8(fh)
    return fh

path = "C:\Users\Nicola\PycharmProjects\play-field\data"
files = [f for f in listdir(path) if isfile(join(path, f))]

for f in files:
    filename = join(path, f)
    im = Image.fromarray(getMatrixfrom_bin(filename, 512)) #转换为图像
    im.save("../output/{0}.png".format(f))
