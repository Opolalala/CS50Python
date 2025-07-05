while True:

    date = input("Date: ")

    if "/" in date:
        m,d,y = date.split("/")
        try:
            m,d,y = map(int, [m,d,y])
            if 1 <= m <= 12 and 1 <= d <= 31:
                print(f"{y}-{m:02d}-{d:02d}")
                break
        except ValueError:
            pass

    else:
        m,d,y = date.split(" ")
        try:
            d = int(d.replace(",",""))
            dict = {
                "January": "01",
                "February": "02",
                "March": "03",
                "April": "04",
                "May": "05",
                "June": "06",
                "July": "07",
                "August": "08",
                "September": "09",
                "October": "10",
                "November": "11",
                "December": "12"
            }
            if m in dict and d <= 31 and "," in date:
                print(f"{y}-{dict[m]}-{d:02d}")
                break
        except ValueError:
            pass