from stats import get_num_words, get_char_count, get_sort
import sys

if len(sys.argv) > 1:
	filename = sys.argv[1]
	with open(filename, encoding='utf-8', errors='ignore') as f:
		file_contents = f.read()
else:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

print("============ BOOKBOT ============")
print("Analyzing book found at... ")
print("----------- Word Count ----------")
print(get_num_words(file_contents))
print("--------- Character Count -------")
#print(get_char_count(file_contents))
print(get_sort(get_char_count(file_contents)))
print("============= END ===============")
