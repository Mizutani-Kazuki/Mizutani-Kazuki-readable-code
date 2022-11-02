import argparse

def make_words_dict():
    """
    txtファイルから複数の文字を読み取り、IDをつけて辞書を作成する関数

    Return
    ------
    word_dict: dictionary
        言葉とIDが連携された辞書
    """
    with open("word_list.txt", "r", encoding="utf-8") as f:
        word_dict = dict()
        for idx, word in enumerate(f, start=1):
            word_dict[idx] = word.rstrip()
    return word_dict


def output_specified_word(idx=None):
    """
    指定されたIDの言葉を出力する

    Parameters
    ----------
    idx: int (default None)
        出力したいID
    """
    # 言葉とIDが連携された辞書の作成
    word_dict = make_words_dict()

    if idx:
        print(f"{idx}:", word_dict[idx])
    else:
        for i, word in word_dict.items():
            print(f"{i}:", word_dict[i])


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='指定されたIDの言葉を出力するプログラム')
    parser.add_argument('-i', '--idx', type=int, help='言葉のID')
    args = parser.parse_args()
    output_specified_word(args.idx)
