# ezImageGrid
a small python script to combine several images into one

## Requirements
ezImageGrid requires the followings to work:
- Python 3
- Pillow

## Usage
```
$ python3 combiner.py path_to_image_folder [general_options]... [-f|--files filename...]
$ python3 combiner.py -h|--help
```

### Options
#### General Options
-w, --width _nrows_ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  number of images per row in the final grid <br>
-s, --sort number|date &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sort the images in the grid either by the number in their filename or by the creation date of the file (for date, non zero-padded filename and zero-padding filename up to 4 digit are supported and can be mixed, filetypes can also be mixed)<br>
-c, --center top|both|both-bottom|bottom &nbsp;&nbsp;&nbsp;&nbsp;  if there is any incomplete row, centers it in the chosen location(s) (not centered by default)

#### Other options
-f, --files _filename_... &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; files to be used (overrides -s and default file seeking)<br>
-h, --help &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prints help message

### Example

<div align="center">
    <h3>Inputs</h3>
    <img src="https://raw.githubusercontent.com/Kehaar-II/Kehaar-II.github.io/main/READMEs/combiner/input.png" alt="Logo" height="200">
</div>
<br>
<div align="center">
    <h3>Output</h3>
    <img src="https://raw.githubusercontent.com/Kehaar-II/Kehaar-II.github.io/main/READMEs/combiner/output.png" alt="Logo" height="200">
</div>
<br>

```shell
$ python3 combiner.py . -w 4
```


written in Python 3.11.3
