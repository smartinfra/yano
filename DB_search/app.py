from flask import Flask, Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app

import dbModule

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('test.html')


# SELECT 함수 예제
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':

       db_class = dbModule.Database()
       name=request.form['nm']
       birth = request.form['birth']
       print(name)

       sql = "SELECT * FROM service where 성명 = '"+str(name)+"' and " +str(birth)
       sql2 = "SELECT * FROM attendance where 성명 = '"+str(name)+"' and " +str(birth)
       sql3 = "SELECT * FROM award where 성명 = '" + str(name) + "' and " + str(birth)


       #df=db_class.executePD(sql, [name,birth])
       #df2 = db_class.executePD(sql2, [name, birth])
       df = db_class.pd(sql)
       df2 = db_class.pd(sql2)
       df3 = db_class.pd(sql3)

       return render_template('simple.html',  tables=[df.to_html(classes='data'),
                                                      df2.to_html(classes='data'),
                                                      df3.to_html(classes='data')],
                                                      titles=['A','봉사실적','출석실적','수상'])


