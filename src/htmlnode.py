"""from enum import Enum"""


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        if children is None:
            self.children = []
        else:
            self.children = children
        if props is None:
            self.props = {}
        else:
            self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        str = ""
        for key, value in self.props.items():
            str += f' {key}="{value}"'
        return str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
