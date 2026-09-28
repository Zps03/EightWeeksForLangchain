def run():
    input_list = [
        {"input": "虽然今天加班到很晚，但项目顺利通过了，心里挺高兴"},
        {"input":"满心期待地打开包裹，结果东西是坏的，客服还一直推脱"},
        {"input":"还可以吧，没什么特别感觉，说不上好也说不上差"},
        {"input":"凑合吧"},
        {"input":"你可真厉害啊"},

    ]

    for input_dict in input_list:
        print(input_dict.get("input"))

if __name__ == "__main__":
    run()