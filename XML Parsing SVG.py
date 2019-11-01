import lxml.etree as ET
from lxml.etree import tostring
from lxml import etree
from lxml.builder import E
from IPython.display import display, HTML
display(HTML(data="""
<style>
    div#notebook-container    { width: 95%; }
    div#menubar-container     { width: 65%; }
    div#maintoolbar-container { width: 99%; }
</style>
"""))

xml = ET.parse('Test.svg')
svg = xml.getroot()
path =svg.getchildren()[6]
path.attrib['x']
path.attrib['y']
path.attrib

parsedXML = ET.parse('test_svg.svg')

from lxml import etree


parsedXML = etree.parse('test2.xml')
a = etree.Element('root')
# doc = etree.ElementTree(a)
# if not ids is None:
    
#     b = etree.SubElement(a,"parent")
    
#     if not ids is None:
#         z = etree.SubElement(b,'id_parent')
#         z.text = ids
# #     b.text = ids

for node in parsedXML.getroot():
    ids = node.attrib.get('id')
    
    if not ids is None:
    
        b = etree.SubElement(a,"parent")
    
    if not ids is None:
        z = etree.SubElement(b,'id_parent')
        z.text = ids

    
       
    
    for node_child in node:
        dd = node_child.attrib.get('d')
        ident = node_child.attrib.get('id')
        style = node_child.attrib.get('style')
        x = node_child.attrib.get('x')
        y = node_child.attrib.get('y')

        if not ident is None:
            c = etree.SubElement(b,'path')
        if not ident is None:    
            s = etree.SubElement(c,'id')
            s.text = ident
        if not dd is None:
            d = etree.SubElement(c,'d')
            d.text = dd
        if not style is None:
            e = etree.SubElement(c,'style')
            e.text = style
        if not x is None:
            f = etree.SubElement(c,'x')
            f.text = x
        if not y is None:
            g = etree.SubElement(c,'y')
            g.text = y
#         ET.dump(a)

# doc.write('lxml_test.xml', xml_declaration=True, encoding='utf-8',pretty_print=True)

for child in b:
    print(child.tag, child.text)
    for mini in child:
        print(mini.tag, mini.text)
et_string = etree.ElementTree(a)
et_string.write('test_lxm.xml', pretty_print=True,xml_declaration=True,   encoding="utf-8")