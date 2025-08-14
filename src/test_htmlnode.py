import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode()
        node2 = f"HTMLNode(None, None, [], {{}})"
        self.assertEqual(repr(node), node2)

    def test_props_to_html(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        node2 = f' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), node2)

    def test_props_plus_repr(self):
        node = HTMLNode(
            tag="a", value=None, children=None, props={"href": "https://boot.dev"}
        )
        node2 = f"HTMLNode(a, None, [], {{'href': 'https://boot.dev'}})"
        result = node.props_to_html()
        result2 = f' href="https://boot.dev"'
        self.assertEqual(repr(node), node2)
        self.assertEqual(result, result2)
