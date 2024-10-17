from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	for old_node in old_nodes:
		if old_node.text_type != TextType.TEXT.value:
			new_nodes.append(old_node)
			continue
		split_nodes = []
		sections = old_node.text.split(delimiter)
		if len(sections) % 2 == 0:
			raise ValueError("Invalid markdown, formatted section not closed")
		for i in range(len(sections)):
			if sections[i] == "":
				continue
			if i % 2 == 0:
				split_nodes.append(TextNode(sections[i], TextType.TEXT))
			else:
				split_nodes.append(TextNode(sections[i], text_type))
		new_nodes.extend(split_nodes)
	return new_nodes


def make_nodes(list_strings, control_string, delimiter):
	new_list = []
	for string in list_strings:
		print(string, control_string)
		
		if string == control_string:
			new_list.append(TextNode(string, delimiter))
		else:
			new_list.append(TextNode(string, "text"))
	return new_list
def extract_markdown_images(text):
	pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
	matches = re.findall(pattern, text)
	return matches
	
	#found = re.findall(r"!\[[^\]]*\]\([^\)]+\)", text)
	#return util_split_links(found)

def extract_markdown_links(text):
	pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
	matches = re.findall(pattern, text)
	return matches

		
