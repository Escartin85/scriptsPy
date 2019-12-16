from html.parser import HTMLParser
import urllib.request

metacount = 0;

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered comment: ", str(data))
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_starttag(self, tag, attrs):
        global metacount
        if tag == 'meta':
            metacount += 1
        print("Encountered tag: ", str(tag))
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

        if attrs.__len__() > 0:
            print("\tAttributes:")
        for a in attrs:
            print("\t", a[0], "=", a[1])

    def handle_endtag(self, tag):
        print("Encountered tag: ",str(tag))
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_data(self, data):
        if data.isspace():
            return
        print("Encountered Data: ", str(data))
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

def main():
    parser = MyHTMLParser()
    url = "https://www.elotrolado.net/"
    webUrl = urllib.request.urlopen(url)
    webContent = webUrl.read()
    webContent = webContent.decode('utf-8')
    parser.feed(webContent)
    print("------")
    print("META tag found: " + str(metacount))
if __name__ == "__main__":
    main()
