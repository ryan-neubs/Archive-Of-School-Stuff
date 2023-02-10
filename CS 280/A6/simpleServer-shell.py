# by Ryan Neubauer
# With help from Sam Schmitz, Brice Rhodes, Jacob VanderWilt, Tryton Harper, Gavin Roy, Nick Henry

from socket import *
from os import path


def main():
    HOST = 'localhost'   # Should it be 'localhost'?
    PORT = 8080 # An arbitrary number > 1024

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)  # How deep the queue is for connection attempts
    mimeTypes = {
        'html' : 'text/html',
        'ico' : 'image/vnd.microsoft.icon',
        'jpg' : 'image/jpeg',
        'jpeg' : 'image/jpeg',
        'png' : 'image/png',
        'css' : 'text/css',
        'gif' : 'image/gif'
        }
    base_html = "<html><head></head><body><h1>{}</h1></body></html>"

    try:
        print("Starting simpleServer!")
        while True:
            handler, addr = sock.accept()

            # If we made it this far, we've got a live one!
            print("Handler connected by", addr)
            data = handler.recv(8192) # receive up to ??k
            data = data.decode()
            print("Data: %s" % data)
            header = data.split('\r\n')
            print(header[0])
            request = header[0]
            if len(request) < 3:
                handler.send(("HTTP/1.1 400 Bad Request\nContent-type: text/html\n\n"
                              + base_html.format(f"400 Bad Request")).encode())
                raise ValueError
            op, uri, protocol = request.split()
            print("URI: %s" % uri)

            uri = uri[1:]
            uri.replace("..","")
            # Send back a response
            file = uri.split('.')
            fileExtension = file[-1]
            # Generate correct responses
            if not (path.isdir(uri) or path.isfile(uri)):
                handler.send(("HTTP/1.1 404 File Not Found\nContent-type: text/html\n\n"
                              + base_html.format(f"404 File {uri} not found")).encode())
                continue
            if fileExtension not in mimeTypes:
                handler.send(("HTTP/1.1 501 Feature Not Implemented: text/html\n\n"
                              + base_html.format(f"501 Feature {fileExtension} Not Implemented")).encode())
                raise KeyError
            response = "HTTP/1.1 200 OK\nContent-type: {}\n\n".format(mimeTypes[fileExtension])
            if mimeTypes[fileExtension] == 'text/html':
                outFile = open(uri, "r")
                html = outFile.read()
                outFile.close()
                handler.send(response.encode() + html.encode())
            else:
                outFile = open(uri, "rb")
                data = outFile.read()
                outFile.close()
                handler.send(response.encode() + data)
            handler.close()

    except ValueError:
        print("400 Bad Request")
    except KeyError:
        print("501 Feature Not Implemented")
    finally:
        print("Closing the socket...")
        sock.close()

if __name__ == "__main__":
    main()


