s = input()
length = int(len(s)/2)
count = ''
for i in range(length):
    last = s[-i-1]
    if s[i] == last:
        count += s[i]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(count)
