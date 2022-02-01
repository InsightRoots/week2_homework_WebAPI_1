
"""
●要件
Hacker Newsという計算機科学やベンチャーなどのテーマを取り扱うソーシャルニュースサイトがあります。
HackerNews/API: Documentation and Samples for the Official HN API を利用して、
ップページに表示されているニュースのタイトルおよびリンクURLを取得してください。

（要件の理解）
・注意事項の時間を決めて必ず行う。
・ここにアクセスする。https://news.ycombinator.com/
・APIを使って取得する→テキスト確認
    -APIってなんだっけ?→テキスト確認
    -出力したい場所のソースコードを検証で確認→テキストの内容確認
        -title
        -title link
    -場所にそって抽出するようにコードを書く→テキストの内容確認
    -それを何回か繰り返す→なんかい？とりあえず3回
・エラーの理解と解消

●具体例、出力結果
{'title': 'Facebook to acquire CTRL-Labs, a startup for controlling computers with the mind', 'link': 'https://www.bloomberg.com/news/articles/2019-09-23/facebook-to-buy-startup-for-controlling-computers-with-your-mind'}
{'title': 'The news industry was complicit in the opioid crisis', 'link': 'https://www.cjr.org/opinion/opioids-news-prescription-doctor.php'}
{'title': 'Adblock Radio', 'link': 'https://github.com/adblockradio/adblockradio'}
{'title': 'Voidcall – Making of 13kb JavaScript RTS Game', 'link': 'https://phoboslab.org/log/2019/09/voidcall-making-of'}
{'title': 'Yahoo Customer Data Security Breach Litigation Settlement', 'link': 'https://yahoodatabreachsettlement.com/'}


"""

import time
from re import split

import requests

# # 変数にHTTPライブラリで、APIの情報を取得して代入する
# responce = requests.get('https://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111')
#
# print(responce)
# print(responce.text)
# newstories
# 30158720.
# 30158821
import strip as strip

responce = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty')

res_list =responce.text
print(res_list[:30])


# # 抽出すると、リストが出てくる。よって、リストで変数を作って、変数を1つだけ取り出す。その一つをURLに入力して出力、同じことを3回だけ繰り返す。
# # print(abc[:4])だと、最初から４つ
#
# for i in range(3):
#     time.sleep(1) # ここで1秒止まる
#     print(i)