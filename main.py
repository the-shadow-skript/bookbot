from stats import calculate_number_of_words, calculate_number_of_characters

def get_book_text(path_to_file):
  with open(path_to_file) as file:
    file_contents = file.read()
  return file_contents

def main():
  book = get_book_text("books/frankenstein.txt")
  character_count = calculate_number_of_characters(book)
  print(f"Found {calculate_number_of_words(book)} total words")
  print(character_count)

main()