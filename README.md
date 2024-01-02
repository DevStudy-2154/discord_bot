# discord_bot
## 環境構築
### 初回のみ
1. 以下のコマンドを実行する
```
docker compose up -d --build
```
2. envファイルを`bot/settings/`に作成する
```
DISCORD_TOKEN=(松岡に聞いてください)
```

### 初回構築以外の時
```
# 起動
docker compose up -d

# コンテナに入って実行する
docker compose exec bot bash
python main.py

# コンテナに入らず実行する
docker compose exec -it bot python main.py

# 停止
docker compose stop
```

### 環境変数を追加する場合
1. `.env`に環境変数を記載
2. `bot/settings/config.py`に環境変数を追記

### パッケージを追加する場合
`docker/requirements.txt`にパッケージ名を追記して再ビルド

## ディレクトリ構成
```
|- .github
|- bot
|  |- settings
|  |  |- .env           環境変数管理
|  |  |- config.py      環境変数をmain.pyで呼び出すための設定ファイル
|  |- main.py           実行ファイル
|- docker
|  |- Dockerfile
|  |- requirements.txt  インストールパッケージ管理用
|- .gitignore
|- compose.yaml
|- README.md
```
