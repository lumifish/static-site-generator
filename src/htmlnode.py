class HTMLNode:
    def __init__(self,tag = None, value = None,  children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        list = [f"{key}=\"{value}\"" for key, value in self.props.items()]
        return f" {" ".join(list)}"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag, value, props = None):
        super().__init__(tag, value, None, props)

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
class ParentNode(HTMLNode):
    def __init__(self,tag, children, props = None):
        super().__init__(tag, None, children, props)

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

