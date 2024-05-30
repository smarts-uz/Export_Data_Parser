import os
import re

def rd_finder():
    html_text = ''
    path = "c:/Users/Administrator/Desktop/Work/data/Files"
    src_html_path ="c:/Users/Administrator/Desktop/Work/data/Ex1"
    for root, dirs, files in os.walk(src_html_path):
        for file in files:
            if file.startswith('message') and file.endswith('.html'):
                print(os.path.join(root, file))
                html_path = os.path.join(root, file)
                with open(html_path, "r") as html_file:
                    html = html_file.read()
                    html_text += html


    list_dir = os.listdir(path)
    for filename in list_dir[:1]:
        print(filename)


                # html_files.append(os.path.join(root, file))
                # for d in dirs: dirs.remove(d)
                # print(html_files)


rd_finder()