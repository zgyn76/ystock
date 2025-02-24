根据若干个filter筛选标的

filter分为spot filter和hist filter两类：

1. spot filter根据实时指标，如市值、市净率筛选对应标的
  
2. hist filter根据历史指标，如KDJ、MACD（须在filter中完成指标计算）筛选对应标的
  
通过ak.stock_zh_a_spot_em()可以一次获取所有股票实时数据；但所有股票依次通过ak.stock_zh_a_hist()获取，耗时很长，因此先spot filter，再hist filter

filter内实现具体的filter逻辑，config/filter_config.py中设置filter所需参数，运行main.py即可筛选
