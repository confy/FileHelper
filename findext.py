import os
import sys
import shutil
import click
from pathlib import Path


@click.command()
@click.option('--inpath', 'i', default=os.getcwd(), help='Path to search for files - defaults = programs directory')
@click.option('--outpath', '-o', help='Path to move/copy files to')
@click.option('--ext', 'e', help='File extension to look for')
@click.option('--action', 'a', default='mv', help='Action to use - mv, cp, or rm, default = mv')
@click.option('--recursive', '-r', default=False, help='Search for files in recursive subdirs - default = False')
def findExt(inpath, outpath, ext, operation, recursive):
    if outpath is None:
        outpath = input("Choose output dir")
    elif operation == 'cp':
        cp_ext_files(inpath, outpath, ext, recursive)
    elif operation == 'mv':
        mv_ext_files(inpath, outpath, ext, recursive)
    elif operation == 'rm':
        rm_ext_files(inpath, ext, recursive)


def mv_ext_files(in_path: str, out_path: str, ext: str, recursive: bool = False):
    """ move all files of some ext to folder"""
    if not recursive:
        for path in os.scandir(in_path):
            shutil.move(path, f'{out_path}/{path}')
    elif recursive == True:
        for path in Path(in_path).rglob(f'*{ext}'):
            shutil.move(path, f'{out_path}\\{path.name}')


def cp_ext_files(in_path: str, out_path: str, ext: str, recursive: bool = False):
    """ copy all files of some ext to f"""
    if not recursive:
        for path in os.scandir(in_path):
            shutil.copy(path, f'{out_path}\\{path}')
    elif recursive == True:
        for path in Path(os.getcwd()).rglob(f'*{ext}'):
            shutil.copy(path, f'{out_path}\\{path.name}')


def rm_ext_files(in_path: str, ext: str, recursive: bool = False):
    """ remove all files of some ext to f"""
    if not recursive:
        for path in os.scandir(in_path):
            os.remove(path)
    elif recursive == True:
        for path in Path(os.getcwd()).rglob(f'*{ext}'):
            os.remove(path.name)


if __name__ == '__main__':
    findExt()
