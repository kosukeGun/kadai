def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    left=0 #インデックスの最小値（初期値）
    right=len(sorted_array)-1 #インデックスの最大値（初期値）

    while left<=right: 
        mid=int((left+right)/2) #探索対象の配列におけるインデックスの中間値

        if sorted_array[mid]==target_number: #探索値と中間の要素が一致する場合
            return mid #インデックスの中間値を返す

        elif sorted_array[mid]<target_number: #探索値が中間の要素の右側にある場合
            left=mid+1 #探索対象の配列を右半分に縮める

        else : #探索値が中間の要素の左側にある場合
            right=mid-1 #探索対象の配列を左半分に縮める

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()