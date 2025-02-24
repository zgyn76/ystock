import pandas as pd

def pb_filter(df: pd.DataFrame, max_pb: float) -> pd.DataFrame:
    """市净率过滤器"""
    return df[df['市净率'] <= max_pb]