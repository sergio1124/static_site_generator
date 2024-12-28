import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_olist,
    block_type_ulist,
    block_type_quote,
)


class TestMarkdownToHTML(unittest.TestCase):
  def test_markdown_to_blocks(self):
    md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
      blocks,
      [
        "This is **bolded** paragraph",
        "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
        "* This is a list\n* with items",
      ],
    )

  def test_markdown_to_blocks_newlines(self):
    md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
      blocks,
      [
        "This is **bolded** paragraph",
        "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
        "* This is a list\n* with items",
      ],
    )

  def test_block_to_block_type_heading(self):
    block = "#### This is a heading"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, "heading")

  def test_block_to_block_type_code(self):
    block = "```\nThis is code\n```"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, "code")

  # def test_block_to_block_type_quote(self):
  #   block = ">This is a quote\n>This is another quote in a newline"
  #   block_type = block_to_block_type(block)
  #   self.assertEqual(block_type, "quote")

if __name__ == "__main__":
  unittest.main()