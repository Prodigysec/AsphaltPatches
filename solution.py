def solution(S):
    patches = 0
    index = 0
    while index < len(S):
        if S[index] == "X":
            patches += 1
            index += 3
        else:
            index += 1
        
    print("patches=>",patches)
        

solution(".X..X")
solution("X.XXXXX.X.")
solution("XX.XXX..")
solution("XXXX")
solution(".X...XX")