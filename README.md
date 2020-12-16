# Photos Extractor

Photos Extractor is a Python module which can help extract images from zipped folders/directories. 

[Google Photos](https://www.photos.google.com) creates folders and sub-folders when [Google Takeouts](https://takeout.google.com) is used for downloading all/selected Google Photos.
Google Photos also downloads multiple versions of the same photo and mark them as edited and original.


### By default, Photos Extractor will keep the latest version of your photos downloaded from Google Takeouts.

## Installation

Use GitHub's `git clone` command or download this repository using Download option.

```bash
git clone <repository address>
```

## Usage
To set-up the Python project, please install `Python` and add python to your path (if needed).
For running the test scripts, the project would need `pytest` library.
```bash
pip install pytest
```
To run the project, open `terminal/cmd` and navigate to the root of project. Type in the terminal:
```bash
python -m photos_extractor.image_extractor
```

For executing test scripts:
```bash
python -m test.test_image_extractor
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)