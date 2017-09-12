# coding: utf-8

from random import Random

def get_random(randomlength = 8):
	ran_str = ""
	chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
	length = len(chars) - 1
	random = Random()
	for i in range(randomlength):
		ran_str += chars[random.randint(0, length)]
	return ran_str