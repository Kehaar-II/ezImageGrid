# imageCombiner
a small python script to combine several images into one

## Requirements
imageCombiner requires the followings to work:
- Python 3
- Pillow

## Usage
- place all images in a folder, number in the desired order (images do not need to have to be zero-padded and can use all formats supported by PIL, images must be numbered continuously, the numbering can start at either 0 or 1)
- run the following command
```bash
$ python3 combiner.py path [width]
```

### Description
path: path to the folder containing the numbered images <br>
width: nb of images per row


written in Python 3.11.3
