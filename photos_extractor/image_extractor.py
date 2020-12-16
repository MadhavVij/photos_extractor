"""Python Module to extract and move images recursively
from given directory and it's subdirectory.
--Author: Madhav Vij
"""
import os, zipfile, errno
from shutil import move
from os.path import exists
import time


def extract_zipfiles(src: str = ".") -> None:
    """Extract files from zipfile recursively
    Args:
        src (str, optional): Source Zipfile Path. Defaults to ".".
    """
    for filename in os.listdir(src):
        if filename.endswith(".zip"):
            name = os.path.splitext(os.path.basename(filename))[0]
            if not os.path.isdir(f"{src}/{name}"):
                try:
                    zip = zipfile.ZipFile(f"{src}/{filename}")
                    os.mkdir(f"{src}/{name}")
                    zip.extractall(path=f"{src}/{name}")
                except zipfile.BadZipfile as e:
                    print("BAD ZIP: " + filename)
                    try:
                        os.remove(f"{src}/{filename}")
                    except OSError as e:
                        if e.errno != errno.ENOENT:
                            raise


def move_images(src: str = ".", dst: str = "./copied_photos") -> None:
    """Move images recursively
    from a directory (and subdirectories)
    and flatten the file structure to destination directory
    Args:
        src (str, optional): [Source Directory]. Defaults to ".".
        dst (str, optional): [Destination directory]. Defaults to "./copied_photos".
    """
    if not exists(dst):
        os.makedirs(dst, exist_ok=True)
    exclude = set(["copied_photos"])
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in exclude]
        for image_name in files:
            if image_name.split(".")[-1].lower() in [
                "jpg",
                "png",
                "jpeg",
                "gif",
                "tiff",
            ]:
                if (
                    f"{image_name.split('.')[-2]}-edited.{image_name.split('.')[-1]}"
                    in files
                    or f"{image_name.split('.')[-2]}-edit.{image_name.split('.')[-1]}"
                    in files
                    or f"{image_name.split('.')[-2]}-edt.{image_name.split('.')[-1]}"
                    in files
                    or f"{image_name.split('.')[-2]}-ed.{image_name.split('.')[-1]}"
                    in files
                ):
                    continue
                else:
                    move(f"{root}/{image_name}", dst)


def rename_files_remove_suffix(directory_path: str = ".") -> None:
    suffix_list = ["-edited", "-edit", "-edt", "-ed"]

    for suffix in suffix_list:
        [
            os.rename(f, f.replace(suffix, ""))
            for f in os.listdir(directory_path)
            if f.split(".")[-2].endswith(suffix)
        ]


if __name__ == "__main__":
    """Driver Function"""
    start_time = time.time()
    curDir, _ = os.path.split(os.path.abspath(__file__))
    src = input(f"Enter zipfile location or leave blank for: {curDir}") or curDir
    dst = f"{curDir}/copied_photos"
    extract_zipfiles(src)
    move_images(src, dst)
    end_time = time.time()
    print(f"Import images to: {dst}")
    # rename_files_remove_suffix(directory_path=src)
    # print(f"Renamed Files in {src}")
    print(f"Time Executed: {end_time - start_time}")
