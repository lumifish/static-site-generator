class HTMLNode:
    def __init__(self, value = None, tag = None, props = None, children = None):
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
        list = [f"{key}=\"{value}\"" for key, value in self.props.items()]
        return f" {" ".join(list)}"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"