
def build(S):
    ans = []
    for c in S:
        if c != '#':
            ans.append(c)
        else:
            if ans:
                ans.pop()
    return "".join(ans)

def backspaceCompare(s: str, t: str) -> bool:
    return build(s) == build(t)

print(backspaceCompare('ab##', 'c#d#'))
