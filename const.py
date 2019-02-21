# Templates
post_message_template = '''\
```
{{tweet.text}}
```
https://twitter.com/i/web/status/{{tweet.id}}
                        _by {{tweet.user.name}} (@{{tweet.user.screen_name}})_
                        ☆ {{tweet.favorite_count}}, RT {{tweet.retweet_count}}
                        lang: {{tweet.lang}}\
'''

result_header_format = '=== 「{query}」 での検索結果 ==='

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
