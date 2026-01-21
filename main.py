from stats import get_num_words, get_char_count, get_sort

with open("./books/frankenstein.txt") as f:
	file_contents = f.read()
print("============ BOOKBOT ============")
print("Analyzing book found at... ")
print("----------- Word Count ----------")
print(get_num_words(file_contents))
print("--------- Character Count -------")
#print(get_char_count(file_contents))
print(get_sort(get_char_count(file_contents)))
print("============= END ===============")
