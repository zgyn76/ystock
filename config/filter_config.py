SPOT_FILTERS = [
    {
        'module': 'filters.spot.market_cap_filter',
        'function': 'market_cap_filter',
        'args': {'min_market_cap': 100 * 1e8}
    },
    {
        'module': 'filters.spot.pb_filter',
        'function': 'pb_filter',
        'args': {'max_pb': 1.0}
    }
]

HIST_FILTERS = [
    {
        'module': 'filters.hist.kdj_filter',
        'function': 'kdj_filter',
        'args': {'max_j': 0}
    }
]