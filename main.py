
def main():
    book = "books/frankenstein.txt"
    text = get_text(book)
    #print(text)
    total_words = word_count(text)
    print(f"There are {total_words} total words found in the book\n\n\n")
    letters = letter_count(text)
    #print(letters)
    slist = parse_dict(letters)
    for k, v in slist.items():
        print(f"The letter {k} was found {v} times")

def get_text(book):
    with open(book) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    counter = 0
    for i in words:
        counter += 1
    return counter

def letter_count(text):
    ldict = {}
    lcstring = text.lower()
    
    for l in lcstring:
        if l.isalpha():
            if l not in ldict:
                ldict[l] = 1
            else:
                ldict[l] += 1
    return ldict

def parse_dict(ldict):
    sorted_dict = dict(sorted(ldict.items(), reverse=True, key=lambda item: item[1]))
    return sorted_dict

main()