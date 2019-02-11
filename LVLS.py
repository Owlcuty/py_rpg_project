nms = {
    0: (10, 10),
    1: (13, 13)
}

lvls_units = [
    {
        'Exit': [[0, nms[0][0] - 1]],
        'Hero': [[nms[0][1] - 1, 0]],
        'mag': [[2, 5], [2, 6], [3, 7]],
        'war': [[3, 4], [4, 5], [8, 5], [6, 7]],
        'pal': [[6, 8]],
        'pro': [],
        'slr': []
    },


    {
        'Exit': [[0, nms[1][0] - 1]],
        'Hero': [[nms[1][1] - 1, 0]],
        'mag': [[2, 5], [2, 6], [3, 7]],
        'war': [[3, 4], [4, 5], [8, 5], [6, 7]],
        'pal': [[6, 8], [5, 8]],
        'pro': [],
        'slr': [[3, 4], [1, 9]]
    }
]