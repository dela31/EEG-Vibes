# Use the data stream as a MIDI instrument


## Install dependencies

- in `midi' run `poetry install`

## Running the app

- Make sure dependencies are installed
- Make sure you have the following environment variables set,
    - EMOTIV_CLIENT_ID
    - EMOTIV_CLIENT_SECRET
- Make sure a device is connected via the EmotivLauncher App 
- Have GarageBand or other audio midi software running
- in `midi` run `poetry run python play.py`
