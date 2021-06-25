from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px
import csv, re, operator
# from textblob import TextBlob

app = Flask(__name__)

person = {
    'name': '二师弟',
    'job': '前端开发人员',
    'about': '性格外向开朗，对新鲜事物抱有好奇心，并热衷于学习有趣的新鲜事物，有较强的组织能力和沟通能力。',
}

contact = {
    'call': '19172919646',
    'address': '点我点我',
    'email': 'ershidi@qq.com',
    'website': 'ershdi.com',
}

@app.route('/')
def cv(person=person):
    return render_template('index.html', person = person, contact = contact)

# 跳转到选择界面
@app.route('/select')
def select():
	return render_template('chartselect.html')

# 人口普查的折线图
@app.route('/callback', methods=['POST', 'GET'])
def cb():
	return gm(request.args.get('data'))

@app.route('/chart')
def index():
	return render_template('charts/chartsajax.html',  graphJSON=gm())

def gm(type='all'):
	df = pd.read_csv('static/data/population(1990-2014).csv')
	if type in ['all', 'man', 'woman', 'city', 'country']:
		# 对图中纵轴对应数据的单位进行判断
		fig = px.line(df, x="year", y=type+'(W)')
	else:
		fig = px.line(df, x='year', y=type+'(%)')
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

# 不同种类花的散点图
@app.route('/callback1', methods=['POST', 'GET'])
def cb1():
	return gm1(request.args.get('data'))

@app.route('/chart1')
def index1():
	return render_template('charts/chartsajax1.html', graphJSON=gm1())

def gm1(type='sepal'):
	df = pd.read_csv('static/data/iris.csv')
	if type == 'sepal':
		fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="rug", marginal_x="histogram")
	elif type == 'petal':
		fig = px.scatter(df, x="petal_width", y="petal_length", color="species", marginal_y="rug", marginal_x="histogram")
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

# 风力的散点极坐标图
@app.route('/chart2')
def index2():
	return render_template('charts/chartsajax2.html', graphJSON=gm2())

def gm2(strength='strength'):
	df = pd.read_csv('static/data/wind.csv')
	fig = px.scatter_polar(df, r="frequency", theta="direction", color=strength, symbol=strength, color_discrete_sequence=px.colors.sequential.Plasma_r)
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

# 三种不同种类的花的平行坐标图
@app.route('/chart3')
def index3():
	return render_template('charts/chartsajax3.html', graphJSON=gm3())

def gm3():
	df = pd.read_csv('static/data/iris.csv')
	fig = px.parallel_coordinates(df, color='species_id', color_continuous_scale=['red', 'green', 'blue'])
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

# 餐厅数据的并行类别图
@app.route('/chart4')
def index4():
	return render_template('charts/chartsajax4.html', graphJSON=gm4())

def gm4():
	df = pd.read_csv('static/data/tips.csv')
	fig = px.parallel_categories(df, color="size", color_continuous_scale=px.colors.sequential.Inferno)
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

# 餐厅数据的矩阵散点图
@app.route('/chart5')
def index5():
	return render_template('charts/chartsajax5.html', graphJSON=gm5())

def gm5():
	df = pd.read_csv('static/data/tips.csv')
	fig = px.scatter_matrix(df, dimensions=["total_bill", "tip"], color="sex")
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

# 餐厅数据的密度等值线图
@app.route('/callback6', methods=['POST', 'GET'])
def cb6():
	return gm6(request.args.get('data'))

@app.route('/chart6')
def index6():
	return render_template('charts/chartsajax6.html', graphJSON=gm6())

def gm6(type = 'time_size'):
	df = pd.read_csv('static/data/tips.csv')
	if type == 'time_size':
		fig = px.density_contour(df, x="time", y="size")
	if type == 'time_totalBill':
		fig = px.density_contour(df, x="time", y="total_bill")
	if type == 'day_size':
		fig = px.density_contour(df, x="day", y="size")
	if type == 'day_totalBill':
		fig = px.density_contour(df, x="day", y="total_bill")
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

# 堆积类型条形图
@app.route('/chart7')
def index7():
	return render_template('charts/chartsajax7.html', graphJSON=gm7())

def gm7():
	df = pd.read_csv('static/data/tips.csv')
	fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

# 三元线条图
@app.route('/chart8')
def index8():
	return render_template('charts/chartsajax8.html', graphJSON=gm8())

def gm8():
	df = pd.read_csv('static/data/election.csv')
	fig = px.line_ternary(df, a="Joly", b="Coderre", c="Bergeron", color="winner", line_dash="winner")
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

# 三维散点图
@app.route('/chart9')
def index9():
	return render_template('charts/chartsajax9.html', graphJSON=gm9())

def gm9():
	df = pd.read_csv('static/data/election.csv')
	fig = px.scatter_3d(df, x="Joly", y="Coderre", z="Bergeron", color="winner",
					size="total", hover_name="district", symbol="result",
	                color_discrete_map={"Joly": "blue", "Bergeron": "green", "Coderre": "red"})
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

# 动画地图
@app.route('/callback10', methods=['POST', 'GET'])
def cb10():
	return gm10(request.args.get('data'))

@app.route('/chart10')
def index10():
	return render_template('charts/chartsajax10.html', graphJSON=gm10())

def gm10(type = 'lifeExp'):
	df = pd.read_csv('static/data/gapminder.csv')
	if type == 'lifeExp':
		fig = px.choropleth(df, locations="iso_alpha", color=type,
             hover_name="country", animation_frame="year",
             range_color=[20, 80], projection="natural earth")
	elif type == 'pop':
		fig = px.choropleth(df, locations="iso_alpha", color=type,
		                    hover_name="country", animation_frame="year",
		                    range_color=[60000, 1400000000], projection="natural earth")
	elif type == 'gdpPercap':
		fig = px.choropleth(df, locations="iso_alpha", color=type,
		                    hover_name="country", animation_frame="year",
		                    range_color=[240, 120000], projection="natural earth")
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

# 堆积区域图
@app.route('/callback11', methods=['POST', 'GET'])
def cb11():
	return gm11(request.args.get('data'))

@app.route('/chart11')
def index11():
	return render_template('charts/chartsajax11.html', graphJSON=gm11())

def gm11(type = 'lifeExp'):
	df = pd.read_csv('static/data/gapminder.csv')
	if type == 'lifeExp':
		fig = px.area(df, x="year", y=type, color="continent", line_group="country")
	elif type == 'pop':
		fig = px.area(df, x="year", y=type, color="continent", line_group="country")
	elif type == 'gdpPercap':
		fig = px.area(df, x="year", y=type, color="continent", line_group="country")
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

@app.route('/senti')
def main():
	text = ""
	values = {"positive": 0, "negative": 0, "neutral": 0}

	with open('ask_politics.csv', 'rt') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
		for idx, row in enumerate(reader):
			if idx > 0 and idx % 2000 == 0:
				break
			if  'text' in row:
				nolinkstext = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', row['text'], flags=re.MULTILINE)
				text = nolinkstext

			blob = TextBlob(text)
			for sentence in blob.sentences:
				sentiment_value = sentence.sentiment.polarity
				if sentiment_value >= -0.1 and sentiment_value <= 0.1:
					values['neutral'] += 1
				elif sentiment_value < 0:
					values['negative'] += 1
				elif sentiment_value > 0:
					values['positive'] += 1

	values = sorted(values.items(), key=operator.itemgetter(1))
	top_ten = list(reversed(values))
	if len(top_ten) >= 11:
		top_ten = top_ten[1:11]
	else :
		top_ten = top_ten[0:len(top_ten)]

	top_ten_list_vals = []
	top_ten_list_labels = []
	for language in top_ten:
		top_ten_list_vals.append(language[1])
		top_ten_list_labels.append(language[0])

	graph_values = [{
					'labels': top_ten_list_labels,
					'values': top_ten_list_vals,
					'type': 'pie',
					'insidetextfont': {'color': '#FFFFFF',
										'size': '14',
										},
					'textfont': {'color': '#FFFFFF',
										'size': '14',
								},
					}]

	layout = {'title': '<b>意见挖掘</b>'}

	return render_template('sentiment.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
  app.run(debug= True,port=5000,threaded=True)
