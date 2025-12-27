def get_book_text(path_to_file):
  with open(path_to_file) as file:
    file_contents = file.read()
  return file_contents

def calculate_number_of_words(book):
  separated_text = book.split()
  count = 0
  for word in separated_text:
    count += 1
  return count

def main():
  book = get_book_text("books/frankenstein.txt")
  print(f"Found {calculate_number_of_words(book)} total words")

main()