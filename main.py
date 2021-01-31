import pandas as pd
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3


DATABASE_LOCATION = "/Users/ashwin/Documents/spotify/my_played_tracks.sqlite"
USER_ID = "bcugwv67d5aa3r56zurktvbnt"
TOKEN = "BQC8XLStsxq69S_yGw3Lx4MKsW254IZ0qepD9FpSEnmf0g4A8mfC50QlNmTRtLciX_7PTB_PQtcoeSCfTKlxWkCKZsn-5XYX2hVmJLDPbJ88SQ88oITtzPON--qMbWBypwxdmUADrg6KSxaDPgdzOfr_ELfF6sevBT2k_Hbz"

if __name__ == "__main__":

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=TOKEN)
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    getapi = "https://api.spotify.com/v1/me/player/recently-played"

    r = requests.get(getapi, headers=headers)

    data = r.json()

    # to view data
    #pretty_data = json.loads(r.text)
    #print(json.dumps(pretty_data, indent=2))

    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    song_dict = {
        "song_name": song_names,
        "artist_name": artist_names,
        "played_at": played_at_list,
        "timestamp": timestamps
    }

    song_df = pd.DataFrame(song_dict, columns={
                           "song_name", "artist_name", "played_at", "timestamp"})

    print(song_df)
