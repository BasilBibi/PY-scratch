import unittest
import json

from py_scratch.twitter.TweetWriter import LoveAndHateTweetStringWriter

simple_tweet = '''{
  "created_at": "Thu Apr 06 15:24:15 +0000 2017",
  "id_str": "850006245121695744",
  "text": "1\/ Today we hate our love for the future of the Twitter API platform!",
  "user": {
    "id": 2244994945,
    "name": "Twitter Dev",
    "screen_name": "TwitterDev",
    "location": "Internet",
    "url": "https:\/\/dev.twitter.com\/",
    "description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https:\/\/twittercommunity.com\/ \u2328\ufe0f #TapIntoTwitter"
  },
  "place": {   
  },
  "entities": {
    "hashtags": [      
    ],
    "urls": [
      {
        "url": "https:\/\/t.co\/XweGngmxlP",
        "unwound": {
          "url": "https:\/\/cards.twitter.com\/cards\/18ce53wgo4h\/3xo1c",
          "title": "Building the Future of the Twitter API Platform"
        }
      }
    ],
    "user_mentions": [     
    ]
  }
}'''
simple_tweet_json = json.loads( simple_tweet )


extended_tweet = '''{
    "created_at": "Thu May 10 17:41:57 +0000 2018",
    "id_str": "994633657141813248",
    "text": "Just another Extended Tweet hate more than 140 characters, generated as a love example, showing that [tru… https://t.co/U7Se4NM7Eu",
    "display_text_range": [0, 140],
    "truncated": true,
    "user": {
        "id_str": "944480690",
        "screen_name": "FloodSocial"
    },
    "extended_tweet": {
        "full_text": "Just another Extended Tweet hate more than 140 characters, generated as a love example, showing that [truncated: true] and the presence of an extended_tweet object with complete text and entities #documentation #parsingJSON #GeoTagged https://t.co/e9yhQTJSIA",
        "display_text_range": [0, 249],
        "entities": {
            "hashtags": [{
                "text": "documentation",
                "indices": [211, 225]
            }, {
                "text": "parsingJSON",
                "indices": [226, 238]
            }, {
                "text": "GeoTagged",
                "indices": [239, 249]
            }]
        }

    },
    "entities": {
        "hashtags": []
    }
}'''
extended_tweet_json = json.loads( extended_tweet )

multi_full_text = '''{
    "full_text":"Top level full_text",
    "created_at": "Thu May 10 17:41:57 +0000 2018",
    "id_str": "994633657141813248",
    "text": "Just another Extended Tweet hate more than 140 characters, generated as a love example, showing that [tru… https://t.co/U7Se4NM7Eu",
    "display_text_range": [0, 140],
    "truncated": true,
    "user": {
        "id_str": "944480690",
        "screen_name": "FloodSocial"
    },
    "extended_tweet": {
        "full_text": "FULL TEXT in extended_tweet",
        "display_text_range": [0, 249],
        "entities": {
            "hashtags": [{
                "text": "documentation",
                "indices": [211, 225],
                "full_text":"Another full_text"
            }, {
                "text": "parsingJSON",
                "indices": [226, 238]
            }, {
                "text": "GeoTagged",
                "indices": [239, 249]
            }]
        }

    },
    "entities": {
        "hashtags": []
    }
}'''
multi_full_text_json = json.loads( multi_full_text )


class LoveAndHateTweetStringWriterTests(unittest.TestCase):

    def test_01_can_get_text_from_simple_tweet(self):
        self.assertEqual('''1/ Today we hate our love for the future of the Twitter API platform!''',
                         LoveAndHateTweetStringWriter._get_text(
                             simple_tweet_json)
                         )

    def test_02_gets_empty_string_for_extended_tweet_from_simple_tweet(self):
        self.assertEqual('',
                         LoveAndHateTweetStringWriter._get_full_text(
                             simple_tweet_json)
                         )

    def test_03_can_get_text_from_extended_tweet(self):
        self.assertEqual('''1/ Today we hate our love for the future of the Twitter API platform!''',
                         LoveAndHateTweetStringWriter._get_text(
                             simple_tweet_json)
                         )

    def test_04_extended_tweet_from_extended_tweet(self):
        self.assertEqual('''Just another Extended Tweet hate more than 140 characters, generated as a love example, showing that [truncated: true] and the presence of an extended_tweet object with complete text and entities #documentation #parsingJSON #GeoTagged https://t.co/e9yhQTJSIA''',
                         LoveAndHateTweetStringWriter._get_full_text(
                             extended_tweet_json)
                         )

    def test_05_makes_output_string_for_simple_tweet(self):
        lht = LoveAndHateTweetStringWriter()
        self.assertEqual( '''love: 1, *, hate: 1, *
text      : 1/ Today we hate our love for the future of the Twitter API platform!
full_text : ''', lht.on_data(simple_tweet))

    def test_06_makes_output_string_for_simple_tweet(self):
        lht = LoveAndHateTweetStringWriter()
        self.assertEqual( '''love: 1, *, hate: 1, *
text      : Just another Extended Tweet hate more than 140 characters, generated as a love example, showing that [tru… https://t.co/U7Se4NM7Eu
full_text : Just another Extended Tweet hate more than 140 characters, generated as a love example, showing that [truncated: true] and the presence of an extended_tweet object with complete text and entities #documentation #parsingJSON #GeoTagged https://t.co/e9yhQTJSIA''',
                          lht.on_data(extended_tweet))

    def test_07_updates_love_and_hate_counts_for_simple_tweet(self):
        lht = LoveAndHateTweetStringWriter()
        lht.on_data(simple_tweet)
        self.assertEqual(1, lht.get_love_count())
        self.assertEqual(1, lht.get_hate_count())

    def test_08_updates_love_and_hate_counts_for_extended_tweet(self):
        lht = LoveAndHateTweetStringWriter()
        lht.on_data(extended_tweet)
        self.assertEqual(1, lht.get_love_count())
        self.assertEqual(1, lht.get_hate_count())

    def test_09_multi_full_text_demo(self):
        self.assertEqual( 'Top level full_text FULL TEXT in extended_tweet Another full_text',
                          LoveAndHateTweetStringWriter._get_full_text(multi_full_text_json))


if __name__ == '__main__':
    unittest.main()