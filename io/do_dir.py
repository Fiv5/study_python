import os

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径


def printRelationPath(key_word, path='.', result=[]):
    for file in os.listdir(path):
        relationFileName = path+'/'+file
        if os.path.isdir(relationFileName):
            printRelationPath(key_word, relationFileName, result)
        if key_word in os.path.splitext(file)[0]:
            result.append(relationFileName)
    return result


files = printRelationPath('class')
print(files)
