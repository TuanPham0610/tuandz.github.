import random
import time

print("Tài Xỉu ")  # <= 10 là xỉu : > 10 là tài
print("_ _ _ _ _ _ _ _ _ _ _ _")

input("Nhấn Enter để chơi ")

money = 50000000

while money > 10000:

    # Đặt cược

    print("Số tiền hiện có : " + str(money))
    selection = input("Tài or Xỉu : ")
    bet = int(input("Cược : "))
    bill = (bet * 2) + money
    ill = money - bet

    # Bắt đầu quay 3 cái xúc xắc
    print("__________________________")
    val = random.randint(1, 6)
    va = random.randint(1, 6)
    v = random.randint(1, 6)

    print("Chờ kết quả ")
    time.sleep(1)

    print("Xúc sắc 1 : " + str(val))
    time.sleep(1)

    print("Xúc sắc 2 : " + str(va))
    time.sleep(1)

    print("Xúc sắc 3 : " + str(v))
    time.sleep(1)

    print("Kết quả : " + str(val + va + v))
    time.sleep(1)

    total = val + va + v  # tính kết quả 3 xúc xắc

    # kết quả của 3 con xúc xắc và tính tiền
    if total <= 10:  # Nhỏ hơn 10 là xỉu nên khi selection = Xỉu thì sẽ cộng tiền và ngược lại
        print("______________")
        print("=> Xỉu")

        if selection == "Xỉu" or selection == "xỉu":
            money = bill
            print("Tiền hiện có : " + str(money) + (" VND"))
        elif selection == "Tài" or selection == "tài":
            print("-Đen rồi ! Hãy thử lại nhé !!-")
            print("_____________")
            money = ill
            print("Tiền hiện có : " + str(money) + " VND")

    if total > 10:  # Lớn hơn 10 là tài nên khi selection =Tài thì sẽ cộng tiền và ngược lại là trừ tiền
        print("______________")
        print("=> Tài")

        if selection == "Tài" or selection == "tài":
            money = bill
            print("Tiền hiện có : " + str(money) + " VND")

        elif selection == "Xỉu" or selection == "xỉu":
            print("-Đen rồi ! Hãy thử lại nhé !!- ")
            print("______________")
            money = ill
            print("Tiền hiện có : " + str(money) + " VND")

    elif money < 1:
        print(">>> Vui lòng ấn Enter để nạp thêm tiền và tiếp tục trò chơi")
        f = input("Nạp tiền ")
        print(list)
        g = int(input("Vui lòng chọn mệnh giá : "))

    # chơi tiếp hay dừng lại
    print("__________________________")

    out = input("Nhấn Enter để tiếp tục hoặc gõ n để dừng trò chơi")
    if out == 'n':
        print("Tạm biệt ")
        break
