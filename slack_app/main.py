import logging
from logging import Logger
from slack_bolt import App, Ack, BoltResponse, BoltContext, Respond, Say
from slack_sdk import WebClient
from typing import Callable, Dict, List

logging.basicConfig(level=logging.DEBUG)

# export SLACK_BOT_TOKEN=xoxb-***
# export SLACK_SIGNING_SECRET=***
app = App()

# ngrok を使っている場合 http://localhost:4040/inspect/http でも確認できますが
# リスナーのログと同時に見るためにペイロードを標準出力に表示するだけの middleware です
@app.use  # または @app.middleware でも可
def log_request(logger: Logger, body: dict, next: Callable[[], BoltResponse]):
    logger.info(body)
    next()

#
# ここに今から解説するコードをそのまま持ってくれば動作します
#

if __name__ == "__main__":
    app.start(3000)  # POST http://localhost:3000/slack/events
