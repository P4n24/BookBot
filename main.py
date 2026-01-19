
with open("./books/frankenstein.txt") as f:
	file_contents = f.read()
def num_words():
	return len(file_contents.split())
print(f"Found {num_words()} total words")
