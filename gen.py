import os

# 获取当前文件夹路径
current_folder = os.getcwd()

# 创建HTML内容
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>rosjava_boostrap maven repo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 5px 0;
        }
        a {
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .folder {
            font-weight: bold;
        }
        .files {
            margin-left: 20px;
        }
    </style>
</head>
<body>
    <h1>rosjava_bootstrap maven center</h1>
    <ul>
"""

def add_to_html(path, indent=0):
    global html_content
    # 获取路径的相对路径
    rel_path = os.path.relpath(path, current_folder)
    if os.path.isdir(path):
        # 跳过隐藏目录（如 .git）
        if os.path.basename(path).startswith('.'):
            return
        # 文件夹路径在同一行显示
        html_content += f'{"  " * indent}<li class="folder">{rel_path}/</li>\n'
        html_content += f'{"  " * indent}<ul>\n'
        # 列出文件
        files = [entry for entry in sorted(os.listdir(path)) if os.path.isfile(os.path.join(path, entry))]
        if files:
            html_content += f'{"  " * (indent + 1)}<ul class="files">\n'
            for entry in files:
                # 跳过 .html 和 .py 文件
                if entry.endswith(('.html', '.py')):
                    continue
                html_content += f'{"  " * (indent + 2)}<li><a href="{rel_path}/{entry}">{entry}</a></li>\n'
            html_content += f'{"  " * (indent + 1)}</ul>\n'
        # 递归处理子文件夹
        for entry in sorted(os.listdir(path)):
            entry_path = os.path.join(path, entry)
            if os.path.isdir(entry_path) and not entry.startswith('.'):
                add_to_html(entry_path, indent + 1)
        html_content += f'{"  " * indent}</ul>\n'
    else:
        # 跳过 .html 和 .py 文件
        if path.endswith(('.html', '.py')):
            return
        html_content += f'{"  " * indent}<li class="files"><a href="{rel_path}">{os.path.basename(path)}</a></li>\n'

# 从当前文件夹开始递归添加内容
add_to_html(current_folder)

html_content += """
    </ul>
</body>
</html>
"""

# 将HTML内容写入index.html文件
with open("index.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print("index.html 文件已生成！")