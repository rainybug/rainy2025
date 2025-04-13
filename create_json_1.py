import csv
import json


#########문자열 저장#############
target = "./data/global"

# 결과 저장용 리스트
answers_q1 = []
answers_q2 = []
answers_q3 = []

#csv 경로는 적절히 수정

"""import csv

# 추출된 답변을 저장할 리스트
answers = []

# CSV 파일 경로 (예: 'answers.csv')
csv_file = 'your_file.csv'

with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        # 각 행에서 "問１,"로 시작하는 열을 찾기
        for cell in row:
            if cell.startswith("問１,"):
                # "問１," 다음부터 시작해서 전체 문자열을 추출
                # 첫 번째 "問１," 제거 후 나머지를 붙이고, 처음과 끝의 큰따옴표 제거
                content = cell.split("問１,", 1)[1]
                if content.startswith('"') and content.endswith('"'):
                    content = content[1:-1]
                answers.append(content)
                break  # 첫 번째 답변만 추출한다면 break

# 결과 확인
for i, answer in enumerate(answers):
    print(f"[{i}] {answer}\n")
"""

with open(target + "_merged_all.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if not row or len(row) < 2:
            continue  # 빈 줄 또는 열이 부족한 줄은 건너뜀
        label = row[0].strip()
        content = row[1]  # 개행 문자나 공백도 포함
        if label == "問１":
            #여기서 큰따옴표가 남아있다면 삭제
            answers_q1.append(content)
        elif label == "問２":
            answers_q2.append(content)
        elif label == "問３":
            answers_q3.append(content)

# 결과 미리보기 (앞의 몇 개)
answers_q1[:1], answers_q2[:1], answers_q3[:1]



#########JSON 생성 (q1까지만)#############



# 저장할 JSON 객체 리스트
json_data_q1 = []
json_data_q2 = []
json_data_q3 = []

# 공통 값
question_text = "この画像に書かれている文書を取り出してください"

# answers_q1의 각 항목을 JSON 객체로 변환
i=0
for answer in answers_q1:
    image_path = target + "_q1_" + str(i) + ".jpg"
    item = {
        "image": image_path,
        "question": question_text,
        "answer": answer
    }
    json_data_q1.append(item)
    i+=1

# answers_q2의 각 항목을 JSON 객체로 변환
i=0
for answer in answers_q2:
    image_path = target + "_q2_" + str(i) + ".jpg"
    item = {
        "image": image_path,
        "question": question_text,
        "answer": answer
    }
    json_data_q2.append(item)
    i+=1

# answers_q3의 각 항목을 JSON 객체로 변환
i=0
for answer in answers_q3:
    image_path = target + "_q3_" + str(i) + ".jpg"
    item = {
        "image": image_path,
        "question": question_text,
        "answer": answer
    }
    json_data_q3.append(item)
    i+=1

# JSON 파일로 저장
output_file = target + "_answers_q1.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(json_data_q1, f, ensure_ascii=False, indent=2)

output_file  # 저장된 경로 반환


# JSON 파일로 저장
output_file = target + "_answers_q2.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(json_data_q2, f, ensure_ascii=False, indent=2)

output_file  # 저장된 경로 반환


# JSON 파일로 저장
output_file = target + "_answers_q3.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(json_data_q3, f, ensure_ascii=False, indent=2)

output_file  # 저장된 경로 반환
