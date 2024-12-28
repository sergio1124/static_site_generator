from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
  textNode = TextNode("TESTING TEXT", TextType.BOLD, "URL")
  print(textNode)
  attributes = {
    "href": "https://www.google.com",
    "target": "_blank",
  }
  htmlNode = HTMLNode("testTAG", "testValue", [], attributes)
  print(htmlNode)

if __name__ == "__main__":
	main()