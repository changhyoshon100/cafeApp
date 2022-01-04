class Menu():
    global lt,dt,result
    get_result_pick = []
    
    def __init__(self):
        self.menu = 0
    def display(self):
        print(
        """
        1.아메리카노 - 3000 // (원두 + 물)
        2.녹차라떼 - 4000   // (녹차가루 + 우유)
        3.녹차 - 3500       // (녹차가루 + 물)
        4.페스츄리 - 4500   // (플레인빵 + 딸기잼)
        5.크림빵 - 4000     // (플레인빵 + 크림)
        6.딸기에이드 - 5000 // (사이다+딸기시럽+물)
        """
        )
    
    def pick(self):
        global get_result_pick
        
        lt = ["아메리카노","녹차라떼","녹차","페스츄리","크림빵","딸기에이드"]
        dt = {
            "아메리카노":3000,
            "녹차라떼":4000,
            "녹차":3500,
            "페스츄리":4500,
            "크림빵":4000,
            "딸기에이드":5000
        }
        result = []
        price = 0
        while True:
            
            a = input("드시고싶은 메뉴에맞게 숫자를 눌러주세요")
            while True:
                if not a.isnumeric():
                    a = input("숫자를 눌러주세요")
                elif int(a)<1 or int(a)>6:
                    a = input("1부터 6까지 눌러주세요")
                else:
                    break 
            
            choice = int(a) - 1
            price += dt[lt[choice]]
            
            result.append(lt[choice])
            
            more = input(("선택한 메뉴는 {0},가격은 {1}, 총 결제금액은{2}입니다. 추가주문하시겠습니까? 예:y 아니오:n".format(lt[choice],dt[lt[choice]]
            ,price)))
            while more !="y" and more != "n":
                more = input("y나 n을 누르시오")
            if more =="n":
                if price >= 5000:
                    print("구매금액이 5000원 이상이므로 10% 할인된 금액인 {0}원을 결제해주세요".format(price*0.9))
                else:    
                    print("{0}원을 결제해주세요".format(price))
                Menu.get_result_pick.append(price)
                Menu.get_result_pick.append(result)
                return [
                    price,result
                ]




        