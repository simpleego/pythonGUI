if sales > 1000 :
    discount = sales*0.1
    print(discount, "할인되었음!")
else :
    if sales > 500 :
        discount = sales*0.05
        print(discount, "할인되었음!")
    else :
        print("할인은 없습니다!")
