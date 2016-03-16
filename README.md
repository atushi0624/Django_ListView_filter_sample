# Django_ListView_filter_sample

## セットアップ
```
# 任意のGit用ディレクトリへ移動
>cd path\to\dir

# GitHubからカレントディレクトリへclone
path\to\dir>git clone https://github.com/thinkAmi-sandbox/Django_ListView_filter_sample.git

# virtualenv環境の作成とactivate
# *Python3.5は、`c:\python35-32\`の下にインストール
path\to\dir>virtualenv -p c:\python35-32\python.exe env
path\to\dir>env\Scripts\activate

# requirements.txtよりインストール
(env)path\to\dir>pip install -r requirements.txt

# マイグレーション
(env)path\to\dir>python manage.py migrate

# 初期データのロード
(env)path\to\dir>python manage.py loaddata initial_data.json

# 開発サーバの起動
(env)path\to\dir>python manage.py runserver

# 開発サーバのURLを既定のブラウザで開く
# (別のコマンドプロンプトを開いて実行)
>start http://localhost:8000/mysite/
```

　  
## テスト環境

- Windows10
- Python 3.5.1
- Django 1.9.4

　  
## 関係するブログ

[DjangoのListViewで、ページをフィルタしてみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2016/03/17/003140)