import os

def change_extension(directory, old_ext, new_ext):
    # 주어진 경로가 유효한 디렉토리인지 확인합니다.
    if not os.path.isdir(directory):
        print(f"'{directory}'는 유효한 디렉토리가 아닙니다.")
        return

    # 디렉토리 내의 각 파일에 대해 작업을 수행합니다.
    for filename in os.listdir(directory):
        # 주어진 old_ext로 끝나는 파일만 처리합니다.
        if filename.endswith(old_ext):
            # 기존 파일의 경로와 새로운 파일명을 생성합니다.
            old_file_path = directory+'\\'+filename
            new_filename = filename.replace(old_ext, new_ext)
            new_file_path = directory+'\\'+new_filename
            # 파일의 확장자를 변경하고 변경사항을 출력합니다.
            os.rename(old_file_path, new_file_path)
            print(f"'{filename}' 파일의 확장자를 '{new_filename}'(으)로 변경했습니다.")

# 예제를 위한 디렉토리 경로 설정
target_directory = 'd://test'
old_extension = '.c'
new_extension = '.py'
# 디렉토리 안의 파일 확장자 변경
change_extension(target_directory, old_extension, new_extension)
