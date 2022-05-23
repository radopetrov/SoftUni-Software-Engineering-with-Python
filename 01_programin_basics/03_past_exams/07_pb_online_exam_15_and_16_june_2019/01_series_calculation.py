series_title = input()
seasons_number = int(input())
episodes_per_season = int(input())
episode_lenth_without_ads = float(input())
episode_lenth_with_ads = episode_lenth_without_ads * 1.2
total_time = (episode_lenth_with_ads * episodes_per_season * seasons_number) + 10 * seasons_number
print(f"Total time needed to watch the {series_title} series is {round(total_time)} minutes.")