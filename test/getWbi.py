from functools import reduce
from hashlib import md5
import json
import urllib.parse
import time
import requests
class GetWbi():
    def __init__(self):
        
        self.mixinKeyEncTab = [
            46, 47, 18, 2, 53, 8, 23, 32, 15, 50, 10, 31, 58, 3, 45, 35, 27, 43, 5, 49,
            33, 9, 42, 19, 29, 28, 14, 39, 12, 38, 41, 13, 37, 48, 7, 16, 24, 55, 40,
            61, 26, 17, 0, 1, 60, 51, 30, 4, 22, 25, 54, 21, 56, 59, 6, 63, 57, 62, 11,
            36, 20, 34, 44, 52
        ]

    def getMixinKey(self, orig: str):
        '对 imgKey 和 subKey 进行字符顺序打乱编码'
        return reduce(lambda s, i: s + orig[i], self.mixinKeyEncTab, '')[:32]

    def encWbi(self, params: dict, img_key: str, sub_key: str):
        '为请求参数进行 wbi 签名'
        mixin_key = self.getMixinKey(img_key + sub_key)
        curr_time = round(time.time())
        params['wts'] = curr_time                                   # 添加 wts 字段
        params = dict(sorted(params.items()))                       # 按照 key 重排参数
        # 过滤 value 中的 "!'()*" 字符
        params = {
            k : ''.join(filter(lambda chr: chr not in "!'()*", str(v)))
            for k, v 
            in params.items()
        }
        query = urllib.parse.urlencode(params)                      # 序列化参数
        wbi_sign = md5((query + mixin_key).encode()).hexdigest()    # 计算 w_rid
        params['w_rid'] = wbi_sign
        return params

    def getWbiKeys(self) -> tuple[str, str]:
        '获取最新的 img_key 和 sub_key'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Referer': 'https://www.bilibili.com/'
        }

        cookie = {"SESSDATA": 'b4d6c94b%2C1737081224%2Ca5f04%2A72CjDsMhrC9W_qoPnAWSfbko6_CmLRu17a_2pODiNbXfW9JDvlTFmFukxPkfjXUxI-O8ESVjhtc2hSTnJ0cVA0Z3NWT3JCeWhOWEpJMTNxSkNWUVNBYlVBR2V2MWY4NzBmRnZxdkxOektOTkR4bm4wWFowWThDeUFFa3VIMmdTdXUwYjY5QXpobDVRIIEC'}
        resp = requests.get('https://api.bilibili.com/x/web-interface/nav', headers=headers, cookies=cookie)
        resp.raise_for_status()
        json_content = resp.json()
        img_url: str = json_content['data']['wbi_img']['img_url']
        sub_url: str = json_content['data']['wbi_img']['sub_url']
        img_key = img_url.rsplit('/', 1)[1].split('.')[0]
        sub_key = sub_url.rsplit('/', 1)[1].split('.')[0]
        return img_key, sub_key
    
    def getWbi(self):
        wbi = GetWbi()
        img_key, sub_key = wbi.getWbiKeys()

        signed_params = wbi.encWbi(
            # params={
            #     'foo': '114',
            #     'bar': '514',
            #     'baz': 1919810
            # },
            params = {
                'bvid': 'BV1YnUQYcEX8',
                'qn':'80',
                'fnval':'1',
                'cid':'26877362549',
                #'SESSDATA':'b4d6c94b%2C1737081224%2Ca5f04%2A72CjDsMhrC9W_qoPnAWSfbko6_CmLRu17a_2pODiNbXfW9JDvlTFmFukxPkfjXUxI-O8ESVjhtc2hSTnJ0cVA0Z3NWT3JCeWhOWEpJMTNxSkNWUVNBYlVBR2V2MWY4NzBmRnZxdkxOektOTkR4bm4wWFowWThDeUFFa3VIMmdTdXUwYjY5QXpobDVRIIEC'
            },
            img_key=img_key,
            sub_key=sub_key
        )
        query = urllib.parse.urlencode(signed_params)
        return query

if __name__ == '__main__':
    param = GetWbi().getWbi()
    cookie = {"SESSDATA": 'b4d6c94b%2C1737081224%2Ca5f04%2A72CjDsMhrC9W_qoPnAWSfbko6_CmLRu17a_2pODiNbXfW9JDvlTFmFukxPkfjXUxI-O8ESVjhtc2hSTnJ0cVA0Z3NWT3JCeWhOWEpJMTNxSkNWUVNBYlVBR2V2MWY4NzBmRnZxdkxOektOTkR4bm4wWFowWThDeUFFa3VIMmdTdXUwYjY5QXpobDVRIIEC'}
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Referer': 'https://www.bilibili.com/'
        }
    url = "https://api.bilibili.com/x/player/wbi/playurl?" + param
    resp = requests.get(url, headers=headers, cookies=cookie).json()
    #t = json.loads(resp)
    url = resp['data']['durl'][0]['url']
    video = requests.get(url, headers=headers, cookies=cookie).content
    with open('./video.mp4','wb') as f:
        f.write(video)
    print(resp['data']['durl'][0]['url'])
    with open ('./video.json','w') as f:
        json.dump(resp,f, indent=4)
