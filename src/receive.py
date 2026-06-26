import socket

# 設定（ポート番号は任意）
PORT = 50001

# 自分のIPアドレスを確認して表示
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]

print(f"受け取り待機中... このPCのIPアドレスは: {ip_address}")

# サーバーの起動
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(("0.0.0.0", PORT))
    server.listen(1)
    
    conn, addr = server.accept()
    with conn:
        print(f"接続されました: {addr}")
        # まずファイル名を受信
        filename = conn.recv(1024).decode('utf-8')
        
        # ファイルの中身を受信して保存
        with open(filename, "wb") as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
                
        print(f"ファイル「{filename}」を受信しました！")

