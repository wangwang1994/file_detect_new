import os
# def is_folder(pathname):
#     if os.path.isdir(pathname):
#         return True
#     elif os.path.isfile(pathname):
#         return True
#     else:
#         return False

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
            if not os.path.isfile(os.getcwd()+'\\'+folder2):
                os.chdir(os.getcwd()+'\\'+str(folder2))
                print(os.getcwd())
            else:
                continue
        # print('now i am in the second folder')
    else:
        continue




# print(os.getcwd())