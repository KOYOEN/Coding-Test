from itertools import product
from collections import Counter

# 가능한 경우의 수
c_str = "01234567789abcdefghijklnmopqrstuvwxyz"

def solution(user_id, banned_id):
    # banned_id 의 경우에 대해 접근한다.
    banned_id = list(set(banned_id))
    for b_id in banned_id:
        # 마스킹 수에 대해 가능한 경우의 수에 대해 접근한다.
        num_mask = sum([1 for b in b_id if b == '*'])
        print(b_id, len(b_id), num_mask)
        # 만약 전부 * 이라면 해당 길이의 문자열은 다 삭제
        if num_mask == len(b_id):
            print("check")
            for u_id in user_id:
                if len(u_id) == num_mask:
                    user_id.remove(u_id)
            continue
        for case in product(c_str, repeat=num_mask):
            temp = ""
            i = 0
            # 마스킹 예측하는 값을 생성
            for t in b_id:
                if t == '*':
                    temp += case[i]
                    i += 1
                else :
                    temp += t

            # 생성한 값이 user_id에 존재한다면 삭제
            if temp in user_id:
                user_id.remove(temp)

        if len(user_id) == 0:
            break
                
    print(len(user_id))

    
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
