def get_book_text(path):
  with open(path) as file:
    return file.read()

def num_of_works(content):
  return len(content.split())

def char_count(content):
  all_chars =  {}
  for char in content:
    if char.lower() not in all_chars:
      all_chars[char.lower()] = 0
    all_chars[char.lower()] += 1
  return all_chars

def sort_on(dict):
  return dict["num"]

def to_sorted_list(all_chars):
  slist = []
  for key in all_chars:
    slist.append({"char": key, "num": all_chars[key]})
  slist.sort(reverse=True, key=sort_on)
  return slist