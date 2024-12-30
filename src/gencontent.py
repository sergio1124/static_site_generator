from markdown_blocks import markdown_to_html_node
from pathlib import Path
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
    template = template_file.read()
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
  template = template.replace("{{ Title }}", title)

  # Replacing content in template with html string
  template = template.replace("{{ Content }}", html_string)

  dest_dir_path = os.path.dirname(dest_path)
  if dest_dir_path != "":
      os.makedirs(dest_dir_path, exist_ok=True)
  to_file = open(dest_path, "w")
  to_file.write(template)

def extract_title(markdown):
  lines = markdown.split("\n")
  for line in lines:
    if line.startswith("# "):
      return line.lstrip("# ").strip()
  raise Exception("Invalid markdown, no h1 title")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  for filename in os.listdir(dir_path_content):
    from_path = os.path.join(dir_path_content, filename)
    dest_path = os.path.join(dest_dir_path, filename)
    if os.path.isfile(from_path):
      dest_path = Path(dest_path).with_suffix(".html")
      generate_page(from_path, template_path, dest_path)
    else:
      generate_pages_recursive(from_path, template_path, dest_path)
