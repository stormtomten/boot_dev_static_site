import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = f"TextNode(This is a text node, bold, None)"
        self.assertEqual(repr(node), node2)

    def test_noteq(self):
        node = TextNode("This is one text", TextType.TEXT)
        node2 = TextNode("This is another text", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is one text", TextType.TEXT)
        node2 = TextNode("This is one text", TextType.TEXT, None)
        self.assertEqual(node, node2)

    def test_url_differ(self):
        node = TextNode("This is one text", TextType.TEXT)
        node2 = TextNode("This is one text", TextType.TEXT, "boot.dev")
        self.assertNotEqual(node, node2)

    def test_same_url(self):
        node = TextNode("This is one text", TextType.TEXT, "boot.dev")
        node2 = f"TextNode(This is one text, text, boot.dev)"
        self.assertEqual(repr(node), node2)

    def test_dif_text_same_url(self):
        node = TextNode("This is one text", TextType.TEXT, "boot.dev")
        node2 = TextNode("This is another text", TextType.TEXT, "boot.dev")
        self.assertNotEqual(node, node2)

    def test_type_differ(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
