from big_sleep import Imagine
import os

brain = os.getcwd()

mind = ['string 1',
        'string 2']

for thought in mind:
    if not os.path.exists(brain + "/" + thought):
        os.makedirs(brain + "/" + thought)
        
    os.chdir(brain + "/" + thought)

    dream = Imagine(
    text = thought,
    save_progress = True
    )

    dream()
