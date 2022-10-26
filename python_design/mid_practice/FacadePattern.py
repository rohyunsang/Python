class Hotelier():
    def __init__(self):
        print("호텔리어 입니다.")

    def bookHotel(self):
        print("호텔 예약 완료 했습니다.")

class Florist():
    def __init__(self):
        print(" 플로어리스트 입니다.")

    def setFlowerRequirements(self):
        print("카네이션, 장미, 백합 꽃 장식을 준비하겠습니다.")

class Caterer():
    def __init__(self):
        print(" 요식업체 입니다.")

    def setFood(self):
        print("한식 코드로 준비하겠습니다.")

class Musician():
    def __init__(self):
        print(" 밴드입니다.")

    def setMusicType(self):
        print("재즈와 클래식 음악을 준비하겠습니다.")


class WeddingPlanner():

    def __init__(self):
        print("웨딩 플래너 입니다.")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setFood()

        self.musician = Musician()
        self.musician.setMusicType()

class Client():
    def __init__(self):
        print("결혼 준비 시작 ")

    def setWeddingPlanner(self):
        print("웨딩 플래너 긔기기기기기기")
        wp = WeddingPlanner()
        wp.arrange()

you = Client()
you.setWeddingPlanner()