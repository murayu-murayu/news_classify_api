## NEWS CLASSIFY API

#### アプリケーションの概要

- ニュース記事のテキストを入力すると、内容によって分類し、カテゴリを返す API
- API 画面において、Input text 欄にニュースのテキストを入力して POSt すると、PyTorch を用いた BERT の分類モデルにより、下記の 9 カテゴリに自動で分類を行います。

- カテゴリ一覧
  [0, 'it_mobile']
  [1, 'movie']
  [2, 'others_for_men']
  [3, 'others_for_wemen']
  [4, 'home_appliance']
  [5, 'sports']
  [6, 'fashion']
  [7, 'it_life-hack']
  [8, 'topic_news']

#### 使用技術等

- Python
- PyTorch
- Django REST Framework
- AWS(EC2)
- Let's Encrypt
- Git, Bitbucket

#### 作成にあたっての概要等

- 分類モデルは、訓練済み BERT モデル(東北大学乾研究室)を基に、livedoor ニュースコーパス用いてファインチューニングを実施し作成。
- AWS の EC2 インスタンス上に、上記分類モデルを搭載した Django アプリを構成(Nginx, Gunicorn を使用)。独自ドメインを取得し、Let's_encrypt(Certbot)により ssl 化を実施。
