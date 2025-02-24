import pandas
#hallways
hallway_1 = pandas.read_csv("../data/hallway1.csv")
hallway_1 = hallway_1.drop(0)
hallway_2 = pandas.read_csv("../data/hallway2.csv")
hallway_2 = hallway_2.drop(0)
hallway_3 = pandas.read_csv("../data/hallway3.csv")
hallway_3 = hallway_3.drop(0)
all_hallways = pandas.concat([hallway_1, hallway_2], axis = 0)
all_hallways = pandas.concat([all_hallways,hallway_3], axis = 0)
all_hallways = all_hallways.drop(all_hallways.columns[1], axis = 1)
hallways_length = len(all_hallways['time'])
hallways_category = ["HALLWAY"] * hallways_length
all_hallways["category"] = hallways_category
#print(all_hallways)

#chairs
open_chair_1 = pandas.read_csv("../data/openchair1.csv")
open_chair_1 = open_chair_1.drop(0)
open_chair_2 = pandas.read_csv("../data/openchair2.csv")
open_chair_2 = open_chair_2.drop(0)
open_chair_3 = pandas.read_csv("../data/openchair3.csv")
open_chair_3 = open_chair_3.drop(0)
all_open_chairs = pandas.concat([open_chair_1, open_chair_2], axis = 0)
all_open_chairs = pandas.concat([all_open_chairs, open_chair_3], axis = 0)
all_open_chairs = all_open_chairs.drop(all_open_chairs.columns[1], axis = 1)
chairs_length = len(all_open_chairs['time'])
chairs_category = ["OPEN_CHAIRS"] * chairs_length
all_open_chairs["category"] = chairs_category
#print(all_open_chairs)

#blinds
mr_blinds_1 = pandas.read_csv("../data/mrblinds1.csv")
mr_blinds_1 = mr_blinds_1.drop(0)
mr_blinds_2 = pandas.read_csv("../data/mrblinds2.csv")
mr_blinds_2 = mr_blinds_2.drop(0)
mr_blinds_3 = pandas.read_csv("../data/mrblinds3.csv")
mr_blinds_3 = mr_blinds_3.drop(0)
mr3_blinds_1 = pandas.read_csv("../data/mr3blinds1.csv")
mr3_blinds_1 = mr3_blinds_1.drop(0)
mr3_blinds_2 = pandas.read_csv("../data/mr3blinds2.csv")
mr3_blinds_2 = mr3_blinds_2.drop(0)
mr3_blinds_3 = pandas.read_csv("../data/mr3blinds3.csv")
mr3_blinds_3 = mr3_blinds_3.drop(0)
all_mr_blinds = pandas.concat([mr_blinds_1, mr_blinds_2], axis=0)
all_mr_blinds = pandas.concat([all_mr_blinds, mr_blinds_3], axis = 0)
all_mr_blinds = pandas.concat([all_mr_blinds, mr3_blinds_1], axis = 0)
all_mr_blinds = pandas.concat([all_mr_blinds, mr3_blinds_2], axis = 0)
all_mr_blinds = pandas.concat([all_mr_blinds, mr3_blinds_3], axis = 0)
all_mr_blinds = all_mr_blinds.drop(all_mr_blinds.columns[1], axis = 1)
blinds_length = len(all_mr_blinds['time'])
blinds_category = ["BLINDS"] * blinds_length
all_mr_blinds["category"] = blinds_category
#print(all_mr_blinds)

#windows
mr_windows_1 = pandas.read_csv("../data/mrwindows1.csv")
mr_windows_1 = mr_windows_1.drop(0)
mr_windows_2 = pandas.read_csv("../data/mrwindows2.csv")
mr_windows_2 = mr_windows_2.drop(0)
mr_windows_3 = pandas.read_csv("../data/mrwindows3.csv")
mr_windows_3 = mr_windows_3.drop(0)
all_mr_windows = pandas.concat([mr_windows_1, mr_windows_2], axis = 0)
all_mr_windows = pandas.concat([all_mr_windows, mr_windows_3], axis = 0)
all_mr_windows = all_mr_windows.drop(all_mr_windows.columns[1], axis = 1)
windows_length = len(all_mr_windows['time'])
windows_category = ["WINDOWS"] * windows_length
all_mr_windows["category"] = windows_category
#print(all_mr_windows)

#entrance
pp_entrance = pandas.read_csv("../data/pplab.csv")
entrance_length = len(pp_entrance['time'])
entrance_category = ["ENTRANCE"] * entrance_length
pp_entrance["category"] = entrance_category
#print(pp_entrance)

#lab
pp_lab_1 = pandas.read_csv("../data/pplab.csv")
pp_lab_1 = pp_lab_1.drop(0)
pp_lab_2 = pandas.read_csv("../data/pplab2.csv")
pp_lab_2 = pp_lab_2.drop(0)
all_lab = pandas.concat([pp_lab_1, pp_lab_2],  axis = 0)
all_lab = all_lab.drop(all_lab.columns[1], axis = 1)
lab_length = len(all_lab['time'])
lab_category = ["LAB"] * lab_length
all_lab["category"] = lab_category
#print(all_lab)

#combining everything

all_frames = pandas.concat([all_hallways, all_open_chairs], axis = 0)
all_frames = pandas.concat([all_frames, all_mr_blinds], axis = 0)
all_frames = pandas.concat([all_frames, all_mr_windows], axis = 0)
all_frames = pandas.concat([all_frames, pp_entrance], axis = 0)
all_frames = pandas.concat([all_frames, all_lab], axis = 0)

print(all_frames)