# -*- coding: UTF-8 -*-

import numpy
from PIL import Image
import binascii
from os import listdir
from os.path import isfile, join

def getMatrixfrom_bin(filename, width):
    with open(filename, 'rb') as f:
        content = f.read()
    hexst = binascii.hexlify(content)  #将二进制文件转换为十六进制字符串
    fh = numpy.array([int(hexst[i:i+2], 16) for i in range(0, len(hexst), 2)])  #按字节分割
    rn = len(fh)/width
    fh = numpy.reshape(fh[:rn*width], (-1, width))  #根据设定的宽度生成矩阵
    fh = numpy.uint8(fh)
    return fh

source_path = "/home/nick/research/vs/Virus.Win"
all_files = [f for f in listdir(source_path) if isfile(join(source_path, f))]
key_word = "Virus.Win32.Bube"
particular_files = [f for f in all_files if key_word in f]

for f in particular_files:
    filename = join(source_path, f)
    im = Image.fromarray(getMatrixfrom_bin(filename, 64)) #转换为图像
    im.save("/home/nick/research/vs-output-images/Virus.Win.Output.Images/{0}.png".format(f))
