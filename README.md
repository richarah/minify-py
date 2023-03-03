# webminify

Python module providing functions for minifying files with the extensions of .html, .js, or .css. It includes two functions, `minify_file()` and `minify_dir()`.



**Please note:** This is a work in progress and in need of further refinement & testing. It is strongly recommended to back up your files before running them through this.



## Prerequisites

Requires csscompressor, htmlmin, and jsmin to be installed in the Python 3 environment.



## Functions

#### minify_file(file_path)

This function takes a file path as input and checks if the file extension is .html, .js, or .css. If the file extension matches, it applies the appropriate minification process, which can reduce the size of the file without changing its functionality. 

Parameters:

- `file_path`: A string that represents the path to the file to be minified.

Returns:

- None. File located at `file_path` is minified.



#### minify_dir(dir_path)

This function takes a directory path as input and applies the minify_file() function recursively to all files within the directory and its subdirectories that have the extensions of .html, .js, or .css.

Parameters:

- dir_path: A string that represents the path to the directory containing the files to be minified.

Returns:

- None. Any valid HTML, CSS or JS files within `dir_path` are minified.