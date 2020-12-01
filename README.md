# 医療ビジネスインパクトシステム（医療優先業務選択システム; Healthcare Priority Task Selection System）

## Target

医療現場状況を加味した優先業務選択を実現すること．

## Project Organization

    .
    ├── README.md
    ├── requirements.txt
    ├── main.py
    ├── data
    ├── modules
    │   ├── ahp.py
    │   └── mp.py
    └── template
        ├── html
        └── css

## Requirement

* Python 3.x

## Installation

### Pythonパッケージ

```bash
pip install -r requirements.txt
```

## Usage

以下のコマンドをターミナルで実行して下さい．
```shell
git clone 
```

### データの準備

述語項構造シソーラスのデータ（dup_checked_pth.xlsx）を用意し，data/raw/においてください．

### モデルの構築

以下のコマンドをターミナルで実行して下さい．
```shell
sh const_model.sh
```

### システムの起動

以下のコマンドをターミナルで実行して下さい．
```shell
python main.py
```

### システムの利用

ブラウザに http://localhost:3000/ を入力して下さい．

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)
