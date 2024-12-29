from markdown_blocks import markdown_to_html_node
from inline_markdown import extract_title

import os

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")

  # Read contents of markdown file and store in a variable.
  try:
    markdown_file = open(from_path, "r")
    markdown_contents = markdown_file.read()
  except FileNotFoundError:
    print(f"Error: File not found at path: {from_path}")
  finally:
    if 'markdown_file' in locals():
      markdown_file.close()

  # Read contents of template file and store in a variable.
  try:
    template_file = open(template_path, "r")
    template_contents = template_file.read()
  except FileNotFoundError:
    print(f"Error: File not found at path: {template_path}")
  finally:
    if 'template_file' in locals():
      template_file.close()

  # Conver markdown to html node and from html node to html string.
  html_node = markdown_to_html_node(markdown_contents)
  html_string = html_node.to_html()

  # Extract the h1 title from markdown
  title = extract_title(markdown_contents)

  # Replacing title in template with the actual title
  template_with_title = template_contents.replace("{{ Title }}", title)

  # Replacing content in template with html string
  template_with_content = template_with_title.replace("{{ Content }}", html_string)

  # Open the dest_file in write mode
  with open(dest_path, "w") as file:
    # Write data to the file
    file.write(template_with_content)
