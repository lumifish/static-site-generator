import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, text_node_to_html_node


class TestHTMLNode(unittest.TestCase):
    def test_html_eq(self):
        node = HTMLNode(None)
        node2 = HTMLNode(None)
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode( "p","This is a paragraph",None, {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_repr(self):
        node = HTMLNode( "p","This is a paragraph",None, {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(repr(node), "HTMLNode(p, This is a paragraph, None, {'href': 'https://www.google.com', 'target': '_blank'})")

    def test_children_html(self):
        child_node1 = HTMLNode( "p","This is a paragraph",None, {"href": "https://www.google.com", "target": "_blank",})
        child_node2 = HTMLNode( "img","This is an image", None, {"href": "https://www.google.com", "target": "_blank",})

        node = HTMLNode( "p","This is a paragraph",[child_node1, child_node2], None)
        self.assertEqual(node.children, [child_node1, child_node2])

    def test_props_html(self):
        node= LeafNode("a", "Click me!" , {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\"")

    def test_proper_html(self):
        node= LeafNode("a", "Click me!" , {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_empty_value(self):
        with self.assertRaises(ValueError):
            node= LeafNode("a", None , {"href": "https://www.google.com"})
            value = node.to_html()

    def test_children_parent(self):
        l_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        b_node = LeafNode("b", "This is a bold text")
        i_node = LeafNode("i", "This is an italics text")
        node = ParentNode("p", [l_node, b_node, i_node])
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a><b>This is a bold text</b><i>This is an italics text</i>")

    def text_to_html(self):
        text_bold = TextNode("this is bold text", "bold")
        text_url = TextNode("this is a link", "link", "https://www.google.com")
        bold_html = text_node_to_html_node(text_bold).props_to_html()
        link_html = text_node_to_html_node(text_url).props_to_html()
        self.assertEqual(bold_html, "<b>this is bold text</b>")
        self.assertEqual(link_html, "<a href=\"https://www.google.com\">this is a link</a>")

if __name__ == "__main__":
    unittest.main()