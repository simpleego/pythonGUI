import os

def list_files_in_directory(directory):
    # 주어진 디렉토리가 유효한지 확인
    if not os.path.isdir(directory):
        print(f"'{directory}' 은 유효한 디렉토리가 아닙니다. ")
        return
    # 디렉토리 안의 파일 목록 출력
    print(f"디렉토리 '{directory}' 안의 파일:")
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            print(filename)

# 예제를 위한 특정 디렉토리 경로 설정
target_directory = 'd:\\test\\'

# 디렉토리 안의 파일 목록 출력
list_files_in_directory(target_directory)
