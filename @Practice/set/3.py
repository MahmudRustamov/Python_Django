nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}

st = set()
for i in nums:
    if i % 2 == 0:
        st.add(i)
print(st)