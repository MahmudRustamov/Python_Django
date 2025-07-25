"""19. Berilgan listga 6000 dan keyin 7000 ni qo'shib qo'ying (xuddi rasmdagidek)..
    Input: [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    Output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
"""

ls = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
ls[2][2].append(7000)
print(ls)