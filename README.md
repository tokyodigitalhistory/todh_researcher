# ToDH Researcher bot
Search tweets about Digital (Humanities|History) and post them to ToDH Slack

## 何かご要望やお気づきの点がある方へ
issueを切って上げてください。
気づかないこともあるかもしれないので、見てなさそうな様子であれば、Slackでもお知らせください。

コード修正ができそうであれば、以下を読み、ブランチを切り、マージリクエストを投げてください。

- [GitHubでPullRequestを使った開発フロー](https://qiita.com/NAKKA-K/items/072e28c3f3ad7178f3a4)

## 雑なつかいかたメモ

```
$ git clone https://github.com/tokyodigitalhistory/todh_researcher.git
$ cd todh_researcher
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ mv secret_info.py.sample secret_info.py
$ vi secret_info.py # 中身を埋める
$ python3 search_and_post.py
```

`slack_channel_id`, `slack_direct_message_id` は~~SlackAPIのgroup.list, 
channel.list, lm.list, lm.historyなどを使って頑張って取る。~~
`get_slack_info.py` を使って取得する。 

cronで動かすには、ラッパースクリプトを書く。
なんかいい方法があるかもしれないが、とりあえずこれで動かしている。

```
$cat run_researcher
#!/bin/bash
cd /path/to/todh_researcher
source env/bin/activate
python3 search_and_post.py
$ crontab -l
[...]
# 
# m h  dom mon dow   command
0 * * * * /path/to/todh_researcher/run_researcher
```