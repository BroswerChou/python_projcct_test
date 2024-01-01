import zipfile
import os


def zip_data(srcpath, targetpath):
    """
    将指定目录下文件压缩
    :param srcpath:
    :param targetpath:
    :return:
    """
    zfobj = zipfile.ZipFile(targetpath, "w", zipfile.ZIP_DEFLATED)
    filelist = os.listdir(srcpath)
    for filename in filelist:
        fullpath = os.path.join(srcpath, filename)
        zfobj.write(fullpath)
    zfobj.close()
    print("文件压缩完毕")
zip_data("D:\\ceshi", "D:\\ceshi.zip")


def unzip_data(srcpath, targetpath):
    """
    将指定目录下的文档解压缩
    :param srcpath:
    :param targetpath:
    :return:
    """
    if zipfile.is_zipfile(srcpath):
        zfobj = zipfile.ZipFile(srcpath)
        zfobj.extractall(targetpath)
        zfobj.close()
        print("文件已经解压完毕")
    else:
        print("不是压缩文件")
unzip_data("D:/ceshi.zip", "E:/")

