
from collections import Counter

input_list = ['hello world', 'world of programming', 'hello programming']

word_count = Counter(lambda phrase: phrase.split(), input_list)
word_count_dict = dict(word_count)

print(word_count_dict)