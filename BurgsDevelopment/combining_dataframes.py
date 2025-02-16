import pandas
#hallways
hallway1 = pandas.read_csv("../data/hallway1.csv")
hallway1 = hallway1.drop(0)
hallway2 = pandas.read_csv("../data/hallway2.csv")
hallway2 = hallway2.drop(0)
hallway3 = pandas.read_csv("../data/hallway3.csv")
hallway3 = hallway3.drop(0)
all_hallways = pandas.concat([hallway1, hallway2], axis = 0)
all_hallways = pandas.concat([all_hallways,hallway3], axis = 0)
all_hallways = all_hallways.drop(all_hallways.columns[1], axis = 1)
print(all_hallways)

#chairs

openchair1 = pandas.read_csv("../data/openchair1.csv")
openchair1 = openchair1.drop(0)
openchair2 = pandas.read_csv("../data/openchair2.csv")
openchair2 = openchair2.drop(0)
openchair3 = pandas.read_csv("../data/openchair3.csv")
openchair3 = openchair3.drop(0)

all_open_chairs = pandas.concat([openchair1, openchair2], axis = 0)
all_open_chairs = pandas.concat([all_open_chairs, openchair3], axis = 0)
all_open_chairs = all_open_chairs.drop(all_open_chairs.columns[1], axis = 1)


#blinds
mrblinds1 = pandas.read_csv("../data/mrblinds1.csv")
mrblinds1 = mrblinds1.drop(0)
mrblinds2 = pandas.read_csv("../data/mrblinds2.csv")
mrblinds2 = mrblinds2.drop(0)
mrblinds3 = pandas.read_csv("../data/mrblinds3.csv")
mrblinds3 = mrblinds3.drop(0)

all_mr_blinds = pandas.concat([mrblinds1, mrblinds2], axis=0)
all_mr_blinds = pandas.concat([all_mr_blinds, mrblinds3], axis = 0)
all_mr_blinds = all_mr_blinds.drop(all_mr_blinds.columns[1], axis = 1)

#windows
mrwindows1 = pandas.read_csv("../data/mrwindows1.csv")
mrwindows1 = mrwindows1.drop(0)
mrwindows2 = pandas.read_csv("../data/mrwindows2.csv")
mrwindows2 = mrwindows2.drop(0)
mrwindows3 = pandas.read_csv("../data/mrwindows3.csv")
mrwindows3 = mrwindows3.drop(0)

all_mr_windows = pandas.concat([mrwindows1, mrwindows2], axis = 0)
all_mr_windows = pandas.concat([all_mr_windows, mrwindows3], axis = 0)
all_mr_windows = all_mr_windows.drop(all_mr_windows.columns[1], axis = 1)