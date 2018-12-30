import requests as R
import json
import bs4
import js2py
import os
import html
import time

S = R.session()


def get_headers():
    cookies_str = """
    :authority: www.toutiao.com
    :method: GET
    :path: /i6608430039597842948/
    :scheme: https
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    accept-encoding: gzip, deflate, br
    accept-language: zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7
    cache-control: no-cache
    dnt: 1
    pragma: no-cache
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
    """
    cs = cookies_str.split("\n")
    cookies = {}
    for i in range(len(cs)):
        pair = cs[i].split(": ")
        if pair.__len__() < 2:
            continue
        name = pair[0].strip(" ")
        value = pair[1].strip(" ")

        if name.startswith(":"):
            name = name[1:]
        cookies[f"{name}"] = value
    return cookies


# 公用request
def reqeuestFun(url=None):
    content = S.get(url, headers=get_headers()).text
    return content

offset = 0
# 获取新闻列表
def getNewsList(keyword):
    global offset
    url = f'https://www.toutiao.com/search_content/?offset={offset}&format=json&keyword={keyword}&autoload=true&count=20&cur_tab=1&from=search_tab&pd=synthesis'
    print(url)
    res = reqeuestFun(url)
    res = json.loads(res)
    arr = []
    for i in res['data']:
        if i.__contains__('abstract') and i['abstract'] != '' and i.__contains__('id'):
            print(i)
            arr.append({
                'abstract': i['abstract'],
                'id': i['id']
            })
        else:
            print('不存在')
    # 检查是否存在并获取详情
    validArr = checkRepeat(arr)
    for j in validArr:
        getNewsContent(j)

    offset+=20
    getNewsList(keyword)

# 获取新闻内容
def getNewsContent(idObj):
    print('延迟20秒')
    time.sleep(0)
    url = f'https://www.toutiao.com/a{idObj["id"]}/'
    res = reqeuestFun(url)
    soup = bs4.BeautifulSoup(res, 'html.parser')
    id1 = soup.find_all('script')
    try:
        pass
        ad = js2py.eval_js(id1[6].get_text())
        # print(ad)
        # 整合数据
        t = {}
        info = ad["articleInfo"]
        if info == None:
            return
        tags = info["tagInfo"]['tags']

        # 集合的集合序列化是有问题的，必须重新整理下
        new_tags = []
        for x in tags:
            new_tags.append(x["name"])
        tags = new_tags

        data = {
            "content": info["content"],
            "title": info["title"],
            "first_line": idObj["abstract"],
            "cover_img": info["coverImg"],
            "post_time": info["subInfo"]["time"],
            "index": idObj["id"],
            "tags": tags,
            "source": "",
            "img_count": "",
            "src_link": ""
        }
        saveNews(data)
    except:
        print('不是文章，换个ID重来')
        return


# 保存新闻内容
def saveNews(data):
    workPath = os.getcwd() + '/news/'
    path = workPath + str(data["index"])
    # 新建文件夹
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print('创建成功')
    else:
        print('文件夹已存在')

    # 保存内容为HTML
    content = html.unescape(data['content'])
    f = open(path + '/index.html', 'w', encoding='utf-8')
    f.write(content)
    f.close()

    downLoadImg(data, path)


# 下载图片
def downLoadImg(data, path):
    print('开始下载图片')
    res = open(path + '/index.html', 'r', encoding='utf-8')
    soup = bs4.BeautifulSoup(res, 'html.parser')
    allImg = soup.find_all('img')
    # 图片保存到本地
    for i in range(len(allImg)):
        bytes = S.get(allImg[i].get('src')).content
        with open(f'{path}/{i}.jpg', "wb") as f:
            f.write(bytes)
            f.close()
        allImg[i]["src"] = f'{i}.jpg'
        del allImg[i]["img_height"]
        del allImg[i]["img_width"]
        del allImg[i]["alt"]
        del allImg[i]["inline"]

    f = open(path + '/index.html', 'w', encoding='utf-8')
    soup = str(soup)
    f.write(soup)
    f.close()

    # 更新JSON信息
    try:
        updateJson(path,data)
    except:
        pass


# 更新JSON
def updateJson(path,data):
    data.pop("content")
    print('开始更新json')
    # 保存封面图
    bytes = S.get(data['cover_img']).content
    with open(path+'/cover_img.jpg', "wb") as f:
        f.write(bytes)
        f.close()
    data['cover_img'] = 'cover_img.jpg'
    # 更新json
    with open('News.json', mode='r+', encoding='utf-8') as f:
        gData = json.loads(f.read())
        gData.append(data)
        f.seek(0)
        f.write(json.dumps(gData))
    updateExist(data['index'])


# 更新已下载文件信息
def updateExist(id):
    with open('existNews.txt', mode='r+', encoding='utf-8') as f:
        gData = json.loads(f.read())
        gData.append(id)
        f.seek(0)
        f.write(json.dumps(gData))

# 检查是否重复
def checkRepeat(idArr):
    idList = open('existNews.txt', 'r', encoding='utf-8').read()
    idList = json.loads(idList)
    arr = []
    for i in idArr:
        arr.append(i['id'])
    # 排除已经下载的新闻
    effArr = []
    vaiArr = set(arr).difference(set(idList))
    for j in vaiArr:
        for t in idArr:
            if (t['id'] == j):
                effArr.append(t)
    return effArr


#     输入关键字
keyword=input()
getNewsList(keyword)
