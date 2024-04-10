def solution(a, b):
    return 2*(a+b) if (a+b)%2 != 0 else (a**2 + b**2 if a%2 != 0 else abs(a-b))