for y in range(1, 6):		# 제목 부분을 출력한다. 
    print(f"x**{y}", end="\t");	
print()

for x in range(1, 6):		
    for y in range(1, 6):
        print(x**y, end="\t")
    print()
