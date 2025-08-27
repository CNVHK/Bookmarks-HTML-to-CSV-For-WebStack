环境需求:
任意版本3.x版本的Python解释器，并通过pip安装BeautifulSoup4包。
```pip install beautifulsoup4```

脚本用途：
对于Wordpress版本的WebStack导航主题，没有从浏览器导入收藏夹的功能，只能自己手动从浏览器导出为HTML，使用该脚本可以把HTML转成CSV，然后使用Wordpress的Ultimate CSV Importer Free插件，导入Sties类型即可。
<img width="2559" height="1169" alt="image" src="https://github.com/user-attachments/assets/69435d6a-0727-41e7-88ba-1224fdaedb29" />
这里需要手动添加两个字段名，_sites_link代表CSV里的网址链接，_sites_order为脚本自动生成的排序权重，默认会保持与浏览器书签一致的排序。
