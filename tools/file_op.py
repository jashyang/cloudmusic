#coding:utf-8
import codecs
import os

def write_file(name, content):
	file = codecs.open(name, "w", "utf-8")
	file.write(content)
	file.close()

def delete_file(name):
	os.remove(name)