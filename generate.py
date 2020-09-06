import math

import tests

def generate_xml(o):
    xml = ''
    if o == 0:
        return xml
    for i in reversed(range(int(math.log2(o))+1)):
        place = 2 ** i
        if o >= place:
            xml += '\n<count/>\n'
            if i!=0:
                xml = '<count>{}</count>'.format(xml)
            o -= place
        else:
            if i!=0:
                xml = '<count>{}</count>'.format(xml)
    return xml

for c in 'Hello World!':
    o = ord(c)
    xml = generate_xml(o)
    print('<character>\n{}\n</character>'.format(xml))
    assert(o==tests.test_char(xml))
