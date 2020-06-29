import sys
from os import path
import markdown
import codecs

css = '''
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<style type="text/css">
    * {
        font-family: SimSun;
    }
</style>
'''

def md2html(tid):
    # print('into md2html')
    in_file = path.join(path.dirname(__file__), str(tid), 'post.md')
    out_file = path.join(path.dirname(__file__), str(tid), 'cvt.html')
    input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    text = input_file.read()
    html = markdown.markdown(text)
    output_file = codecs.open(out_file, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_file.write(css + html)
