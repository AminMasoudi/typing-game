from django.contrib.auth.models import User

from string import ascii_letters
from random import choices

from .models import Profile


def random(k):
    my_list = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Cras tincidunt lobortis feugiat vivamus at augue eget arcu dictum. Interdum velit euismod in pellentesque massa placerat duis ultricies. Id cursus metus aliquam eleifend mi in nulla. Purus faucibus ornare suspendisse sed nisi lacus. Enim lobortis scelerisque fermentum dui faucibus. At urna condimentum mattis pellentesque id nibh tortor id aliquet. Elementum pulvinar etiam non quam. Fermentum odio eu feugiat pretium nibh ipsum consequat nisl vel. In metus vulputate eu scelerisque felis. Ac feugiat sed lectus vestibulum mattis ullamcorper velit sed ullamcorper. Felis eget velit aliquet sagittis id consectetur purus ut. Massa tempor nec feugiat nisl pretium fusce id velit. Sed felis eget velit aliquet sagittis id consectetur purus ut. Ipsum a arcu cursus vitae congue mauris rhoncus aenean. Molestie nunc non blandit massa. Vel risus commodo viverra maecenas. Egestas dui id ornare arcu odio ut sem nulla. Aliquam sem fringilla ut morbi. Ornare arcu odio ut sem nulla. Commodo nulla facilisi nullam vehicula ipsum a arcu. Mus mauris vitae ultricies leo integer malesuada nunc. Dui sapien eget mi proin sed libero. Imperdiet massa tincidunt nunc pulvinar sapien et. Mattis pellentesque id nibh tortor id aliquet lectus. Dignissim suspendisse in est ante.

    Proin libero nunc consequat interdum varius sit amet mattis. Eget sit amet tellus cras adipiscing enim eu turpis egestas. Gravida rutrum quisque non tellus orci ac auctor augue mauris. In pellentesque massa placerat duis ultricies. Elementum curabitur vitae nunc sed velit dignissim sodales. Faucibus interdum posuere lorem ipsum dolor sit. Quis lectus nulla at volutpat diam ut venenatis. Congue quisque egestas diam in arcu. Ac turpis egestas integer eget. Auctor urna nunc id cursus metus aliquam eleifend mi in. Tortor id aliquet lectus proin nibh nisl condimentum id venenatis. Diam ut venenatis tellus in. Volutpat ac tincidunt vitae semper quis lectus nulla.

    Sed tempus urna et pharetra pharetra massa massa ultricies. Lectus magna fringilla urna porttitor rhoncus dolor purus. Tortor aliquam nulla facilisi cras. Montes nascetur ridiculus mus mauris vitae ultricies leo. Facilisi cras fermentum odio eu feugiat. Vel pharetra vel turpis nunc eget lorem dolor. Eu consequat ac felis donec et odio pellentesque diam volutpat. Ultricies lacus sed turpis tincidunt id aliquet risus feugiat. Proin sagittis nisl rhoncus mattis. Varius sit amet mattis vulputate enim nulla aliquet. Aliquam ut porttitor leo a diam sollicitudin tempor id. In dictum non consectetur a erat nam at. Sapien pellentesque habitant morbi tristique senectus et netus et. Ac orci phasellus egestas tellus rutrum tellus pellentesque eu tincidunt. Morbi tristique senectus et netus et malesuada fames ac turpis.

    Molestie a iaculis at erat pellentesque adipiscing commodo. Adipiscing tristique risus nec feugiat in. Ut faucibus pulvinar elementum integer enim neque. Ultrices mi tempus imperdiet nulla malesuada pellentesque elit eget gravida. Tellus at urna condimentum mattis pellentesque id. Rhoncus aenean vel elit scelerisque mauris. Arcu cursus vitae congue mauris rhoncus. Enim facilisis gravida neque convallis. Tristique senectus et netus et. Convallis a cras semper auctor neque vitae tempus quam. Volutpat blandit aliquam etiam erat velit scelerisque in. Id semper risus in hendrerit gravida rutrum quisque non. Et tortor consequat id porta nibh venenatis cras. Eget sit amet tellus cras adipiscing enim eu turpis.

    Duis ut diam quam nulla porttitor. Egestas congue quisque egestas diam in arcu. Donec et odio pellentesque diam. Pulvinar sapien et ligula ullamcorper. Nec sagittis aliquam malesuada bibendum. Bibendum est ultricies integer quis auctor. Odio ut sem nulla pharetra diam. Sed velit dignissim sodales ut eu sem integer. Neque vitae tempus quam pellentesque nec nam aliquam. Faucibus nisl tincidunt eget nullam. Et molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. At varius vel pharetra vel turpis nunc eget lorem. Nibh sit amet commodo nulla facilisi nullam vehicula. Eget arcu dictum varius duis at.""".split()
    
    my_list += list(ascii_letters)
    random_choices = choices(my_list, k=k)
    secuense = " ".join(random_choices)
    return secuense, random_choices



def calculate(seq, original_seq):
    score = 0
    seq = seq.split()
    original_seq = original_seq.split()
    for i in range(len(original_seq)):
        try:
            if seq[i] == original_seq[i]:
                score += 1
            else:
                score -= 1
        except:
            score -= 1
    return score



def create_user(username, password, *, score):
    user = User.objects.create_user(username=username,
                             password=password)
    Profile.objects.create(user=user)

    return user