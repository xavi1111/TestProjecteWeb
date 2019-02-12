
from urllib.request import urlopen

class ClientWeb(object):
    """client web per la web de la EPS"""
    def __init__(self):
        super(ClientWeb, self).__init__()
        pass

    def descarregar_html(self):
        f = urlopen("http://www.eps.udl.cat/ca/")
        html = f.read
        f.close
        return html

    def run(self):
        #descarregar-me html
        html=self.descarregar_html()
        #buscar activitats
        #imprimir resultat
        print(html)

if __name__== "__main__":
    c=ClientWeb()
    c.run()