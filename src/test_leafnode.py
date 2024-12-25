import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
  def test_eq_attributes(self):
    attributes = {
      "href": "https://www.google.com",
      "target": "_blank",
    }
    leafNode = LeafNode("a", "Click me!", attributes)
    testValue = leafNode.to_html()
    expectedValue = '<a href="https://www.google.com" target="_blank">Click me!</a>'
    self.assertEqual(testValue, expectedValue)

  def test_not_eq_attributes(self):
    attributes = {
      "href": "https://www.google.com",
      "target": "_blank",
    }
    leafNode = LeafNode("a", "Click me!", attributes)
    testValue = leafNode.to_html()
    expectedValue = '<ahref="https://www.google.com" target="_blank">Click me!</a>'
    self.assertNotEqual(testValue, expectedValue)

if __name__ == "__main__":
  unittest.main()