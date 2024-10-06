from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    l_node = LeafNode("Click me!", "a", {"href": "https://www.google.com"})
    b_node = LeafNode("This is a bold text", "b", None)
    i_node = LeafNode("This is an italics text", "i", None)
    node = ParentNode("p", None, [l_node, b_node, i_node])
    print(node.to_html())

if __name__ =="__main__":
    main()