height = [1,8,6,2,5,4,8,3,7]

def maxwat(li: list) -> int:
    res = 0
    l, r = 0, len(li) -1

    while l < r:
        area = (r -l) * min(li[r], li[l])
        res = max(res,area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    
    return res

print(maxwat(height))
        