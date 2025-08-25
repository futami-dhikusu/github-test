# test_main.py
# main.py の関数をテストするファイル

from main import add, multiply

def test_add():
    """add関数のテスト"""
    assert add(2, 3) == 5  # 正しい結果の場合、テストは成功
    assert add(-1, 1) == 0

def test_multiply():
    """multiply関数のテスト"""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
