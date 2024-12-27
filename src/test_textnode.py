import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)

  def test_not_eq_text(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text", TextType.BOLD)
    self.assertNotEqual(node, node2)

  def test_not_eq_text_type(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.TEXT)
    self.assertNotEqual(node, node2)
  
  def test_eq_url(self):
    node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
    node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
    self.assertEqual(node, node2)

  def test_repr(self):
    node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
    self.assertEqual(
      "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
    )

class TestTextNodeToHTMLNode(unittest.TestCase):
  def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

  def test_image(self):
    node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(
        html_node.props,
        {"src": "https://www.boot.dev", "alt": "This is an image"},
    )

  def test_bold(self):
    node = TextNode("This is bold", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, "This is bold")
  
  def test_italic(self):
    node = TextNode("This is italic", TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "i")
    self.assertEqual(html_node.value, "This is italic")
  
  def test_code(self):
    node = TextNode("This is code", TextType.CODE)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "code")
    self.assertEqual(html_node.value, "This is code")
  
  def test_link(self):
    node = TextNode("This is a link", TextType.LINK)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "This is a link")

if __name__ == "__main__":
  unittest.main()