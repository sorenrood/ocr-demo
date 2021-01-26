import pandas as pd
import plotly.express as px

# data = {
#     'positive': [1],
#     'negative': [4],
#     'neutral': [7],
#     'date': ['jan-1']
# }

data = {
    'sentiscore': [4, 2, 6, 7, 3, 8, 5, 4],
    'date': ['jan-1', 'jan-2', 'jan-2', 'jan-3', 'jan-4', 'jan-5', 'jan-6', 'jan-7']
}

df = pd.DataFrame(data, columns=['sentiscore', 'date'])

print(df)

fig = px.bar(data, x='date', y='sentiscore', title='Ocular Sentiment Analysis Library Chart')
fig.show()