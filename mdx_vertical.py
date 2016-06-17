'''
Vertical Text Extension for Python-Markdown
==================================

Converts "\@This is text" to a vertical text.
Its syntax is inspired by block quote's.

License: [BSD](http://www.opensource.org/licenses/bsd-license.php)

'''

from __future__ import unicode_literals
from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor
from markdown.util import etree
import re


class VerticalProcessor(BlockProcessor):

    RE = re.compile(r'(^|\n)[ ]{0,3}@[ ]?(.*)')
    WM = re.compile(r'writing-mode:')

    def test(self, parent, block):
        return bool(self.RE.search(block))

    def run(self, parent, blocks):
        block = blocks.pop(0)
        m = self.RE.search(block)
        if m:
            before = block[:m.start()]  # Lines before vertical
            # Pass lines before vertical in recursively for parsing forst.
            self.parser.parseBlocks(parent, [before])
            # Remove ``@ `` from begining of each line.
            block = '\n'.join(
                [self.clean(line) for line in block[m.start():].split('\n')]
            )
        sibling = self.lastChild(parent)
        if sibling is not None and\
            sibling.tag == "div" and self.WM.search(sibling.get('style')):
            # Previous block was a vertical so set that as this blocks parent
            vertical = sibling
        else:
            # This is a new vertical. Create a new parent element.
            vertical = etree.SubElement(parent, 'div')
            vertical.set('style', 'writing-mode:vertical-rl;text-indent:1em;'\
                       + ''.join(x + 'column-width:'+self.config['column']+';'\
                           for x in ('', '-moz-', '-webkit-', '-o-', '-ms-'))\
                       + vertical.get('style', ''))
        # Recursively parse block with vertical as parent.
        # change parser state so top2bottom embedded in lists use p tags
        self.parser.parseChunk(vertical, block)

    def clean(self, line):
        """ Remove ``@`` from beginning of a line. """
        m = self.RE.match(line)
        if line.strip() == "@":
            return ""
        elif m:
            return m.group(2)
        else:
            return line

class VerticalExtension(Extension):
    def __init__(self, *args, **kwargs):
        self.config = {
            'column':['290px', '']
        }
        super(Extension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        """ Add VerticalProcessor to the Markdown instance. """
        vertical = VerticalProcessor(md.parser)
        vertical.config = self.getConfigs()
        md.parser.blockprocessors.add('top2bottom', vertical, '<hashheader')

def makeExtension(*args, **kwargs):
    return VerticalExtension(*args, **kwargs)
