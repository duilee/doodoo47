test = {
  'name': 'smallest-int',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int;
          11/11/2015 10:01:03|7
          11/11/2015 13:53:36|7
          11/11/2015 14:52:07|7
          11/11/2015 15:36:00|7
          11/11/2015 15:46:03|7
          11/11/2015 16:11:56|7
          11/11/2015 17:42:09|7
          11/11/2015 11:49:59|8
          11/12/2015 14:30:09|8
          11/11/2015 9:57:49|9
          11/11/2015 10:29:15|10
          11/11/2015 11:18:22|10
          11/11/2015 16:56:15|10
          11/11/2015 10:04:51|11
          11/11/2015 10:27:47|11
          11/11/2015 11:04:43|11
          11/11/2015 12:27:14|11
          11/11/2015 12:52:33|11
          11/11/2015 13:05:03|11
          11/11/2015 13:48:29|11
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
