import xml.sax
import subprocess
import mwparserfromhell
class WikiXmlHandler(xml.sax.handler.ContentHandler):
    """Content handler for Wiki XML data using SAX"""
    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)
        self._buffer = None
        self._values = {}
        self._current_tag = None
        self._pages = []
        self._number = 0

    def characters(self, content):
        """Characters between opening and closing tags"""
        if self._current_tag:
            self._buffer.append(content)

    def startElement(self, name, attrs):
        """Opening tag of element"""
        if name in ('title','text'):
            self._current_tag = name
            self._buffer = []

    def endElement(self, name):
        """Closing tag of element"""
        if name == self._current_tag:
            self._values[name] = ' '.join(self._buffer)

        if name == 'page':
            self._number += 1
            # print(self._number)
            found = self.process_article(self._values['title'],self._values['text'])
            if(found):
                self._pages.append((self._values['title'],self._values['text']))
            # if(self._values['title']=="Perang Padri"):
            #     print(len(self._pages))
            #     print(self._number)
            #     # self._pages.append((self._values['title'],self._values['text']))
    
    def process_article(self,title, text):
        """Process a wikipedia article looking for template"""
        
        # Create a parsing object
        wikicode = mwparserfromhell.parse(text)
        
        # Search through templates for the template
        matches = wikicode.filter_text()[-10:]
        
        
        return "Kategori:Sejarah Nusantara" in matches
            # Extract information from infobox
            # properties = {param.name.strip_code().strip(): param.value.strip_code().strip() 
            #             for param in matches[0].params
            #             if param.value.strip_code().strip()}
            
            # # Extract internal wikilinks
            # wikilinks = [x.title.strip_code().strip() for x in wikicode.filter_wikilinks()]
            # # Extract external links
            # exlinks = [x.url.strip_code().strip() for x in wikicode.filter_external_links()]
            # return (title, properties, wikilinks, exlinks, timestamp)

data = "idwiki-20240101-pages-articles.xml.bz2"

# Object for handling xml
handler = WikiXmlHandler()
# Parsing object
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
# Iteratively process file
for line in subprocess.Popen(['bzcat'], 
                              stdin = open(data), 
                              stdout = subprocess.PIPE).stdout:
    # print(line)
    parser.feed(line)
    
    # Stop when 3 articles have been found
    # if len(handler._pages) == 1:
    #     break

# print(handler._pages[0])
# wiki = mwparserfromhell.parse(handler._pages[0][1])
# wikilinks = [x.title for x in wiki.filter_wikilinks()]
# print(wikilinks[:5])
# template = wiki.filter_text()
# print(template)
print(handler._number)
print(len(handler._pages))