#import path
from DyCommon.DyCommon import *
from Stock.BackTesting.DyStockBackTestingCommon import *
from EventEngine.DyEventEngine import *

from Stock.BackTesting.Engine.Strategy.DyStockBackTestingStrategyEngine import *


class DyStockBackTestingMainEngine(object):
    """ 股票回测主引擎 """

    def __init__(self):
        self._eventEngine = DyEventEngine(DyStockBackTestingEventHandType.nbr, False)
        self._info = DyInfo(self._eventEngine)

        self._strategyEngine = DyStockBackTestingStrategyEngine(self._eventEngine, self._info)

        self._eventEngine.start()

    @property
    def eventEngine(self):
        return self._eventEngine

    @property
    def info(self):
        return self._info

    def exit(self):
        pass

    def setThreadMode(self):
        self._strategyEngine.setThreadMode()

    def setProcessMode(self, mode):
        self._strategyEngine.setProcessMode(mode)


if __name__ == "__main__":
# try to run backTestingMainEngine    
        DyBackTestingMainEngine = DyStockBackTestingMainEngine()
        # set thredMode   
        DyBackTestingMainEngine.setThreadMode()
        # set ProcessMode
        # self._mainEngine.setProcessMode(text)

        # strategy class 
        from Stock.Trade.Strategy.Cta.DyST_AbnormalVolatility import DyST_AbnormalVolatility
        # 
        from Stock.Select.Ui.Basic.DyStockSelectStrategyWidget import DyStockSelectStrategyWidget
       
        DyStockSelectStrategyWidget = DyStockSelectStrategyWidget()
        DyStockSelectStrategyWidget._curStrategyCls = '异常波动'

        self._widgetStrategy, dockStrategy = self._createDock(DyStockBackTestingStrategyWidget, '策略', Qt.LeftDockWidgetArea, widgetParam)
        strategyCls, param = self._widgetStrategy.getStrategy()

        strategyCls =  DyST_AbnormalVolatility()
        event = DyEvent(DyEventType.stockStrategyBackTestingReq) # 策略回测请求，收到后会分成几个周期并行运行
        data = {}
        data['startDate'] = "2019-04-05"
        data['endDate'] = "2019-05-11"
        param = OrderedDict()
        event.data = DyStockBackTestingStrategyReqData(strategyCls, [data['startDate'], data['endDate']], data, param)

        DyBackTestingMainEngine.eventEngine.put(event)
        
        
        from  Stock.BackTesting.Ui.Basic.DyStockBackTestingStrategyWidget import DyStockBackTestingStrategyWidget