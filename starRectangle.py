'''
문제 설명
이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

제한 조건
n과 m은 각각 1000 이하인 자연수입니다.
예시
입력

5 3
출력

*****
*****
*****
'''


#해결1
#입력된 두 숫자를 순서대로 n과 m에 대입시킨다
n, m = map(int, input().split())
if n<=1000 and m<=1000:
    #n개만큼 *출력 후 줄 바꾸기를 m번 출력
    print((('*'*n)+'\n')*m)


#해결2
#입력된 두 숫자를 순서대로 n과 m에 대입시킨다
a, b = map(int, input().split())
if a<=1000 and b<=1000:
    #b의 범위 중 i번 반복 즉, b번 반복 출력 후 반복이 끝나면 줄 바꾸기
    for i in range(b):
        #a범위 중 j번 반복 즉, a번 반복해서 출력 후 반복이 끝나면 끝
        for j in range(a):
            print('*', end='')
        print(end='\n')