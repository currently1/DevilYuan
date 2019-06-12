# 增加天软接口 获取期权分笔数据
import sys
sys.path.append('D:\\Tinysoft\\Analyse.NET')        #路径
import TSLPy3 as ts

# 登录
def tsl_login ():
	ts.ConnectServer ("tsl.tinysoft.com.cn", 443)
	dl = ts.LoginServer ("htccqh", "htfc2018")  # Tuple(ErrNo,ErrMsg) 登陆用户
	if dl [0] == 0:
		print ("登陆成功")
		print ("服务器设置:", ts.GetService ())
		ts.SetComputeBitsOption (64)  # 设置计算单位
		print ("计算位数设置:", ts.GetComputeBitsOption ())
	else:
		print (dl [1])
		
		
def Batch_Encoding(items):
    ret = []
    for i in range(len(items)):
        item = items[i]
        if type(item).__name__=='dict':
            K = list(item.keys())
            V = list(item.values())
            K1 = []
            V1 = []
            for j in range(len(K)):
                try:
                    K1.append(K[j].decode('gbk'))
                except:
                    K1.append(K[j])
                try:
                    V1.append(V[j].decode('gbk'))
                except:
                    V1.append(V[j])
            ret.append(dict(zip(K1,V1)))
        else:
            try:
                ret.append(item.decode('gbk'))
            except:
                ret.append(item)
    return ret

def tsbytestostr(data):
    if isinstance(data, (tuple, list)):
        lendata = len(data)
        ret = []
        for i in range(lendata):
            ret.append(tsbytestostr(data[i]))
    elif isinstance(data, dict):
        ret = {}
        for i in data:
            ret[tsbytestostr(i)] = tsbytestostr(data[i])
    elif isinstance(data, bytes):
        ret = data.decode('gbk')
    else:
        ret = data
    return ret

def get_data(date,stocks):
	'''
	
	:param stocks: 可以是个list
	:param date: 字符串形式：2019-01-01
	:return:
	'''
	d = ts.RemoteCallFunc ("GetFutureTick", [date, stocks], {})
	print (tsbytestostr (d [1]))
	
	return tsbytestostr (d [1])

def get_code():
	r = ts.RemoteCallFunc ('Option_Contract', {}, {})
	print (r [1])
	
	return tsbytestostr (r [1])
	
if __name__ == "__main__":
    stocks=['SH600000','SZ000002']
    date='2019-6-5'
#登录，第一步必须
    tsl_login()
# get_data(stocks = stocks,date = date)
#期权合约代码
    test = get_code()
    print(test)
    test_code = test[8]
#tick数据
    get_data(stocks = test_code,date = date)