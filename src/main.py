from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
  textNode = TextNode("TESTING TEXT", TextType.BOLD, "URL")
  print(textNode)
  attributes = {
    "href": "https://www.google.com",
    "target": "_blank",
  }
  htmlNode = HTMLNode("testTAG", "testValue", [], attributes)
  print(htmlNode)
  leafNode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
  print(leafNode)

if __name__ == "__main__":
	main()