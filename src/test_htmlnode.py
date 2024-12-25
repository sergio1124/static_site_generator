import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
  def test_eq_attributes(self):
    attributes = {
      "href": "https://www.google.com",
      "target": "_blank",
    }
    htmlNode = HTMLNode("testTAG", "testValue", [], attributes)
    testValue = htmlNode.props_to_html()
    expectedValue = ' href="https://www.google.com" target="_blank"'
    self.assertEqual(testValue, expectedValue)

  def test_not_eq_attributes(self):
    attributes = {
      "href": "https://www.google.com",
      "target": "_blank",
    }
    htmlNode = HTMLNode("testTAG", "testValue", [], attributes)
    testValue = htmlNode.props_to_html()
    expectedValue = 'href="https://www.google.com"target="_blank"'
    self.assertNotEqual(testValue, expectedValue)

if __name__ == "__main__":
  unittest.main()