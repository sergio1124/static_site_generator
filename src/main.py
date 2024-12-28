from textnode import TextNode, TextType
from htmlnode import HTMLNode
from inline_markdown import split_nodes_link

def main():
  textNode = TextNode("TESTING TEXT", TextType.BOLD, "URL")
  print(textNode)
  attributes = {
    "href": "https://www.google.com",
    "target": "_blank",
  }
  htmlNode = HTMLNode("testTAG", "testValue", [], attributes)
  print(htmlNode)

  node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
  )
  new_nodes = split_nodes_link([node])
  print(new_nodes)
  # [
  #     TextNode("This is text with a link ", TextType.TEXT),
  #     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
  #     TextNode(" and ", TextType.TEXT),
  #     TextNode(
  #         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
  #     ),
  # ]

if __name__ == "__main__":
	main()