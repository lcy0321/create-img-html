#! python3
# -*- coding: utf-8 -*-
# pylint: disable=W0622
"""Create a html file that shows the images.

This script create a html file that shows the images in the specified
directory.

usage: create_img_html.py [-h] [-t TITLE] [-w WIDTH] [-e [EXT [EXT ...]]]
                          [-T TEMPLATE] [-o OUTPUT]
                          [path]
"""
from __future__ import print_function
from __future__ import unicode_literals
from builtins import open

from pathlib import Path
from argparse import ArgumentParser
from argparse import ArgumentDefaultsHelpFormatter
from mako.template import Template

def get_img_list(path, ext_name):
    """Get the filenames of the images with the given path and entension name.

    Args:
        path (str): the path contains the image files.
        ext_name (list of str): the file with the extension name in the
            ext_name will be considered as a image file.

    Returns:
        list of str: a list contains the filenames of the images.

    """
    img_list = []
    img_path = Path(path)
    for file in img_path.iterdir():
        if file.suffix in ext_name:
            img_list.append(file.name)
    return img_list

def create_html(img_list, title, width, template_file):
    """Create a html string that shows the images.

    Args:
        img_list (list of str): the list contains the filenames of the images.
        title (str): the title of the html.
        width (int): the width of the image in the html.
        template_file (str): the template filename.

    Returns:
        str: a html string that shows the images.

    """
    var_dict = {
        'title': title,
        'width': width,
        'img_list': img_list
    }
    template = Template(filename=template_file)
    return template.render(**var_dict)

def main():
    """Create a html file that shows the images.

        Step1: Parse the arguments.
        Step2: Get the filenames of the images.
        Step3: Create a html string that shows the images.
        Step4: Write it to a output file.

    """
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        description='Create a html file that shows the images.')
    parser.add_argument('path', default='.', nargs='?',
                        help='path that contains the images')
    parser.add_argument('-t', '--title', default='View',
                        help='title of the html file')
    parser.add_argument('-w', '--width', type=int, default='800',
                        help='width of the image in the html file')
    parser.add_argument('-e', '--ext', nargs='*', default=['jpg', 'png'],
                        help='extension names of the images')
    parser.add_argument('-T', '--template', default='template.html',
                        help='the template file of the html')
    parser.add_argument('-o', '--output', default='View.html',
                        help='the output file name')

    args = parser.parse_args()
    args.ext = ['.' + ext_name for ext_name in args.ext]    #add '.' to ext

    img_list = get_img_list(args.path, args.ext)
    img_html = create_html(img_list, args.title, args.width, args.template)
    with open(args.output, 'w', encoding='utf-8', newline='') as output:
        output.write(img_html)

if __name__ == '__main__':
    main()
