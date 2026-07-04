paragraph = input("enter a paragraph: ")
list_paragraph = paragraph.lower().split()

print(f"total character with space: {len(paragraph)}")
print(f"total character without space: {len(paragraph.replace(' ',''))}")
print(f"total words: {len(list_paragraph)}")
print(f"total sentence: {paragraph.count('.') + paragraph.count('!') + paragraph.count('?')}")

container = {}
for word in list_paragraph:
    if word in container:
        container[word] = container[word] + 1
    else:
        container[word] = 1

most_repeated = None
highest_count = 0
for word in container:
    if container[word] > highest_count:
        highest_count = container[word]
        most_repeated = word

print(f"most repeated word: {most_repeated}({highest_count} times)")
if paragraph[0] in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    print("yes, paragraph start with capital letter")
else:
    print("no, paragraph does not start with capital letter")