def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_size = get_words_count(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)
    print(words_size)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words_size} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_words_count(text):
    count = text.split()
    return len(count)


def get_book_text(path):
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


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=lambda x: x["num"])  # Sorting based on frequency of characters
    return sorted_list


if __name__ == "__main__":
    main()
