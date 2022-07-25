genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# genres = ["hiphop",  "pop", "classic", "pop", "hiphop"]
# plays = [2000, 600, 8000, 2500, 2000]


def compare_album(album_1, album_2):
    if album_1[0] < album_2[0]:
        return True
    elif album_1[0] > album_2[0]:
        return False

    if album_1[1] > album_2[1]:
        return True
    elif album_1[1] < album_2[1]:
        return False

    if album_1[2] < album_2[2]:
        return True
    return False


def compare_play(genre_1, genre_2):
    if genre_1[1] > genre_2[1]:
        return True
    return False


def compare_default(num_1, num_2):
    return num_1 > num_2


def merge_sort(array, func=compare_default):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = merge_sort(array[:mid], func=func)
    right_array = merge_sort(array[mid:], func=func)
    return merge(left_array, right_array, func=func)


def merge(array_1, array_2, func=compare_default):
    merge_array = []
    index_1 = 0
    index_2 = 0

    while True:
        if index_1 >= len(array_1):
            merge_array.extend(array_2[index_2:])
            break

        if index_2 >= len(array_2):
            merge_array.extend(array_1[index_1:])
            break

        if func(array_1[index_1], array_2[index_2]):
            merge_array.append(array_1[index_1])
            index_1 += 1
        else:
            merge_array.append(array_2[index_2])
            index_2 += 1

    return merge_array


def get_melon_best_album(genre_array, play_array):

    all_genres = list(set(genre_array))
    all_plays = dict()

    for genre in all_genres:
        all_plays[genre] = 0

    for i, genre in enumerate(genre_array):
        all_plays[genre] += play_array[i]

    all_plays = list(all_plays.items())
    all_plays = merge_sort(all_plays, compare_play)
    all_plays = [(i, k, v) for i, (k, v) in enumerate(all_plays)]

    all_plays_dict = dict()
    for play in all_plays:
        all_plays_dict[play[1]] = (play[0], play[2])

    album_store = []
    for i, genre in enumerate(genre_array):
        album = (all_plays_dict[genre][0], play_array[i], i)
        album_store.append(album)

    merge_array = merge_sort(album_store, compare_album)

    album_store = dict()
    for order in all_plays:
        album_store[order[0]] = list()

    for album in merge_array:
        album_store[album[0]].append((album[1], album[2]))

    result = []
    for i, play in enumerate(all_plays):
        if album_store[i] is not None:
            result.append(album_store[i][0][1])
        if len(album_store[i]) >= 2:
            result.append(album_store[i][1][1])

    return result



print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!