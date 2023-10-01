# ezImageGrid
a small python script to combine several images into one

## Requirements
ezImageGrid requires the followings to work:
- Python 3
- Pillow

## Usage

```
$ python3 combiner.py path_to_image_folder [-w|--width nrows] [-s|--sort number|date] [-c|--center top|bottom|both]
$ python3 combiner.py -h|--help
```

### Options

-w, --width _nrows_ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  number of images per row in the final grid <br>
-s, --sort _number_|_date_ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sort the images in the grid either by the number in their filename or by the creation date of the file (for _date_, non zero-padded filename and zero-padding filename up to 4 digit are supported and can be mixed, filetypes can also be mixed)<br>
~~-c, --center _top_|_bottom_|_both_ &nbsp;&nbsp;&nbsp;&nbsp;  if there is any incomplete row, centers it in the chosen location(s) (not centered by default)~~ <br>
-h, --help &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prints this message


written in Python 3.11.3
