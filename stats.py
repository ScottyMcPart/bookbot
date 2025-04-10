def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    result={}

    for char in text.lower():
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result

def sort_on_count(dict):
    return dict["count"]

def sort_char_list(char_dict):
    result = []

    for key, value in char_dict.items():
        if(key.isalpha()):
            result.append({"char": key, "count": value})

    result.sort(reverse=True, key=sort_on_count)

    return result