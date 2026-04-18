import sys
start = int(sys.argv[1])
end = int(sys.argv[2])
maxlen = int(sys.argv[3]) if len(sys.argv) > 3 else 300
with open('index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if i >= start and i <= end:
            print(f"{i}: {line.rstrip()[:maxlen]}")
        if i > end:
            break
