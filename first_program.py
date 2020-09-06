import bs4

"""
    Print a message
    
    Message is encoded in XML, where the a dangling child tag (a child that is
    not a parent) <count> represents 1.
    
    <count> tags can be added, so <count/><count/> is 2.
    
    A parent <count> tag doubles the value of of its contents, 
    so <count><count/></count> is 2. 
"""

xml = """<message>
    <character>
        <count><count><count>
            <count><count><count><count/></count></count></count>
            <count/>
        </count></count></count>
    </character>
    <character>
        <count><count>
            <count><count><count>
                <count><count/></count>
                <count/>
            </count></count></count>
            <count/>
        </count></count>
        <count/>
    </character>
    <character>
        <count><count>
            <count>
                <count><count>
                    <count><count/></count>
                    <count/>
                </count></count>
                <count/>
            </count>
            <count/>
        </count></count>
    </character>
    <character>
        <count><count>
            <count>
                <count><count>
                    <count><count/></count>
                    <count/>
                </count></count>
                <count/>
            </count>
            <count/>
        </count></count>
    </character>
    <character>
        <count>
            <count>
                <count>
                    <count><count>
                        <count><count/></count>
                        <count/>
                    </count></count>
                    <count/>
                </count>
                <count/>
            </count>
            <count/>
        </count>
        <count/>
    </character>
    <character>
        <count><count><count><count><count><count/></count></count></count></count></count>
    </character>
    <character>
        <count>
            <count>
                <count><count>
                    <count><count><count/></count></count>
                    <count/>
                </count></count>
                <count/>
            </count>
            <count/>
        </count>
        <count/>
    </character>
    <character>
        <count>
            <count>
                <count>
                    <count><count>
                        <count><count/></count>
                        <count/>
                    </count></count>
                    <count/>
                </count>
            <count/>
            </count>
            <count/>
        </count>
        <count/>
    </character>
    <character>
        <count>
            <count><count><count>
                <count>
                    <count><count/></count>
                    <count/>
                </count>
                <count/>
            </count></count></count>
            <count/>
        </count>
    </character>
    <character>
        <count><count>
            <count>
                <count><count>
                    <count><count/></count>
                    <count/>
                </count></count>
                <count/>
            </count>
            <count/>
        </count></count>
    </character>
    <character>
        <count><count>
            <count><count><count>
                <count><count/></count>
                <count/>
            </count></count></count>
            <count/>
        </count></count>
    </character>
    <character>
        <count><count><count><count><count><count/></count></count></count></count></count>
        <count/>
    </character>
</message>"""


def get_ascii_char(node):
    """
    Process the contents of a <character> element, and determine its ascii value

    By recursively walking the XML tree, and using find_all, which also
    recursively returns all descendants, the deeper a count node is in the
    tree, the more often it is counted.

    :param node: element tag of the character element
    :return: ascii value
    """
    total = 0
    counts = list(node.find_all('count'))
    print(node, counts)
    # dangling count elements have the value 1
    if not counts:
        return 1
    return sum([
        get_ascii_char(count) for count in counts
    ])


if __name__ == '__main__':
    # read in XML message
    soup = bs4.BeautifulSoup(xml, 'lxml')
    # loop through character elements, and print each character
    for character in soup.message.find_all('character'):
        print(chr(get_ascii_char(character)), end='')

    print()
