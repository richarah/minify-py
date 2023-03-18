import os
import sys
import csscompressor
import htmlmin
from jsmin import jsmin


# Functions for minifying strings of content
# Not using the htmlmin, csscompressor etc. directly, so we can easily switch minification engines in the future
def minify_html(html):
    return htmlmin.minify(html, remove_comments=True, remove_empty_space=True)

def minify_css(css):
    return csscompressor.compress(css)

def minify_js(js):
    return jsmin(js)

def minify_content(string, content_type=None):
    try:
        if content_type="html":
            return minify_html(string)
        elif content_type="css":
            return minify_css(string)
        elif content_type="js":
            return minify_js(string)
        else:
            return string
    except:
        return string
        

# File & dir manipulation related functions
def fwrite(path, content):
    with open(path, 'w') as f:
        f.write(content)

# Use regular expression to match the file extension at the end of the filename
# Not using os/mimetypes etc.; this has to work with a string
def get_content_type(filename):
    match = re.search(r'\.([^.]+)$', filename)
    if match:
        return match.group(1)
    else:
        return None

def minify_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            content_type = get_content_type(file_path)
            minified = minify_content(content, content_type)
            
            # No matter the result
            print("Minified", file_path)
            print("Size factor:", sys.getsizeof(minified) / sys.getsizeof(content))
            fwrite(file_path, minified)
    except:
        print("ERROR", file_path)

def minify_dir(directory):
  for root, dirs, files in os.walk(directory):
      for file in files:
          file_path = os.path.join(root, file)
          minify_file(file_path)
          
# DEBUG
if __name__ == "__main__":
    dirname = input("Path to directory: ")
    minify_dir(os.path.join(os.path.abspath(os.path.dirname(__file__)), dirname))
