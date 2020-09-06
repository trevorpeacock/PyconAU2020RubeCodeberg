import math
import tests

"""
    Take the challenge string and generate an XML representation.
    This representation isn't formatted particularly nicely, but it works.
"""


def generate_xml(ascii_value):
    xml = ''
    if ascii_value == 0:
        return xml
    # loop through each position in the binary representation of the
    #   ascii_value
    for position in reversed(range(int(math.log2(ascii_value)) + 1)):
        place = 2 ** position
        # is the binary representation of this position a 1
        if ascii_value >= place:
            xml += '\n<count/>\n'
            ascii_value -= place
        # advance a binary digit, doubling the current value
        if position != 0:
            xml = '<count>{}</count>'.format(xml)
    return xml


for c in 'Hello world!':
    o = ord(c)
    xml_character = generate_xml(o)
    print('<character>\n{}\n</character>'.format(xml_character))
    assert(o == tests.test_char(xml_character))
