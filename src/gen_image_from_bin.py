# -*- coding: UTF-8 -*-

import numpy
from PIL import Image
import binascii

def getMatrixfrom_bin(filename,  width):
    with open(filename, 'rb') as f:
        content = f.read()
    hexst = binascii.hexlify(content)  #将二进制文件转换为十六进制字符串
    fh = numpy.array([int(hexst[i:i+2], 16) for i in range(0, len(hexst), 2)])  #按字节分割
    rn = len(fh)/width
    fh = numpy.reshape(fh[:rn*width], (-1, width))  #根据设定的宽度生成矩阵
    fh = numpy.uint8(fh)
    return fh

filename = "C:\Users\Nicola\PycharmProjects\play-field\data\class2_02K5GMYITj7bBoAisEmD.bytes"
im = Image.fromarray(getMatrixfrom_bin(filename, 512)) #转换为图像
im.save("../output/class2_02K5GMYITj7bBoAisEmD.bytes.png")
