
def get_order_sn(userid):
    import time
    import random
    order_sn = '{timestr}{userid}{randomint}'.format(timestr=time.strftime("%Y%m%d%H%M%S"),
                                                     userid=userid,
                                                     randomint=random.randint(10, 99))
    return order_sn