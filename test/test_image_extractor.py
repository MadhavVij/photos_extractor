import pytest
import os
from google_photos_extractor.image_extractor import (
    extract_zipfiles,
    move_images,
    rename_files_remove_suffix,
)


def test_extract_zipfiles():
    extract_zipfiles("./test/data")
    assert os.path.isdir("./test/data/sample_images")


def test_move_images():
    move_images("./test/data/sample_images", "./test/data/copied_photos")
    assert os.path.isdir("./test/data/copied_photos")


def test_rename_files_remove_suffix():
    sample_dir = "./test/data/copied_photos"
    rename_files_remove_suffix(sample_dir)
    for f in os.listdir(sample_dir):
        assert not f.split(".")[-2].endswith("-edit")
