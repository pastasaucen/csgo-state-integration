from pprint import pprint as pp
from flask import *
app = Flask(__name__)

state = {}
state['players'] = {}

def getIconUrl(x):
    return {
        "weapon_glock": "Glock-18",
        "weapon_usp_silencer": "USP-S",
        "weapon_hkp2000": "P2000",
        "weapon_p250": "P250",
        "weapon_fiveseven": "Five-SeveN",
        "weapon_cz75a": "CZ75-Auto",
        "weapon_elite": "Dual Berettas",
        "weapon_deagle": "Desert Eagle"
    }[x]

@app.route('/', methods=['POST'])
def hello():
    global state
    print("post:")
    content = request.get_json()

    if 'allplayers' in content:
        state['players'] = {}
        for (key, p) in content['allplayers'].items():
            state['players'][key] = p
    
    #print(list(state['players'])[0])
    #print(state['players']['76561197960265768']['name'])
    #print(list(state['players'])[1])
    #print(state['players']['76561197960265769']['name'])
    #print(list(state['players'])[2])
    #print(state['players']['76561197960265770']['name'])
    #print(list(state['players'])[3])
    #print(state['players']['76561197960265771']['name'])

    '''if 'match_stats' in content['player']:
        if 'kills' in content['player']['match_stats'] and 'deaths' in content['player']['match_stats']:
            state['kills']     = content['player']['match_stats']['kills']
            state['deaths']    = content['player']['match_stats']['deaths']

        if 'equip_value' in content['player']['state']:
            state['inv_value'] = content['player']['state']['equip_value']
    else:
        if 'kills' in state and 'deaths' in state and 'equip_value' in state:
            del state['kills']
            del state['deaths']
            del state['equip_value']'''
    #pp(content)
    #pp(state['players'])
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/get')
def renderForOBS():
    global state

    in_game = True

    playerObject = {}

    

    for key in state['players']:
        playerObject[key] = {}
        playerObject[key]['name']          = state['players'][key]['name']
        playerObject[key]['observer_slot'] = state['players'][key]['observer_slot']
        playerObject[key]['team']          = state['players'][key]['team']
        playerObject[key]['health']        = state['players'][key]['state']['health']
        playerObject[key]['armor']         = state['players'][key]['state']['armor']
        playerObject[key]['helmet']        = state['players'][key]['state']['helmet']
        #playerObject[key]['defusekit']     = state['players'][key]['state']['defusekit']
        playerObject[key]['flashed']       = state['players'][key]['state']['flashed']
        playerObject[key]['burning']       = state['players'][key]['state']['burning']
        playerObject[key]['money']         = state['players'][key]['state']['money']
        playerObject[key]['round_kills']   = state['players'][key]['state']['round_kills']
        playerObject[key]['round_killhs']  = state['players'][key]['state']['round_killhs']
        playerObject[key]['round_totaldmg']= state['players'][key]['state']['round_totaldmg']
        playerObject[key]['equip_value']   = state['players'][key]['state']['equip_value']
        playerObject[key]['kills']         = state['players'][key]['match_stats']['kills']
        playerObject[key]['assists']       = state['players'][key]['match_stats']['assists']
        playerObject[key]['deaths']        = state['players'][key]['match_stats']['deaths']
        playerObject[key]['mvps']          = state['players'][key]['match_stats']['mvps']
        playerObject[key]['score']         = state['players'][key]['match_stats']['score']
        #playerObject[key]['weapons']       = state['players'][key]['weapons']
        playerObject[key]['weapons']            = {}
        if 'weapon_1' in state['players'][key]['weapons']:
            tempWep_1                          = state['players'][key]['weapons']
            playerObject[key]['weapons']['weapon_1_name'] =  getIconUrl(tempWep_1['weapon_1']['name'])
            playerObject[key]['weapons']['weapon_1_state'] =  tempWep_1['weapon_1']['state']
        #tempWep_2                          = state['players'][key]['weapons']['weapon_2']
        #playerObject[key]['weapons']['weapon_2_name'] = getIconUrl(tempWep_2['name'])
        #playerObject[key]['weapon_1_ammo']         = state['players'][key]['weapons']['weapon_1']['ammo_clip']
        #playerObject[key]['weapon_1_reserve']         = state['players'][key]['weapons']['weapon_1']['ammo_reserve']
        
    if 'kills' in state and 'deaths' in state:
        kills     = state['kills']
        deaths    = state['deaths']
        inv_value = state['inv_value']
        in_game   = True
    '''else:
        kills     = 0
        deaths    = 0
        inv_value = 0
        in_game   = False'''

    return render_template('test.html',
                            players = playerObject,
                           # players_2 = list(state['players'])[1],

                            in_game   = in_game
                            )


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=3000)
    app.state = {}