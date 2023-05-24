#카운트 업 : start 부터 end까지 배열에 들어갈 수 구하기 ex. 3,10 [3,4,5,6,7,8,9,10]
def solution(start, end):
    answer = []
    for i in range(start, end+1):
        answer.append(i)
    return answer


#두 수의 곱
def solution(num1, num2):
    answer = 0
    answer = num1 * num2
    return answer


#나이 출력
def solution(age):
    answer = 0
    answer = (2022-age) + 1
    return answer


#잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    if (len(my_str) % n == 0):
        cnt = len(my_str) // n
    else:
        cnt = len(my_str) // n + 1
    start = 0
    lenth = len(my_str)
    for i in range(cnt):
        if lenth >= n:
            answer.append(my_str[start:(start + n)])
            start += n
            lenth -= n
        else:
            answer.append(my_str[start:(start + lenth)])

    return answer

#잘라서 배열로 저장하기 다른 답 (슬라이싱은 초과해도 에러가 발생하지 않음)
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]