import unittest
from textnode import TextNode
from markdown import *

class TestMarkdown(unittest.TestCase):
    
    def test_delimiter(self):
        node = TextNode("This is text with a `code block` word", "text")
        node2 = TextNode("This is text with a **bold block** word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(new_nodes[1], TextNode("code block", "code", None))

    def test_extract_markdown(self):
        text_image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        text_link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_images(text_image), [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])
        self.assertEqual(extract_markdown_links(text_link), [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])
        
        #[('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        #[('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]

    
if __name__ == "__main__":
    unittest.main()