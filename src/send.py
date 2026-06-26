import socket
import os
import time

# ★ステップ1で手動確認したWindowsの「IPv4 アドレス」を入力してください
SERVER_IP = "192.168.X.X" 
PORT = 50002
FILE_PATH = "test.txt" 

if not os.path.exists(FILE_PATH):
    print(f"エラー: {FILE_PATH} が見つかりません。")
    exit()

filename = os.path.basename(FILE_PATH)

# UDPソケットの作成
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    target = (SERVER_IP, PORT)
    print(f"{SERVER_IP} へ送信開始...")
    
    # 1. ファイル名を送る
    client.sendto(filename.encode('utf-8'), target)
    time.sleep(0.1)
    
    # 2. ファイルの中身を送る
    with open(FILE_PATH, "rb") as f:
        client.sendto(f.read(), target)
        
    # 3. 終了の合図を送る
    time.sleep(0.1)
    client.sendto(b"__EOF__", target)
        
    print("送信完了しました！")

