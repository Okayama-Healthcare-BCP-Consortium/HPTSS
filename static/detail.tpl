<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Cache-Control" content="no-cache">
    <link rel="stylesheet" href="css/result.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>
      述語項構造シソーラス拡張補助システム
    </title>
  </head>

  <body>
    <canvas id="myBarChart"></canvas>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.bundle.js"></script>
    <div class="container">
      <script>
        var ctx = document.getElementById("myBarChart");
        var myBarChart = new Chart(ctx, {
          type: 'bar',
          //データの設定
          data: {
            //データ項目のラベル
            labels: {{ labels }},
            //データセット
            datasets: [{
              //凡例
              label: "スコア",
              //背景色
              backgroundColor: "rgba(75,192,192,0.4)",
              //枠線の色
              borderColor: "rgba(75,192,192,1)",
              //グラフのデータ
              data: {{ scores }}
            }]
          },
          options: {
            title: {
              display: true,
              text: '{{ cate }}'
            },
            scales: {
              yAxes: [{
                ticks: {
                  beginAtZero: true
                }
              }]
            },
          }
        });
      </script>
      <br>
      <button type="button" class="btn btn-primary btn-sm btn-block" onclick="history.back()">戻る</button>
      <button type="button" class="btn btn-secondary btn-sm btn-block" onclick="location.href='/'">入力フォームへ</button>
      <br>
    </div>
  </body>
</html>