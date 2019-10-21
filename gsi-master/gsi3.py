from pprint import pprint as pp
from flask import *
import json

app = Flask(__name__)

state = {}
state['players'] = {}

def getSkinName(x):
    weaponskinsObj = open('weaponskins.json', encoding="utf8")
    weaponskinsStr = weaponskinsObj.read()
    weaponskins = json.loads(weaponskinsStr)
    #pp(weaponskins)
    try:
        return weaponskins['paintkit_names'][x]
        pprint('Heh')
    except:
        return x
        pprint('Neh')

def getWeaponName(x):
    names = {
        "weapon_usp_silencer": "USP",
        "weapon_hkp2000": "P2000",
        "weapon_glock": "Glock",
        "weapon_p250": "P250",
        "weapon_elite": "Duals",
        "weapon_deagle": "Deagle",
        "weapon_cz75a": "CZ75",
        "weapon_fiveseven": "Five7",
        "weapon_revolver": "Revolver",
        "weapon_tec9": "Tec9",
        "weapon_bizon": "PP-Bizon",
        "weapon_mac10": "Mac-10",
        "weapon_mp7": "MP7",
        "weapon_mp9": "MP9",
        "weapon_p90": "P90",
        "weapon_ump45": "UMP-45",
        "weapon_mp5sd": "test",
        "weapon_m4a1": "M4A4",
        "weapon_m4a1_silencer": "M4A1-S",
        "weapon_ak47": "Ak47",
        "weapon_aug": "Aug",
        "weapon_awp": "AWP",
        "weapon_famas": "Famas",
        "weapon_gs3sg1": "gs3sg1",
        "weapon_galilar": "Galil",
        "weapon_scar20": "Scar",
        "weapon_sg556": "Sg556",
        "weapon_ssg08": "SSG 08",
        "weapon_m249": "M249",
        "weapon_mag7": "Mag7",
        "weapon_negev": "Negev",
        "weapon_nova": "Nova",
        "weapon_sawedoff": "Sawed-off",
        "weapon_xm1014": "XM1014",
        "weapon_knife_ct": "CTKnife",
        "weapon_knife_t": "TKnife",
        "weapon_bayonet": "Bayonet",
        "weapon_knife_flip": "Flip Knife",
        "weapon_knife_gut": "Gut Knife",
        "weapon_knife_karambit": "Karambit",
        "weapon_knife_m9_bayonet": "M9bayonet",
        "weapon_knife_tactical": "Huntsman",
        "weapon_knife_butterfly": "Butterfly",
        "weapon_knife_falchion": "Falchion",
        "weapon_knife_survival_bowie": "Bowie",
        "weapon_taser": "Tazer"
    }

    try:
        return names[x]
    except:
        return 'test'

def testGetWeaponName(x):
    icons = {
        "weapon_cz75a": "http://vignette3.wikia.nocookie.net/cswikia/images/c/cf/C75a_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_deagle": "http://vignette2.wikia.nocookie.net/cswikia/images/7/7d/Deagle_hud_go.png/revision/latest/scale-to-width-down/400",
        "weapon_elite": "http://vignette2.wikia.nocookie.net/cswikia/images/8/82/Elite_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_fiveseven": "http://vignette2.wikia.nocookie.net/cswikia/images/9/9c/Fiveseven_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_glock": "http://vignette2.wikia.nocookie.net/cswikia/images/3/33/Glock18_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_p250": "http://vignette2.wikia.nocookie.net/cswikia/images/5/57/P250_hud.png/revision/latest/scale-to-width-down/400",
        "weapon_hkp2000": "http://vignette1.wikia.nocookie.net/cswikia/images/6/67/Hkp2000_hud.png/revision/latest/scale-to-width-down/400",
        "weapon_tec9": "http://vignette3.wikia.nocookie.net/cswikia/images/5/55/Tec9_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_usp_silencer": "http://vignette2.wikia.nocookie.net/cswikia/images/7/73/Usps_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_mag7": "http://vignette2.wikia.nocookie.net/cswikia/images/2/2e/Mag7_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_revolver": "http://vignette2.wikia.nocookie.net/cswikia/images/7/7d/Deagle_hud_go.png/revision/latest/scale-to-width-down/400",
        "weapon_nova": "http://vignette4.wikia.nocookie.net/cswikia/images/c/c8/Nova_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_sawedoff": "http://vignette1.wikia.nocookie.net/cswikia/images/9/94/Sawedoff_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_xm1014": "http://vignette2.wikia.nocookie.net/cswikia/images/a/ad/Xm1014_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_mac10": "http://vignette2.wikia.nocookie.net/cswikia/images/f/f7/Mac10_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_mp7": "http://vignette4.wikia.nocookie.net/cswikia/images/8/8d/Mp7_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_mp9": "http://vignette2.wikia.nocookie.net/cswikia/images/1/14/Mp9_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_p90": "http://vignette3.wikia.nocookie.net/cswikia/images/b/bd/P90_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_bizon": "http://vignette1.wikia.nocookie.net/cswikia/images/d/d5/Bizon_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_ump45": "http://vignette3.wikia.nocookie.net/cswikia/images/c/c4/Ump45_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_ak47": "http://vignette1.wikia.nocookie.net/cswikia/images/7/76/Ak47_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_aug": "http://vignette2.wikia.nocookie.net/cswikia/images/6/6f/Aug_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_famas": "http://vignette2.wikia.nocookie.net/cswikia/images/8/8f/Famas_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_galilar": "http://vignette1.wikia.nocookie.net/cswikia/images/4/4a/Galilar_hud.png/revision/latest/scale-to-width-down/400",
        "weapon_m4a1_silencer": "http://vignette3.wikia.nocookie.net/cswikia/images/4/4f/M4a1s_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_m4a1": "http://vignette2.wikia.nocookie.net/cswikia/images/d/d9/M4a4_hud.png/revision/latest/scale-to-width-down/400",
        "weapon_sg556": "http://vignette1.wikia.nocookie.net/cswikia/images/9/9b/Sg556_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_awp": "http://vignette3.wikia.nocookie.net/cswikia/images/e/eb/Awp_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_gs3sg1": "http://vignette4.wikia.nocookie.net/cswikia/images/4/4a/G3sg1_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_ssg08": "http://vignette4.wikia.nocookie.net/cswikia/images/3/3c/Ssg08_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_scar20": "http://vignette4.wikia.nocookie.net/cswikia/images/c/c9/Scar20_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_m249": "http://vignette2.wikia.nocookie.net/cswikia/images/e/ea/M249_hud_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_negev": "http://vignette2.wikia.nocookie.net/cswikia/images/b/be/Negev_hud.png/revision/latest/scale-to-width-down/400",

        "weapon_knife_ct": "http://vignette2.wikia.nocookie.net/cswikia/images/4/4b/Knife_ct_hud_outline_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_knife_t": "http://vignette3.wikia.nocookie.net/cswikia/images/2/28/Knife_t_hud_outline_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_bayonet": "http://vignette2.wikia.nocookie.net/cswikia/images/2/28/Csgo_knife_Bayonet.png/revision/latest/scale-to-width-down/400",
        "weapon_knife_butterfly": "http://vignette2.wikia.nocookie.net/cswikia/images/d/df/Knife_butterfly_hud_outline_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_knife_falchion": "http://vignette4.wikia.nocookie.net/cswikia/images/7/7e/Falchion_Knife_hud_outline_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_knife_flip": "http://vignette3.wikia.nocookie.net/cswikia/images/a/a4/Knife_flip_hud_outline_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_knife_gut": "http://vignette2.wikia.nocookie.net/cswikia/images/f/ff/Knife_gut_hud_outline_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_knife_tactical": "http://vignette2.wikia.nocookie.net/cswikia/images/5/53/Knife_hustman_hud_outline_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_knife_karambit": "http://vignette4.wikia.nocookie.net/cswikia/images/5/57/Knife_karambit_hud_outline_csgo.png/revision/latest/scale-to-width-down/400",
        "weapon_knife_m9_bayonet": "http://vignette4.wikia.nocookie.net/cswikia/images/d/d3/Csgo_knife_M9_Bayonet.png/revision/latest/scale-to-width-down/400",
        "weapon_knife_push": "http://vignette4.wikia.nocookie.net/cswikia/images/f/f1/Knife_push_hud_outline_csgo.png/revision/latest/scale-to-width-down/400"
    }
    try:
        return icons[x]
    except:
        return 'test'

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
    #pp(getSkinName("something"))

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
        if 'defusekit' in state['players'][key]['state']:
            playerObject[key]['defusekit']     = state['players'][key]['state']['defusekit']
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
        playerObject[key]['weapons']['grenades'] = {}
        if 'weapon_1' in state['players'][key]['weapons']:
            tempWep_1                          = state['players'][key]['weapons']
            if state['players'][key]['weapons']:
               # playerObject[key]['weapons']['secondary_name'] =  getWeaponName(state['players'][key]['weapons']['weapon_1']['name'])
               # playerObject[key]['weapons']['secondary_state'] =  state['players'][key]['weapons']['weapon_1']['state']

                if len(state['players'][key]['weapons']) > 1:
                    for t in state['players'][key]['weapons']:
                        if 'type' in state['players'][key]['weapons'][t] and state['players'][key]['weapons'][t]['type'] not in ['Knife', 'Grenade', 'C4', 'Pistol']:
                            playerObject[key]['weapons']['primary_name'] =  getWeaponName(state['players'][key]['weapons'][t]['name'])
                            playerObject[key]['weapons']['primary_type'] =  state['players'][key]['weapons'][t]['type']
                            playerObject[key]['weapons']['primary_state'] =  state['players'][key]['weapons'][t]['state']

                        elif 'type' in state['players'][key]['weapons'][t] and state['players'][key]['weapons'][t]['type'] == 'Pistol':
                            playerObject[key]['weapons']['secondary_name'] =  getWeaponName(state['players'][key]['weapons'][t]['name'])
                            playerObject[key]['weapons']['secondary_type'] =  state['players'][key]['weapons'][t]['type']
                            playerObject[key]['weapons']['secondary_state'] =  state['players'][key]['weapons'][t]['state']

                        elif 'type' in state['players'][key]['weapons'][t] and state['players'][key]['weapons'][t]['type'] == 'Grenade':
                            playerObject[key]['weapons']['grenades'][state['players'][key]['weapons'][t]['name']] = True
                            if state['players'][key]['weapons'][t]['ammo_reserve'] > 1:
                                playerObject[key]['weapons']['grenades'][state['players'][key]['weapons'][t]['name']+"_2"] = True
                            
                        elif 'type' in state['players'][key]['weapons'][t] and state['players'][key]['weapons'][t]['type'] == 'Knife':
                            if state['players'][key]['weapons'][t]['name'] == 'weapon_knife':
                                playerObject[key]['weapons']['knife'] = getWeaponName(state['players'][key]['weapons'][t]['name'] + "_" + state['players'][key]['team'].lower())
                            else:
                                playerObject[key]['weapons']['knife'] = getWeaponName(state['players'][key]['weapons'][t]['name'])
                        
                        elif 'type' in state['players'][key]['weapons'][t] and state['players'][key]['weapons'][t]['type'] == 'C4':
                            playerObject[key]['C4'] = True

                            #pp(playerObject[key]['weapons']['knife'])

                
                    #pp(state['players'][key]['weapons']['weapon_2'])

                #pp(state['players'][key]['weapons'])
                #tempWep_2                          = state['players'][key]['weapons']['weapon_2']
                #playerObject[key]['weapons']['weapon_2_name'] = getIconUrl(tempWep_2['name'])
                #playerObject[key]['weapon_1_ammo']         = state['players'][key]['weapons']['weapon_1']['ammo_clip']
                #playerObject[key]['weapon_1_reserve']         = state['players'][key]['weapons']['weapon_1']['ammo_reserve']

                skinname = state['players'][key]['weapons']['weapon_1']['paintkit']
                playerObject[key]['weapons']['skin'] = getSkinName(skinname)
        
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
    
    testObject = {
        "primary": testGetWeaponName("weapon_ak47"),
        "secondary": testGetWeaponName("weapon_hkp2000"),
        "knife": testGetWeaponName("weapon_knife_falchion")
    }

    return render_template('test.html',
                            players = playerObject,
                            weaponTest = testObject,
                           # players_2 = list(state['players'])[1],

                            in_game   = in_game
                            )


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=3000)
    app.state = {}