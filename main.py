def get_num_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

def main():
    path = 'books/frankenstein.txt'
    text = get_text(path)
    num_words = get_num_words(text)
    print(f'The book has {num_words} words.')

if __name__ == '__main__':
    main()
