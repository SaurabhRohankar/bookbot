def main(filePath):
    print(f"--- Begin report of {filePath} ---")
    with open(filePath, "r") as f:
        file_contents = f.read()
        return file_contents

def count_words(content):
    words = content.split()
    total_words_count = len(words)
    print(f"{total_words_count} words found in the document")
    return total_words_count

def count_letters(content):
    content = content.lower()
    letters_count = {}
    for letter in content:
        if letter.isalpha():
            if letter in letters_count:
                letters_count[letter] += 1
            else:
                letters_count[letter] = 1
    
    result = [{"letter": letter, "count": count} for letter,count in letters_count.items()]
    return result

def sort_on(dict):
    return dict['count']

if __name__ == "__main__":
   file_content = main("./books/frakenstein.txt")
   count_words(file_content)
   letters_count = count_letters(file_content)
   letters_count.sort(reverse=True, key=sort_on)

   for pair in letters_count:
       print(f"The '{pair['letter']}' character was found {pair['count']} times")


