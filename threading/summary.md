# threading

## プロセスとは

例えば，Excel を立ち上げると 1 個の Excel プロセスが作成される．  
他にも，何かしらのソフトを立ち上げた時も同様に，1 個のそのソフトのプロセスが作成される．

ただ，プロセスが 1 個だからと言って 1 つの処理を行っているわけではない．  
1 つのプロセスの中に，スレッドと呼ばれるものが複数動いていて，CPU がスレッド間で交替で実行している．  
CPU は早いのでこの交替で実行しているのも，人間の感覚からすると同時に実行しているように見える．

## スレッドとは

IDE を例に挙げると，コードを入れると同時にコード補完が出てくる．  
これは大まかに分けると，文字入力を受け付ける処理(スレッド)と，コード補完を表示させる処理(もう一つのスレッド)が動いているということ．

## プロセスとスレッドの関係

プロセスは OS によってメモリが割り当てられ，スレッドはそのプロセス内で複数立ち上げることができる．  
なので，同じプロセスから立ち上げられたスレッド間の通信は同じメモリ空間内を共有しているため，CPU の交替実行や値の受け渡しが比較的容易．  
だが，別のプロセスで動いているスレッド間だと難しくなる．

## スレッドのインスタンスを生成

`threading.Thread`でインスタンスを生成することができる

```py
import threading

def func(arg):
    pass

thread_instance = threading.Thread(
    target=func,
    args=("arg",),
    name="naming_the_thread"
)
```

## スレッドのインスタンスを実行

`start()` メソッドで，スレッドを実行することができる．

```py
thread_instance.start()
```

## スレッドの呼び出し元のスレッドをブロックする

`join(timeout=None)` メソッドで，呼び出し元のスレッドをブロックすることができる．

```py
thread_instance = threading.Thread(
    target=func,
    args=("arg",),
    name="naming_the_thread"
)
# スレッドを実行
thread_instance.start()

# 呼び出し元(このときはメインスレッド)を，
# thread_instanceが正常終了または例外によって終了するまで，
# あるいは timeout 引数で指定した時間までブロックする．
thread_instance.join()
```

## 自作スレッドクラス

`threading.Thread` を継承し，`start()` が呼び出す `run()` メソッドをオーバーライドすることで，作ることができる．

```py
import threading

class ThreadClass(threading.Thread):
    def __init__(self, arg):
        self.arg = arg

    def run(self):
        pass

thread_instance = ThreadClass("arg")
```

## 現在起動させているスレッド数を取得

`threading.active_count()` で，現在起動させている**全てのスレッド数**を取得することができる．

自分で作成したスレッドのインスタンスは勿論だが，呼び出し元であるメインスレッド自身も数え上げられる対象となる．

```py
import threading
import time

def run(n):
    print(f"Thread {n}")
    time.sleep(3)

for i in range(3):
    threading.Thread(target=run, args=(i,)).start()

print('Create three threads')
print(threading.active_count())
```

上記の出力結果は以下の通りで，メインスレッドも含めた４つのスレッドが起動状態であることを指している．

```txt
Thread 0
Thread 1
Thread 2
Create three threads
4
```

## デーモンスレッド

TODO
