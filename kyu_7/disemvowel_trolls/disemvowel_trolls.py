#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def disemvowel(string):
	"""
	A function that takes a string and return
	a new string with all vowels removed.

	For example, the string "This website is
	for losers LOL!" would become "Ths wbst s fr lsrs LL!".

	Note: for this kata y isn't considered a vowel.
	:param string:
	:return:
	"""
	vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

	return ''.join(char for char in string if char not in vowels)
