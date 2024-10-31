import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        point1 = data.Point(2,2)
        point2 = data.Point(10,10)
        results = hw2.create_rectangle(point1,point2)
        expected = data.Rectangle(data.Point(2,10),data.Point(10,2))
        self.assertEqual(expected , results)
    def test_create_rectangle_2(self):
        point1 = data.Point(2,2)
        point2 = data.Point(2,2)
        results = hw2.create_rectangle(point1,point2)
        expected = data.Rectangle(data.Point(2,2),data.Point(2,2))
        self.assertEqual(expected , results)
    # Part 2
    def test_shorter_duration_than_1(self):
        time1 = data.Duration(4,19)
        time2 = data.Duration(4,59)
        results = hw2.shorter_duration_than(time1,time2)
        expected = True
        self.assertEqual(expected,results)
    def test_shorter_duration_than_2(self):
        time1 = data.Duration(18,19)
        time2 = data.Duration(4,59)
        results = hw2.shorter_duration_than(time1,time2)
        expected = False
        self.assertEqual(expected,results)
    # Part 3
    def test_songs_shorter_than_1(self):
        song_list = [data.Song('Wallen','More Than My Hometown',data.Duration(3,37)),data.Song('1D','Night Changes',data.Duration(4,29))]
        song_length = data.Duration(4,30)
        results = hw2.songs_shorter_than(song_list,song_length)
        expected = [data.Song('Wallen','More Than My Hometown',data.Duration(3,37)),data.Song('1D','Night Changes',data.Duration(4,29))]
        self.assertEqual(expected,results)

    def test_songs_shorter_than_2(self):
        song_list = [data.Song('Drake','Hours in Silence',data.Duration(6,39)),data.Song('Jhene','Sativa',data.Duration(4,37))]
        song_length = data.Duration(4,30)
        results = hw2.songs_shorter_than(song_list,song_length)
        expected = []
        self.assertEqual(expected,results)
    # Part 4
    def test_running_time_1(self):
        song_list = [data.Song('Drake','Hours in Silence',data.Duration(6,39)),data.Song('Jhene','Sativa',data.Duration(4,37)),data.Song('Wallen','More Than My Hometown',data.Duration(3,37)),data.Song('1D','Night Changes',data.Duration(4,29))]
        number = [0,1,2,3]
        results = hw2.running_time(song_list,number)
        expected = data.Duration(19,22)
        self.assertEqual(expected,results)
    def test_running_time_2(self):
        song_list = [data.Song('Jackson 5','I Want You Back',data.Duration(3,29)),data.Song('Natasha','Unwritten',data.Duration(4,19)),data.Song('Wallen','7 Summers',data.Duration(3,37)),data.Song('Billy Joel','Uptown Girl',data.Duration(3,18))]
        number = [0,1,2,3]
        results = hw2.running_time(song_list,number)
        expected = data.Duration(19,22)
        self.assertEqual(expected,results)
    # Part 5
    def test_validate_route(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        city_route = ['san luis obispo', 'santa margarita', 'atascadero']
        results = hw2.validate_route(city_links,city_route)
        expected = True
        self.assertEqual(expected,results)

    def test_validate_route_2(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        city_route = ['san luis obispo', 'creston', 'atascadero']
        results = hw2.validate_route(city_links, city_route)
        expected = False
        self.assertEqual(expected, results)
    # Part 6
    def test_longest_rep_1(self):
        values = [1,1,1,2,3,4]
        results = hw2.longest_repetition(values)
        expected = 3
        self.assertEqual(expected,results)
    def test_longest_rep_2(self):
        values = [1,1,2,2,3,4,5,5,5,5]
        results = hw2.longest_repetition(values)
        expected = 4
        self.assertEqual(expected,results)



if __name__ == '__main__':
    unittest.main()
