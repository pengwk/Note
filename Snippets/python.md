# Python代码片段


## 持久化 pickle

```python
def dump_data(data, file_name):
    import pickle
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)


def load_data(file_name):
    import pickle
    with open(file_name, 'rb') as f:
        data = pickle.load(f)
    return data
```
