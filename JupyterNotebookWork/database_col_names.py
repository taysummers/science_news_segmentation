def get_database_columns():

    ## Dummy Column Names
    dummy_column_names = {
    # Other
    'LIFE': {1.0: 'Life is better than 50 yrs ago',
             2.0: 'Life is worse than 50 yrs ago',
             3.0: 'Life is the same as 50 yrs ago'},

    # General News
    'TOPICINT_a': {1.0: 'Very interested in government and politics news',
                   2.0: 'Somewhat interested in government and politics news',
                   3.0: 'Not too interested in government and politics news',
                   4.0: 'Not at all interested in government and politics news'},

    # General News
    'TOPICINT_a_t2b': {1.0: 'Interested in government and politics news',
                       2.0: 'Not interested in government and politics news'},

    # General News
    'TOPICINT_b': {1.0: 'Very interested in local community news',
                   2.0: 'Somewhat interested in local community news',
                   3.0: 'Not too interested in local community news',
                   4.0: 'Not at all interested in local community news'},

    # General News
    'TOPICINT_b_t2b': {1.0: 'Interested in local community news',
                       2.0: 'Not interested in local community news'},

    # General News
    'TOPICINT_c': {1.0: 'Very interested in sports news',
                   2.0: 'Somewhat interested in sports news',
                   3.0: 'Not too interested in sports news',
                   4.0: 'Not at all interested in sports news'},

    # General News
    'TOPICINT_c_t2b': {1.0: 'Interested in sports news',
                       2.0: 'Not interested in sports news'},


    # General News
    'TOPICINT_d': {1.0: 'Very interested in business and finance news',
                   2.0: 'Somewhat interested in business and finance news',
                   3.0: 'Not too interested in business and finance news',
                   4.0: 'Not at all interested in business and finance news'},

    # General News
    'TOPICINT_d_t2b': {1.0: 'Interested in business and finance news',
                       2.0: 'Not interested in business and finance news'},

    # General News
    'TOPICINT_e': {1.0: 'Very interested in science news',
                   2.0: 'Somewhat interested in science news',
                   3.0: 'Not too interested in science news',
                   4.0: 'Not at all interested in science news'},

    # General News
    'TOPICINT_e_t2b': {1.0: 'Interested in science news',
                       2.0: 'Not interested in science news'},

    # General News
    'TOPICINT_f': {1.0: 'Very interested in entertainment news',
                   2.0: 'Somewhat interested in entertainment news',
                   3.0: 'Not too interested in entertainment news',
                   4.0: 'Not at all interested in entertainment news'},

    # General News
    'TOPICINT_f_t2b': {1.0: 'Interested in entertainment news',
                       2.0: 'Not interested in entertainment news'},


    # Science News
    'SCIOFTEN': {1.0: 'I read, watch or listen to science news nearly every day',
                 2.0: 'I read, watch or listen to science news a few times a week',
                 3.0: 'I read, watch or listen to science news a few times a month',
                 4.0: 'I read, watch or listen to science news less often than a few times a month'},
    # Science News
    'TOPICS1': {1.0: 'Get science news on a couple topics',
                2.0: 'Get science news on a lot of different topics'},
    # Science News
    'TOPICMOST': {'1': 'Most interested in health & medicine',
                  '2': 'Most interested in technology',
                  '3': 'Most interested in energy and environment',
                  '4': 'Most interested in food and nutrition',
                  '5': 'Most interested in space and astronomy',
                  '6': 'Most interested in evolution of human & animals',
                  '7': 'Most interested in the mind and brain',
                  '8': 'Most interested in other',
                  '9': 'Not interested in any of these science topics',
                  '-1': 'TOPICMOST: Refused',
                  ' ': 'TOPICMOST: Not asked'},
    # Science News
    'SOURCE1': {1.0: 'Get science news from a couple sources',
                2.0: 'Get science news from many different sources'},
    # Science News
    'SOURCE2': {1.0: 'Get science news from sources that specialize in science topics',
                2.0: 'Get science news sources that cover all sorts of topics'},
    # Science News
    'ENJOY': {1.0: 'Enjoy science news a lot more than other news',
              2.0: 'Enjoy science news more than other news',
              3.0: 'Enjoy science news less than other news',
              4.0: 'Enjoy science news a lot less than other news'},
    # Science News
    'KNOWLEDGE': {1.0: 'I know a lot about science',
                  2.0: 'I know some about science',
                  3.0: 'I know not much about science',
                  4.0: 'I know nothing at all about science'},
    # Science News
    'SEEK': {1.0: "I mostly get science news because I'm looking for it",
             2.0: "I mostly get science news because I happen to come across it"},
    # Science News
    'SOURCEALT': {1.0: 'I regularly get science new from sources that provide alternative perspectives to conventional science or medical research',
                  2.0: 'I do not regularly get science new from sources that provide alternative perspectives to conventional science or medical research'},
    # Science News
    'SCIWHY_a': {1.0: "Enjoy talking with others about what's happening in science is a major reason to follow science news",
                 2.0: "Enjoy talking with others about what's happening in science is a minor reason to follow science news",
                 3.0: "Enjoy talking with others about what's happening in science is not a reason to follow science news"},
    # Science News
    'SCIWHY_b': {1.0: "It is related to things I need to know for my job is a major reason to follow science news",
                 2.0: "It is related to things I need to know for my job is a minor reason to follow science news",
                 3.0: "It is related to things I need to know for my job is not a reason to follow science news"},
    # Science News
    'SCIWHY_c': {1.0: "Helps me make decision about every day life is a major reason to follow science news",
                 2.0: "Helps me make decision about every day life is a minor reason to follow science news",
                 3.0: "Helps me make decision about every day life is not a reason to follow science news"},
    # Science News
    'SCIWHY_d': {1.0: "I feel I have a social or civil obligation to stay informed is a major reason to follow science news",
                 2.0: "I feel I have a social or civil obligation to stay informed is a minor reason to follow science news",
                 3.0: "I feel I have a social or civil obligation to stay informed is not a reason to follow science news"},
    # Science News
    'SCIWHY_e': {1.0: "I am curious about what's happening in science is a major reason to follow science news",
                 2.0: "I am curious about what's happening in science is a minor reason to follow science news",
                 3.0: "I am curious about what's happening in science is not a reason to follow science news"},
    # Science News
    'SCIWHY_f': {'1': "It is related to my children's activities, interests or education is a major reason to follow science news",
                 '2': "It is related to my children's activities, interests or education is a minor reason to follow science news",
                 '3': "It is related to my children's activities, interests or education is not a reason to follow science news",
                 ' ': 'SCIWHY_f: Not Asked',
                 '-1': 'SCIWHY_f: Refused'},
    # Science News
    'SCIWHY_g': {1.0: "It is related to my activities, hobbies or interests is a major reason to follow science news",
                 2.0: "It is related to my activities, hobbies or interests is a minor reason to follow science news",
                 3.0: "It is related to my activities, hobbies or interests is not a reason to follow science news"},
    # Science News
    'WHYNOT_a': {1.0: "Science news is boring is a major reason to not follow science news",
                 2.0: "Science news is boring is a minor reason to not follow science news",
                 3.0: "Science news is boring is not a reason to not follow science news"},
    # Science News
    'WHYNOT_b': {1.0: "Science news is hard to understand is a major reason to not follow science news",
                 2.0: "Science news is hard to understand is a minor reason to not follow science news",
                 3.0: "Science news is hard to understand is not a reason to not follow science news"},
    # Science News
    'WHYNOT_c': {1.0: "I often disagree with science news is a major reason to not follow science news",
                 2.0: "I often disagree with science news is a minor reason to not follow science news",
                 3.0: "I often disagree with science news is not a reason to not follow science news"},
    # Science News
    'WHYNOT_d': {1.0: "Science news is less important than other topics is a major reason to not follow science news",
                 2.0: "Science news is less important than other topics is a minor reason to not follow science news",
                 3.0: "Science news is less important than other topics is not a reason to not follow science news"},
    # Science News
    'WHYNOT_e': {1.0: "I am too busy to keep up with science news more often is a major reason to not follow science news",
                 2.0: "I am too busy to keep up with science news more often is a minor reason to not follow science news",
                 3.0: "I am too busy to keep up with science news more often is not a reason to not follow science news"},
    # Science News
    'WHYNOT_f': {1.0: "I already get enough science news is a major reason to not follow science news",
                 2.0: "I already get enough science news is a minor reason to not follow science news",
                 3.0: "I already get enough science news is not a reason to not follow science news"},
    # Science News
    'WHYNOT_g': {1.0: "The sources I regulary get news from don't cover a lot of science is a major reason to not follow science news",
                 2.0: "The sources I regulary get news from don't cover a lot of science is a minor reason to not follow science news",
                 3.0: "The sources I regulary get news from don't cover a lot of science is not a reason to not follow science news"},
    # Science News
    'WHYNOT_h': {1.0: "The science topics I'm most interested in are not covered often is a major reason to not follow science news",
                 2.0: "The science topics I'm most interested in are not covered often is a minor reason to not follow science news",
                 3.0: "The science topics I'm most interested in are not covered often is not a reason to not follow science news"},
    # Media
    'NEWSJOB': {1.0: 'News media does a very good job in covering science',
                2.0: 'News media does a somewhat good job in covering science',
                3.0: 'News media does a somewhat bad job in covering science',
                4.0: 'News media does a very bad job in covering science'},
    # Media
    'NEWSFACTS_a': {1.0: 'News outlets that cover a range of topics get the facts right almost all of the time',
                    2.0: 'News outlets that cover a range of topics get the facts right more than half of the time',
                    3.0: 'News outlets that cover a range of topics get the facts right about half of the time',
                    4.0: 'News outlets that cover a range of topics get the facts right less than half of the time',
                    5.0: 'News outlets that cover a range of topics get the facts right hardly ever',
                    6.0: "Don't know enough to say if news outlets that cover a range of topics get the facts right"},

    'NEWSFACTS_a_t2b': {1: 'News outlets that cover a range of topics get the facts right almost all or more than half of the time',
                        2: 'News outlets that cover a range of topics get the facts right half of the time',
                        3: 'News outlets that cover a range of topics get the facts right less than half of the time or hardly ever',
                        4: 'Don\'t know enough about news outlets that cover a range of topics'},

    # Media
    'NEWSFACTS_b': {1.0: 'Documentaries or other science video programs get the facts right almost all of the time',
                    2.0: 'Documentaries or other science video programs get the facts right more than half of the time',
                    3.0: 'Documentaries or other science video programs get the facts right about half of the time',
                    4.0: 'Documentaries or other science video programs get the facts right less than half of the time',
                    5.0: 'Documentaries or other science video programs get the facts right hardly ever',
                    6.0: "Don't know enough to say if Documentaries or other science video programs get the facts right"},

    'NEWSFACTS_b_t2b': {1: 'Documentaries or other science video programs get the facts right almost all or more than half of the time',
                        2: 'Documentaries or other science video programs get the facts right half of the time',
                        3: 'Documentaries or other science video programs get the facts right less than half of the time or hardly ever',
                        4: 'Don\'t know enough about documentaries or other science video programs'},

    # Media
    'NEWSFACTS_c': {1.0: 'Science magazines (print/online) get the facts right almost all of the time',
                    2.0: 'Science magazines (print/online) get the facts right more than half of the time',
                    3.0: 'Science magazines (print/online) get the facts right about half of the time',
                    4.0: 'Science magazines (print/online) get the facts right less than half of the time',
                    5.0: 'Science magazines (print/online) get the facts right hardly ever',
                    6.0: "Don't know enough to say if Science magazines (print/online) get the facts right"},

    'NEWSFACTS_c_t2b': {1: 'Science magazines (print/online) get the facts right almost all or more than half of the time',
                        2: 'Science magazines (print/online) get the facts right half of the time',
                        3: 'Science magazines (print/online) get the facts right less than half of the time or hardly ever',
                        4: 'Don\'t know enough about science magazines (print/online)'},

    # Media
    'NEWSFACTS_d': {1.0: 'Online discussion forums about science get the facts right almost all of the time',
                    2.0: 'Online discussion forums about science get the facts right more than half of the time',
                    3.0: 'Online discussion forums about science get the facts right about half of the time',
                    4.0: 'Online discussion forums about science get the facts right less than half of the time',
                    5.0: 'Online discussion forums about science get the facts right hardly ever',
                    6.0: "Don't know enough to say if Online discussion forums about science get the facts right"},

    'NEWSFACTS_d_t2b': {1: 'Online discussion forums about science get the facts right almost all or more than half of the time',
                        2: 'Online discussion forums about science get the facts right half of the time',
                        3: 'Online discussion forums about science get the facts right less than half of the time or hardly ever',
                        4: 'Don\'t know enough about online discussion forums about science'},

    # Media
    'NEWSFACTS_e': {1.0: 'Science podcasts or radio programs get the facts right almost all of the time',
                    2.0: 'Science podcasts or radio programs get the facts right more than half of the time',
                    3.0: 'Science podcasts or radio programs get the facts right about half of the time',
                    4.0: 'Science podcasts or radio programs get the facts right less than half of the time',
                    5.0: 'Science podcasts or radio programs get the facts right hardly ever',
                    6.0: "Don't know enough to say if Science podcasts or radio programs get the facts right"},

    'NEWSFACTS_e_t2b': {1: 'Science podcasts or radio programs get the facts right almost all or more than half of the time',
                        2: 'Science podcasts or radio programs get the facts right half of the time',
                        3: 'Science podcasts or radio programs get the facts right less than half of the time or hardly ever',
                        4: 'Don\'t know enough about science podcasts or radio programs'},

    # Media
    'NEWSFACTS_f': {1.0: 'Family, friends & acquaintances get the facts right almost all of the time',
                    2.0: 'Family, friends & acquaintances get the facts right more than half of the time',
                    3.0: 'Family, friends & acquaintances get the facts right about half of the time',
                    4.0: 'Family, friends & acquaintances get the facts right less than half of the time',
                    5.0: 'Family, friends & acquaintances get the facts right hardly ever',
                    6.0: "Don't know enough to say if Family, friends & acquaintances get the facts right"},

    'NEWSFACTS_f_t2b': {1: 'Family, friends & acquaintances get the facts right almost all or more than half of the time',
                        2: 'Family, friends & acquaintances get the facts right half of the time',
                        3: 'Family, friends & acquaintances get the facts right less than half of the time or hardly ever',
                        4: 'Don\'t know enough about family, friends & acquaintances'},

    # Media
    'NEWSFACTS_g': {1.0: 'Government agencies get the facts right almost all of the time',
                    2.0: 'Government agencies get the facts right more than half of the time',
                    3.0: 'Government agencies get the facts right about half of the time',
                    4.0: 'Government agencies get the facts right less than half of the time',
                    5.0: 'Government agencies get the facts right hardly ever',
                    6.0: "Don't know enough to say if Government agencies get the facts right"},

    'NEWSFACTS_g_t2b': {1: 'Government agencies get the facts right almost all or more than half of the time',
                        2: 'Government agencies get the facts right half of the time',
                        3: 'Government agencies get the facts right less than half of the time or hardly ever',
                        4: 'Don\'t know enough about government agencies'},

    # Media
    'NEWSFACTS_h': {1.0: 'Advocacy organizations get the facts right almost all of the time',
                    2.0: 'Advocacy organizations get the facts right more than half of the time',
                    3.0: 'Advocacy organizations get the facts right about half of the time',
                    4.0: 'Advocacy organizations get the facts right less than half of the time',
                    5.0: 'Advocacy organizations get the facts right hardly ever',
                    6.0: "Don't know enough to say if Advocacy organizations get the facts right"},

    'NEWSFACTS_h_t2b': {1: 'Advocacy organizations get the facts right almost all or more than half of the time',
                        2: 'Advocacy organizations get the facts right half of the time',
                        3: 'Advocacy organizations get the facts right less than half of the time or hardly ever',
                        4: 'Don\'t know enough about advocacy organizations'},

    # Media
    'NEWSFACTS_i': {1.0: 'Science technology centers or museums get the facts right almost all of the time',
                    2.0: 'Science technology centers or museums get the facts right more than half of the time',
                    3.0: 'Science technology centers or museums get the facts right about half of the time',
                    4.0: 'Science technology centers or museums get the facts right less than half of the time',
                    5.0: 'Science technology centers or museums get the facts right hardly ever',
                    6.0: "Don't know enough to say if Science technology centers or museums get the facts right"},

    'NEWSFACTS_i_t2b': {1: 'Science technology centers or museums get the facts right almost all or more than half of the time',
                        2: 'Science technology centers or museums get the facts right half of the time',
                        3: 'Science technology centers or museums get the facts right less than half of the time or hardly ever',
                        4: 'Don\'t know enough about Science technology centers or museums'},

    # Other
    'SNSUSE': {1.0: 'Use social media',
               2.0: "Don't use social media"},
    # Other
    'SNSFREQ': {'1': "Use social media several times a day",
                '2': "Use social media about once a day",
                '3': "Use social media a few times a week",
                '4': "Use social every few weeks",
                '5': "Use social media less often than every few weeks",
                ' ': 'SNSFREQ: Not Asked',
                '-1': 'SNSFREQ: Refused'},
    # Science News
    'FOLLOW': {'1': "Follow science organizations, people or pages on social media",
               '2': "Don't follow science organizations, people or pages on social media",
               ' ': 'FOLLOW: Not Asked',
               '-1': 'FOLLOW: Refused'},

    'FOLLOWANTI': {'1': "Follow science organizations, people or pages on social media that provide alt. perspectives to conventional science",
                   '2': "Don't follow science organizations, people or pages on social media that provide alt. perspectives to conventional science",
                   ' ': 'FOLLOWANTI: Not Asked',
                   '-1': 'FOLLOWANTI: Refused'},
    # Science News
    'SNSSCI': {'1': "A lot of the posts I see on social media are about science",
               '2': "Some of the posts I see on social media are about science",
               '3': "Not many of the posts I see on social media are about science",
               '4': "None of the posts I see on social media are about science",
               ' ': 'SNSSCI: Not Asked',
               '-1': 'SNSSCI: Refused'},
    # Science News
    'SNSCLICK': {'1': "I often click on a link to news when I see a science news post on social media",
                 '2': "I sometimes click on a link to news when I see a science news post on social media",
                 '3': "I hardly ever click on a link to news when I see a science news post on social media",
                 '4': "I never click on a link to news when I see a science news post on social media",
                 ' ': 'SNSCLICK: Not Asked',
                 '-1': 'SNSCLICK: Refused'},
    # Science News
    'SNSSCIIMP': {'1': "Social media are the most important way I get science news",
                  '2': "Social media are an important way I get science news, but not the most important",
                  '3': "Social media are not a very important way I get science news",
                  ' ': 'SNSSCIIMP: Not Asked',
                  '-1': 'SNSSCIIMP: Refused'},
    # Science News
    'SNSNEW': {'1': "I often see science news stories on social media that I wouldn't have seen elsewhere",
               '2': "I sometimes see science news stories on social media that I wouldn't have seen elsewhere",
               '3': "I hardly ever see science news stories on social media that I wouldn't have seen elsewhere",
               '4': "I never see science news stories on social media that I wouldn't have seen elsewhere",
               ' ': 'SNSNEW: Not Asked',
               '-1': 'SNSNEW: Refused'},
    # Science News
    'SNSTRUST': {'1': "I mostly trust the posts I see on social media about science",
                 '2': "I mostly distrust the posts I see on social media about science",
                 ' ': 'SNSTRUST: Not Asked',
                 '-1': 'SNSTRUST: Refused'},
    # Media
    'PROBSET_a': {1.0: 'The news media are too quick to report research findings that may not hold up is a big problem',
                  2.0: 'The news media are too quick to report research findings that may not hold up is a small problem',
                  3.0: 'The news media are too quick to report research findings that may not hold up is not a problem'},
    # Media
    'PROBSET_b': {1.0: 'The news media cover too many research findings that are not really important is a big problem',
                  2.0: 'The news media cover too many research findings that are not really important is a small problem',
                  3.0: 'The news media cover too many research findings that are not really important is not a problem'},
    # Media
    'PROBSET_c': {1.0: 'There are so many research studies it\'s hard to distinguish between high and low quality is a big problem',
                  2.0: 'There are so many research studies it\'s hard to distinguish between high and low quality is a small problem',
                  3.0: 'There are so many research studies it\'s hard to distinguish between high and low quality is not a problem'},
    # Media
    'PROBSET_d': {1.0: 'The public jumps to conclusions about how to apply new research findings to their lives is a big problem',
                  2.0: 'The public jumps to conclusions about how to apply new research findings to their lives is a small problem',
                  3.0: 'The public jumps to conclusions about how to apply new research findings to their lives is not a problem'},
    # Media
    'PROBSET_e': {1.0: 'The public doesn\'t know enough about science to really understand research findings covered in news is a big problem',
                  2.0: 'The public doesn\'t know enough about science to really understand research findings covered in news is a small problem',
                  3.0: 'The public doesn\'t know enough about science to really understand research findings covered in news is not a problem'},
    # Media
    'PROBSET_f': {1.0: 'The news media oversimplifies scientific research findings is a big problem',
                  2.0: 'The news media oversimplifies scientific research findings is a small problem',
                  3.0: 'The news media oversimplifies scientific research findings is not a problem'},
    # Media
    'PROBSET_g': {1.0: 'Science researchers overstate the implications of their findings is a big problem',
                  2.0: 'Science researchers overstate the implications of their findings is a small problem',
                  3.0: 'Science researchers overstate the implications of their findings is not a problem'},
    # Media
    'PROBSET_h': {1.0: 'The news media are too quick to report on disagreement about research findings is a big problem',
                  2.0: 'The news media are too quick to report on disagreement about research findings is a small problem',
                  3.0: 'The news media are too quick to report on disagreement about research findings is not a problem'},
    # Media
    'BLAME': {1.0: 'The way news reporters cover scientific research findings is a bigger problem than the way science researchers publish new findigns',
              2.0: 'The way science researchers publish/share their new findings is a bigger problem than the way news reporters cover findings'},
    # Science News
    'DISCUSS': {1.0: 'I discuss science news with others nearly every day',
                2.0: 'I discuss science news with others a few times a week',
                3.0: 'I discuss science news with others a few times a month',
                4.0: 'I discuss science news with others less often than few times a month'},
    # Science News
    'LEAD': {'1': "I tend to listen to the conversation about science news more than lead",
             '2': "I tend to lead the conversation about science news more than listen",
             ' ': 'LEAD: Not Asked',
             '-1': 'LEAD: Refused'},
    # Science News
    'TURN': {'1': "I tend to listen to turn to others for science news",
             '2': "People tend to turn to me for science news",
             ' ': 'TURN: Not Asked',
             '-1': 'TURN: Refused'},
    # Other
    'ENTCRIM1': {1.0: 'I often watch entertainment programs on CRIMINAL INVESTIGATIONS',
                 2.0: 'I sometimes watch entertainment programs on CRIMINAL INVESTIGATIONS',
                 3.0: 'I hardly ever watch entertainment programs on CRIMINAL INVESTIGATIONS',
                 4.0: 'I never watch entertainment programs on CRIMINAL INVESTIGATIONS'},

    'ENTCRIM1_t2b': {1: 'I typically watch entertainment programs on CRIMINAL INVESTIGATIONS',
                     2: 'I typically don\'t watch entertainment programs on CRIMINAL INVESTIGATIONS'},

    # Other
    'ENTCRIM2': {1.0: 'CRIMINAL INVESTIGATION shows generally portray science, tech & medicine in a realistic way',
                 2.0: 'CRIMINAL INVESTIGATION shows focus on entertainment more than getting the science, tech & medicine right'},
    # Other
    'ENTCRIM3': {1.0: 'Watching CRIMINAL INVESTIGATION shows helps my understanding of science, tech & medicine',
                 2.0: 'Watching CRIMINAL INVESTIGATION shows hurts my understanding of science, tech & medicine',
                 3.0: 'Watching CRIMINAL INVESTIGATION shows makes no difference in understanding of science, tech & medicine'},
    # Other
    'ENTCRIM4': {1.0: 'CRIMINAL INVESTIGATION shows give a favorable impression of working in science, tech & medicine',
                 2.0: 'CRIMINAL INVESTIGATION shows gives an unfavorable impression of working in science, tech & medicine',
                 3.0: 'CRIMINAL INVESTIGATION shows give a neutral impression of working in science, tech & medicine'},
    # Other
    'ENTHOSP1': {1.0: 'I often watch entertainment programs on HOSPITALS AND MEDICAL SETTINGS',
                 2.0: 'I sometimes watch entertainment programs on HOSPITALS AND MEDICAL SETTINGS',
                 3.0: 'I hardly ever watch entertainment programs on HOSPITALS AND MEDICAL SETTINGS',
                 4.0: 'I never watch entertainment programs on HOSPITALS AND MEDICAL SETTINGS'},

    'ENTHOSP1_t2b': {1: 'I typically watch entertainment programs on HOSPITALS AND MEDICAL SETTINGS',
                     2: 'I typically don\'t watch entertainment programs on HOSPITALS AND MEDICAL SETTINGS'},

    # Other
    'ENTHOSP2': {1.0: 'HOSPITALS AND MEDICAL SETTINGS shows generally portray science, tech & medicine in a realistic way',
                 2.0: 'HOSPITALS AND MEDICAL SETTINGS shows focus on entertainment more than getting the science, tech & medicine right'},
    # Other
    'ENTHOSP3': {1.0: 'Watching HOSPITALS AND MEDICAL SETTINGS shows helps my understanding of science, tech & medicine',
                 2.0: 'Watching HOSPITALS AND MEDICAL SETTINGS shows hurts my understanding of science, tech & medicine',
                 3.0: 'Watching HOSPITALS AND MEDICAL SETTINGS shows makes no difference in understanding of science, tech & medicine'},
    # Other
    'ENTHOSP4': {1.0: 'HOSPITALS AND MEDICAL SETTINGS shows give a favorable impression of working in science, tech & medicine',
                 2.0: 'HOSPITALS AND MEDICAL SETTINGS shows gives an unfavorable impression of working in science, tech & medicine',
                 3.0: 'HOSPITALS AND MEDICAL SETTINGS shows give a neutral impression of working in science, tech & medicine'},
    # Other
    'ENTSCIFI1': {1.0: 'I often watch entertainment programs on SCIENCE FICTION',
                  2.0: 'I sometimes watch entertainment programs on SCIENCE FICTION',
                  3.0: 'I hardly ever watch entertainment programs on SCIENCE FICTION',
                  4.0: 'I never watch entertainment programs on SCIENCE FICTION'},

    'ENTSCIFI1_t2b': {1: 'I typically watch entertainment programs on SCIENCE FICTION',
                      2: 'I typically don\'t watch entertainment programs on SCIENCE FICTION'},

    # Other
    'ENTSCIFI2': {1.0: 'SCIENCE FICTION shows generally portray science, tech & medicine in a realistic way',
                  2.0: 'SCIENCE FICTION shows focus on entertainment more than getting the science, tech & medicine right'},
    # Other
    'ENTSCIFI3': {1.0: 'Watching SCIENCE FICTION shows helps my understanding of science, tech & medicine',
                  2.0: 'Watching SCIENCE FICTION shows hurts my understanding of science, tech & medicine',
                  3.0: 'Watching SCIENCE FICTION shows makes no difference in understanding of science, tech & medicine'},
    # Other
    'ENTSCIFI4': {1.0: 'SCIENCE FICTION shows give a favorable impression of working in science, tech & medicine',
                  2.0: 'SCIENCE FICTION shows gives an unfavorable impression of working in science, tech & medicine',
                  3.0: 'SCIENCE FICTION shows give a neutral impression of working in science, tech & medicine'},
    # Science News
    'HOBBY': {1.0: 'I have science-related hobbies, interests or activities outside of work',
              2.0: 'I do not have science-related hobbies, interests or activities outside of work'},

    # Demographic
    'PARTY': {1.0: 'I consider myself a Republican',
              2.0: 'I consider myself a Democrat',
              3.0: 'I consider myself an Independent',
              4.0: 'I consider myself a different party'},

    # Demographic
    'PARTYLN': {'1': "I tend to lean more to the Republican Party",
                '2': "I tend to lean more to the Democratic Party",
                ' ': 'PARTYLN: Not Asked',
                '-1': 'PARTYLN: Refused'},
    # Demographic
    'IDEO': {1.0: 'My political views are Very Conservative',
             2.0: 'My political views are Conservative',
             3.0: 'My political views are Moderate',
             4.0: 'My political views are Liberal',
             5.0: 'My political views are Very Liberal'},
    # Demographic
    'xparent': {1: "I am the parent of a 0-17 year old",
                2: "I am not the parent of a 0-17 year old"},
    # Demographic
    'IND1': {1.0: 'Industry: other',
             16.0: 'Industry: Health Care & Social Assistance',
             15.0: 'Industry: Educational Services',
             12.0: 'Industry: Professional, Scientific & Technical services',
             7.0: 'Industry: Retail Trade',
             5.0: 'Industry: Manufacturing',
             19.0: 'Industry: Other Services & Community/Non-Profit Organizations',
             10.0: 'Industry: Finance and Insurance',
             4.0: 'Industry: Construction',
             18.0: 'Industry: Accommodation & Food Services',
             8.0: 'Industry: Transportation & Warehousing',
             9.0: 'Industry: Information',
            -2.0: 'IND1: Not Asked'},
    # Demographic
    'DOV_PPP20072': {1.0: 'I attend religious services more than once a week',
                     2.0: 'I attend religious services once a week',
                     3.0: 'I attend religious services once or twice a month',
                     4.0: 'I attend religious services a few times a year',
                     5.0: 'I attend religious services once a year or less',
                     6.0: 'I never attend religious services'},
    # Demographic
    'DOV_PPC10017': {1.0: 'I own a smartphone',
                     2.0: 'I don\'t use a smartphone',
                     3.0: 'I don\'t know if I use a smartphone',
                     4.0: 'Not asked/dont use a cellphone'},
    # Demographic
    'DOV_PPC20217': {1: "Use a cellphone/smartphone for internet",
                     2: "Use a desktop computer for internet",
                     3: "Use a laptop computer for internet",
                     4: "Use Netbook for internet",
                     5: "Use a tablet for internet",
                     6: "Use another device for internet"},
    # Demographic
    'DOV_PPC21501': {1.0: 'I own a desktop computer',
                     2.0: 'I own a laptop/notebook computer',
                     3.0: 'I own both a desktop and laptop computer',
                     4.0: 'I don\'t own a desktop/laptop computer',
                     5.0: 'I don\'t know if I own a desktop/laptop computer',
                     6.0: 'Not asked: don\'t have desktop/laptop in HH'},
    # Demographic
    'DOV_PPC11518': {1: "I own an Apple iPad",
                     2: "I own another type of tablet",
                     3: "I don't own a tablet",
                     4: "I don't know/not sure if I own a tablet",
                     6: "I own an Android tablet",
                     7: "I own a Microsoft Surface",
                     9: "Not asked: don't have a tablet in HH"},
    # Demographic
    'ppagecat': {1: "18-24 years old",
                 2: "25-34 years old",
                 3: "35-44 years old",
                 4: "45-54 years old",
                 5: "55-64 years old",
                 6: "65-74",
                 7: "75+"},

    'ppagecat_short': {1: "18-34 years old",
                       2: "35-54 years old",
                       3: "55-74 years old",
                       4: "75+"},

    # Demographic
    'PPEDUCAT': {1: "Completed less than HS education",
                 2: "Completed HS education",
                 3: "Completed some college education",
                 4: "Completed Bachelors degree or higher"},
    # Demographic
    'PPETHM': {1: "White, non-hispanic",
               2: "Black, non-hispanic",
               3: "Other, non-hispanic",
               4: "Hispanic",
               5: "2+ races, non-hispanic"},
    # Demographic
    'PPGENDER': {1: "Male",
                 2: "Female"},
    # Demographic
    'PPHHSIZE': {1: "HH Size: 1",
                 2: "HH Size: 2",
                 3: "HH Size: 3",
                 4: "HH Size: 4",
                 5: "HH Size: 5",
                 6: "HH Size: 6+"},
    # Demographic
    'PPHOUSE': {1: "Live in a one-family house detached from other houses",
                2: "Live in a one-family house attached to one or more houses",
                3: "Live in a building with 2 or more apartments",
                4: "Live in a mobile home",
                5: "Live in a boat, RV, van, etc."},
    # Demographic
    'PPINCIMP': {1.0: '<$20,000',
                2.0: '$20,000 - $40,000',
                3.0: '$40,000 - $60,000',
                4.0: '$60,000 - $85,000',
                5.0: '$85,000 - $125,000',
                6.0: '$125,000 - $175,000',
                7.0: '$175,000 - $200,000',
                8.0: '$200,000+'},
    # Demographic
    'PPMARIT': {1: "Married",
                2: "Widowed",
                3: "Divorced",
                4: "Separated",
                5: "Never Married",
                6: "Living with partner"},
    # Demographic
    'PPREG4': {1: "Northeast Region",
               2: "Midwest Region",
               3: "South Region",
               4: "West Region"},
    # Demographic
    'PPRENT': {1: "Home Ownership: Own or bought by someone in HH",
               2: "Home Ownership: Rented for cash",
               3: "Occupied without payment of cash rent"},
    # Demographic
    'PPWORK': {1: "Working- as paid employee",
                2: "Working- self employed",
                3: "Not working- temporary layoff from a job",
                4: "Not working- looking for work",
                5: "Not working- retired",
                6: "Not working- disabled",
                7: "Not working- other"},
    # Demographic
    'Segment': {0: "SEGMENT 0",
                1: "SEGMENT 1",
                2: "SEGMENT 2",
                3: "SEGMENT 3",
                4: "SEGMENT 4",
                5: "SEGMENT 5",
                6: "SEGMENT 6",
                7: "SEGMENT 7",
                8: "SEGMENT 8"}
    }

    ## Other column names (not dummy)
    column_names = {
    "MUSEUM_a": 'Visited zoo',
    "MUSEUM_b": 'Visited art museum',
    "MUSEUM_c": 'Visited natural history museum',
    "MUSEUM_d": 'Visited science/tech center/museum',
    "MUSEUM_e": 'Visited national, state or country park',
    "MUSEUM_f": 'Visited public library',
    "MUSEUM_g": 'Attended event with live music',
    "MUSEUM_h": 'Attended sport event',
    "MUSEUM_i": 'Attended science lecture/talk',
    "MUSEUM_j": "Didn't visit musuem",
    "MUSEUM_Refused": "MUSEUM: Refused",
    "TOPICS2_a": "Interested in health & medicine",
    "TOPICS2_b": "Interested in technology",
    "TOPICS2_c": "Interested in energy and environment",
    "TOPICS2_d": "Interested in food and nutrition",
    "TOPICS2_e": "Interested in space and astronomy",
    "TOPICS2_f": "Interested in evolution of human & animals",
    "TOPICS2_g": "Interested in the mind and brain",
    "TOPICS2_h": "Interested in other",
    "TOPICS2_i": "Not interested in any of these science topics",
    "TOPICS2_Refused": "TOPICS2: Refused",
    "SOURCE3_a": "Get science news regularly from news outlets that cover a range of topics",
    "SOURCE3_b": "Get science news regularly from documentaries or other science video programns",
    "SOURCE3_c": "Get science news regularly from science magazines (print/online)",
    "SOURCE3_d": "Get science news regularly from online discussion forums about science",
    "SOURCE3_e": "Get science news regularly from science podcasts or radio programs",
    "SOURCE3_f": "Get science news regularly from family, friends and acquaintances",
    "SOURCE3_g": "Get science news regularly from government agencies",
    "SOURCE3_h": "Get science news regularly from advocacy organizations",
    "SOURCE3_i": "Get science news regularly from science and tech centers",
    "SOURCE3_j": "Get science news regularly from other websites/blogs focused on science",
    "SOURCE3_k": "Get science news regularly from none of the above",
    "SOURCE3_Refused": "SOURCE3: Refused",
    "STORIES_a": "I watch/read/listen to news stories that report new scientific discoveries",
    "STORIES_b": "I watch/read/listen to news stories that report scientific info that helps make decisions about everyday life",
    "STORIES_c": "I watch/read/listen to news stories that report disagreement among scientific experts",
    "STORIES_d": "I watch/read/listen to news stories that report scientific research findings that conflict with earlier research findings on same topic",
    "STORIES_e": "I watch/read/listen to news stories that report strange or weird scientific research findings",
    "STORIES_f": "I watch/read/listen to news stories that report scientific research findings that seem completely made up",
    "STORIES_g": "I watch/read/listen to news stories that report stories about a science researcher's misconduct",
    "STORIES_h": "I don't watch/read/listen to news stories that report any of the above",
    "STORIES_Refused": "STORIES: Refused",
    "SNSPOST_a": 'I see social media posts about new scientific discoveries',
    "SNSPOST_b": 'I see social media posts about scientific information that helps you make decisions about everyday life',
    "SNSPOST_c": 'I see social media posts about disagreements among scientific experts',
    "SNSPOST_d": 'I see social media posts about scientific research findings that conflict with earlier research findings on the same topic',
    "SNSPOST_e": 'I see social media posts about strange or weird scientific research findings',
    "SNSPOST_f": 'I see social media posts about scientific research findings that seem completely made up',
    "SNSPOST_g": "I see social media posts about sotires about a science researcher's misconduct",
    "SNSPOST_h": "I see social media posts about stories I disagree with",
    "SNSPOST_i": 'I see social media posts about celebrities providing health or medical advice',
    "SNSPOST_j": "I don't see social media posts about the above",
    "SNSCHECK1_a": "I have commented on a story in response to a social media post about scientific findings that seemed completely made up",
    "SNSCHECK1_b": "I have searched for more information about a story in response to a social media post about scientific findings that seemed completely made up",
    "SNSCHECK1_c": "I have shared the story to show it's wrong in response to a social media post about scientific findings that seemed completely made up",
    "SNSCHECK1_d": "I have ignored or hid a story in response to a social media post about scientific findings that seemed completely made up",
    "SNSCHECK1_e": "I have unfollowed/blocked the person the story came from in response to a social media post about scientific findings that seemed completely made up",
    "SNSCHECK1_f": "I have searched for mode information about a story in response to a social media post about scientific findings that seemed completely made up",
    "SNSCHECK1_Refused": "I have done none of the above in response to a social media post about scientific findings that seemed completely made up",
    "SNSCHECK2_a": "I have commented on a story in response to a social media post about scientific findings that I disagreed with",
    "SNSCHECK2_b": "I have searched for more information about a story in response to a social media post about scientific findings that I disagreed with",
    "SNSCHECK2_c": "I have shared the story to show it's wrong in response to a social media post about scientific findings that I disagreed with",
    "SNSCHECK2_d": "I have ignored or hid a story in response to a social media post about scientific findings that I disagreed with",
    "SNSCHECK2_e": "I have unfollowed/blocked the person the story came from in response to a social media post about scientific findings that I disagreed with",
    "SNSCHECK2_f": "I have searched for mode information about a story in response to a social media post about scientific findings that I disagreed with",
    "SNSCHECK2_Refused": "I have done none of the above in response to a social media post about scientific findings that I disagreed with",
    "LIST1_a": 'I have participated in a medical or clinical research study',
    "LIST1_b": 'I have made observations or collected data samples as part of a science research project',
    "LIST1_c": 'I have contributed to a science-related online crowdsourcing activity',
    "LIST1_d": 'I have helped a child with a science project whether for school or for an outside school activity',
    "LIST1_e": 'I have participated in a maker movement or hack-a-thon event to develop new technologies',
    "LIST1_f": 'I have donated blood',
    "LIST1_g": 'I have donated money to support medical or science research',
    "LIST1_Refused": 'LIST1: Refused',
    "POLSOURCE1_1": 'I regularly get news from ABC news about GOVERNMENT AND POLITICS',
    "POLSOURCE1_2": 'I regularly get news from CBS news about GOVERNMENT AND POLITICS',
    "POLSOURCE1_3": 'I regularly get news from NBC news about GOVERNMENT AND POLITICS',
    "POLSOURCE1_4": 'I regularly get news from Business Insider about GOVERNMENT AND POLITICS',
    "POLSOURCE1_5": 'I regularly get news from Vox about GOVERNMENT AND POLITICS',
    "POLSOURCE1_6": 'I regularly get news from Independent Journal Review (IJR) about GOVERNMENT AND POLITICS',
    "POLSOURCE1_99": 'I don\'t regularly get news from any of the above about GOVERNMENT AND POLITICS',
    "POLSOURCE1_Refused": 'POLSOURCE1: Refused',
    "POLSOURCE2_1": 'I regularly get news from PBS news about GOVERNMENT AND POLITICS',
    "POLSOURCE2_2": 'I regularly get news from Politico about GOVERNMENT AND POLITICS',
    "POLSOURCE2_3": 'I regularly get news from International Business Times about GOVERNMENT AND POLITICS',
    "POLSOURCE2_4": 'I regularly get news from Slate about GOVERNMENT AND POLITICS',
    "POLSOURCE2_5": 'I regularly get news from Los Angeles Times about GOVERNMENT AND POLITICS',
    "POLSOURCE2_99": 'I don\'t regularly get news from any of the above about GOVERNMENT AND POLITICS',
    "POLSOURCE2_Refused": 'POLSOURCE1: Refused',
    "PPMSACAT": 'Live in metro area'}

    dummy_columns = ['LIFE', 'TOPICINT_a', 'TOPICINT_b', 'TOPICINT_c',
                    'TOPICINT_d', 'TOPICINT_e', 'TOPICINT_f',
                    'TOPICINT_a_t2b', 'TOPICINT_b_t2b', 'TOPICINT_c_t2b',
                    'TOPICINT_d_t2b', 'TOPICINT_e_t2b', 'TOPICINT_f_t2b',
                    'SCIOFTEN', 'TOPICS1', 'TOPICMOST', 'SOURCE1',
                    'SOURCE2', 'ENJOY', 'KNOWLEDGE', 'SEEK', 'SOURCEALT',
                    'SCIWHY_a', 'SCIWHY_b', 'SCIWHY_c', 'SCIWHY_d', 'SCIWHY_e',
                    'SCIWHY_f', 'SCIWHY_g', 'WHYNOT_a', 'WHYNOT_b', 'WHYNOT_c',
                    'WHYNOT_d', 'WHYNOT_e', 'WHYNOT_f', 'WHYNOT_g', 'WHYNOT_h',
                    'NEWSJOB', 'NEWSFACTS_a', 'NEWSFACTS_b', 'NEWSFACTS_c', 'NEWSFACTS_d',
                    'NEWSFACTS_e', 'NEWSFACTS_f', 'NEWSFACTS_g', 'NEWSFACTS_h', 'NEWSFACTS_i',
                    'NEWSFACTS_a_t2b', 'NEWSFACTS_b_t2b', 'NEWSFACTS_c_t2b', 'NEWSFACTS_d_t2b',
                    'NEWSFACTS_e_t2b', 'NEWSFACTS_f_t2b', 'NEWSFACTS_g_t2b', 'NEWSFACTS_h_t2b', 'NEWSFACTS_i_t2b',
                    'SNSUSE', 'SNSFREQ', 'FOLLOW', 'FOLLOWANTI', 'SNSSCI', 'SNSCLICK', 'SNSSCIIMP',
                    'SNSNEW', 'SNSTRUST', 'PROBSET_a', 'PROBSET_b', 'PROBSET_c', 'PROBSET_d',
                    'PROBSET_e', 'PROBSET_f', 'PROBSET_g', 'PROBSET_h', 'BLAME', 'DISCUSS',
                    'LEAD', 'TURN', 'ENTCRIM1', 'ENTCRIM1_t2b', 'ENTCRIM2', 'ENTCRIM3', 'ENTCRIM4',
                    'ENTHOSP1', 'ENTHOSP1_t2b', 'ENTHOSP2', 'ENTHOSP3', 'ENTHOSP4',
                    'ENTSCIFI1', 'ENTSCIFI1_t2b', 'ENTSCIFI2', 'ENTSCIFI3', 'ENTSCIFI4',
                    'HOBBY', 'PARTY', 'PARTYLN', 'IDEO', 'xparent', 'IND1',
                    'DOV_PPP20072', 'DOV_PPC10017', 'DOV_PPC20217',
                    'DOV_PPC21501', 'DOV_PPC11518', 'ppagecat', 'ppagecat_short',
                    'PPEDUCAT', 'PPETHM', 'PPGENDER', 'PPHHSIZE',
                    'PPHOUSE', 'PPINCIMP', 'PPMARIT', 'PPREG4',
                    'PPRENT', 'PPWORK', 'Segment']

    return dummy_column_names, column_names, dummy_columns
