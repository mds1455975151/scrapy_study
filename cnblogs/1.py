# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json
import webbrowser


with open("data.json", 'r') as f:
    messages = []
    for line in f.readlines():
        title_name = json.loads(line)['title_name'][0]
        title_url = json.loads(line)['title_url'][0]
        message = """<tr><td>没想好如何生成!!!</td><td><a href=%s" target="_blank">%s</a></td></tr>""" % (title_url, title_name)
        print message
        messages.append(message)
    print messages
    messagess = """%s""" % "".join(messages)
    print messagess


demo_html = "demo.html"  # 命名生成的html
f = open(demo_html, 'w')

html_context = """
<html>
    <head></head>
    <body>
        <p>人生苦短,我用Python!!!</p>
        <table border="1">
            <tr>
                <th>序号</th>
                <th>文章名称</th>
            </tr>
            <tr>
                %s
            </tr>
        </table>
    </body>
</html>""" % (messagess)
f.write(html_context)
f.close()
webbrowser.open(demo_html, new=1)
