import random #기본 라이브러리 중 하나이며, random 모듈을 불러오는 코드(random 모듈은 난수(예측할 수 없는 값)를 생성하는 함수들을 제공하는 라이브러리)
#capitals 딕셔너리 변수 선언하고, 해당하는 수도 정보 저장
capitals = {
    "대한민국": "서울",
    "멕시코": "멕시코시티",
    "스페인": "마드리드",
    "프랑스": "파리",
    "영국": "런던",
    "그리스": "아테네",
    "독일": "베를린",
    "일본": "도쿄",
    "중국": "베이징",
    "러시아": "모스크바"
}

def guess_capital(): # guess_capital 함수는 무한 루프 실행
    while True:
        country = random.choice(list(capitals.keys())) # 나라 중에서 랜덤하게 하나 선택
        capital = capitals[country] # 선택된 나라에 해당하는 수도를 capital 변수에 저장
        
        answer = input(f"{country}의 수도는 무엇일까요? ")
        
        if answer.lower() == capital.lower(): #사용자가 입력한 값을 answer 변수에 저장
            print("정답!!")
        elif answer.lower() == "그만": # "그만"을 입력하면 루프 종료
            break
        else:
            print("아닙니다!!")

def print_capitals(): #print_capitals() 함수는 저장된 나라와 해당하는 수도 리스트 출력
    print("=================================")
    print("저장된 나라/수도 리스트")
    print("=================================")
    
    for country, capital in capitals.items(): #capitals.items()를 사용하여 딕셔너리의 모든 키값을 반복하면서 각 나라와 수도 출력
        print(f"{country}: {capital}")
    print("=================================")
    print(f"현재 총 {len(capitals)} 개의 수도가 입력되어 있습니다.")
    print("=================================")

#나라 입력하면 해당 나라 존재 확인 후 존재하지 않으면 해당 나라의 수도(도시)를 capitals 딕셔너리에 추가 
def add_capital():
    country = input("추가할 나라 입력 > ")
    
    if country in capitals: #이미 존재하는 나라인 경우 해당 메시지 출력
        print(f"{country} 는 이미 있습니다.")
    else:
        capital = input("추가할 수도(도시) 입력 > ")
        capitals[country] = capital

#수정할 나라 이름 입력받고, 해당 나라가 capitals  딕셔너리에 존재하는지 확인 후 존재하는 경우 수정할 수도(도시)의 이름을 입력받아 capitals 딕셔너리 수정
def modify_capital():
    country = input("수정할 나라를 입력하세요 : ")
    
    if country in capitals:
        capital = input("수정할 수도(도시) 이름을 입력해주세요 : ")
        capitals[country] = capital
    else: #나라가 존재하지 않는 경우 해당 메시지 출력
        print(f"{country}는 존재하지 않습니다.")

# 삭제할 나라 이름을 입력받으면 해당 나라가 capitals 딕셔vkfl너리에 존재하는지 확인 후 나라가 존재하면 del 키워드를 사용하여 해당 나라를 capitals 딕셔너리에서 삭제 및 삭제 완료 메시지 출력
def delete_capital():
    country = input("삭제할 나라를 입력하세요 : ")
    
    if country in capitals:
        del capitals[country]
        print("삭제가 완료되었습니다.")
    else: # 나라가 존재하지 않는다면 해당 메시지 출력
        print("등록된 나라가 아닙니다.")

def main_menu(): #메인 메뉴 함수 정의
    while True: #무한루프 시작
        print("========================")
        print("수도 맞추기 게임")
        print("========================")
        print("1. 게임시작")
        print("2. 정보 확인")
        print("3. 정보 추가")
        print("4. 정보 수정")
        print("5. 정보 삭제")
        print("6. 종료")
        
        choice = input(">> ")

        #사용자의 선택에 따라 다른 동작을 수행
        if choice == "1": #함수 호출하여 게임 시작
            guess_capital()

        elif choice == "2": #함수 호출하여 저장된 정보 확인
            print_capitals()

        elif choice == "3": #함수 호출하여 정보 추가 후 main_menu 함수 호출
            add_capital() #정보 추가 수행 함수
            main_menu()

        elif choice == "4": #입력을 받아서 수정 또는 삭제를 선택
            modify_choice = input("수정은 1, 삭제는 2를 입력해주세요 : ") #modify_choice 변수에 값을 입력받고
            if modify_choice == "1":
                modify_capital() #함수 호출
            elif modify_choice == "2":
                delete_capital() #함수 호출

        elif choice == "5":
            delete_capital()

        elif choice == "6":
            break

main_menu() #메인 메뉴 함수를 호출하여 다시 시작
