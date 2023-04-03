# ticket() 打印对应的购物小票
def ticket(cost, is_vip=False, vip_id=None, counter_id=001):
  line = '--------------------'
  print(line)
  if is_vip:
    print(f'会员编号：{vip_id}')
    cost = round(cost * 0.9, 2)
  print(f'本次消费：{cost}')
  print(f'收银柜台：{counter_id}')
  print('欢迎您的下次光临')
  print(line)

# 第一位顾客的购物小票
ticket(48)
# 第二位顾客的购物小票
ticket(57, True, 233)
# 第三位顾客的购物小票
ticket(107,counter_id=002)
# 第四位顾客的购物小票
ticket(32, True, 423, 002)