import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", "italic")
        self.assertEqual(node.text, "This is a text node") #no self

    def test_text_node(self):
        node = TextNode("This is a text node", "italic")
        self.assertEqual(node.text_type, "italic")
    def test_text_node_uneq(self):
        node = TextNode("This is a text node", "italic")
        self.assertNotEqual(node.text_type, "bold")

    def test_url_none(self):
        node = TextNode("This is a text node", "italic")
        self.assertEqual(node.url, None)
    

if __name__ == "__main__":
    unittest.main()