import os
#在程序最开始增加一些注释，看能否提交到GitHub上

# def is_folder(pathname):
#     if os.path.isdir(pathname):
#         return True
#     elif os.path.isfile(pathname):
#         return True
#     else:
#         return False
files=[]
path=input('please input the path you want to detect')
print(path)
path=path.lstrip('"')
path=path.rstrip('"')
print(path)
os.chdir(path)
print('第一层下的文件有这些：')
print(os.listdir())
for folder1 in os.listdir():
    if  not os.path.isfile(path+'\\'+str(folder1)):#进入第一层，查看是否是文件夹
        os.chdir(path+'\\'+str(folder1))#如果是文件夹，那么就进入第二层
        print(os.getcwd())#这里是进入了第二层
        print(str(folder1)+'第二层下的文件有这些')
        print(os.listdir())#打印出第二层的文件名
        for folder2 in os.listdir():#往下是进入第三层
            if not os.path.isfile(path+'\\'+folder1+'\\'+folder2):
                os.chdir(path+'\\'+folder1+'\\'+folder2)
                print('第三层下的文件夹有这些')
                print(os.listdir())
                for folder3 in os.listdir():
                    print(folder3)
                    files.append(folder3)
            else:
                files.append(folder2)
    else:
        files.append(folder1)
print(files)




# print(os.getcwd())