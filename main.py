import sys
from stats import char_count, get_book_text, num_of_works, to_sorted_list

def print_report(path, total_words, char_list):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}...")
  print("----------- Word Count ----------")
  print(f"Found {total_words} total words")
  print("--------- Character Count -------")
  for key in char_list:
    if key["char"].isalpha():
      print(f"{key['char']}: {key['num']}")
  print("============= END ===============")

def main():
  if len(sys.argv ) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  path = sys.argv[1] #"./books/frankenstein.txt"
  content = get_book_text(path)
  word_count = num_of_works(content)
  print(f"{word_count} words found in the document")
  all_chars = char_count(content)
  # print(all_chars)
  slist = to_sorted_list(all_chars)
  print(slist)
  print_report(path,word_count,slist)
main()