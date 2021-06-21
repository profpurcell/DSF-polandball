# 4/12/21
# Country Frequencies
# Create new df to isolate country frequencies
# Think we can adjust this to create a dataset with country connected to sub_id
# But focusing on raw frequencies first

# Sources:
# Try this: https://stackoverflow.com/questions/38709423/python-pandas-split-slash-separated-strings-in-two-or-more-columns-into-multipl
# For NLP, try this: https://stackoverflow.com/questions/58120996/text-analysis-finding-the-most-common-word-in-a-column-using-python

import pandas as pd
import nltk
from collections import Counter

df_merged = pd.read_csv("C:/Users/carson/Documents/DSF-polandball/FINALPolandballSubmissionsData.csv")

country_s1 = df_merged.mod_countries_ocr.str.split('/', expand=True).stack()

#country_df = country_s1.to_frame()
country_df = pd.DataFrame(country_s1, columns = ['countries'])
#print(country_df[:15])


#print(sorted(country_df))

# get frequency using counter
# count the number of distinct country names
distinct_count = Counter()
country_df['countries'].replace(' ', '-')
country_df['countries'].str.split().apply(distinct_count.update)
#print(distinct_count)

df_country_counter = pd.DataFrame.from_dict(distinct_count, orient='index').reset_index()
print(df_country_counter[:10])

df_country_counter.to_csv("polandballCountryCountOCR.csv", index=False, encoding='utf-8-sig')


# TODO
# Add distinct_count as its own column?

# FIXME 
# I'm not sure if I need to do all of this get frequency
# Maybe just use distinct_count?



# Note:
    # The following code is included for educational/comparison purposes

#FIXME 
    # I tried to isolate country names in the mod_countries_comments column:
# mod_countries_comments:
#country_s2 = df_merged.mod_countries_comments.str.split('/', expand=True).stack()
#distinct_count2 = Counter()
#country_df2['countries'].str.lower().str.split().apply(distinct_count.update)
#print(distinct_count2)

#FIXME
    # This is some standard NLP code
    # I found a simpler way, but I think it is interesting to compare

# Get frequency using nltk:
# replace all non-alphanumeric characters
#country_df['sub_rep'] = country_df.countries.str.lower().str.replace('\W', ' ')

# tokenize
#country_df['tok'] = country_df.sub_rep.apply(nltk.tokenize.word_tokenize)

# all tokenized words to a list
#words = country_df.tok.tolist()  # this is a list of lists
#words = [word for list_ in words for word in list_]

# frequency distribution
#word_dist = nltk.FreqDist(words)

#top_N = 50

#result = pd.DataFrame(word_dist.most_common(top_N), columns=['Word', 'Frequency'])
#print(result[:10])