import tarfile
import os


def tar_data(srcpath, targetpath):
    """
    将指定目录下文件压缩
    :param srcpath:
    :param targetpath:
    :return:
    """
    tarobj = tarfile.TarFile(targetpath, "w")
    filelist = os.listdir(srcpath)
    for filename in filelist:
        fullpath = os.path.join(srcpath, filename)
        tarobj.add(fullpath)
    tarobj.close()
    print("文件压缩完毕")
    tarobj.getnames()
tar_data("D:\\ceshi", "D:\\ceshi.tar")
# 修改测试



