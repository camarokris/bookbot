def countwords(string):
    words = string.split()
    return len(words)

def countchar(string):
    string = string.lower()
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    #print(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{countwords(file_contents)} words found in the document\n")
    char_counts = countchar(file_contents)
    sorted_char_counts = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

main()