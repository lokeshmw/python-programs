# with max
a = [231, 454, 45, 47, 70, 78, 2334, 555]
fir_large = a[0]
sec_large = a[1]
for i in a:
    if i >= fir_large:
        sec_large = fir_large
        fir_large = i
    else:
        sec_large = max(sec_large, i)

print(sec_large)


# without max
a = [231, 454, 45, 47, 70, 78, 2334, 555]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a[-2])
