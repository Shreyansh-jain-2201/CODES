import base64
  
  
file = open(r'C:\Users\Shreyansh Jain\.vscode\.vscode\message (1).txt', 'rb')
byte = file.read()
file.close()
  
decodeit = open('shruti1234567.jpeg', 'wb')
decodeit.write(base64.b64decode((byte)))
decodeit.close()