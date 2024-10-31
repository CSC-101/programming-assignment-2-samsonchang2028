import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1:data.Point,point2:data.Point)->data.Rectangle:
    x1=min(point1.x,point2.x)
    y1= max(point1.y,point2.y)
    topleft = data.Point(x1,y1) #the top left of a rectangle needs the smallest x value but the biggest y value
    x2 = max(point1.x,point2.x)
    y2= min(point1.y,point2.y)
    bottomright = data.Point(x2,y2)# the bottom right of a rectangle needs the smallest y value and the biggest x value
    return data.Rectangle(topleft,bottomright)

# Part 2
def shorter_duration_than(time1:data.Duration,time2:data.Duration)->bool:
    if time1.minutes < time2.minutes: # if the minutes value is bigger, then the time duration will be bigger, this checks if
        #time1 is less than time2
        return True
    elif time1.minutes == time2.minutes:# if the minutes are the same, this compares time1's seconds and time2's to see
        #which is bigger
        if time1.seconds < time2.seconds:
            return True
    else:
        return False

# Part 3
def songs_shorter_than(song_list:list[data.Song],song_length:data.Duration)->list[data.Song]:
   new_song_list = [] #creates a new list for the songs that will be less than said time
   for song in song_list:
        if song.duration.minutes < song_length.minutes: # checks the same as before in part 2,  if the minutes value is bigger, then
        # the time duration will be bigger, this checks if
        #the songs in the list are less than the upperbound duration
            new_song_list.append(song) # adds teh song to the new list if it's smaller than said duration
        elif song.duration.minutes == song_length.minutes: # checks the seconds to see if the song is within the upper bound
            if song.duration.seconds < song_length.seconds:
                new_song_list.append(song)
   return new_song_list
    # return [songs for songs in song_list if songs.duration < song_length]


# Part 4
def running_time(song_list:list[data.Song],number:list[int])->data.Duration:
    minutes = 0
    seconds =0
    duration = data.Duration(minutes, seconds)
    for i in number:
        duration.minutes = duration.minutes + song_list[number[i]].duration.minutes
        duration.seconds = duration.seconds + song_list[number[i]].duration.seconds #adds the seconds and minutes together from the list
        if duration.seconds > 60: # if the secodns value is bigger than 60, adds 1 to minute and resets back value- 60
            duration.minutes = duration.minutes + 1
            duration.seconds = duration.seconds - 60

            print(duration)
    return duration
# Part 5
def validate_route(city_links:list[list[str]],city_names_route:list[str])->bool:
    for i in range(len(city_names_route) - 1):
        city1 = city_names_route[i] #first in the citynamesroute list
        city2 = city_names_route[i+1] #second in the citynamesroute list
        if [city1,city2] not in city_links and [city2,city1] not in city_links:# checks if they are linked backwards or forwards
            return False
    return True


# Part 6
def longest_repetition(values:list[int]):
    if len(values) < 1:
        return None
    long_repetition = 1
    long_index = 0
    current_len =1
    current_idx =0
    for i in range(len(values)-1):
        if values[i] == values[i-1]
            current_len +=1
        elif current_len > long_repetition:
            long_repetition = current_len
            long_index = current_idx
        current_len = i
        current_idx = i
    if current_len > long_repetition:
        long_index = current_idx
    return long_index