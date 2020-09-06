import bs4


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

soup = bs4.BeautifulSoup(xml, 'html.parser')


def process_count(node):
    total = 0
    counts = list(node.find_all('count'))
    for count in counts:
        total += process_count(count)
    if not counts:
        return 1
    return total


def get_ascii_char(node):
    ascii_char = 0
    for count in node.find_all('count'):
        ascii_char += process_count(count)
    return ascii_char


if __name__ == '__main__':
    for character in soup.message.find_all('character'):
        print(chr(get_ascii_char(character)), end='')

    print()
