from big_sleep import Imagine
import os

brain = os.getcwd()

mind = ['string 1',
        'string 2']

for thought in mind:
    anthought = ''.join(char for char in thought if char.isalnum())
    if not os.path.exists(brain + "/" + anthought):
        os.makedirs(brain + "/" + anthought)
        
    os.chdir(brain + "/" + anthought)

    dream = Imagine(
    text = thought,
    save_progress = True
    )

    dream()

