from training import models

training_name = "speed_evolution"
cycle_number = 1
session_number = 10
number_of_drill = 5
number_of_set = 1
number_of_rep = 4
rest_time = "00:01:00"
description = "If you are on your own, complete four to five sets of each exercise. Do all sets of one exercise before moving on to the next, taking no more than one minute rest in between sets. If you have a partner or group of up to 12 (such as a club soccer team), you can set up each drill in the gym, a studio space, or outside. Put two people in each station and work through the drills as a circuit."

for x in range(number_of_drill):
    reel_number = x + 1
    models.TrainingExercises.objects.create(name="drill " + str(reel_number), level=1, rest_time=rest_time,
                                            number_of_repetition=number_of_rep, number_of_set=number_of_set,
                                            image="video_compress/" + training_name + "/cycle_" + str(
                                                cycle_number) + "_session_" + str(session_number) + "/drill_" + str(
                                                reel_number) + ".jpeg",
                                            video="video_compress/" + training_name + "/cycle_" + str(
                                                cycle_number) + "_session_" + str(session_number) + "/drill_" + str(
                                                reel_number) + ".mp4")


    res = models.TrainingExercises.objects.all()
    res.update(description=description)