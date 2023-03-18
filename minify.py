import os
import sys
import csscompressor
import htmlmin
from jsmin import jsmin


# Functions for minifying strings of content
def minify_html(html):
    return htmlmin.minify(html, remove_comments=True, remove_empty_space=True)

def minify_css(css):
    return csscompressor.compress(css)

def minify_js(js):
    return jsmin(js)



def fwrite(path, content):
    with open(path, 'w') as f:
        f.write(content)


# WIP; rewirte to return
def minify_file(file_path):
    try:
        with open(file_path, 'r') as f:
            file_content = f.read()
            if file_path.endswith(".js"):
                # Uses different syntax to the others(?)
                minified = jsmin(f.read())
            elif file_path.endswith(".html") or file_path.endswith(".css"):
                if file_path.endswith('.html'):
                    minified = htmlmin.minify(file_content, remove_comments=True, remove_empty_space=True)
                elif file_path.endswith('.css'):
                    minified = csscompressor.compress(file_content)
            else:
                minified = file_content
            
            # No matter the result
            print("Minified", file_path)
            print("Size factor:", sys.getsizeof(minified) / sys.getsizeof(file_content))
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
