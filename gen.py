'''
Author: Ceoifung
Date: 2025-02-26 15:20:30
LastEditors: Ceoifung
LastEditTime: 2025-02-26 15:20:35
Description: XiaoRGEEK All Rights Reserved. Powered By Ceoifung
'''
import os

# 获取当前文件夹路径
current_folder = os.getcwd()

# 获取当前文件夹中的所有文件和文件夹
entries = os.listdir(current_folder)

# 创建HTML内容
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index of Current Folder</title>
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
    </style>
</head>
<body>
    <h1>Index of Current Folder</h1>
    <ul>
"""

# 遍历文件夹中的内容并添加到HTML列表中
for entry in entries:
    if entry == "index.html":  # 跳过生成的index.html文件本身
        continue
    if os.path.isdir(os.path.join(current_folder, entry)):
        html_content += f'        <li><a href="{entry}/">{entry}/</a></li>\n'
    else:
        html_content += f'        <li><a href="{entry}">{entry}</a></li>\n'

html_content += """
    </ul>
</body>
</html>
"""

# 将HTML内容写入index.html文件
with open("index.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print("index.html 文件已生成！")