#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys
from glob import iglob

from nbconvert import MarkdownExporter


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


def execute(arguments):
    exporter = MarkdownExporter()
    input_dir = os.path.normpath(arguments.input_dir)
    output_dir = os.path.normpath(arguments.output_dir)
    search_pat = os.path.join(input_dir, '**', '*.ipynb')
    for path in iglob(search_pat, recursive=True):
        dirname, filename = os.path.split(path)
        subdir = os.path.relpath(dirname, input_dir)
        filename, _ = os.path.splitext(filename)
        output_file = os.path.join(output_dir, subdir, f'{filename}.md')
        os.makedirs(os.path.join(output_dir, subdir), exist_ok=True)
        print(f'{path} ==> {output_file}')
        content, _ = exporter.from_filename(path)
        with open(output_file, 'w') as fp:
            print(content, file=fp)


def main():
    arguments = parse_arguments()
    try:
        return execute(arguments)
    except KeyboardInterrupt:
        print('KeyboardInterrupt', file=sys.stderr)


if __name__ == '__main__':
    main()
