# Scrapy — 爬虫项目集合

`D:\pycharm\Scrapy` 是一个 **Scrapy 爬虫项目集合**，包含 4 个独立爬虫，分别爬取亚马逊、京东、QQ 新闻与手机靓号网站的数据。`main.py` 为 PyCharm 默认模板文件（占位，非实际入口）。

## 子项目一览

| 子目录 | 爬虫 | 目标站点 | 采集内容 |
| --- | --- | --- | --- |
| `amazon/` | mobile | amazon.com | 亚马逊手机搜索页的商品标题 |
| `jd/` | electrical | dc.3.cn（京东分类接口） | 京东 3C/家电商品分类链接与标题 |
| `news_qq/` | news | qq.com | QQ 首页新闻栏目链接 |
| `phone_test/` | phone | jihaoba.com | 手机靓号（11 位）及对应价格 |

## 目录结构

```
Scrapy/
├── main.py                 # PyCharm 默认模板（占位）
├── amazon/                 # 亚马逊爬虫（Scrapy 标准工程）
│   └── amazon/spiders/mobile.py
├── jd/                     # 京东分类爬虫
│   └── jd/spiders/electrical.py
├── news_qq/                # QQ 新闻爬虫
│   └── news_qq/spiders/news.py
└── phone_test/             # 手机靓号爬虫
    ├── phone_test/spiders/phone_spider.py   # 主爬虫（翻页采集号码+价格）
    ├── phone_test/spiders/news.py           # 测试爬虫
    └── a.json                               # 爬取结果样例
```

## 运行方式

每个子项目都是标准 Scrapy 工程，在其目录下执行：

```bash
cd Scrapy/amazon
scrapy crawl mobile          # 亚马逊手机标题

cd Scrapy/jd
scrapy crawl electrical      # 京东分类

cd Scrapy/news_qq
scrapy crawl news            # QQ 新闻链接

cd Scrapy/phone_test
scrapy crawl phone           # 手机靓号 + 价格
```

## 爬虫说明

- **amazon**：解析 `sg-col-inner` 区块中的 `h2` 商品标题，属于搜索页标题采集示例。
- **jd**：请求京东分类接口 `https://dc.3.cn/category/get`（GBK 编码 JSON），解析分类 url 与标题。
- **news_qq**：解析 QQ 首页 `qqhome-command-area` 区块的新闻链接（`a.linkto`）。
- **phone_test**：遍历靓号列表页，用正则提取 11 位手机号与价格（支持"万"单位换算），并自动翻页至最后一页；结果写入 `a.json`。

## 注意事项

- 爬虫主要用于学习与测试，请遵守目标网站 robots 协议与相关法律法规，控制请求频率。
- 各工程含标准的 `items.py` / `pipelines.py` / `settings.py`，可按需启用 Item Pipeline 持久化。
