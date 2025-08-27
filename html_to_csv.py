from bs4 import BeautifulSoup
import csv
from datetime import datetime
import urllib.parse

Init_ID = 187

# 读取 Edge 导出的 HTML 收藏夹文件
with open('bookmarks.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 获取当前系统时间
current_time = datetime.now()
current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
current_time_gmt_str = current_time.strftime('%Y-%m-%d %H:%M:%S')

# 先获取所有链接的数量
links = list(soup.find_all('a'))
total_links = len(links)

# 准备写入 CSV 文件
with open('bookmarks.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # 写入表头，对应 wp_posts 表的字段
    writer.writerow([
        'ID', 'post_author', 'post_date', 'post_date_gmt', 'post_content',
        'post_title', '_sites_link', '_sites_sescribe', '_sites_order', 'post_excerpt', 'post_status', 'comment_status',
        'ping_status', 'post_password', 'post_name', 'to_ping', 'pinged',
        'post_modified', 'post_modified_gmt', 'post_content_filtered',
        'post_parent', 'guid', 'menu_order', 'post_type', 'post_mime_type',
        'comment_count'
    ])
    
    # 计数器，用于生成ID
    post_id = Init_ID
    
    # 提取所有链接并转换为 wp_posts 格式
    for a in soup.find_all('a'):
        title = a.text.strip()
        _sites_link = a.get('href', '')
        
        # 获取添加日期（Unix时间戳转换为日期时间）
        add_date = a.get('add_date', '0')
        if add_date:
            try:
                post_date = datetime.fromtimestamp(int(add_date))
                post_date_str = post_date.strftime('%Y-%m-%d %H:%M:%S')
                post_date_gmt_str = post_date.strftime('%Y-%m-%d %H:%M:%S')
            except:
                post_date_str = current_time_str          # 使用当前系统时间
                post_date_gmt_str = current_time_gmt_str  # 使用当前系统时间
        else:
            post_date_str = current_time_str              # 使用当前系统时间
            post_date_gmt_str = current_time_gmt_str      # 使用当前系统时间
        
        # 生成 post_name（URL编码的标题）
        post_name = urllib.parse.quote(title)

        # 计算倒序的排序值（第一个链接排序值最大）
        _sites_order = total_links + 2*Init_ID - post_id - 1
        
        # 构建一行数据
        row = [
            "",                         # ID
            1,                          # post_author (默认1)
            post_date_str,              # post_date
            post_date_gmt_str,          # post_date_gmt
            '',                         # post_content
            title,                      # post_title
            _sites_link,                # _sites_link
            '',                         # _sites_sescribe
            _sites_order,               # _sites_order
            '',                         # post_excerpt
            'publish',                  # post_status
            'open',                     # comment_status
            '',                         # ping_status
            '',                         # post_password
            post_name,                  # post_name
            '',                         # to_ping
            '',                         # pinged
            post_date_str,              # post_modified
            post_date_gmt_str,          # post_modified_gmt
            '',                         # post_content_filtered
            0,                          # post_parent
            f'http://192.168.0.180:8088/sites/{post_id}.html',  # guid
            0,                          # menu_order
            'sites',                    # post_type
            '',                         # post_mime_type
            0                           # comment_count
        ]
        
        writer.writerow(row)
        post_id += 1

print("转换完成，已生成 bookmarks.csv")
print(f"系统时间: {current_time_str}")