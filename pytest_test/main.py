# main.py
# 簡単な計算関数を定義するサンプル

def add(a, b):
    """2つの数値を足す"""
    return a + b

def multiply(a, b):
    """2つの数値を掛ける"""
    return a * b

if __name__ == "__main__":
    # 動作確認用の簡単な出力
    print("3 + 5 =", add(3, 5))
    print("3 * 5 =", multiply(3, 5))