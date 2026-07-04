sentence = input("enter sentence: ")
after_split = sentence.split()

print(f"after removing spaces : {sentence.strip()}")
print(f"after split into list: {sentence.split()}")
print(f"length of words: {len(after_split)}")
print(f"joined: {' - '.join(after_split)}")


