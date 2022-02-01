
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
    -場所にそって抽出するようにコードを書く→テキストの内容確認
・エラーの理解と解消

●具体例、出力結果
{'title': 'Facebook to acquire CTRL-Labs, a startup for controlling computers with the mind', 'link': 'https://www.bloomberg.com/news/articles/2019-09-23/facebook-to-buy-startup-for-controlling-computers-with-your-mind'}
{'title': 'The news industry was complicit in the opioid crisis', 'link': 'https://www.cjr.org/opinion/opioids-news-prescription-doctor.php'}
{'title': 'Adblock Radio', 'link': 'https://github.com/adblockradio/adblockradio'}
{'title': 'Voidcall – Making of 13kb JavaScript RTS Game', 'link': 'https://phoboslab.org/log/2019/09/voidcall-making-of'}
{'title': 'Yahoo Customer Data Security Breach Litigation Settlement', 'link': 'https://yahoodatabreachsettlement.com/'}


"""

import time
import requests


for i in range(10):
    time.sleep(1) # ここで1秒止まる
    print(i)