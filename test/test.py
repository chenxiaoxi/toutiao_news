# coding=gbk
import requests
import bs4
import json

res = open('test.html', 'r', encoding='utf-8')
soup = bs4.BeautifulSoup(res, 'html.parser')
allImg = soup.find_all('img')

# ���浽����
for i in range(len(allImg)):
    # bytes = requests.get(allImg[i].get('src')).content
    # ͼƬ���浽����
    # with open(r'G:\chenxi\LuProject\test\toutiao\news\6210604417477017857/'+f'{i}.jpg',"wb") as f:
    # 	f.write(bytes)
    # 	f.close()
    # allImg[i]["src"] = f'{i}.jpg'
    allImg[i]["class"] = 'ImageLayout'
# print(soup)


a = {'title': '������Լ��˾����ӭ�����󿼡� ��Ȼ����Ӣ���',
     'first_line': '������Լ��˾����ӭ�����󿼡������գ������н�ί������Լ�������Ŀ���٣����������ݲ����漰·��·�ߡ����ĵ����Ȼ���֪ʶ�����������ݳ�ò����ʻ�����ȡ�Ӳͨ������ֵ��һ����ǣ������Ŀ�����ܷ�Ϊ100�֣�80��Ϊ�����ߡ�',
     'cover_img': 'http://p9.pstatp.com/list/300x196/13540012bc3e281b676f.jpg', 'post_time': '2017-01-13 14:27:54',
     'index': '6374926754255094018', 'tags': [{'name': 'Ӣ��'}, {'name': 'BASIC����'}, {'name': '����'}], 'source': '',
     'img_count': '', 'src_link': ''}

b = [{'title': '������Լ��˾����ӭ�����󿼡� ��Ȼ����Ӣ���',
      'first_line': '������Լ��˾����ӭ�����󿼡������գ������н�ί������Լ�������Ŀ���٣����������ݲ����漰·��·�ߡ����ĵ����Ȼ���֪ʶ�����������ݳ�ò����ʻ�����ȡ�Ӳͨ������ֵ��һ����ǣ������Ŀ�����ܷ�Ϊ100�֣�80��Ϊ�����ߡ�',
      'cover_img': 'http://p9.pstatp.com/list/300x196/13540012bc3e281b676f.jpg', 'post_time': '2017-01-13 14:27:54',
      'index': '6374926754255094018', 'tags': [{'name': 'Ӣ��'}, {'name': 'BASIC����'}, {'name': '����'}], 'source': '',
      'img_count': '', 'src_link': ''}, {'title': '������Լ��˾����ӭ�����󿼡� ��Ȼ����Ӣ���',
                                         'first_line': '������Լ��˾����ӭ�����󿼡������գ������н�ί������Լ�������Ŀ���٣����������ݲ����漰·��·�ߡ����ĵ����Ȼ���֪ʶ�����������ݳ�ò����ʻ�����ȡ�Ӳͨ������ֵ��һ����ǣ������Ŀ�����ܷ�Ϊ100�֣�80��Ϊ�����ߡ�',
                                         'cover_img': 'http://p9.pstatp.com/list/300x196/13540012bc3e281b676f.jpg',
                                         'post_time': '2017-01-13 14:27:54', 'index': '6374926754255094018',
                                         'tags': [{'name': 'Ӣ��'}, {'name': 'BASIC����'}, {'name': '����'}], 'source': '',
                                         'img_count': '', 'src_link': ''}]
# print(json.loads(b))
with open('News.json', mode='r+', encoding='utf-8') as f:
    gData = json.loads(f.read())
    print(gData)
    gData.append(a)
    print(gData)
    f.seek(0)
    f.write(json.dumps(gData))

a = {'play_effective_count': '1934', 'open_url': '/group/6638784662325953031/', 'media_name': '��֦����', 'read_count': 1553, 'media_url': 'http://toutiao.com/m6976379136/', 'item_source_url': '/group/6638784662325953031/', 'labels': [], 'image_list': [{'url': '//p3-tt.bytecdn.cn/list/tos-cn-i-0000/af6afb1b4ec04f65bd98a665d471a77c'}], 'media_avatar_url': '//p3.pstatp.com/medium/78f0014658e65b8ee69', 'datetime': '2018-12-25 16:54:00', 'more_mode': False, 'create_time': '1545728040', 'has_gallery': False, 'video_duration': 246, 'id': '6638784662325953031', 'user_id': 6976474883, 'title': '����Űͯ�¼���Ů�������⸸ĸ���Ź���ֶβ��̲���ֱ�ӣ�', 'show_play_effective_count': 1, 'has_video': True, 'share_url': 'http://vod.v.jstv.com/2018/12/25/JSTV_JSGG_1545704210235_vx5w0x3_2578.mp4', 'source': '��֦����', 'comment_count': 8, 'article_url': 'http://vod.v.jstv.com/2018/12/25/JSTV_JSGG_1545704210235_vx5w0x3_2578.mp4', 'group_source': 2, 'comments_count': 8, 'large_mode': False, 'abstract': '����Űͯ�¼� Ů��������Ź�� �ֶβ��̲���ֱ��', 'large_image_url': 'http://p1-tt.bytecdn.cn/large/tos-cn-i-0000/af6afb1b4ec04f65bd98a665d471a77c', 'display_time': '1545728040', 'publish_time': '1545728040', 'middle_mode': True, 'media_creator_id': 6976474883, 'tag_id': 6638784662325953031, 'source_url': '/group/6638784662325953031/', 'video_duration_str': '04:06', 'item_id': '6638784662325953031', 'user_auth_info': {'auth_type': '0', 'auth_info': '���չ�缯����֦���ſͻ��˹ٷ��˺�'}, 'seo_url': '/group/6638784662325953031/', 'keyword': '����', 'single_mode': True, 'middle_image_url': 'http://p3-tt.bytecdn.cn/list/300x196/tos-cn-i-0000/af6afb1b4ec04f65bd98a665d471a77c', 'digg_count': 19, 'behot_time': '1545728040', 'tag': 'video_domestic', 'image_url': '//p3-tt.bytecdn.cn/list/tos-cn-i-0000/af6afb1b4ec04f65bd98a665d471a77c', 'has_image': True, 'highlight': {'source': [], 'abstract': [[0, 2]], 'title': [[0, 2]]}, 'group_id': '6638784662325953031', 'image_count': 0}
{'open_url': '/group/6638172227114107406/', 'media_name': '�Ϸ����б�', 'read_count': 213648, 'media_url': 'http://toutiao.com/m5827361912/', 'item_source_url': '/group/6638172227114107406/', 'labels': [], 'image_list': [{'url': '//p3-tt.bytecdn.cn/list/pgc-image/RD3ZpDOIwGhmL'}], 'media_avatar_url': '//p1.pstatp.com/medium/18a400112cb3ea178df2', 'datetime': '2018-12-23 20:58:32', 'more_mode': False, 'create_time': '1545569912', 'has_gallery': False, 'id': '6638172227114107406', 'user_id': 5827361912, 'title': '̽��������ŰŮͯ���������Ƶ�����ߵ��ĺ��ӳ��������˸�', 'show_play_effective_count': 0, 'has_video': False, 'share_url': 'https://rsstoutiao.oeeee.com/mp/toutiao/BAAFRD000020181223125960.html', 'source': '�Ϸ����б�', 'comment_count': 345, 'article_url': 'https://rsstoutiao.oeeee.com/mp/toutiao/BAAFRD000020181223125960.html', 'group_source': 2, 'comments_count': 345, 'large_mode': False, 'abstract': '������һСŮ�����Ƽ����⸸ĸŹ������ţ��������������������������¡�12��23�����磬���ڱ�������ͨ������ĸŰͯ��Ƶ����������Ůͯ��ĸ�׶�Ź���ӵ���Ϊ���ϲ��䡣', 'large_image_url': 'http://p1-tt.bytecdn.cn/large/pgc-image/RD3ZpDOIwGhmL', 'display_time': '1545569912', 'publish_time': '1545569912', 'middle_mode': True, 'media_creator_id': 5827361912, 'tag_id': 6638172227114107406, 'source_url': '/group/6638172227114107406/', 'item_id': '6638172227114107406', 'user_auth_info': {'auth_type': '0', 'auth_info': '�Ϸ����б��ٷ��˺�'}, 'seo_url': '/group/6638172227114107406/', 'keyword': '����', 'single_mode': True, 'middle_image_url': 'http://p3-tt.bytecdn.cn/list/300x196/pgc-image/RD3ZpDOIwGhmL', 'digg_count': 542, 'behot_time': '1545569912', 'tag': 'news_society', 'image_url': '//p3-tt.bytecdn.cn/list/pgc-image/RD3ZpDOIwGhmL', 'has_image': True, 'highlight': {'source': [], 'abstract': [[1, 2], [43, 2]], 'title': [[2, 2]]}, 'group_id': '6638172227114107406', 'image_count': 1}
������
������
{'play_effective_count': '97��', 'open_url': '/group/6638070123238261252/', 'media_name': '������', 'read_count': 407469, 'media_url': 'http://toutiao.com/m3507812656/', 'item_source_url': '/group/6638070123238261252/', 'labels': [], 'image_list': [{'url': '//p3-tt.bytecdn.cn/list/pgc-image/7c8978e904844ffa8de6544661ba85f1'}], 'media_avatar_url': '//p3.pstatp.com/medium/364500122cf11186f98d', 'datetime': '2018-12-23 14:22:19', 'more_mode': False, 'create_time': '1545546139', 'has_gallery': False, 'video_duration': 79, 'id': '6638070123238261252', 'user_id': 3507130514, 'title': '�����ϳͣ�СŮ���ڼұ����Ź�����ھ����������', 'show_play_effective_count': 1, 'has_video': True, 'share_url': 'http://toutiao.com/group/6638070123238261252/', 'source': '������', 'comment_count': 45095, 'article_url': 'http://toutiao.com/group/6638070123238261252/', 'group_source': 2, 'comments_count': 45095, 'large_mode': False, 'abstract': '\u200b\u200b���죬һ�����ڸ�ĸ����Űͯ����Ƶ������ע����Ƶ��ʾ������10���ڼ䣬һŮ���ڼ���д��ҵ�ͳԷ������б��ҳ�����Ź�򣬳������⣬��ס����ͷ���򣬺���ĸ�׻���ɨ�ѡ��������ӵ���ƷŹ���ӡ������������������ֹ������İְֳ��ֺ�Ҳ��Ů������Ź����һĻĻ������ͷ����������', 'large_image_url': 'http://p3-tt.bytecdn.cn/large/pgc-image/7c8978e904844ffa8de6544661ba85f1', 'display_time': '1545546139', 'publish_time': '1545546139', 'middle_mode': True, 'media_creator_id': 3507130514, 'tag_id': 6638070123238261252, 'source_url': '/group/6638070123238261252/', 'video_duration_str': '01:19', 'item_id': '6638070123238261252', 'user_auth_info': {'auth_type': '0', 'auth_info': '�����ձ����ٷ��˺�'}, 'seo_url': '/group/6638070123238261252/', 'keyword': '����', 'single_mode': True, 'middle_image_url': 'http://p9-tt.bytecdn.cn/list/300x196/pgc-image/7c8978e904844ffa8de6544661ba85f1', 'digg_count': 5840, 'behot_time': '1545546139', 'tag': 'video_domestic', 'image_url': '//p3-tt.bytecdn.cn/list/pgc-image/7c8978e904844ffa8de6544661ba85f1', 'has_image': True, 'highlight': {'source': [], 'abstract': [[7, 2]], 'title': [[16, 2]]}, 'group_id': '6638070123238261252', 'image_count': 1}
{'open_url': '/group/6638156562558878221/', 'media_name': '�Ϸ����б�', 'read_count': 261186, 'media_url': 'http://toutiao.com/m5827361912/', 'item_source_url': '/group/6638156562558878221/', 'labels': [], 'image_list': [{'url': '//p3-tt.bytecdn.cn/list/pgc-image/RD1biU2CKcqKyB'}, {'url': '//p3-tt.bytecdn.cn/list/pgc-image/RD1biSC5bYZQIE'}], 'media_avatar_url': '//p1.pstatp.com/medium/18a400112cb3ea178df2', 'datetime': '2018-12-23 19:57:45', 'more_mode': False, 'create_time': '1545566265', 'has_gallery': False, 'id': '6638156562558878221', 'user_id': 5827361912, 'title': '����Űͯ��Ƶ�����߽�����Դ���ƴ�app���أ��·���ͥװ�м��', 'show_play_effective_count': 0, 'has_video': False, 'share_url': 'https://rsstoutiao.oeeee.com/mp/toutiao/BAAFRD000020181223125955.html', 'source': '�Ϸ����б�', 'comment_count': 382, 'article_url': 'https://rsstoutiao.oeeee.com/mp/toutiao/BAAFRD000020181223125955.html', 'group_source': 2, 'comments_count': 382, 'large_mode': False, 'abstract': 'Ŀǰ���϶�������ϵ��������������Ƶ��΢�����ѡ������񡱣������߼��ߣ���Ƶ�Ǵ�һ����ͥ���app�����صġ�', 'large_image_url': 'http://p3-tt.bytecdn.cn/large/pgc-image/RD1biU2CKcqKyB', 'display_time': '1545566265', 'publish_time': '1545566265', 'middle_mode': True, 'media_creator_id': 5827361912, 'tag_id': 6638156562558878221, 'source_url': '/group/6638156562558878221/', 'item_id': '6638156562558878221', 'user_auth_info': {'auth_type': '0', 'auth_info': '�Ϸ����б��ٷ��˺�'}, 'seo_url': '/group/6638156562558878221/', 'keyword': '����', 'single_mode': True, 'middle_image_url': 'http://p1-tt.bytecdn.cn/list/300x196/pgc-image/RD1biU2CKcqKyB', 'digg_count': 879, 'behot_time': '1545566265', 'tag': 'news_society', 'image_url': '//p3-tt.bytecdn.cn/list/pgc-image/RD1biU2CKcqKyB', 'has_image': True, 'highlight': {'source': [], 'abstract': [], 'title': [[0, 2]]}, 'group_id': '6638156562558878221', 'image_count': 2}
{'play_effective_count': '7��', 'open_url': '/group/6639136096645022212/', 'media_name': '�����������ռ�', 'read_count': 61510, 'media_url': 'http://toutiao.com/m1577130506463245/', 'item_source_url': '/group/6639136096645022212/', 'labels': [], 'image_list': [{'url': '//p3-tt.bytecdn.cn/list/tos-cn-i-0000/f928a96ae4fb45bf91cfdc3a898a552b'}], 'media_avatar_url': '//p3.pstatp.com/medium/6eda0001e80f5bf0ce64', 'datetime': '2018-12-26 11:41:27', 'more_mode': False, 'create_time': '1545795687', 'has_gallery': False, 'video_duration': 263, 'id': '6639136096645022212', 'user_id': 61908191867, 'title': '��Ưһ�壺����Ҫ�뿪�����ˣ�������Է���ϣ������δ������', 'show_play_effective_count': 1, 'has_video': True, 'share_url': 'http://toutiao.com/group/6639136096645022212/', 'source': '�����������ռ�', 'comment_count': 168, 'article_url': 'http://toutiao.com/group/6639136096645022212/', 'group_source': 2, 'comments_count': 168, 'large_mode': False, 'abstract': '���ڴ��� ��ش� �����뿪���� ��ͳԷ� 90����ഺ�ܶ���Ưһ�壺����Ҫ�뿪�����ˣ�������Է���ϣ������δ�����ù��ۻ���Ҫ�ؾŽ��ϼң��ٱ���Դ�ͣ�һ��������ף�Ϊ������', 'large_image_url': 'http://p3-tt.bytecdn.cn/large/tos-cn-i-0000/f928a96ae4fb45bf91cfdc3a898a552b', 'display_time': '1545795687', 'publish_time': '1545795687', 'middle_mode': True, 'media_creator_id': 61908191867, 'tag_id': 6639136096645022212, 'source_url': '/group/6639136096645022212/', 'video_duration_str': '04:23', 'item_id': '6639136096645022212', 'user_auth_info': {'auth_type': '0', 'other_auth': {'interest': '����������������'}, 'auth_info': '����������������'}, 'seo_url': '/group/6639136096645022212/', 'keyword': '����', 'single_mode': True, 'middle_image_url': 'http://p1-tt.bytecdn.cn/list/300x196/tos-cn-i-0000/f928a96ae4fb45bf91cfdc3a898a552b', 'digg_count': 1099, 'behot_time': '1545795687', 'tag': 'video_food', 'image_url': '//p3-tt.bytecdn.cn/list/tos-cn-i-0000/f928a96ae4fb45bf91cfdc3a898a552b', 'has_image': True, 'highlight': {'source': [], 'abstract': [[0, 2], [15, 2], [41, 2]], 'title': [[10, 2]]}, 'group_id': '6639136096645022212', 'image_count': 0}
������
{'open_url': '/group/6638083180152750596/', 'media_name': '�����ձ�', 'read_count': 484243, 'media_url': 'http://toutiao.com/m1610946690248711/', 'item_source_url': '/group/6638083180152750596/', 'labels': [], 'image_list': [{'url': '//p1-tt.bytecdn.cn/list/pgc-image/RD2Ekn46P5T9a8'}, {'url': '//p1-tt.bytecdn.cn/list/pgc-image/RD2Eko9CnVoxST'}, {'url': '//p3-tt.bytecdn.cn/list/pgc-image/RD2EksN1cXR6aR'}, {'url': '//p1-tt.bytecdn.cn/list/pgc-image/RD2EktGG59qIXl'}, {'url': '//p3-tt.bytecdn.cn/list/pgc-image/RD2Eku726odWBH'}, {'url': '//p3-tt.bytecdn.cn/list/pgc-image/RD2Eo8fFM7sV9F'}, {'url': '//p3-tt.bytecdn.cn/list/pgc-image/RD2Eo9VGbe7pCK'}], 'media_avatar_url': '//p9.pstatp.com/medium/b725000102bd7072f33f', 'datetime': '2018-12-23 15:12:59', 'more_mode': True, 'create_time': '1545549179', 'has_gallery': False, 'id': '6638083180152750596', 'user_id': 104246645773, 'title': '����Ů���⸸ĸ����Ź����Ƶ��ת�����������ҵ�������', 'show_play_effective_count': 0, 'has_video': False, 'share_url': 'https://app.peopleapp.com/Api/600/DetailApi/shareArticle?type=0&article_id=3308036', 'source': '�����ձ�', 'comment_count': 7217, 'article_url': 'https://app.peopleapp.com/Api/600/DetailApi/shareArticle?type=0&article_id=3308036', 'group_source': 2, 'comments_count': 7217, 'large_mode': False, 'abstract': '���ʱ��3�ֶ��ӵ���Ƶ����¼��9����10�£�һ����������У����Ů�����ڼ����⵽�����丸ĸŹ��Ű����Ű�ĳ��档', 'large_image_url': 'http://p3-tt.bytecdn.cn/large/pgc-image/RD2Ekn46P5T9a8', 'display_time': '1545549179', 'publish_time': '1545549179', 'middle_mode': False, 'media_creator_id': 104246645773, 'tag_id': 6638083180152750596, 'source_url': '/group/6638083180152750596/', 'item_id': '6638083180152750596', 'user_auth_info': {'auth_type': '0', 'auth_info': '�����ձ��ٷ��˺�'}, 'seo_url': '/group/6638083180152750596/', 'keyword': '����', 'single_mode': True, 'middle_image_url': 'http://p1-tt.bytecdn.cn/list/300x196/pgc-image/RD2Ekn46P5T9a8', 'digg_count': 2282, 'behot_time': '1545549179', 'tag': 'news_society', 'image_url': '//p1-tt.bytecdn.cn/list/pgc-image/RD2Ekn46P5T9a8', 'has_image': True, 'highlight': {'source': [], 'abstract': [[26, 2]], 'title': [[0, 2]]}, 'group_id': '6638083180152750596', 'image_count': 7}
{'open_url': '/group/6638127834327941639/', 'media_name': '��³Ҽ��', 'read_count': 40155, 'media_url': 'http://toutiao.com/m52308248531/', 'item_source_url': '/group/6638127834327941639/', 'labels': [], 'image_list': [{'url': '//p3-tt.bytecdn.cn/list/pgc-image/RD2gNaa25gDbjf'}], 'media_avatar_url': '//p9.pstatp.com/medium/134b000797d79e45a4e0', 'datetime': '2018-12-23 18:06:16', 'more_mode': False, 'create_time': '1545559576', 'has_gallery': False, 'id': '6638127834327941639', 'user_id': 52308248531, 'title': '���ۣ�����Űͯ��Ϊ�������̣����ɸó���ʱ�ͳ���', 'show_play_effective_count': 0, 'has_video': False, 'share_url': 'http://qiluyidian.mobi/newsjin/show/source/rss/type/1/id/9632512.html', 'source': '��³Ҽ��', 'comment_count': 392, 'article_url': 'http://qiluyidian.mobi/newsjin/show/source/rss/type/1/id/9632512.html', 'group_source': 2, 'comments_count': 392, 'large_mode': False, 'abstract': '���ʱ�����ֶ��ӵ���Ƶ����¼��9����10�¼䣬һ����������У����Ů�����ڼ����⵽�����丸ĸŹ��Ű����Ű�ĳ��档', 'large_image_url': 'http://p9-tt.bytecdn.cn/large/pgc-image/RD2gNaa25gDbjf', 'display_time': '1545559576', 'publish_time': '1545559576', 'middle_mode': True, 'media_creator_id': 52308248531, 'tag_id': 6638127834327941639, 'source_url': '/group/6638127834327941639/', 'item_id': '6638127834327941639', 'user_auth_info': {'auth_type': '0', 'auth_info': '��³Ҽ��ٷ��˺�'}, 'seo_url': '/group/6638127834327941639/', 'keyword': '����', 'single_mode': True, 'middle_image_url': 'http://p9-tt.bytecdn.cn/list/300x196/pgc-image/RD2gNaa25gDbjf', 'digg_count': 354, 'behot_time': '1545559576', 'tag': 'news_society', 'image_url': '//p3-tt.bytecdn.cn/list/pgc-image/RD2gNaa25gDbjf', 'has_image': True, 'highlight': {'source': [], 'abstract': [[27, 2]], 'title': [[3, 2]]}, 'group_id': '6638127834327941639', 'image_count': 1}
{'open_url': '/group/6638493332320289288/', 'media_name': 'ѧ����', 'read_count': 34, 'media_url': 'http://toutiao.com/m6164131851/', 'item_source_url': '/group/6638493332320289288/', 'labels': [], 'image_list': [{'url': '//p3-tt.bytecdn.cn/list/pgc-image/1d99c8f265f94cbeb6f7a19685df6596'}], 'media_avatar_url': '//p3.pstatp.com/medium/2b6001b07644673a16a', 'datetime': '2018-12-26 14:07:17', 'more_mode': False, 'create_time': '1545804437', 'has_gallery': False, 'id': '6638493332320289288', 'user_id': 6164043236, 'title': '2019������ʮ���籣���ֽ��أ����籣��ӡ����', 'show_play_effective_count': 0, 'has_video': False, 'share_url': 'http://toutiao.com/group/6638493332320289288/', 'source': 'ѧ����', 'comment_count': 0, 'article_url': 'http://toutiao.com/group/6638493332320289288/', 'group_source': 2, 'comments_count': 0, 'large_mode': False, 'abstract': 'BBMM�ǿ����֪���籣�������ۼƻ��������������ܲ��ܼ����������3.��ɽ�����ڻ���ѧ������10�֣������ڻ���ѧ����������籣������Ϊ2�ࡣ', 'large_image_url': 'http://p1-tt.bytecdn.cn/large/pgc-image/1d99c8f265f94cbeb6f7a19685df6596', 'display_time': '1545804437', 'publish_time': '1545804437', 'middle_mode': True, 'media_creator_id': 6164043236, 'tag_id': 6638493332320289288, 'source_url': '/group/6638493332320289288/', 'item_id': '6638493332320289288', 'user_auth_info': {'auth_type': '3', 'other_auth': {'interest': '������������'}, 'auth_info': 'ѧ�����ٷ��˺� ������������'}, 'seo_url': '/group/6638493332320289288/', 'keyword': '����', 'single_mode': True, 'middle_image_url': 'http://p1-tt.bytecdn.cn/list/300x196/pgc-image/1d99c8f265f94cbeb6f7a19685df6596', 'digg_count': 0, 'behot_time': '1545804437', 'tag': 'news_society', 'image_url': '//p3-tt.bytecdn.cn/list/pgc-image/1d99c8f265f94cbeb6f7a19685df6596', 'has_image': True, 'highlight': {'source': [], 'abstract': [[38, 2], [51, 2]], 'title': [[5, 2]]}, 'group_id': '6638493332320289288', 'image_count': 12}