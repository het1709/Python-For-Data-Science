# Uses a predefined data set of users and movies to generate movie recommendations for a particular user.
# Uses the 100k MovieLens database and the LightFM package

import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#fetches and formats the data from dataset
data = fetch_movielens()

#training data - data['train']
#testing data - data['test']

#create a model for recommendations
model = LightFM(loss='warp')

#train the model with the training data
model.fit(data['train'], epochs=30, num_threads=2)

def recommendation(model, data, user_ids):
    #no. of users and movies in the training data
    num_users, num_movies = data['train'].shape

    #generate recommendation for each user in the user_ids array
    for user in user_ids:
        #movies they like
        liked_movies = data['item_labels'][data['train'].tocsr()[user].indices]

        #predicted movies
        predicted = model.predict(user, np.arange(num_movies))
        #rank them from most liked to least
        ranked = data['item_labels'][np.argsort(-predicted)]

        #print the results
        print('User: %s' % user)
        print('Liked movies: ')
        for x in liked_movies[:3]:
            print('             %s' % x)
        print('Recommended:')
        for x in ranked[:3]:
            print('             %s' % x)
        print('')

#Call the above function
num = int(input('Enter the number of users you want recommendations for: '))
print('Enter the IDs of the users: ')
array = []
for i in range(0, num):
    id = int(input(''))	
    array.append(id)
recommendation(model, data, array)
