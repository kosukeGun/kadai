for num in range(1, 101):
    string = ''

    # ここから記述

    if num%15==0:#値が5の倍数かつ3の倍数である場合（すなわち15の倍数である場合）
        string='FizzBuzz'#"FizzBuzz"を出力
    
    elif num%5==0:#値が15の倍数でない、かつ5の倍数である場合
        string='Buzz' #"Buzzを出力" 
    
    elif num%3==0: #値が5の倍数でない、かつ3の倍数である場合
        string='Fizz' #"Fizz"を出力

    else:#上の3つの条件全て満たさない場合
        string=num #値自体を出力

    # ここまで記述

    print(string)