def calculate_number_of_words(book):
  separated_text = book.split()
  count = 0
  for word in separated_text:
    count += 1
  return count

def calculate_number_of_characters(book):
  separated_text = book.lower()
  char_count = {}
  for char in separated_text:
    if char not in char_count:
      char_count[char] = 1
    elif char in char_count:
      char_count[char] += 1
  return char_count