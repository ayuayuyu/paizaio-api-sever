# paiza.ioのAPIとの通信を仲介してくれるサーバー
## セットアップ
```bash
pip install -r requirements.txt
```

## python実行
```bash
uvicorn main:app --reload
```
## 本番環境
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
## 以下フロントエンド
### [paizaioApiFrontend](https://github.com/ayuayuyu/paizaioApiFrontend)
