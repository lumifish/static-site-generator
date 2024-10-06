import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(None)
        node2 = HTMLNode(None)
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode( "This is a paragraph","p", {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_repr(self):
        node = HTMLNode( "This is a paragraph", "p", {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(repr(node), "HTMLNode(p, This is a paragraph, None, {'href': 'https://www.google.com', 'target': '_blank'})")

    def test_children(self):
        child_node1 = HTMLNode( "This is a paragraph","p", {"href": "https://www.google.com", "target": "_blank",})
        child_node2 = HTMLNode( "This is an image","img", {"href": "https://www.google.com", "target": "_blank",})

        node = HTMLNode( "This is a paragraph","p",None, [child_node1, child_node2])
        self.assertEqual(node.children, [child_node1, child_node2])


if __name__ == "__main__":
    unittest.main()