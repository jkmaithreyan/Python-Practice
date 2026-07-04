sentence = input("enter sentence: ")
print(f"characters count: {len(sentence.replace(" ",""))}")

list_sentence = sentence.split()
print(f"total words: {len(list_sentence)}")

list_sentence.reverse()
print(f"reversed: {' '.join(list_sentence)}")
search = input("enter word to search: ")
if search in sentence:
    print(f"{search} is found")
else:
    print("not found")
