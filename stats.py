def get_book_words(text):
    words = text.split()
    return words

def get_char_presence(text):
    text = text.lower()
    unique_symbols = set()
    for i in range(0, len(text)):
        unique_symbols.add(text[i])

    unique_symbols = sorted(unique_symbols)
    chars = dict.fromkeys(unique_symbols, 0)

    for i in range(0, len(text)):
        chars[text[i]] += 1

    return chars

def structure_data(chars):
    char_info_list = []
    for c in chars:
        char_info = {"char": c, "num": chars[c]}
        char_info_list.append(char_info)

    char_info_list.sort(reverse=True, key=sort_num)
    return char_info_list

def sort_num(char_list):
    return char_list["num"]
        

    
