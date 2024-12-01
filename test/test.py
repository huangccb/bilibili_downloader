import re, requests, json
text = "https://www.bilibili.com/video/BV1wC4y1V7MK?spm_id_from=333.788.recommend_more_video.-1&vd_source=df46a6a2a12007dd3a36bbfe67ee9a46"
bvid = re.findall("https://www.bilibili.com/video/(.*?)\?.*?",text)

api = "https://api.bilibili.com/x/web-interface/view"
bvid = re.findall("https://www.bilibili.com/video/(.*?)\?.*?", text)[0]
params = {
    'bvid': bvid
}

cookies = {"SESSDATA":"b4d6c94b%2C1737081224%2Ca5f04%2A72CjDsMhrC9W_qoPnAWSfbko6_CmLRu17a_2pODiNbXfW9JDvlTFmFukxPkfjXUxI-O8ESVjhtc2hSTnJ0cVA0Z3NWT3JCeWhOWEpJMTNxSkNWUVNBYlVBR2V2MWY4NzBmRnZxdkxOektOTkR4bm4wWFowWThDeUFFa3VIMmdTdXUwYjY5QXpobDVRIIEC"}

#头文件
headers = {
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
"Referer" : "https://www.bilibili.com/",
}


res = requests.get(url=api, headers=headers, params=params, cookies=cookies).json()

with open("./video.json",'w') as f:
    json.dump(res, f, indent=4)
print(res['data']['cid'])