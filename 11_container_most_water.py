def contianer_water(height):
    l = 0
    j = len(height)-1
    max_area = 0
    while l < j:
        area = min(height[l], height[j])*(j-l)
        max_area = max(max_area, area)
        if height[l] < height[j]:
            l += 1
        else:
            j -= 1
    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(contianer_water(height))
