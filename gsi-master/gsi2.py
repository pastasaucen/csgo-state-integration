from pprint import pprint as pp
from flask import *
app = Flask(__name__)

state = {}

@app.route('/', methods=['POST'])
def hello():
    global state
    print("post:")
    content = request.get_json()

    pp('yas')

    if 'allplayers' in content:
        for key, p in content['allplayers']:
            state[key]['kills'] = content['allplayers'][p]['match_stats']['kills']
            state[key]['deaths'] = content['allplayers'][p]['match_stats']['deaths']

            if 'equip_value' in content['allplayer'][p]['state']:
                state['inv_value'] = content['allplayers'][p]['state']['equip_value']
    
    pp(content)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/get')
def renderForOBS():
    global state

    if 'kills' in state and 'deaths' in state[0]:
        kills     = state[0]['match_stats']['kills']
        #deaths    = state['deaths']
        #inv_value = state['inv_value']
        in_game   = True
    else:
        kills     = 0
        deaths    = 0
        inv_value = 0
        in_game   = False

    return render_template('test.html',
                            kills     = kills,
                            #deaths    = deaths,
                            #inv_value = inv_value,
                            in_game   = in_game)


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=3030)
    app.state = {}
