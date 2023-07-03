import pandas as pd

dict_idx = {i - 43: range(i, 484, 22) for i in range(44, 66)}
list_speed = {0.10: .2, .3: .2, .5: .2, .7: .2, .9: .2,
    1.2: .4, 1.6: .4, 2.0: .4, 2.4: .4, 2.8: .4, 3.2: .4,
    3.8: .8, 4.6: .8, 5.4: .8, 6.2: .8, 7.0: .8, 7.8: .8, 8.6: .8,
    9.5: 1.,
    11.: 10.}
list_size = {.125: .125, .25: .125, .375: .125,
    .5: .25, .75: .25, 1.: .25, 1.25: .25, 1.5: .25, 1.75: .25,
    2.: .5, 2.5: .5, 3.: .5, 3.5: .5, 4.: .5, 4.5: .5,
    5.: .5, 5.5: .5, 6.: .5, 6.5: .5, 7.: .5, 7.5: .5,
    8.: 1.}
delta_diam = pd.Series(sorted(list_size.values()), index=sorted(list_size)).astype(float)
diameters = pd.Series(sorted(list_size.keys()), index=sorted(list_size)).astype(float)


def calc_nd(sr_event, dict_speed, dsize=.125, area=45.6 / (100 ** 2), dt=60):
    ND = 0

    for speed in sr_event.index:
        if pd.notnull(sr_event.loc[speed]):
            dspeed = dict_speed[speed]
            ND += int(sr_event.loc[speed]) / (speed * area * dt * dsize)
    return ND


def calc_nt(sr_event, dict_speed, dsize=.125, area=45.6 / (100 ** 2), dt=60):
    NT = 0
    for speed in sr_event.index:
        if pd.notnull(sr_event.loc[speed]):
            dspeed = dict_speed[speed]
            NT += (int(sr_event.loc[speed]) / (speed * area * dt))
    return NT


def calc_W(sr_event, dict_speed, dsize=.125, area=45.6 / (100 ** 2), dt=60):
    W = 0
    for speed in sr_event.index:

        if pd.notnull(sr_event.loc[speed]):
            dspeed = dict_speed[speed]
            W += (int(sr_event.loc[speed]) / (speed * area * dt)) * dsize ** 3
    return W


def calc_R(sr_event, dict_speed, dsize=.125, area=45.6 / (100 ** 2), dt=60):
    R = 0
    for speed in sr_event.index:
        if pd.notnull(sr_event.loc[speed]):
            dspeed = dict_speed[speed]
            R += (int(sr_event.loc[speed]) / (area * dt)) * dsize * 3.
    return R


def calc_Z(sr_event, dict_speed, dsize=.125, area=45.6 / (100 ** 2), dt=60):
    Z = 0
    for speed in sr_event.index:

        if pd.notnull(sr_event.loc[speed]):
            dspeed = dict_speed[speed]
            Z += (int(sr_event.loc[speed]) / (speed * area * dt)) * dsize ** 6

    return Z

def calc_MParams(sr_nd,exp):
    m = pd.Series(index=sorted(list_size))
    m = sr_nd * delta_diam * diameters ** exp
    M = m.sum()
    return M
def preprocess_csv(chunk):
    dsd_data_final = chunk.copy()
    dsd_data_final['Date_str'] = chunk[0].astype(str)
    dsd_data_final['Date'] = pd.to_datetime(dsd_data_final['Date_str'], format='%Y-%m-%d %H:%M:%S')
    dsd_data_final = dsd_data_final.drop_duplicates('Date', keep='first')
    dsd_data_final.set_index('Date', drop=True, inplace=True)
    dsd_data_final.drop(['Date_str'], axis=1, inplace=True)
    dsd_data_final.drop(range(9), axis=1, inplace=True)
    dsd_data_final.sort_index(inplace=True)
    dsd_data_final=dsd_data_final.dropna()
    dsd_data_final=dsd_data_final.drop(dsd_data_final.index[-1])
    return dsd_data_final

def getIndexOfCondition(dataframe,num_gotas):
    sr_sum_drisd = dataframe.sum(axis=1)
    idx_events = sr_sum_drisd[sr_sum_drisd.iloc[:] > num_gotas].index
    return idx_events