def calc_nd(sr_event, dict_speed, dsize=.125, area=45.6 / (100 ** 2), dt=60):
    ND = 0

    for speed in sr_event.index:
        if pd.notnull(sr_event.loc[speed]):
            dspeed = dict_speed[speed]
            ND += sr_event.loc[speed] / (speed * area * dt * dsize)
    return ND


def calc_nt(sr_event, dict_speed, dsize=.125, area=45.6 / (100 ** 2), dt=60):
    NT = 0
    for speed in sr_event.index:
        if pd.notnull(sr_event.loc[speed]):
            dspeed = dict_speed[speed]
            NT += (sr_event.loc[speed] / (speed * area * dt))
    return NT


def calc_W(sr_event, dict_speed, dsize=.125, area=45.6 / (100 ** 2), dt=60):
    W = 0
    for speed in sr_event.index:

        if pd.notnull(sr_event.loc[speed]):
            dspeed = dict_speed[speed]
            W += (sr_event.loc[speed] / (speed * area * dt)) * size ** 3
    return W


def calc_R(sr_event, dict_speed, dsize=.125, area=45.6 / (100 ** 2), dt=60):
    R = 0
    for speed in sr_event.index:
        if pd.notnull(sr_event.loc[speed]):
            dspeed = dict_speed[speed]
            R += (sr_event.loc[speed] / (area * dt)) * size * 3.
    return R


def calc_Z(sr_event, dict_speed, dsize=.125, area=45.6 / (100 ** 2), dt=60):
    Z = 0
    for speed in sr_event.index:

        if pd.notnull(sr_event.loc[speed]):
            dspeed = dict_speed[speed]
            Z += (sr_event.loc[speed] / (speed * area * dt)) * size ** 6

    return Z