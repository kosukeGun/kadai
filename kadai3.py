def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    left=0 #対照配列のインデックスの最小値
    right=len(array)-1 #対照配列のインデックスの最大値（0から始まる為、要素数から1引いている）
    
    while left < right: #先頭・末端それぞれの探索がぶつかるまでループ
        tmp=None #二つの値を交換する際、値を一時補完する空の変数

        if array[left]<pivot or array[right]>=pivot: #先頭・末端からの探索のいずれかが条件を満たさない場合 
            if array[left]<pivot: #先頭からの探索が基準値を下回る場合
                left+=1 #探索対象を右側の要素に変更
                
            if array[right]>=pivot: #末端からの探索が基準値以上になる場合
                right-=1 #探索対象を左側の要素に変更
        
        else: #いずれの探索も条件を満たす場合（先頭からの探索は基準値以上、末端からの探索は基準値未満の両条件を満たす場合）
            tmp=array[left]
            array[left]=array[right]
            array[right]=tmp
            #上の3行で二つの要素を交換
    
    new_array1=[] #基準値未満の要素を納めるリスト
    new_array2=[] #基準値以上の要素を納めるリスト
    sorted_array=[] #ソートした要素を納めるリスト（戻り値）

    if min(array)==pivot: #基準値が要素の最小値の時（基準値未満の要素が一つも無い場合）
        for array_element in array: #対照配列の全ての要素を分類するまでループ
            if array_element == pivot: #対象の要素が基準値であった時
                new_array1.append(array_element)

            else:
                new_array2.append(array_element)

    else:
        for array_element in array:
            if array_element < pivot: #対象の要素が基準値未満
                new_array1.append(array_element)

            else: #対象の要素が基準値以上
                new_array2.append(array_element)
    
    for new_array1_element in sort(new_array1): #基準値未満（又は以下）の配列をソートした要素を先にsorted_arrayに格納
        sorted_array.append(new_array1_element)
    
    for new_array2_element in sort(new_array2): #基準値以上の配列について同様にsorted_arrayに格納
        sorted_array.append(new_array2_element)

    return sorted_array

     # ここまで記述

if __name__ == '__main__':
    main()