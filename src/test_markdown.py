import unittest
from textnode import TextNode
from inline_markdown import *
from markdown_blocks import *

class TestMarkdown(unittest.TestCase):
    
    def test_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[1], TextNode("code block", TextType.CODE, None))

    def test_extract_markdown(self):
        text_image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        text_link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_images(text_image), [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])
        self.assertEqual(extract_markdown_links(text_link), [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])
        
        #[('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        #[('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]

    def test_split_images(self):
        node_with_images = TextNode("This is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif)",TextType.TEXT, None)
        self.assertEqual(split_nodes_image([node_with_images]), [TextNode("This is text with an image ", TextType.TEXT, None), TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif")])
    
    def test_split_links(self):
        node_with_links = TextNode("This is text with a link [to boot dev](https://www.boot.dev)",TextType.TEXT, None)
        self.assertEqual(split_nodes_link([node_with_links]), [TextNode("This is text with a link ", TextType.TEXT, None), TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")])
    
    def test_split_text(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com / fJRm4Vk.jpeg) and a[link](https: // boot.dev)"
        split_text = text_to_textnodes(text)
        self.assertEqual(split_text[3], TextNode("italic", TextType.ITALIC, None))
        
    def test_split_blocks(self):
        text = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it. It also has some more **bold** and *italic* words inside of it.

        ## This is a smaller header

        * This is the first list item in a list block
        * This is a list item
        * This is another list item"""
        
        self.assertEqual(markdown_to_blocks(text)[2],"## This is a smaller header")

  
if __name__ == "__main__":
    unittest.main()