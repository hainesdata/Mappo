import json
import datetime
import pandas as pd
import requests
import time


class Scanner:
    def __init__(self):
        self.locations = None
        self.f = None

    def waze_fetch(self):
        headers = {
            "referer": "https://www.waze.com/livemap",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        }

        r = requests.get("https://na-georss.waze.com/rtserver/web/TGeoRSS", headers=headers)
        r.raise_for_status()
        alerts = r.json().get('alerts', [])
        alerts = filter(lambda x: x['type'] == 'POLICE', alerts)
        self.locations = map(lambda x: dict(lat=x['location']['y'], long=x['location']['x']), alerts)
        self.locations = list(self.locations)
        print(self.locations)
        return self.locations

    def api_call(self, debug=False):
        timestamp = int(datetime.datetime.utcnow().timestamp() * 1000)
        content = f'{json.dumps(self.waze_fetch())}@{timestamp}'

        fetch_data_split = content.split('@')
        fetch_time = fetch_data_split[1]
        fetch_data = fetch_data_split[0]
        data = json.loads(fetch_data)
        df = pd.DataFrame(columns=['timestamp', 'lat', 'lon'])
        for entry in data:
            lat = entry.get('lat')
            lon = entry.get('long')
            df.loc[len(df)] = [fetch_time, lat, lon]
        if debug:
            df.to_csv('._tiajffd', index=False, header=True)
        else:
            try:
                df.to_csv('._data', mode='a', header=False, index=False)
            except FileNotFoundError:
                df.to_csv('._data', index=False, header=True)
        del df

    def write_content(self, debug=False, i=-1, n=-1):
        print('--------------------------------------')
        print(f'Initiating API request [{i + 1}/{n}]...')
        self.api_call(debug)
        print('Done.')
        for j in range(120):
            print(f'\rWaiting for API update: {120 - j}s remaining...', end='', flush=True)
            time.sleep(1)
        print('\n')

    def run(self, n=-1, debug=False):
        if n == -1:
            i = 0
            while True:
                self.write_content(debug=debug, i=i, n='∞')
                i += 1
        else:
            for i in range(n):
                self.write_content(debug, epoch=i, length=str(n))


if __name__ == '__main__':
    s = Scanner()
    s.write_content(debug=False)
