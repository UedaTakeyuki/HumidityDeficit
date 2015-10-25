# coding:utf-8 Copy Right Atelier Grenouille © 2015 -
#

# 
# 飽差関連式
# 

# http://d.hatena.ne.jp/Rion778/20121203/1354546179
def HumidityDeficit(t,rh): # t: 温度, rh: 相対湿度
    ret = AbsoluteHumidity(t, 100) - AbsoluteHumidity(t, rh)
    print "HD = " + str(ret)
    return ret; 

# http://d.hatena.ne.jp/Rion778/20121203/1354461231
def AbsoluteHumidity(t, rh):
    ret = 2.166740 * 100 * rh * tetens(t)/(100 * (t + 273.15))
    print "AH = " + str(ret)
    return ret


#  飽和水蒸気圧
#  function GofGra(t){};
# http://d.hatena.ne.jp/Rion778/20121126/1353861179
def tetens(t):
    ret = 6.11 * 10 ** (7.5*t/(t + 237.3))
    print "tetens = " + str(ret)
    return ret

if __name__ == "__main__":
    HumidityDeficit(24.1, 60.1)

