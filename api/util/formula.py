# 常用计算公式
import numpy as np
import pandas as pd

NO_RISK_RATIO = 0.015


class Formula(object):
    """
    计算DataFrame对象，要求index必须为date类型
                     nav_adj      close
    date
    2008-06-19  1.000000  2773.0760
    2008-06-19  1.000000  2773.0760
    2008-06-19  1.000000  2773.0760
    """

    @staticmethod
    def acc_return_yield(data):
        """累计收益"""
        y = data.iloc[-1] / data.iloc[0] - 1
        y = round(y, 4)
        return y

    @staticmethod
    def annualized_return_yield(data):
        """年化累计收益"""
        y = Formula.acc_return_yield(data)
        count = len(data)
        y = np.power(y+1, 252/count) - 1
        y = round(y, 4)
        return y

    @staticmethod
    def daily_change(data):
        """日收益统计"""
        data = data.pct_change().dropna()
        y = data.agg(['mean', 'max', 'min', win_ratio])
        y = round(y, 4)
        return y

    @staticmethod
    def trading_day_count(data):
        """交易日统计"""
        data = data.pct_change().dropna()
        count = data.agg([win, lose, draw])
        return count

    @staticmethod
    def annualized_volatility(data):
        """年化波动率及下行波动率"""
        data = data.pct_change().dropna()
        std = data.agg([vol, downside_vol])
        std = round(std, 4)
        return std

    @staticmethod
    def max_drawback(data):
        """最大回撤及发生日期"""
        ret = data.agg(max_drawback)
        ret = pd.DataFrame(ret, columns=['ret'])
        ret['start'] = ret['ret'].apply(lambda x: x[0].strftime("%Y-%m-%d"))
        ret['end'] = ret['ret'].apply(lambda x: x[1].strftime("%Y-%m-%d"))
        ret['drawback'] = ret['ret'].apply(lambda x: x[2])
        ret = ret.drop('ret', axis=1)
        return ret.T

    @staticmethod
    def sharpe_ratio(data):
        """夏普比"""
        annual_return = Formula.annualized_return_yield(data)
        volatility = Formula.annualized_volatility(data).loc['vol', :]
        sharpe = (annual_return - NO_RISK_RATIO) / volatility
        sharpe = round(sharpe, 2)
        return sharpe

    @staticmethod
    def calmar_ratio(data):
        """卡玛比"""
        annualized_return = Formula.annualized_return_yield(data)
        drawback = Formula.max_drawback(data).loc['drawback', :]
        calmar = - annualized_return / drawback
        calmar = calmar.astype('float')
        calmar = np.round(calmar, 2)
        return calmar

    @staticmethod
    def sortino_ratio(data):
        """索提诺值"""
        annual_return = Formula.annualized_return_yield(data)
        pct = data.pct_change().dropna()
        dr = pct.agg(downside_risk)
        sortino = (annual_return - NO_RISK_RATIO) / dr
        sortino = round(sortino, 2)
        return sortino


def win_ratio(pct):
    """胜率"""
    positive = pct[pct > 0]
    ratio = len(positive) / len(pct)
    ratio = round(ratio, 4)
    return ratio


def win(pct):
    positive = pct[pct > 0]
    return len(positive)


def lose(pct):
    negative = pct[pct < 0]
    return len(negative)


def draw(pct):
    zero = pct[pct == 0]
    return len(zero)


def vol(pct):
    std = pct.std()
    annual_std = np.sqrt(250) * std
    return annual_std


def downside_vol(pct):
    """下行波动率"""
    pct = pct[pct < 0]
    std = np.sqrt(sum(pct**2)/len(pct))
    annual_std = np.sqrt(250) * std
    return annual_std


def max_drawback(data):
    """最大回撤"""
    drawback = []
    max_ = 0
    max_date = data.index[0]
    for date, value in data.iteritems():
        if value > max_:
            max_ = value
            max_date = date
        else:
            drawback.append((max_date, date, value/max_ - 1))
    drawback = sorted(drawback, key=lambda x: x[2])[0]
    start = drawback[0]
    end = drawback[1]
    back = round(drawback[2], 4)
    return start, end, back


def downside_risk(pct):
    """用于计算sortino的下行标准差计算方式"""
    pct = pct - NO_RISK_RATIO/365
    pct = pct[pct < 0]
    std = np.sqrt(sum(pct**2)/len(pct)*250)
    return std


def var(hist_change, days=7, alpha=0.05):
    """
    计算var
    """
    hist_change = hist_change.values[-days:]
    p = np.percentile(hist_change, alpha*100, interpolation='midpoint')
    return p


def cvar(hist_change, days=7, alpha=0.05):
    """计算CVAR"""
    hist_change = hist_change.values[-days:]
    hist_change = sorted(hist_change)
    p = np.percentile(hist_change, alpha * 100, interpolation='midpoint')
    data = [x for x in hist_change if x < p]
    return sum(data) / len(data)
