sentence = input("enter sentence: ")
words = sentence.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

print(word_count)

most_repeated = None
highest_count = 0

for word in word_count:
    if word_count[word] > highest_count:
        highest_count = word_count[word]
        most_repeated = word

print(f"Total words: {len(words)}")
print(f"Word counts:")
for word in word_count:
    print(f"{word} -> {word_count[word]}")
print(f"Most repeated: {most_repeated} ({highest_count} times)")