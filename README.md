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

[Docker](https://www.docker.com/) で環境を作成します．事前に[公式ドキュメント](https://docs.docker.com/)を参照しローカル環境にDockerを導入してください．以下はDockerがインストールされており，DockerHubのアカウントを持っていることを想定しています．

## Usage

### コードのクローン

以下のコマンドをターミナルで実行して下さい．
```shell
git clone git@github.com:Okayama-Healthcare-BCP-Consortium/HPTSS.git
```

### データの準備

dataディレクトリにahp.xlsxという名前で基本入力データを準備してください．

### システムの起動

以下のコマンドをターミナルで実行して下さい．
```shell
docker pull kunifuohbc/hptss
docker run -p 3000:3000 -v $(pwd):/work --rm kunifuohbc/hptss
```

### システムの利用

ブラウザに http://localhost:3000/ を入力して下さい．

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)
