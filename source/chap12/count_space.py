def parse_file(path):
    # 파일을 읽기 모드로 열어 infile에 저장한다.
    infile = open(path)
    
    # 스페이스와 탭의 개수를 저장할 변수를 초기화한다.
    spaces = 0
    tabs = 0

    # 파일을 한 줄씩 읽어서 스페이스와 탭의 개수를 센다.
    for line in infile:
        spaces += line.count(' ')  # 현재 줄에서 스페이스의 개수를 세어 spaces에 더한다.
        tabs += line.count('\t')   # 현재 줄에서 탭의 개수를 세어 tabs에 더한다.
    
    # 파일을 닫는다.
    infile.close()

    # 스페이스와 탭의 개수를 반환한다.
    return spaces, tabs

# 사용자로부터 파일 이름을 입력받는다.
filename = input("파일 이름을 입력하시오: ")

# parse_file 함수를 호출하여 스페이스와 탭의 개수를 계산하고 출력한다.
spaces, tabs = parse_file(filename)
print("스페이스 수 = %d, 탭의 수 = %d" % (spaces, tabs))
