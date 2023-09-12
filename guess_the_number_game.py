import random
# gamestart()はguessGameSysten()を呼ぶためにあります。
# もし、他のゲームを入れる場合でもここで選択が可能です。
def gamestart():
    print('このゲームは、２つの整数の範囲内にある値を当てるゲームです。')
    guessGameSystem()
# max and min を input()　して整数の配列を返す関数
# 整数以外の入力をされても問題ないようにしてある
def getMinMaxValue():
    minVal = input('最小の整数値を入力して下さい：')
    maxVal = input('最大の整数値を入力して下さい：')
    if not minVal.isdecimal() or not maxVal.isdecimal():
        print('入力した値が不正です。')
        return getMinMaxValue()
    if minVal > maxVal:
        print('入力した値が大きいです')
        return getMinMaxValue()
    return [int(minVal),int(maxVal)]
# やり直す回数を入力する関数
# 整数以外の入力をされても問題ないようにしてある
def difficultLevel():
    levelInt = input('やり直す回数を入力して下さい：')
    if not levelInt.isdecimal():
        print('入力した値が不正です。')
        return difficultLevel()
    return int(levelInt)
# int answer, int levelInt　を引数にして gameOver()に int answer, booleanを引数として返すようにしてある。
# 整数以外の入力をされても問題ないようにしてある
def isAnswer(answer, levelInt):
    if levelInt == 0:
        return gameOver(answer,False)
    call = input('値を入力して下さい：')
    if not call.isdecimal():
        print('値が不正です。')
        return isAnswer(answer,levelInt)
    if int(answer) == int(call):
        return gameOver(answer,True)
    elif int(answer) > int(call):
        print('答えより値が小さいです。')
    else:
        print('答えより値が大きいです。')
    return isAnswer(answer,int(levelInt) - 1)
# ゲームの結果を返す関数
def gameOver(answer,isSame):
    print('答えは' + str(answer) + 'でした。')
    if isSame:
        print('Your Congratulations!!')
    else:
        print('Game Over')
# minMaxArr = [minValue,maxValue]
# answer = int値の乱数を受け取る
# levelInt = 試行回数を受け取る
def guessGameSystem():
    minMaxArr = getMinMaxValue()
    answer = random.randint(int(minMaxArr[0]),int(minMaxArr[1]))
    levelInt = difficultLevel()
    return isAnswer(answer,levelInt)
gamestart()