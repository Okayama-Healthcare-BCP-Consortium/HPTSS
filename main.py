from flask import Flask, request, redirect, url_for, render_template
import os
from scipy.stats import entropy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from jinja2 import Environment, FileSystemLoader
from modules import ahp
from modules import mp


app = Flask(__name__, template_folder='templates/html')

@app.route('/', methods=['GET', 'POST'])
def calc_ahp():

    task_cands = ahp.calc('data/ahp.xlsx')
    
    if request.method == 'POST':

        top = int(request.form['text'])
        task_cands = task_cands[:top]

        return redirect(url_for('input_mp', task_cands=task_cands, problems=request.form.getlist('problems')))

    return render_template('index.html', task_num=len(task_cands))


@app.route('/confirm', methods=['GET', 'POST'])
def input_mp():

    task_cands = request.args.getlist('task_cands')
    problems = request.args.getlist('problems')

    # AHPの結果に基づきエクセルテンプレートを作成
    with pd.ExcelWriter('data/mp.xlsx') as writer:

        for problem in problems:

            data = [[task, 1, 1, 1, 1] for task in task_cands]
            data.append(['上限', 1, 3, 4, 5])

            df_temp = pd.DataFrame(
                data,
                columns=['業務名', '重要度', 'サンプル１', 'サンプル２', 'サンプル３']
            )

            df_temp.to_excel(writer, sheet_name=f'{problem}', index=False)

    if request.method == 'POST':

        if request.form['confirm'] == 'ok':

            return redirect(url_for('render_result'))

    return render_template('confirm.html', task_cands=task_cands, problems=problems)


@app.route('/result')
def render_result():

    sheet2df = pd.read_excel('data/mp.xlsx', sheet_name=None)
    problem2result = dict()
    
    for sheet, df in sheet2df.items():

        problem2result[sheet] = mp.maximize(df, isBinary=False)

    return render_template('result.html', problem2result=problem2result)


# @app.route('/result/detail')
# def render_detail():

#     html = request.args.get('html')

#     return render_template(html)


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=3000)
