class Kiosk:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, x):
        y = self.price * x
        return y

Coffee = Kiosk("커피", 3000)
GreenTea = Kiosk("녹차", 2500)
IceTea = Kiosk("아이스티", 3000)

def main():
    a = input("음료를 선택하세요 (커피, 녹차, 아이스티): ")

    if a not in ["커피", "녹차", "아이스티"]:
        print("잘못된 음료 선택입니다.")
        return

    x = int(input("수량을 입력하세요: "))

    if a == "커피":
        y = Coffee.calculate(x)
    elif a == "녹차":
        y = GreenTea.calculate(x)
    elif a == "아이스티":
        y = IceTea.calculate(x)

    print(f"{a} {x}잔의 총 가격은 {y}원 입니다.")

main()
