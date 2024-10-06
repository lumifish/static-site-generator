import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        l_node= LeafNode("Click me!", "a" , {"href": "https://www.google.com"})
        node = ParentNode("a", "nothing", [l_node])
        node2 = ParentNode("a", "nothing", [l_node])
        self.assertEqual(node, node2)

    def test_children(self):
        l_node= LeafNode("Click me!", "a" , {"href": "https://www.google.com"})
        b_node= LeafNode("This is a bold text", "b" , None)
        i_node = LeafNode("This is an italics text", "i", None)
        node = ParentNode("p", None, [l_node, b_node, i_node])
        self.assertEqual(node.to_html())


        self.assertEqual()



if __name__ == "__main__":
    unittest.main()