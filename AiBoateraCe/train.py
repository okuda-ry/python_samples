import numpy as np
import pandas as pd

racelist_df = pd.read_csv(
    "./downloads/racelists/csv/timetable_200901-200907.csv", encoding="shift-jis"
)
detail_df = pd.read_csv(
    "./downloads/results/details/details_200901-200907.csv", encoding="shift-jis"
)

print(racelist_df.head(3))
print(detail_df.head(3))


df = racelist_df.merge(detail_df, on=["日次", "レース場", "レース回"])

print(racelist_df["レース日"].head(3))
print(detail_df["レース日"].head(3))

# # とりあえず使うカラムだけ抜き出す
# usecols = [
#     "day",
#     "place_cd",
#     "race_type",
#     "wether",
#     "wind_d",
#     "wind_v",
#     "water_t",
#     "wave_h",
# ]
# usecols += [
#     f"{k}_{i}"
#     for k in (
#         "age",
#         "weight",
#         "glob_win",
#         "glob_in2",
#         "loc_win",
#         "loc_in2",
#         "moter_in2",
#         "boat_in2",
#     )
#     for i in range(1, 7)
# ]
# X = df[usecols]

# X.head(3)
