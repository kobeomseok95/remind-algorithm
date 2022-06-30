"""
  속한 노래가 가장 많이 재생된 장르부터!

  장르 내에서는 가장 재생이 많이 된 순서

  재생 순서가 같다면 고유 번호를 오름차순으로
"""


def solution(genres, plays):
    sorted_play_time_genres = sort_genre_play_time(genres, plays)
    most_two_songs_per_genre = find_two_songs_per_genre(genres, plays)
    answer = []
    for genre in sorted_play_time_genres:
        answer.extend(most_two_songs_per_genre[genre])
    return answer


def sort_genre_play_time(genres, plays):
    genre_dict = {}
    for i in range(len(genres)):
        if genres[i] not in genre_dict:
            genre_dict[genres[i]] = 0
        genre_dict[genres[i]] += plays[i]
    return [genre for genre, play_time in sorted(genre_dict.items(), key=lambda x: (-x[1]))]


def find_two_songs_per_genre(genres, plays):
    genre_dict = {}
    for i in range(len(genres)):
        if genres[i] not in genre_dict:
            genre_dict[genres[i]] = []
        genre_dict[genres[i]].append(i)
    for key in genre_dict.keys():
        genre_dict[key].sort(key=lambda x: (-plays[x], x))
        genre_dict[key] = genre_dict[key][:2]
    return genre_dict
