#coding:utf-8

import json
from req import *

url = "http://api.kekaoyun.com/article/list"
headers = {}
params = {
	"key": "fa4423921a97e5e2a3e528271a0e71a2",
}

def get_shehui():
	return _getmsg(u"社会新闻\r\n", 1007)

def get_guonei():
	return _getmsg(u"国内新闻\r\n", 1004)

def get_guonji():
	return _getmsg(u"国际新闻\r\n", 1005)

def get_caijing():
	return _getmsg(u"财经新闻\r\n", 1010)

def _getmsg(name, cid, page = 1, rows = 5, dtype = "JSON"):
	msg = name

	params.update({"cid": cid})
	params.update({"page": page})
	params.update({"rows": rows})
	params.update({"dtype": dtype})

	json_res = req("GET", url, headers, params)
	parsed_json = json.loads(json_res)
	for i in range(rows):
		msg += str(i + 1) + ". " + parsed_json["result"][i]["title"] + "\r\n"

	msg += "\r\n"
	return msg
