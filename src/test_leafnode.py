import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(None)
        node2 = LeafNode(None)
        self.assertEqual(node, node2)

    def test_props_html(self):
        node= LeafNode("Click me!", "a" , {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\"")

    def test_proper_html(self):
        node= LeafNode("Click me!", "a" , {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_empty_value(self):
        with self.assertRaises(ValueError):
            node= LeafNode(None, "a" , {"href": "https://www.google.com"})
            value = node.to_html()

if __name__ == "__main__":
    unittest.main()