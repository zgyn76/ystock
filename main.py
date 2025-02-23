from core.processor import StockProcessor

if __name__ == "__main__":
    # 初始化处理器
    processor = StockProcessor()

    # 加载过滤配置
    processor.load_filters("config.filter_config")

    # 执行处理流程
    final_stocks = processor.process()

    print("最终筛选出的股票代码:")
    print("\n".join(final_stocks))