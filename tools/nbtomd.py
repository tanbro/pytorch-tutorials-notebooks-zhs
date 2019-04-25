#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import subprocess
import sys
from glob import iglob


def parse_arguments():  # type:()->argparse.Namespace
    parser = argparse.ArgumentParser(
        description='将项目中 notebooks 目录下的笔记以 markdown 格式导出到 docs 目录')
    parser.add_argument(
        '--input-dir', '-i', type=str,
        default='notebooks',
        help='要导出的笔记文件的所在目录。该目录及其子目录下的所有笔记都将被导出(default="%(default)s")',
    )
    parser.add_argument(
        '--output-dir', '-o', type=str,
        default='docs',
        help='将笔记导出到这个目录，保留原有的子目录结构(default="%(default)s")',
    )
    return parser.parse_args()


def execute(arguments):  # type:(argparse.Namespace)->None
    root_input_dir = os.path.abspath(arguments.input_dir)
    root_output_dir = os.path.abspath(arguments.output_dir)
    search_pat = os.path.join(root_input_dir, '**', '*.ipynb')
    for filepath in iglob(search_pat, recursive=True):
        dirname, _ = os.path.split(filepath)
        subdir = os.path.relpath(dirname, root_input_dir)
        output_dir = os.path.join(root_output_dir, subdir)
        args = [
            'jupyter-nbconvert',
            '--to', 'markdown',
            '--output-dir', output_dir,
            filepath
        ]
        subprocess.run(args, check=True)


def main():
    arguments = parse_arguments()
    try:
        return execute(arguments)
    except KeyboardInterrupt:
        print('KeyboardInterrupt', file=sys.stderr)


if __name__ == '__main__':
    main()
