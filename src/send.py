import socket

PORT = 50002

# UDPソケットの作成
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind(("0.0.0.0", PORT))
    print(f"【受信側】ポート {PORT} で待機中...")
    
    # 1. まずファイル名を受信
    data, addr = server.recvfrom(1024)
    filename = data.decode('utf-8')
    print(f"{addr} から接続。ファイル名: {filename}")
    
    # 2. ファイルの中身を受信して保存
    with open(filename, "wb") as f:
        while True:
            data, addr = server.recvfrom(4096)
            if data == b"__EOF__": # 終了の合図
                break
            f.write(data)
            
    print(f"ファイル「{filename}」を正常に受信しました！")

