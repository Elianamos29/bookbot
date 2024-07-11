def get_num_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict['num']

def sort_chars_dict(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({'char': ch, 'num': num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def generate_report(path):
    print(f'--- Begin report of {path} ---')
    text = get_text(path)
    num_words = get_num_words(text)
    print(f'{num_words} words found in the document')
    print()
    
    chars_dict = get_chars_dict(text)
    sorted_chars_dict = sort_chars_dict(chars_dict)
    for item in sorted_chars_dict:
        if not item['char'].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print('--- End report --')

def main():
    path = 'books/frankenstein.txt'
    generate_report(path)

if __name__ == '__main__':
    main()
