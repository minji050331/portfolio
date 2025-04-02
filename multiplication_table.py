while True:
    # 사용자에게 몇 단까지 출력할지 입력 받기
    print('몇단까지 출력할까요(2~9단, 나머지 정수 입력시 종료)')
    num = int(input('>>'))

    if num >= 2 and num <= 9:
        if num <= 5:
            # 2단부터 입력받은 숫자까지의 구구단 출력
            for i in range(1, 10):
                for j in range(2, num + 1):
                    print(j, '*', i, '=', j * i, end=' ')
                print()
            print()

        else:
            # 2단부터 5단까지 출력
            for i in range(1, 10):
                for j in range(2, 6):
                    print(j, '*', i, '=', j * i, end=' ')
                print()
            print()

            # 6단부터 입력받은 숫자까지의 구구단 출력
            for i in range(1, 10):
                for j in range(6, num + 1):
                    print(j, '*', i, '=', j * i, end=' ')
                print()
            print()

    else:
        # 프로그램 종료 메시지 출력
        print('이용해주셔서 감사합니다.')
        print('개발자 : 김민지(20243578)')
        break
