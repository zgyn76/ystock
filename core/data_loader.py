import akshare as ak

class DataLoader:
    @staticmethod
    def get_spot_data():
        """获取实时行情数据"""
        return ak.stock_zh_a_spot_em()

    @staticmethod
    def get_hist_data(symbol, period="daily"):
        """获取个股历史数据"""
        try:
            # 使用 stock_zh_a_hist 获取单只股票的日线数据，前复权
            return ak.stock_zh_a_hist(symbol=symbol, period=period, start_date='20000101', adjust="qfq")
        except Exception as e:
            print(f"获取 {symbol} 历史数据失败: {str(e)}")
            return None