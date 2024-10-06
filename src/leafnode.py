from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    def __init__(self,value, tag = None, props = None):
        super().__init__(value, tag, props)
        self.children = None

    def __eq__(self, other):
        return (
            self.value == other.value and
            self.tag == other.tag and
            self.props == other.props
        )
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
