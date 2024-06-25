import xml.sax
import subprocess
import mwparserfromhell
import json
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
            self._pages.append(self._values['title'])
            # found = self.process_article(self._values['title'],self._values['text'])
            # if(found):
            #     self._pages.append((self._values['title'],self._values['text']))
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
parser = xml.sax.make_parser()
parser.setContentHandler(handler)

for line in subprocess.Popen(['bzcat'], 
                              stdin = open(data), 
                              stdout = subprocess.PIPE).stdout:
    parser.feed(line)
    
print(len(handler._pages))
    # Stop when 3 articles have been found
    
# with open("mapping_id.xml") as file:
#     for i in file:
        
#         parser.feed(i)
#         # if len(handler._pages) == 1:
#         #     break
# print(handler._pages)

# handler2 = WikiXmlHandler()
# parser2 = xml.sax.make_parser()
# parser2.setContentHandler(handler2)

# with open("mapping_en.xml") as file:
#     for i in file:
#         parser2.feed(i)
#         # if len(handler._pages) == 1:
#         #     break
# print(handler2._pages)
# with open("type_mapping_en.json",'w') as file:
#     file.write(json.dumps(handler2._pages))
