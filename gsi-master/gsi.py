from pprint import pprint as pp
from flask import *
app = Flask(__name__)

state = {}

@app.route('/', methods=['POST'])
def hello():
    global state
    print("post:")
    content = request.get_json()

    if 'match_stats' in content['player']:
        if 'kills' in content['player']['match_stats'] and 'deaths' in content['player']['match_stats']:
            state['kills']     = content['player']['match_stats']['kills']
            state['deaths']    = content['player']['match_stats']['deaths']

        if 'equip_value' in content['player']['state']:
            state['inv_value'] = content['player']['state']['equip_value']
    else:
        if 'kills' in state and 'deaths' in state and 'equip_value' in state:
            del state['kills']
            del state['deaths']
            del state['equip_value']
    pp(content)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/get')
def renderForOBS():
    global state
    if 'kills' in state and 'deaths' in state:
        kills     = state['kills']
        deaths    = state['deaths']
        inv_value = state['inv_value']
        in_game   = True
    else:
        kills     = 0
        deaths    = 0
        inv_value = 0
        in_game   = False

    return render_template('kd.html',
                            kills     = kills,
                            deaths    = deaths,
                            inv_value = inv_value,
                            in_game   = in_game)


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=3000)
    app.state = {}
