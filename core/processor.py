import importlib
from functools import reduce
from typing import Dict
from .data_loader import DataLoader
from tqdm import tqdm


class FilterLoader:
    @staticmethod
    def _load_filter_func(filter_config: Dict):
        """动态加载过滤函数"""
        try:
            module = importlib.import_module(filter_config['module'])
            return getattr(module, filter_config['function'])
        except (ImportError, AttributeError) as e:
            raise RuntimeError(f"无法加载过滤器 {filter_config['module']}.{filter_config['function']}") from e


def _apply_filters(data, filter_chain):
    """应用过滤器链"""
    return reduce(lambda d, f: f(d), filter_chain, data)


class StockProcessor(FilterLoader):
    def __init__(self):
        self.spot_filter_chain = []
        self.hist_filter_chain = []

    def _build_filter_chain(self, config_type: str):
        """构建过滤器链"""
        config = getattr(self.config, config_type, [])
        chain = []

        for filter_config in config:
            filter_func = self._load_filter_func(filter_config)
            # 使用闭包保留参数
            chain.append(
                (lambda func, args: lambda x: func(x, **args))(
                    filter_func,
                    filter_config.get('args', {})
                )
            )
        return chain

    def load_filters(self, config_module: str):
        """加载所有过滤器"""
        self.config = importlib.import_module(config_module)
        self.spot_filter_chain = self._build_filter_chain('SPOT_FILTERS')
        self.hist_filter_chain = self._build_filter_chain('HIST_FILTERS')

    def process(self):
        # 获取并过滤实时数据
        raw_df = DataLoader.get_spot_data()
        filtered_df = _apply_filters(raw_df, self.spot_filter_chain)

        # 处理历史数据
        results = []
        for symbol in tqdm(filtered_df['代码'].tolist()):
            hist_data = DataLoader.get_hist_data(symbol)
            if hist_data is not None:
                if all(
                        _apply_filters(hist_data, [f])
                        for f in self.hist_filter_chain
                ):
                    results.append(symbol)
        return results