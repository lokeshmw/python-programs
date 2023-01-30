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
