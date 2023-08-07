
# 프로그래머스에서는 동작, 일반 파이썬에서는 입력값을 받는 부분도 구현해줘야 한다.
def solution(nums):
    dict = {}
    for i in range(len(nums)):
        if (nums[i] in dict): # 해시함수에 존재하면
            continue # 그냥 진행
        else: # 존재하지 않으면
            dict[nums[i]] = 0 # dictionary에 추가
    if len(dict) >= len(nums) / 2: # 만약 dictionary의 길이보다, nums의 길이가 더 작거나 같다면
        answer = len(nums)/2 # nums의 길이로 답을 설정
    else:
        answer = len(dict)
    return answer