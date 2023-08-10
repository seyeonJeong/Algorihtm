
# 해시를 쓰지 않고 풀 수 있는 방법이다.

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if (participant[i] != completion[i]):
            return participant[i]

    return participant[-1]


# 밑에서부터는 해시를 쓰는 방법

def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    for part in participant:
        hashDict[hash(part)] = part # hash(part)를 하게되면, 그 key값에 해당되는, 해시 값이 형성이된다.
        sumHash += hash(part) # sumHash에 더해준다.

    for comp in completion:
        sumHash -= hash(comp) # 여기서 완주자의 해시 값을 빼준다.

    return hashDict[sumHash] # 남아있는 해시값(key)의 값(value)가 완주하지 못한 사람이다.


