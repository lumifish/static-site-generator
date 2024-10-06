from htmlnode import HTMLNode
class ParentNode(HTMLNode):
    def __init__(self, tag = None, props = None, children = None):
        super().__init__(tag, props, children = children)

    def __eq__(self, other):
        return (
            self.tag == other.tag and
            self.props == other.props and
            self.children == other.children
        )

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tags passed")
        if self.children == None:
            raise ValueError("No children passed")
        child_list = list(map(lambda x: x.to_html(), self.children))
        return "".join(child_list)