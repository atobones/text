text = "hello world wonderful world"
map = {}

for word in text.split():
    map.setdefault(word, 0)
    map[word] += 1

print(map) 