

def main():
    book_path = 'books/frankenstein.txt'
    print()
    print(f"--- Begin report of {book_path} ---")
    print()
  
    content = read_text(book_path)
    count = word_count(content)
    print(f"{count} words found in the document.")

    c = get_chars_dict(content)
    c = [(v, k) for k,v in c.items()]
    c.sort(reverse=True)
    for value, key in c:
        print(f"The {key} character was found {value} times")
    print("--- End report ---")




def read_text(book_path):
    with open(book_path, 'r') as f:
        return f.read() # returns a string and not a list 


def word_count(content):
    return len(content.split())

def character_count(content):
    content = content.lower()
    counts = {}
    for char in content:
        if char.isalpha():
            counts[char] = counts.get(char, 0)+1
    return  counts

def get_chars_dict(content):
    content = content.lower()
    chars = {}
    for char in content:
        if char.isalpha():
            if char in chars:
                chars[char] +=1
            else:
                chars[char] = 1
    return chars

main()