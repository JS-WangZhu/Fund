# Fund简介

代码是Python3实现，爬取天天基金网站的相关基金估值与净值，喜欢玩基金的小伙伴一定不要错过（本项目爬虫方式实现，启动较慢，Fund2.0是接口方法获取数据，大家可以转到https://github.com/JS-WangZhu/Fund2.0）

# 安装部署
1. 安装依赖 

    ① Python3 依赖库列表：beautifulsoup4, requests, selenium, prettytable, colorama (pip安装即可)
    ② Phantomjs 用于模拟浏览器访问 (记得修改代码中的本地调用地址，项目dependency文件夹下提供了macOS版本，其他操作系统版本请自行前往官网下载)

2. 修改fund.py中18行左右内容，按照注释修改，记得把dependency文件夹下的压缩包解压

3. 在目录下创建my.txt，文本格式：每行填写一个需要查询的基金号码,结尾不留空行,并以utf-8编码保存

4. 运行项目   `python3 fund.py`

# 项目运行
![项目运行截图](https://github.com/JS-WangZhu/Fund/blob/master/pic.png)

# 最新内容 

1. 加入大盘指数查看功能
2. 添加涨跌显示颜色，便于查看行情
