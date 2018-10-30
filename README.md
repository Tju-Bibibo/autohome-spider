# autohome-spider
汽车之家爬虫
主要实现了爬取汽车之家https://car.autohome.com.cn
上面的所有厂家和其车型的各种价格，包括在售，即将销售，停售
共计30000多条数据

# car_url_get.py
作用：从https://car.autohome.com.cn/AsLeftMenu/As_LeftListNew.ashx?typeId=1%20&brandId=36%20&fctId=152%20&seriesId=0
这个界面得到要爬取的所有厂商url和名字分别存到car_url和car_url_name中

# car_spider.py
作用：主爬虫，从上面得到的厂商里面把所有状态的车型信息全部爬取下来

# data.txt
爬取结果

# car_home_data.xlsx
爬取结果转换成xlsx格式
