
#https://pypi.org/project/graphviz/
import graphviz
import xml.etree.ElementTree as ET

dt = graphviz.Digraph(comment='callGraph')

tree = ET.parse('callGraph.xml')
root = tree.getroot()

mcs = root.findall('.//maxCallChain')
for mc in mcs:
    oldnode = None
    for e in mc.findall('./entry'):
        node = e.find('./function').text
        xpath_string =  f"./functions/function/[id='{node}']"
        name = root.find(xpath_string).find('name').text
        stack = e.find('./stack').text
        dt.node(node, name)
        if (oldnode):
            dt.edge(oldnode, node)
        oldnode = node

dt.render('doctest-output/round-table.gv', view=True)
#dot.render('doctest-output/round-table.gv').replace('\\', '/')
