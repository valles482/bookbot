def get_num_words(filepath):
    num_words = 0
    with open(filepath) as file:
        for line in file:
            words = line.split()
            num_words += len(words)
            
    string = (num_words)
    return string

def count_characters(filepath):
    char_counts = {}
    with open(filepath) as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    char = char.lower()
                    if char not in char_counts:
                        char_counts[char] = 0
                    char_counts[char] += 1
    return char_counts

def sort_dictionary(char_counts):
    return dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
