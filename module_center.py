'''import theater_module
theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
theater_module.price_morning(4)
theater_module.price_soldier(5)'''

'''import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)'''

'''from theater_module import *
price(3)
price_morning(4)
price_soldier(5)'''

'''from theater_module import price, price_morning # 필요한 함수만 가져다쓰기
price(5)
price_morning(4)'''

from theater_module import price_soldier as price
price(5) # 군인할인가격