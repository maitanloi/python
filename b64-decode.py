import base64
print ('Nhập nội dung cần giải mã:')
encoded =input()
data = base64.b64decode(encoded)
print ('Kết quả:',data)