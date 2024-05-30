import os
import re
import time
from tkinter import filedialog

# Display the dialog for browsing files.
# filename = filedialog.askopenfilename()

# Print the selected file path.

def rd_finder():
    html_text = ''

    path = filedialog.askdirectory()
    src= filedialog.askopenfilename(
        filetypes=(
            ("html files", "*.html"),
            # ("Python Files", ("*.py", "*.pyx")),
            # ("All Files", "*.*")
        )
    )
    src_html_path, ext = os.path.split(src)

    for root, dirs, files in os.walk(src_html_path):
        for file in files:
            if file.startswith('message') and file.endswith('.html'):
                html_path = os.path.join(root, file)
                with open(html_path, "r") as html_file:
                    html = html_file.read()
                    html_text += html
    list_dir = os.listdir(path)
    for filename in list_dir:
        x = re.search(f'{filename}', html_text)
        if bool(x) == True:
            continue
        else:
            with open(f'c:/export_data_search.txt', "a") as f:
                f.write(f'{filename}\n')


                # html_files.append(os.path.join(root, file))
                # for d in dirs: dirs.remove(d)
                # print(html_files)


if __name__ == '__main__':
    rd_finder()