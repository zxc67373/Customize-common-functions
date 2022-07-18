import os

files = os.listdir('./dataset/test/')
n =0

for file in files:
    print(file)
    oldname = './dataset/test/' + os.sep + files[n]  # os.sep添加系统分隔符

    # 设置新文件名
    newname = './dataset/train/' + os.sep + 'a' + str(n + 1) + '.JPG'

    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    print(oldname, '======>', newname)

    n += 1

