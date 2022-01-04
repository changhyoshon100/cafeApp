from menu import Menu
class Ingredient(Menu):
#
    global dt
    global dt_ingredient

    m = Menu()
    dt = m.pick()
    dt_ingredient = {
    "아메리카노" : 0,
    "녹차라떼" : 0,
    "녹차" : 0,
    "페스츄리" : 0,
    "크림빵" : 0,
    "딸기에이드" : 0
    }
    def __init__(self):
        pass    
    def check_order(dt):
        
        for i in range(len(dt[1])):
        
            if dt[1][i] == "아메리카노":
                dt_ingredient["아메리카노"] += 1
            elif dt[1][i] == "녹차라떼":
                dt_ingredient["녹차라떼"] += 1
            elif dt[1][i] == "녹차":
                dt_ingredient["녹차"] += 1
            elif dt[1][i] == "페스츄리":
                dt_ingredient["페스츄리"] += 1
            elif dt[1][i] == "크림빵":
                dt_ingredient["크림빵"] += 1
            elif dt[1][i] == "딸기에이드":
                dt_ingredient["딸기에이드"] += 1
            else: pass

        in_components = {
          "원두":550,
          "우유":600,
          "녹차가루":400,
          "물":100,
          "딸기시럽":370,
          "사이다":200,
          "플레인빵":500,
          "딸기잼":600,
          "크림":400
        }
        
            
        net_income = 0
        dt_change = dt_ingredient
        
        net_income = dt_change['아메리카노']*3000 - dt_change['아메리카노']*(in_components["원두"]+in_components["물"])+ dt_change['녹차라떼']*4000 - dt_change['녹차라떼']*(in_components["녹차가루"]+in_components["우유"])+ dt_change['녹차']*3500 - dt_change['녹차']*(in_components["녹차가루"]+in_components["물"])+ dt_change['페스츄리']*4500 - dt_change['페스츄리']*(in_components["플레인빵"]+in_components["딸기잼"])+ dt_change['크림빵']*4000 - dt_change['크림빵']*(in_components["플레인빵"]+in_components["크림"])+ dt_change['딸기에이드']*5000 - dt_change['딸기에이드']*(in_components["사이다"]+in_components["딸기시럽"]+in_components["물"])
        
        return ("구매내역:{0} , 순이익:{1}".format(dt_ingredient,net_income))
    print(check_order(dt))

    def ingredient_price(self):
        """
        1.원두 - 50
		2.우유 - 200
		3.녹차가루 - 100
		4.물 - 30
		5.딸기시럽 -70
		6.사이다 - 100
		7.플레인빵 - 300
		8.딸기잼 - 200
		9.크림 - 400
        """

