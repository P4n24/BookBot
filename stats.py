def get_num_words(file_contents):
        return f"Found {len(file_contents.split())} total words"

def get_char_count(file_contents):
	char_count = {}
	#loop through the string
	for i in file_contents.lower():
		# if the key is not already in the dictionary, add it with value of 1
		if i not in char_count:
			char_count[i] = 1
		# else create add 1 to the value
		else:
			char_count[i] += 1
	return char_count
