from itertools import permutations

def isMatch(user_set, banned_set):
    # 선택된 user_set 집합이 banned_set의 목록들에 순서까지 맞아떨어지는가?
    for i in range(len(user_set)):
        # 길이가 맞지 않다면 False
        if len(user_set[i]) != len(banned_set[i]):
            return False
        # 마스킹 이외에 모든 부분은 같은가?
        for j in range(len(user_set[i])):
            if banned_set[i][j] == '*':
                continue
            if user_set[i][j] != banned_set[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    ans = []
    for com_set in permutations(user_id, len(banned_id)):
        # user_id 중 banned_id의 수에 해당하는 만큼 고르자. 단, banned_id와의 순서를 고려해서 순열을 활용한다.
        if isMatch(com_set, banned_id):
            # 들어갈 때는 순서에 상관없이 같은 경우로 봐야하기 때문에 set으로 변경
            com_set = set(com_set) # 중복 제거
            if com_set not in ans:
                ans.append(com_set)
    return len(ans)
        
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
