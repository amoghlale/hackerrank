import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    root_children_mapping = {}
    for elem in elem.iter():
        if len(list(elem)) != 0 and elem.tag not in root_children_mapping:
            root_children_mapping[elem.tag] = [i.tag for i in list(elem)]
            maxdepth += 1

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
