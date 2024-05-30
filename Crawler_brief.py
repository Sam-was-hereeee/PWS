import requests
from bs4 import BeautifulSoup
from lxml.html import fromstring
from bs4 import BeautifulSoup
import html_to_json
import json
import xmljson
from lxml import etree
import time

f_in = open("courses_selenium.txt", "rt", encoding='utf-8')
f_out = open("courses_brief.txt", "wt", encoding='utf-8')
all_courses = f_in.readlines()
base_url = "https://nol.ntu.edu.tw/nol/coursesearch/"
final_dict = {}
counter = 0
for course in all_courses[6000:]:
    counter += 1
    c = course.split('/')
    id = c[0]
    try:
        link = c[6]
    except IndexError:
        print(id, "is not a valid")
        continue
    if link == "no_link":
        print(id, "is no link")
    else:
        try:
            print("working on", id)
            response = requests.get(base_url + link)
            html_string = response.text
            # tree1 = etree.HTML(response.text)
            tree = etree.HTML(response.text)

            table = tree.xpath("/html/body/table")[0]
            table_data = {}
            for c, row in enumerate(table.xpath(".//tr")):
                row_data = []
                for cell in row.xpath(".//td | .//th"):
                    cell_text = ''.join(cell.itertext()).strip()
                    cell_text = cell_text.replace("    ", "")
                    cell_text = cell_text.replace("\t", "")
                    cell_text = cell_text.replace('\n', ' ')
                    cell_text = cell_text.replace('\n', ' ')
                    cell_text = cell_text.replace('\n', ' ')
                    row_data.append(cell_text)
                if c >= 2:
                    table_data[row_data[0]] = row_data[1:]


            # Convert the table data to a JSON string

            # new_tree = etree.Element(table[0].tag)
            # # Append selected elements to the new tree
            # for element in table:
            #     new_tree.append(element)
            # table_dict = html_to_json.convert(etree.tostring(new_tree, encoding='unicode', pretty_print=True))
            # json_result = json.dumps(table_dict, ensure_ascii=False)

            final_dict[id] = table_data

            print(table_data)

            # Serialize the new tree to string
            # new_tree_string = etree.tostring(new_tree, pretty_print=True, method="text", encoding="UTF-8")
            # new_tree_string = new_tree_string.decode("utf-8")
            # new_tree_string = new_tree_string.replace("    ", "")
            # new_tree_string = new_tree_string.replace("\t", "")
            # new_tree_string = new_tree_string.replace('\n', ' ')
            # new_tree_string = new_tree_string.replace('\n', ' ')
            # new_tree_string = new_tree_string.replace('\n', ' ')
            # f_out.write(id + new_tree_string + "\n")
        except IndexError as e:
            print("index_error")
            f_out.write(id + "index_error\n")
            continue
        except Exception as e:
            f_out.write(id + "unknown error\n")
            print("unknown error")
            continue
    if int(id) >= 6050:
        break
f_out.write(str(final_dict))
