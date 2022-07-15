def test(**kwargs):
    for key, arg in kwargs.items():
        print(key, arg)
        
if __name__ == "__main__":
    test(**{"a": 1, "b": 2})