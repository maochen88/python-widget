#coding: utf-8

#使用递归查找指定目录下所有文件，并美化输出
import os
import glob
def searchFile(root_path,flag=0):
    if glob.glob(os.path.join(root_path, '*')):
        for x in glob.glob(os.path.join(root_path, '*')):
            if flag == 1:
                print '\t\t', x
            else:
                print x
            searchFile(x, flag=1)
            
            
#输出指定目录下所有文件大小总和，可选为MB或者GB
def check_memory(path, style='M'):
    i = 0
    for dirpath, dirname, filename in os.walk(path):
        for ii in filename:
            i += os.path.getsize(os.path.join(dirpath,ii))
    if style == 'M':
        memory = i / 1024. / 1024.
        print memory
        return memory 
    else:
        memory = i / 1024. / 1024./ 1024.
        print memory
        return memory

if __name__ == '__main__':
    searchFile('.')
    check_memory('.', '')
