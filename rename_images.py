import os

# 2. 글로벌 정수 선언
i = 0

# 1. 경로 설정
folder_path = "shou_ronbun/data"

# 4. 루프를 통해 모든 파일 확인
for filename in os.listdir(folder_path):
    if "ansimg" in filename:
        # 3. 조건을 만족하는 경우 i 증가 및 이름 변경
        i += 1
        new_filename = f"global_q1_{i}.jpg"
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {filename} -> {new_filename}")
