with open("word_list.txt", "r", encoding="utf-8") as f:
    for word in f:
        print(word.rstrip())