import sys
from collections import Counter

def main():
    txt = sys.argv[1]
    clean = clean_text(txt)
    print(wordcount(clean))


def clean_text(str):
    txt = str
    for char in "-.',\n":
        txt = txt.replace(char, ' ')
    return txt.lower()


def wordcount(str):
    word_list = str.split()
    return Counter(word_list).most_common()


if __name__ == "__main__":
    main()
