import  pandas as pd

def calculate_kdj(data, n=9, m1=3, m2=3):
    """
    计算 KDJ 指标
    :param data: 包含 'close', 'high', 'low' 列的 DataFrame
    :param n: RSV 周期，默认为 9
    :param m1: K 平滑因子，默认为 3
    :param m2: D 平滑因子，默认为 3
    :return: 包含 'K', 'D', 'J' 列的 DataFrame
    """
    low_min = data['最低'].rolling(window=n).min()
    high_max = data['最高'].rolling(window=n).max()
    rsv = (data['收盘'] - low_min) / (high_max - low_min) * 100
    data['K'] = rsv.ewm(com=m1 - 1, adjust=False).mean()
    data['D'] = data['K'].ewm(com=m2 - 1, adjust=False).mean()
    data['J'] = 3 * data['K'] - 2 * data['D']
    return data

def kdj_filter(df: pd.DataFrame, max_j: int):
    data_with_kdj = calculate_kdj(df)
    return data_with_kdj['J'].iloc[-1] < max_j