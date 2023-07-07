# ドキュメント更新方法

## 事前準備

---

`sphinx`, `sphinx-rtd-theme` が必要 <br>
ない場合は以下を実行 : <br>

```bash
pip install sphinx
pip install sphinx-rtd-theme 
```

## 実行手順

---

```bash
cd PythonConsoleTypingApp/docs
sphinx-build -b html . docs
```