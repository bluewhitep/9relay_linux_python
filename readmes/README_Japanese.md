# インストール
**リポジトリをクローンしてインストール**
ターミナルを開いて、以下のコマンドを実行します：
```bash
git clone https://github.com/bluewhitep/nine_relay_linux_python
cd ./nine_relay_linux_python
pip install .
```
これにより、リポジトリがクローンされ、必要なPythonパッケージがインストールされます。

**pipを使って直接インストール**
または、pipを使用して直接インストールすることもできます：
```bash
pip install git+https://github.com/bluewhitep/nine_relay_linux_python.git
```

# 使用方法
インストール後、Pythonスクリプトを使用してリレーを制御できます。リレーの使用方法についての基本ガイドは以下の通りです：

インポートと初期化：

```python
from nine_relay_linux_python import relay

relay_console = relay()
```
制御コマンド：

- 全リレーをオフにする： `relay_console.all_off()`
- 全リレーをオンにする： `relay_console.all_on()`
単一のリレーを制御する：
  - オンにする: `relay_console.on(relay_num=0)` はRY1用
  - オフにする: `relay_console.off(relay_num=0)` はRY1用
複数のリレーを制御する：
  - オンにする: `relay_console.on(relay_num=[0,2,4]) `はRY1、RY3、RY5用
  - オフにする: `relay_console.off(relay_num=[0,2,4])` はRY1、RY3、RY5用
- リレーの状態を取得する： `print(relay_console.get_status())` ここで 0 はオフ、1 はオンです

# ドキュメント
relay関数とメソッドには、以下のドキュメントがあります：

relay関数：
```python
relay(idVendor:str="22ea", idProduct:str="005f", init="off")
```
これは、デフォルトまたは指定されたUSBベンダーIDと製品IDでリレーを初期化します。initパラメーターはリレーの初期状態を決定します（全てオンまたは全てオフ）。

`.on() `/ `.off()`メソッド：これらのメソッドは、指定されたリレーを制御します。
- リレー番号（0〜8）を表す整数または整数のリストを受け入れます。
- `relay_num`が0〜8の範囲内でない場合はValueErrorを発生させます。

#メモ
ADUBRU9のデフォルト情報：

ベンダーID: 0x22ea
製品ID: 0x005f