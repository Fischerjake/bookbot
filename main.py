def main():
    with open("books/frakenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()
    # print(len(words))
    new_dict = {}

    for word in words:
        character_occurence(word,new_dict)
    book_length = len(words)
    word_list = dictionary_convert_to_list(new_dict)
    word_list.sort(reverse=True, key=sort_dictionary)
    print_report(word_list, book_length)

def sort_dictionary(dict1):
    key = [i for i in dict1.keys()][0]
    return dict1[key]
def character_occurence(word, dict1):
    for char in word:
        char = char.lower()
        if char not in dict1:
            dict1[char] = 1
        else:
            dict1[char] += 1

def dictionary_convert_to_list(dict1):
    new_list = []
    for char in dict1:
        if char.isalpha():
            base_dict = {char : dict1[char]}
            new_list.append(base_dict)
    return new_list


def print_report(word_list, word_length):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_length} words found in the document")
    for i in word_list:
        for key in i:
            print(f"The {key} character was found {i[key]} times")
    print("--- End report ---")
main()