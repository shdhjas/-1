def send_message(to_user, access_token, city_name , weather, max_wd, min_wd, tips, yy):
    url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(access_token)
    week_list = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
    # 年月日
    today = datetime.date(datetime(year=localtime().tm_year, month=localtime().tm_mon, day=localtime().tm_mday))
    # 计算星期
    week = week_list[today.isoweekday() % 7]
data = {
        "touser": to_user,
        "template_id": template_id,  # 模板id
        "url": "http://weixin.qq.com/download",
        "topcolor": "#FF0000",
        "data": {
            "date": {
                "value": "{} {}".format(today, week),
                "color": get_color()
            },
            "time": {
                "value": (datetime.today() - datetime(2017,9,1)).days,
                "color": get_color()
            },
            "city": {
                "value": city_name,
                "color": get_color()
            },
            "weather": {
                "value": weather,
                "color": get_color()
            },
            "min_wd": {
                "value": min_wd,
                "color": get_color()
            },
            "max_wd": {
                "value": max_wd,
                "color": get_color()
            },
            "tips": {
                "value": tips,
                "color": get_color()
            },
            "yy": {
                "value": yy,
                "color": get_color()
            },
            "yiqing": {
                "value": cqyq(),
                "color": get_color()
            },
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = requests.post(url, headers=headers, json=data).json()
    if response["errcode"] == 40037:
        print("[INFO]推送消息失败，请检查模板id是否正确")
    elif response["errcode"] == 40036:
        print("[INFO]推送消息失败，请检查模板id是否为空")
    elif response["errcode"] == 40003:
        print("[INFO]推送消息失败，请检查微信号是否正确")
    elif response["errcode"] == 0:
        print("[INFO]推送消息成功")
    else:
        print(response)
