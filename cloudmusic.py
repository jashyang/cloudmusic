#!/usr/bin/env python
# coding=utf-8

from tools.req import *
from tools.file_op import *

import threading
import json

class CloudMusic(threading.Thread): 
	phone = ""
	password = ""

	'''
	headers = {"Host": "115.29.202.191:3000",
				"Connection": "keep-alive",
				"Pragma": "no-cache",
				"Cache-Control": "no-cache",
				"Upgrade-Insecure-Requests": "1",
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
				"Accept-Encoding": "gzip, deflate",
				"Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"
				}
	'''
	headers = {}
	#cks = "MUSIC_U=ab60fee70716887249b3dd060c19099737eabf14720a26a2e5584ef047a76b3cf34da0a0397418534bf063f97dd7ddc0fe2897047e8106fb; __csrf=4d1f42cebf48dd37d6300881068581bd"
	cks = "MUSIC_U=ab60fee70716887249b3dd060c190997296da3909880e84e4dca606fa755c7cd148a1a4a8ace3403a97737574464569541049cea1c6bb9b6; __csrf=cf548c34b23021ce17c6826ed73f1c8d"
	uid = "106000356"

	def run(self):
		#self.phone_login(self.phone, self.password)
		#self.login_refresh()
		#self.get_user_playlist(self.uid)
		#self.get_personalized()
		self.get_songs()

	def phone_login(self, username, password):
		url = "http://115.29.202.191:3000/login/cellphone"
		pl = {}
		pl.update({"phone":username})
		pl.update({"password":password})
		res = req("GET", url, self.headers, pl)

		print res.headers
		print res.text
		#write_file("login_head.txt", res.headers)

	def login_refresh(self):
		url = "http://115.29.202.191:3000/login/refresh"
		pl = {}

		res = req("GET", url, self.headers, pl)

	def get_user_playlist(self, uid):
		url = "http://115.29.202.191:3000/user/playlist"
		pl = {}
		#pl.update({"Cookie": self.cks})
		#self.headers.update({"cookies": self.cks})
		pl.update({"uid": uid})

		res = req("GET", url, self.headers, pl)

		print res.headers
		#print res.text
		print res.text.encode("utf-8")

	def get_songs(self):
		# 日推
		url = "http://115.29.202.191:3000/recommend/songs"
		self.headers.update({"Cookie": self.cks})
		pl = {}

		res = req("GET", url, self.headers, pl)
		write_file("songs.txt", res.text)
		for song in json.loads(res.text)['recommend']:
			print song['name'] + ' - ' + song['artists'][0]['name']
		#write_file("test.txt", json.loads(res.text)['recommend'][0])

	def get_personalized(self):
		url = "http://115.29.202.191:3000/personalized/newsong"
		pl = {}
		pl.update({"Cookie": self.cks})

		res = req("GET", url, self.headers, pl)

		#print res.headers
		#print res.text.encode("utf-8")
		write_file("personalized.txt", res.text)

if __name__ == '__main__':
	cm = CloudMusic()
	cm.run()
