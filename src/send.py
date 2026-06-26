import socket
import os

# 設定
# ★ここに、受け取り側の画面に表示されたIPアドレスを入力してください
SERVER_IP = "192.168.x.x" 
PORT = 50001
# ★送りたいテキストファイルのパス
FILE_PATH = "test.txt" 

if not os.path.exists(FILE_PATH):
    print(f"エラー: {FILE_PATH} が見つかりません。")
    exit()

filename = os.path.basename(FILE_PATH)

# 送信処理
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    print(f"{SERVER_IP} に接続中...")
    client.connect((SERVER_IP, PORT))
    
    # 1. まずファイル名を送る
    client.sendall(filename.encode('utf-8'))
    # 少し待つ（データ混ざり防止）
    import time
    time.sleep(0.5)
    
    # 2. ファイルの中身を送る
    with open(FILE_PATH, "rb") as f:
        client.sendall(f.read())
        
    print("送信が完了しました！")

