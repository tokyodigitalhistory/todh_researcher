# Templates
post_message_template = '''\
```
{{tweet.text}}
```
https://twitter.com/{{tweet.user.screen_name}}/status/{{tweet.id}}
                        _by {{tweet.user.name}} (@{{tweet.user.screen_name}})_
                        ☆ {{tweet.favorite_count}}, RT {{tweet.retweet_count}}
                        lang: {{tweet.lang}}\
'''

result_header_template = '''\
=== `{{query}}` での検索結果({{num_tweets}}件) ===\
'''

# Queries
query_strings = (
    '"Digital Humanities"',
    '"Digital Humanity"',
    '"デジタル歴史学"',
    '"デジタルヒストリ"',
    '"デジタル・ヒストリ"',
    '"digital history"',
    '#DigHist'
)

excluded_patterns = [
    '^RT @',    # Retweeted statuses
]
