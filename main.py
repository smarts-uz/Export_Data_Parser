import os
import re
import time
from tkinter import filedialog
from rich import print
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
    if os.path.exists(f"{path}/All.txt"):
        os.remove(f"{path}/All.txt")
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
            print(f'{filename} [green]found')
        else:
            print(f'{filename} [red]not found')
            with open(f'{path}/All.txt', "a") as f:
                f.write(f'{filename}\n')
    print('Process Successfully ended!!!!!!!!!!!')
    print('Process Successfully ended!!!!!!!!!!!')
    print('Process Successfully ended!!!!!!!!!!!')
    print('Process Successfully ended!!!!!!!!!!!')
    with open(f'{path}/All.txt', "r") as f:
        txt = f.read()
        input(f"path: {path}/All.txt\n"
              f"{txt}\n"
              f"press enter to close window")



if __name__ == '__main__':
    rd_finder()