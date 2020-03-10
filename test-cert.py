
import ssl
import socket
import json

class GetCertDate(object):
    def datute(self, myUri):
        print(myUri)
        #socket.getaddrinfo(myUri, 443)
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=myUri)
        conn.connect((myUri, 443))
        cert = conn.getpeercert()
        print(cert.get('notAfter'))
        conn.close()
        #ssl.get_server_certificate(myUri)
        #x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        #return x509.get_notAfter()
    def fileread(self):
        myFile = open("urls.json", "r")
        datastore = json.loads(myFile.read())
        for id, url in enumerate(datastore['urls']):
            self.datute(url)
        myFile.close()

    def readlist(self):
        urls = ["vtb.ru","candystav.ru"]
        for id, url in enumerate(urls):
            self.datute(url)

if __name__== "__main__":
    gd = GetCertDate()
    gd.readlist()
    gd.fileread()
