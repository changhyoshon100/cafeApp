from menu import Menu

class Customer(Menu):
    def __init__(self, my_money, pre_point):
        print("어플 접속")
        self.my_money = my_money
        self.pre_point = pre_point

    def choose():
        Menu.get_result_pick

    def point(self):
        if self.in_case_short_money() !=0:
            sales_price = Menu.get_result_pick[0]*0.05 ### 포인트 계산을 위해Menu.pick(self)[0]*0.05의 결과값만을 받아서 대입하고싶으나
            self.pre_point = self.pre_point + sales_price   ### 변수대입을 위해 pick메소드를 호출시 pick함수전체가 돌아감
                                              ### 그래서 값만 받기위해 menu에 글로벌 get_result_pick 리스트변수 선언후 [price, result]를 받으려고했으나
                                              ### 글로별변수 인식이안되서 삽질
            return print("결재 포인트 {1}원 적립되셔서 총 포인트 {0}원이 있습니다".format(self.pre_point,sales_price))

    def in_case_short_money(self):
        p = Menu.get_result_pick[0] ##Menu.get_result_pick[0] 대신 Menu.pick(self)[0]를 대입했었음
        if self.my_money < p:
            return False

    def pay(self):
        if self.in_case_short_money() !=0:
            self.my_money -= Menu.get_result_pick[0]
        else:
            return print("결제금액이 잔액을 초과하였습니다.")
        return print("결제완료후 남은잔액:{0} 입니다".format(self.my_money))






    

    

        
