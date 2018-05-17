from flask import Flask, render_template

app=Flask('MyViz')

@app.route('/', methods=['GET'])
def Choose():
    incidents = ['13', '4031', '4183', '4016', '56', 'Select']
    path = ['Shimonoseki Campaign', 'Spainish Candian dispute', 'American Candian salmon dispute', 'Haitan Coup', 'Berlin Blockade', 'Select']
    return render_template('choice.html', incidents=incidents, path=path)

@app.route('/13')
def Shimonoseki():
    return(render_template('Shimonoseki.html'))

@app.route('/4031')
def Spain_Canada():
    return(render_template('Spain_Canada.html'))

@app.route('/4183')
def Canada_v_US():
    incidents = ['13', '4031', '4183', '4016', '56']
    return(render_template('Canada_v_US.html'))

@app.route('/4016')
def Haiti():
    incidents = ['13', '4031', '4183', '4016', '56']
    return(render_template('Haiti.html'))

@app.route('/56')
def Berlin_blockade():
    incidents = ['13', '4031', '4183', '4016', '56']
    return(render_template('Berlin_blockade.html'))

app.run(port=5000, debug=True)
