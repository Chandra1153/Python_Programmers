def solution(arr):
    result = []
    for i in arr:
        if i >= 50:
            result.append(i) if i % 2 else result.append(i/2)
        else:
            result.append(i*2) if i % 2 else result.append(i)
    return result
