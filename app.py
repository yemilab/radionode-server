import time
import json

from flask import Flask, request

app = Flask(__name__)

@app.route('/checkin', methods=['POST'])
def checkin():
    data = { 'time': int(time.time()) }

    mac = request.form.get('MAC')
    if mac is not None:
        data['mac'] = mac
    ip = request.form.get('IP')
    if ip is not None:
        data['ip'] = ip
    model = request.form.get('MODEL')
    if model is not None:
        data['model'] = model
    splrate = request.form.get('splrate')
    if splrate is not None:
        data['splrate'] = int(splrate)
    interval = request.form.get('interval')
    if interval is not None:
        data['interval'] = int(interval)   
    ver = request.form.get('VER')
    if ver is not None:
        data['ver'] = int(ver)
    bssid = request.form.get('bssid')
    if bssid is not None:
        data['bssid'] = bssid
    ssid = request.form.get('ssid')
    if ssid is not None:
        data['ssid'] = ssid
    tags = request.form.get('TAGS')
    if tags is not None:
        for i, tag in enumerate(tags.split('|')[:-1]):
            data[f'tag_ch{i:02d}'] = tag

    with open('data/rn400_checkin.log', 'a') as fp:
        fp.write(json.dumps(data)+'\n')

    return '', 204

@app.route('/datain', methods=['POST'])
def datain():
    data = { 'time': int(time.time()) }

    mac = request.form.get('mac')
    if mac is not None:
        data['mac'] = mac
    bat = request.form.get('bat')
    if bat is not None:
        data['bat'] = int(bat)
    volt = request.form.get('volt')
    if volt is not None:
        volt_lst = volt.split('|')
        data['volt0'] = int(volt_lst[0])
        data['volt1'] = float(volt_lst[1])
    sig = request.form.get('sig')
    if sig is not None:
        data['sig'] = int(sig)
    smodel = request.form.get('SMODEL')
    if smodel is not None:
        data['smodel'] = smodel  
    vals = request.form.get('C000')
    if vals is not None:
        for i, v_str in enumerate(vals.split('|')[:-1]):
            if i == 0:
                data[f'c000_ch{i:02d}'] = int(v_str)
            else:
                if v_str == 'NULL':
                    data[f'c000_ch{i:02d}'] = None
                else:
                    data[f'c000_ch{i:02d}'] = float(v_str)

    with open('data/rn400_datain.log', 'a') as fp:
        fp.write(json.dumps(data)+'\n')

    return '', 204
