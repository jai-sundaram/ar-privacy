{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "a29b53bb-8df1-42a8-9d0a-79336c17e3d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas\n",
    "from sklearn.model_selection import train_test_split \n",
    "from sklearn.svm import SVC\n",
    "from sklearn.metrics import accuracy_score \n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.compose import ColumnTransformer\n",
    "from sklearn.preprocessing import OneHotEncoder\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "import time \n",
    "import random\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay\n",
    "import numpy as np\n",
    "from sklearn.model_selection import cross_val_score, KFold"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f2e1a596-28e8-4f85-bf66-3247ae51bd5c",
   "metadata": {},
   "outputs": [],
   "source": [
    "blinds1 = pandas.read_csv(\"../../data3/blinds_data/blinds_meetingroom_1.csv\")\n",
    "blinds2 = pandas.read_csv(\"../../data3/blinds_data/blinds_meetingroom_2.csv\")\n",
    "blinds3 = pandas.read_csv(\"../../data3/blinds_data/blinds_meetingroom_3_offset2seconds.csv\")\n",
    "blinds_test = pandas.read_csv(\"../../data3/blinds_data/blinds_meetingroom_4.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "afeac3d4-bed8-4925-8705-d5484977c091",
   "metadata": {},
   "outputs": [],
   "source": [
    "blinds_train = pandas.concat([blinds1, blinds2], axis=0)\n",
    "blinds_train = pandas.concat([blinds_train, blinds3], axis=0)\n",
    "blinds_category_train_length = len(blinds_train['cpu'])\n",
    "blinds_category_train = [\"BLINDS\"] * blinds_category_train_length \n",
    "blinds_category_test_length = len(blinds_test['cpu'])\n",
    "blinds_category_test = [\"BLINDS\"] * blinds_category_test_length"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7b1dda8f-06ff-4fef-9d93-96e6eda6ad8e",
   "metadata": {},
   "outputs": [],
   "source": [
    "hallway1 = pandas.read_csv(\"../../data3/hallway_data/hallway_1.csv\")\n",
    "hallway2 = pandas.read_csv(\"../../data3/hallway_data/hallway_2.csv\")\n",
    "hallway3 = pandas.read_csv(\"../../data3/hallway_data/hallway_3.csv\")\n",
    "hallways_test = pandas.read_csv(\"../../data3/hallway_data/hallway_4.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "743f509d-7131-4ae5-a4ef-639f8013c93b",
   "metadata": {},
   "outputs": [],
   "source": [
    "hallways_train = pandas.concat([hallway1, hallway2], axis = 0)\n",
    "hallways_train = pandas.concat([hallways_train, hallway3], axis = 0)\n",
    "hallways_category_train_length = len(hallways_train['cpu'])\n",
    "hallways_category_train = [\"HALLWAYS\"] * hallways_category_train_length\n",
    "hallways_category_test_length = len(hallways_test['cpu'])\n",
    "hallways_category_test = [\"HALLWAYS\"] * hallways_category_test_length"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "795822fc-bf7c-4935-9404-20605cf295d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "windows1 = pandas.read_csv(\"../../data3/windows_data/windows_meetingroom_1.csv\")\n",
    "windows2 = pandas.read_csv(\"../../data3/windows_data/windows_meetingroom_2.csv\")\n",
    "windows3 = pandas.read_csv(\"../../data3/windows_data/windows_meetingroom_3.csv\")\n",
    "windows_test = pandas.read_csv(\"../../data3/windows_data/windows_meetingroom_4.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "131e2257-5006-4b28-b46a-c525ed0a3c67",
   "metadata": {},
   "outputs": [],
   "source": [
    "windows_train = pandas.concat([windows1, windows2], axis = 0)\n",
    "windows_train = pandas.concat([windows_train, windows3], axis = 0)\n",
    "windows_category_train_length = len(windows_train['cpu'])\n",
    "windows_category_train = [\"WINDOWS\"] * windows_category_train_length \n",
    "windows_category_test_length = len(windows_test['cpu'])\n",
    "windows_category_test = [\"WINDOWS\"] * windows_category_test_length"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "31be340c-02b4-42d4-9989-e53f6a2afcba",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train = pandas.concat([blinds_train, hallways_train], axis = 0)\n",
    "X_train = pandas.concat([X_train, windows_train], axis = 0)\n",
    "X_test = pandas.concat([blinds_test, hallways_test], axis = 0)\n",
    "X_test = pandas.concat([X_test, windows_test], axis = 0)\n",
    "y_train = blinds_category_train + hallways_category_train + windows_category_train\n",
    "y_test = blinds_category_test + hallways_category_test + windows_category_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "619b2d47-2e2a-4eda-acb0-444cf1d9e0c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9512690355329949\n"
     ]
    }
   ],
   "source": [
    "le = LabelEncoder()\n",
    "y_train = le.fit_transform(y_train)\n",
    "y_test = le.fit_transform(y_test)\n",
    "sc = StandardScaler()\n",
    "X_train = X_train.astype(float)\n",
    "X_test = X_test.astype(float)\n",
    "X_train.iloc[:,:] = sc.fit_transform(X_train)\n",
    "X_test.iloc[:,:] = sc.transform(X_test)\n",
    "svm = SVC(decision_function_shape='ovo', probability=True)\n",
    "svm.fit(X_train, y_train)\n",
    "y_pred = svm.predict(X_test)\n",
    "print(accuracy_score(y_test, y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "e508ec3e-711e-4737-860c-7577395c5c9f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9818987076156764\n"
     ]
    }
   ],
   "source": [
    "folds = 5\n",
    "X = pandas.concat([X_train, X_test], axis = 0)\n",
    "y= np.concatenate([y_train, y_test])\n",
    "kf = KFold(n_splits = folds, shuffle = True)\n",
    "results = cross_val_score(svm, X, y, cv=kf)\n",
    "print(results.mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c4d9a9a5-dbed-4d3e-b496-01cc00522501",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
