import pandas as pd

def market_cap_filter(df: pd.DataFrame, min_market_cap: int) -> pd.DataFrame:
    """总市值过滤器"""
    return df[df['总市值'] >= min_market_cap]