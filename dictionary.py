with open("word_list.txt", "r", encoding="utf-8") as f:
    for idx, word in enumerate(f, start=1):
        print(f"{idx}:", word.rstrip())