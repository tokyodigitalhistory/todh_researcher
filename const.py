post_message_format = '''\
https://twitter.com/i/web/status/{tweet_id}
---
{text}
---
by {username} (@{screen_name})\
'''

result_header_format = '=== 「{query}」 での検索結果 ==='

query_strings = (
    '"Digital Humanities"',
    '"Digital Humanity"',
    '"デジタル歴史学"',
    '"デジタルヒストリ"',
    '"デジタル・ヒストリ"',
    '"digital history"',
    '#DigHist'
)