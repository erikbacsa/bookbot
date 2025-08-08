def get_num_words(text):
    text = text.split()
    num_words = len(text)
    return num_words

def get_num_letters(text):
    letters = {}
    for letter in text:
        letter = letter.lower()
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    return letters

def sort_letters(letters):
    dict_letters = []
    
    for key, value in letters.items():
        if key.isalpha():
            dict_letters.append({'char': key, 'num': value})
        
    dict_letters.sort(reverse=True, key=lambda letter: letter["num"])
    return dict_letters

def print_sorted_letters(sorted_letters):
    for item in sorted_letters:
        print(f"{item["char"]}: {item["num"]}")