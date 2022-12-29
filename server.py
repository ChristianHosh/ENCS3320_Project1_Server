from socket import *

serverPort = 7788
serverSocket = socket(AF_INET, SOCK_STREAM)  # TCP OR UDP
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
print(serverSocket.getsockname())
while True:
    clientSocket, addr = serverSocket.accept()
    ip = addr[0]
    port = addr[1]
    print('Got Connection from, IP: ' + ip + ", Port: " + str(port))
    full_request = clientSocket.recv(1024).decode()
    print(full_request)
    request = full_request.split()[1]
    print("request: " + request)
    if request == '/' or request == '/en':
        html_en_file = open("mainEN.html", "rb")
        file_content = html_en_file.read()
        html_en_file.close()
        clientSocket.send(bytes("HTTP/1.1 200 OK\r\n", "utf-8"))
        clientSocket.send(bytes("Content-Type: text/html\r\n", "utf-8"))
        clientSocket.send(bytes("\r\n", "utf-8"))
        clientSocket.send(file_content)
        print("SENT HTML_EN\r\n\n")
    elif request == '/ar':
        html_ar_file = open("mainAR.html", "rb")
        file_content = html_ar_file.read()
        html_ar_file.close()
        clientSocket.send(bytes("HTTP/1.1 200 OK\r\n", "utf-8"))
        clientSocket.send(bytes("Content-Type: text/html\r\n", "utf-8"))
        clientSocket.send(bytes("\r\n", "utf-8"))
        clientSocket.send(file_content)
        print("SENT HTML_AR\r\n\n")
    elif request == '/style.css':
        css_file = open("style.css", "r")
        file_content = css_file.read()
        css_file.close()
        clientSocket.send(bytes("HTTP/1.1 200 OK\r\n", "utf-8"))
        clientSocket.send(bytes("Content-Type: text/css\r\n", "utf-8"))
        clientSocket.send(bytes("\r\n", "utf-8"))
        clientSocket.send(bytes(file_content, "utf-8"))
        print("SENT STYLE_CSS\r\n\n")
    elif request == '/bzuCircle.png':
        png_file = open("bzuCircle.png", "rb")
        file_content = png_file.read()
        png_file.close()
        clientSocket.send(bytes("HTTP/1.1 200 OK\r\n", "utf-8"))
        clientSocket.send(bytes("Content-Type: image/png\r\n", "utf-8"))
        clientSocket.send(bytes("\r\n", "utf-8"))
        clientSocket.send(file_content)
        print("SENT BZU_CIRCLE_PNG\r\n\n")
    elif request == '/bzuUni.jpg':
        jpg_file = open("bzuUni.jpg", "rb")
        file_content = jpg_file.read()
        jpg_file.close()
        clientSocket.send(bytes("HTTP/1.1 200 OK\r\n", "utf-8"))
        clientSocket.send(bytes("Content-Type: image/jpeg\r\n", "utf-8"))
        clientSocket.send(bytes("\r\n", "utf-8"))
        clientSocket.send(file_content)
        print("SENT BZU_UNI_JPEG\r\n\n")
    elif request == '/favicon.ico':
        ico_file = open("icon.ico", "rb")
        file_content = ico_file.read()
        ico_file.close()
        clientSocket.send(bytes("HTTP/1.1 200 OK\r\n", "utf-8"))
        clientSocket.send(bytes("Content-Type: image/ico\r\n", "utf-8"))
        clientSocket.send(bytes("\r\n", "utf-8"))
        clientSocket.send(file_content)
        print("SENT WEB_ICON\r\n\n")
    elif request == '/go':
        clientSocket.send(bytes("HTTP/1.1 307 temporary Redirect\r\n", "utf-8"))
        clientSocket.send(bytes("Content-Type:\r\n", "utf-8"))
        clientSocket.send(bytes("location: https://google.com/\r\n", "utf-8"))
        print("REDIRECT TO GOOGLE\r\n\n")
    elif request == '/so':
        clientSocket.send(bytes("HTTP/1.1 307 temporary Redirect\r\n", "utf-8"))
        clientSocket.send(bytes("Content-Type:\r\n", "utf-8"))
        clientSocket.send(bytes("location: https://stackoverflow.com\r\n", "utf-8"))
        print("REDIRECT TO STACKOVERFLOW\r\n\n")
    elif request == '/bzu':
        clientSocket.send(bytes("HTTP/1.1 307 temporary Redirect\r\n", "utf-8"))
        clientSocket.send(bytes("Content-Type:\r\n", "utf-8"))
        clientSocket.send(bytes("location: https://www.birzeit.edu/en\r\n", "utf-8"))
        print("REDIRECT TO BIRZEIT\r\n\n")
    else:
        client = ip + ":" + str(port)
        html_error = f"""
                <!DOCTYPE html>
        <html lang="">
        <head>
          <title>Error</title>
          <link rel="stylesheet" type="text/css" href="style.css">
        </head>
        <body>
          <h1 style="color:red">The file is not found</h1>
          <h2><strong>Group Members:</strong></h2>
          <ul class="boldlist">
            <li>Christian Hosh : 1200482</li>
            <li>Eliana Ellati : 1202528</li>
            <li>Hala Abdel Halim : 1201266</li>
          </ul>
          <p>IP and port number of the client: {client}</p>
        </body>
        </html>
        """
        clientSocket.send(bytes("HTTP/1.1 404 NOT FOUND\r\n", "utf-8"))
        clientSocket.send(bytes("Content-Type: text/html\r\n", "utf-8"))
        clientSocket.send(bytes("\r\n", "utf-8"))
        clientSocket.send(bytes(html_error, "utf-8"))
        print("SENT HTML_ERROR\r\n\n")

    clientSocket.close()
