import os

def calcDirSize(name):
    totalSize = 0

    if os.path.isfile(name):  # 파일인 경우
        totalSize += os.path.getsize(name)  # 파일 크기를 더한다
    else:  # 디렉터리인 경우
        fileList = os.listdir(name)  # 디렉터리 내의 파일과 서브 디렉터리 리스트를 얻는다
        # 서브 디렉터리의 용량을 계산하여 모두 합한다.
        for subDir in fileList:
            totalSize += calcDirSize(os.path.join(name, subDir))  # 재귀적으로 서브 디렉터리 용량을 더한다
    return totalSize

name = input("디렉터리 이름을 입력하시오: ")
print(calcDirSize(name))
