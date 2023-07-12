def odd_sum():
    num = 0
    for i in range(11):
        if i % 2 == 0:
            continue
        num = num + i

    
    return num 
    print(f'0부터 10까지 짝수ㅇㅇㅇㅇ의 합은 {num} 입니다.')


hoho = odd_sum()
# print(f'0부터 10까지 홀수의 합은 {hoho} 입니다.')