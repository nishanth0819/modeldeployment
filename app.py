{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv(\"diabetes.csv\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>148</td>\n",
       "      <td>72</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>33.6</td>\n",
       "      <td>0.627</td>\n",
       "      <td>50</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>66</td>\n",
       "      <td>29</td>\n",
       "      <td>0</td>\n",
       "      <td>26.6</td>\n",
       "      <td>0.351</td>\n",
       "      <td>31</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8</td>\n",
       "      <td>183</td>\n",
       "      <td>64</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>23.3</td>\n",
       "      <td>0.672</td>\n",
       "      <td>32</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>89</td>\n",
       "      <td>66</td>\n",
       "      <td>23</td>\n",
       "      <td>94</td>\n",
       "      <td>28.1</td>\n",
       "      <td>0.167</td>\n",
       "      <td>21</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>137</td>\n",
       "      <td>40</td>\n",
       "      <td>35</td>\n",
       "      <td>168</td>\n",
       "      <td>43.1</td>\n",
       "      <td>2.288</td>\n",
       "      <td>33</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
       "0            1      148             72             35        0  33.6   \n",
       "1            1       85             66             29        0  26.6   \n",
       "2            8      183             64              0        0  23.3   \n",
       "3            1       89             66             23       94  28.1   \n",
       "4            0      137             40             35      168  43.1   \n",
       "\n",
       "   DiabetesPedigreeFunction  Age  Outcome  \n",
       "0                     0.627   50        1  \n",
       "1                     0.351   31        0  \n",
       "2                     0.672   32        1  \n",
       "3                     0.167   21        0  \n",
       "4                     2.288   33        1  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 768 entries, 0 to 767\n",
      "Data columns (total 9 columns):\n",
      " #   Column                    Non-Null Count  Dtype  \n",
      "---  ------                    --------------  -----  \n",
      " 0   Pregnancies               768 non-null    int64  \n",
      " 1   Glucose                   768 non-null    int64  \n",
      " 2   BloodPressure             768 non-null    int64  \n",
      " 3   SkinThickness             768 non-null    int64  \n",
      " 4   Insulin                   768 non-null    int64  \n",
      " 5   BMI                       768 non-null    float64\n",
      " 6   DiabetesPedigreeFunction  768 non-null    float64\n",
      " 7   Age                       768 non-null    int64  \n",
      " 8   Outcome                   768 non-null    int64  \n",
      "dtypes: float64(2), int64(7)\n",
      "memory usage: 54.1 KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(768, 9)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>3.838542</td>\n",
       "      <td>120.894531</td>\n",
       "      <td>69.105469</td>\n",
       "      <td>20.536458</td>\n",
       "      <td>79.799479</td>\n",
       "      <td>31.992578</td>\n",
       "      <td>0.471876</td>\n",
       "      <td>33.240885</td>\n",
       "      <td>0.348958</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>3.370239</td>\n",
       "      <td>31.972618</td>\n",
       "      <td>19.355807</td>\n",
       "      <td>15.952218</td>\n",
       "      <td>115.244002</td>\n",
       "      <td>7.884160</td>\n",
       "      <td>0.331329</td>\n",
       "      <td>11.760232</td>\n",
       "      <td>0.476951</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.078000</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>99.000000</td>\n",
       "      <td>62.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>27.300000</td>\n",
       "      <td>0.243750</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>117.000000</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>30.500000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>0.372500</td>\n",
       "      <td>29.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>6.000000</td>\n",
       "      <td>140.250000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>127.250000</td>\n",
       "      <td>36.600000</td>\n",
       "      <td>0.626250</td>\n",
       "      <td>41.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>17.000000</td>\n",
       "      <td>199.000000</td>\n",
       "      <td>122.000000</td>\n",
       "      <td>99.000000</td>\n",
       "      <td>846.000000</td>\n",
       "      <td>67.100000</td>\n",
       "      <td>2.420000</td>\n",
       "      <td>81.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Pregnancies     Glucose  BloodPressure  SkinThickness     Insulin  \\\n",
       "count   768.000000  768.000000     768.000000     768.000000  768.000000   \n",
       "mean      3.838542  120.894531      69.105469      20.536458   79.799479   \n",
       "std       3.370239   31.972618      19.355807      15.952218  115.244002   \n",
       "min       0.000000    0.000000       0.000000       0.000000    0.000000   \n",
       "25%       1.000000   99.000000      62.000000       0.000000    0.000000   \n",
       "50%       3.000000  117.000000      72.000000      23.000000   30.500000   \n",
       "75%       6.000000  140.250000      80.000000      32.000000  127.250000   \n",
       "max      17.000000  199.000000     122.000000      99.000000  846.000000   \n",
       "\n",
       "              BMI  DiabetesPedigreeFunction         Age     Outcome  \n",
       "count  768.000000                768.000000  768.000000  768.000000  \n",
       "mean    31.992578                  0.471876   33.240885    0.348958  \n",
       "std      7.884160                  0.331329   11.760232    0.476951  \n",
       "min      0.000000                  0.078000   21.000000    0.000000  \n",
       "25%     27.300000                  0.243750   24.000000    0.000000  \n",
       "50%     32.000000                  0.372500   29.000000    0.000000  \n",
       "75%     36.600000                  0.626250   41.000000    1.000000  \n",
       "max     67.100000                  2.420000   81.000000    1.000000  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI'], dtype='object')"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "na_cols=df.columns[df.describe().loc[\"min\"]==0][1:6] ##Get all the columns with minimum value 0 except Pregnancies and Outcome column\n",
    "na_cols"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "repalce_0=lambda x:np.nan if x==0 else x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "for col in na_cols:\n",
    "    df[col]=df[col].map(repalce_0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 768 entries, 0 to 767\n",
      "Data columns (total 9 columns):\n",
      " #   Column                    Non-Null Count  Dtype  \n",
      "---  ------                    --------------  -----  \n",
      " 0   Pregnancies               768 non-null    int64  \n",
      " 1   Glucose                   763 non-null    float64\n",
      " 2   BloodPressure             733 non-null    float64\n",
      " 3   SkinThickness             541 non-null    float64\n",
      " 4   Insulin                   394 non-null    float64\n",
      " 5   BMI                       757 non-null    float64\n",
      " 6   DiabetesPedigreeFunction  768 non-null    float64\n",
      " 7   Age                       768 non-null    int64  \n",
      " 8   Outcome                   768 non-null    int64  \n",
      "dtypes: float64(6), int64(3)\n",
      "memory usage: 54.1 KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x1080 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "_,ax = plt.subplots(figsize=(15,15))\n",
    "sns.heatmap(df.isnull(), ax = ax)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### There does not seem to be any pattern here for NA values and also the Insulin column seems to have a lot of NA valus"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[<AxesSubplot:title={'center':'Pregnancies'}>,\n",
       "        <AxesSubplot:title={'center':'Glucose'}>,\n",
       "        <AxesSubplot:title={'center':'BloodPressure'}>],\n",
       "       [<AxesSubplot:title={'center':'SkinThickness'}>,\n",
       "        <AxesSubplot:title={'center':'Insulin'}>,\n",
       "        <AxesSubplot:title={'center':'BMI'}>],\n",
       "       [<AxesSubplot:title={'center':'DiabetesPedigreeFunction'}>,\n",
       "        <AxesSubplot:title={'center':'Age'}>,\n",
       "        <AxesSubplot:title={'center':'Outcome'}>]], dtype=object)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x1080 with 9 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.hist(figsize=(15,15))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###      There is to something wrong with 'Glucose' and 'BloodPressure' columns. Glucose below 70 is considered highly dangerous and BP cannot be less than 60. These are wrong values and I will replace them with NA."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "replace_glucose_70=lambda x:np.nan if x<70 else x\n",
    "replace_bp_60=lambda x:np.nan if x<60 else x\n",
    "\n",
    "df[\"Glucose\"]=df[\"Glucose\"].map(replace_glucose_70)\n",
    "df[\"BloodPressure\"] = df[\"BloodPressure\"].map(replace_bp_60)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 768 entries, 0 to 767\n",
      "Data columns (total 9 columns):\n",
      " #   Column                    Non-Null Count  Dtype  \n",
      "---  ------                    --------------  -----  \n",
      " 0   Pregnancies               768 non-null    int64  \n",
      " 1   Glucose                   752 non-null    float64\n",
      " 2   BloodPressure             647 non-null    float64\n",
      " 3   SkinThickness             541 non-null    float64\n",
      " 4   Insulin                   394 non-null    float64\n",
      " 5   BMI                       757 non-null    float64\n",
      " 6   DiabetesPedigreeFunction  768 non-null    float64\n",
      " 7   Age                       768 non-null    int64  \n",
      " 8   Outcome                   768 non-null    int64  \n",
      "dtypes: float64(6), int64(3)\n",
      "memory usage: 54.1 KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###   For the columns that look gaussian(Glucose, SkinThickness, BMI,BloodPressure) I will be replacing NA values with mean and for other columns(Insulin) I will be replacing with median."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"Glucose\"].fillna(df[\"Glucose\"].mean(), inplace=True)\n",
    "df[\"SkinThickness\"].fillna(df[\"SkinThickness\"].mean(), inplace=True)\n",
    "df[\"BMI\"].fillna(df[\"BMI\"].mean(), inplace=True)\n",
    "df[\"BloodPressure\"].fillna(df[\"BloodPressure\"].mean(), inplace=True)\n",
    "df[\"Insulin\"].fillna(df[\"Insulin\"].median(), inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 768 entries, 0 to 767\n",
      "Data columns (total 9 columns):\n",
      " #   Column                    Non-Null Count  Dtype  \n",
      "---  ------                    --------------  -----  \n",
      " 0   Pregnancies               768 non-null    int64  \n",
      " 1   Glucose                   768 non-null    float64\n",
      " 2   BloodPressure             768 non-null    float64\n",
      " 3   SkinThickness             768 non-null    float64\n",
      " 4   Insulin                   768 non-null    float64\n",
      " 5   BMI                       768 non-null    float64\n",
      " 6   DiabetesPedigreeFunction  768 non-null    float64\n",
      " 7   Age                       768 non-null    int64  \n",
      " 8   Outcome                   768 non-null    int64  \n",
      "dtypes: float64(6), int64(3)\n",
      "memory usage: 54.1 KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x1440 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "_,ax = plt.subplots(figsize=(15,20))\n",
    "sns.heatmap(df[df.columns[:-1]].corr())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "####   We can't remove the Insulin column as Glucose and Insulin have correlation. Insulin is used for glucose control and that might be the reason why. Also pregnancy and age also seem to have a correlation along with BMI and skin thickness. The correlations seem to make sense."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###  Pregnancies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1     136\n",
       "0     111\n",
       "2     103\n",
       "3      75\n",
       "4      68\n",
       "5      57\n",
       "6      49\n",
       "7      45\n",
       "8      38\n",
       "9      28\n",
       "10     24\n",
       "11     11\n",
       "13     10\n",
       "12      9\n",
       "14      2\n",
       "15      1\n",
       "17      1\n",
       "Name: Pregnancies, dtype: int64"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Pregnancies\"].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There seem to be people with more than 10 pregnancies as well, to check the genuineness of the value, we can check the age as I believe it is impossible for people with less age(less than 25) to have more than 10 pregnancies."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "159    47\n",
       "Name: Age, dtype: int64"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Age\"][df[\"Pregnancies\"]==17] #check the age for woman with 17 pregnancies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "28     57\n",
       "72     42\n",
       "86     45\n",
       "274    52\n",
       "323    43\n",
       "357    44\n",
       "518    41\n",
       "635    38\n",
       "691    44\n",
       "744    39\n",
       "Name: Age, dtype: int64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Age\"][df[\"Pregnancies\"] == 13]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "from the above observations age and pregnancies are making sense"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Pregnancies', ylabel='Density'>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYgAAAEJCAYAAACOr7BbAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAAA7SUlEQVR4nO3dd3yV5fn48c+VkwlZhAxGCCTsvcISUVBRwIF1VUq1aFtEpY7Wb2trf7XDql1arauuuhDqFi3iYigqe69AIIEkjEyyd+7fH8+JxniSnEDOzPV+vc4rOc9zP+e5DiG5zr3FGINSSinVXICnA1BKKeWdNEEopZRySBOEUkophzRBKKWUckgThFJKKYc0QSillHLIpQlCRGaJSJqIpIvI3Q7ODxGRr0SkWkTuanK8j4isFpF9IrJHRG53ZZxKKaW+S1w1D0JEbMABYCaQDWwC5hlj9jYpEw/0BS4Hiowxf7cf7wn0NMZsFZEIYAtwedNrlVJKuVagC197IpBujDkMICLLgLnA13/kjTG5QK6IXNz0QmPMceC4/ftSEdkH9G56rSOxsbGmX79+HfkelFLKr23ZsiXfGBPn6JwrE0RvIKvJ82xgUntfRET6AWOBDS2cXwgsBEhKSmLz5s3tDlQppTorETnS0jlX9kGIg2Ptas8SkXDgTeAOY0yJozLGmKeNManGmNS4OIdJUCml1GlwZYLIBvo0eZ4IHHP2YhEJwkoOS4wxb3VwbEoppdrgygSxCRgoIskiEgxcCyx35kIREeA5YJ8x5iEXxqiUUqoFLuuDMMbUichi4EPABjxvjNkjIovs558SkR7AZiASaBCRO4BhwCjgOmCXiGy3v+RvjDErXBWvUko1VVtbS3Z2NlVVVZ4OpUOEhoaSmJhIUFCQ09e4bJirJ6SmphrtpFZKdYSMjAwiIiLo3r07VqOG7zLGUFBQQGlpKcnJyd86JyJbjDGpjq7TmdRKKeVAVVWVXyQHABGhe/fu7a4NaYJQSqkW+ENyaHQ670UTRCdljKGhwX+aF5VSHU8TRCdTXFnL4le3Mux3HzLhz5/w9GeH8Kd+KKVcLTs7m7lz5zJw4ED69+/P7bffTk1NTavX3H///W6KrmNpguhEKmvqueapr1i5+wRXju/N8N5R3L9iP/f9b58mCaWcYIzhiiuu4PLLL+fgwYMcOHCAsrIy7rnnnlav0wShvN4DH+wj7WQpz/wolfsuH8mLN0xgwVn9eG5dBu/tPO7p8JTyeqtWrSI0NJQbbrgBAJvNxsMPP8zzzz/PE088weLFi78ue8kll7BmzRruvvtuKisrGTNmDPPnzwfgpZdeYtSoUYwePZrrrrsOgCNHjnD++eczatQozj//fI4ePQrAggULuPnmm5kxYwYpKSmsXbuWG2+8kaFDh7JgwYKv7/fRRx8xZcoUxo0bx9VXX01ZWdkZv19NEJ1E2olSXvrqCAvO6seMwfGA1Wn1/y4ZxsjeUfzxvb0UV9Z6OEqlvNuePXsYP378t45FRkaSlJREXV2dw2sefPBBwsLC2L59O0uWLGHPnj38+c9/ZtWqVezYsYNHHnkEgMWLF3P99dezc+dO5s+fz2233fb1axQVFbFq1SoefvhhLr30Uu6880727NnDrl272L59O/n5+dx333188sknbN26ldTUVB566MznGGuC6CSeXJNOl2Abd1ww8FvHbQHCA1eMpKC8mmc/P+yh6JTyDcYYh6OBWjruyKpVq7jqqquIjY0FICYmBoCvvvqKH/zgBwBcd911rFu37utrLr30UkSEkSNHkpCQwMiRIwkICGD48OFkZmayfv169u7dy9SpUxkzZgwvvvgiR460uAaf01y5mqvyEjmnKlm+4xg/mZZCdJfg75wf0TuKC4cl8OKXmSw8J4WIUOdnWirVmQwfPpw333zzW8dKSkrIysoiKiqKhoaGr4+3NOfA2WTStExISAgAAQEBX3/f+Lyurg6bzcbMmTNZunRpu95PW7QG0Qm8vTWbBgPXTe7bYplbpg+gpKqO/27KarGMUp3d+eefT0VFBS+99BIA9fX1/OIXv2DBggWkpKSwfft2GhoayMrKYuPGjV9fFxQURG1t7dev8dprr1FQUABAYWEhAGeddRbLli0DYMmSJZx99tlOxzV58mS++OIL0tPTAaioqODAgQNn/H41Qfg5Ywxvb8thYr8Y+sR0abHc6D7RjO/bjVc3HtURTUq1QER4++23ef311xk4cCCDBg0iNDSU+++/n6lTp5KcnMzIkSO56667GDdu3NfXLVy4kFGjRjF//nyGDx/OPffcw7nnnsvo0aP5+c9/DsCjjz7Kf/7zH0aNGsXLL7/8dd+EM+Li4njhhReYN28eo0aNYvLkyezfv//M368//THQtZi+a1d2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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.kdeplot(data = df, x = \"Pregnancies\", hue=\"Outcome\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "from the above KDE plot we can say people with low pregnancies have lower risk of diabetes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##  Glucose"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Glucose', ylabel='Density'>"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.kdeplot(data=df, x=\"Glucose\", hue=\"Outcome\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "People having diabetes have higher level of Glucose"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###  BloodPressure"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='BloodPressure', ylabel='Density'>"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAY4AAAEGCAYAAABy53LJAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAABC30lEQVR4nO3deXxU1fn48c+Tyb6QkJCwBQhL2Hcjm4gLLuCGawtVEDfqQqvWLrb2963aaq3VWm2tVi0KakURF7C44q7syL6GACYQQhII2dc5vz/uDcaYZRLmzkzC83695pWZe8+Z+0wIeXLuPfc5YoxBKaWU8lSQvwNQSinVtmjiUEop1SKaOJRSSrWIJg6llFItoolDKaVUiwT7OwBf6NSpk0lJSfF3GEop1aasW7cuzxiTWH/7SZE4UlJSWLt2rb/DUEqpNkVE9je0XU9VKaWUahFNHEoppVpEE4dSSqkWOSmucSillDdVVVWRlZVFeXm5v0PxivDwcJKTkwkJCfGovSYOpZRqoaysLGJiYkhJSUFE/B3OCTHGkJ+fT1ZWFr179/aoj56qUkqpFiovLychIaHNJw0AESEhIaFFoydNHEop1QrtIWnUauln0cShApKW+1cqcGniUAGlqsbNz175hlMfWM6LK/ZR49YEotqGrKwspk2bRmpqKn379uX222+nsrKyyT4PPvigj6LzLk0cKmAYY7h94Tcs3XiQTtGh/L+3t/LsFxn+DkupZhljuPzyy7n00kvZvXs3u3btori4mHvuuafJfpo4lDpBX6Xns2zzIX51/gDevf10JvVP5NnPMyirrPF3aEo16eOPPyY8PJzrrrsOAJfLxWOPPca8efP417/+xdy5c4+3veiii/j000+5++67KSsrY+TIkVx99dUALFiwgOHDhzNixAhmzpwJwP79+5k8eTLDhw9n8uTJfPvttwDMnj2bW265hbPOOos+ffrw2Wefcf311zNo0CBmz559/HgffPAB48ePZ/To0Vx11VUUFxef8OfVxKECxksr99MxMoQbJvZGRJh7Vj/ySyp5bW2mv0NTqklbt27llFNO+d62Dh060LNnT6qrqxvs89BDDxEREcGGDRt4+eWX2bp1Kw888AAff/wxGzdu5PHHHwdg7ty5zJo1i02bNnH11Vfz85///Ph7HD16lI8//pjHHnuMiy++mDvvvJOtW7eyefNmNmzYQF5eHn/605/46KOPWL9+PWlpafztb3874c+r93GogHDoWDkfbs/hxtN7Ex7iAmBM73hOTenIf77cy6zxvdrVLBbVvhhjGvz5bGx7Qz7++GOuvPJKOnXqBEB8fDwAK1as4I033gBg5syZ/PrXvz7e5+KLL0ZEGDZsGJ07d2bYsGEADBkyhH379pGVlcW2bds47bTTAKisrGT8+PGt/6A2TRwqICxam4nbGK4e0+t72y8blczv3tzMntxi+iXF+Ck6pZo2ZMgQFi9e/L1thYWFZGZmEhsbi9vtPr69sfslPE0ydduEhYUBEBQUdPx57evq6mpcLhfnnnsur7zySos+T3P0VJUKCMt3HGZkjzh6JkR+b/uk/tZfX5/uzPVHWEp5ZPLkyZSWlrJgwQIAampquOuuu5g9ezZ9+vRhw4YNuN1uMjMzWb169fF+ISEhVFVVHX+P1157jfz8fACOHDkCwIQJE1i4cCEAL7/8MhMnTvQ4rnHjxvHVV1+Rnp4OQGlpKbt27Trhz6uJQ/ndsdIqNmUVMCn1B+vFkNwxkn5J0Xy2SxOHClwiwptvvsmiRYtITU2lf//+hIeH8+CDD3LaaafRu3dvhg0bxi9/+UtGjx59vN+cOXMYPnw4V199NUOGDOGee+7hjDPOYMSIEfziF78A4IknnuD5559n+PDhvPjii8evfXgiMTGRF154gRkzZjB8+HDGjRvHjh07Tvzzngw3WqWlpRldyClwvbs5m1teXs/rN48nLSX+B/v/+M42Xly5n43/dx4RoS4/RKjU923fvp1Bgwb5Owyvaugzicg6Y0xa/bY64lB+9/nuPGLCghnRI67B/ZP6J1JZ7Wbl3nzfBqaUapAmDuVXxhi+2J3LuL4JhLga/nEckxKPK0hYt++oj6NTSjXE0cQhIlNEZKeIpIvI3Q3sFxF5wt6/SURG29vDRWS1iGwUka0icl+dPveKyAER2WA/LnDyMyhnHTxWTtbRMk7rm9Bom4hQF6lJ0Ww6cMyHkSmlGuNY4hARF/AkMBUYDMwQkcH1mk0FUu3HHOApe3sFcLYxZgQwEpgiIuPq9HvMGDPSfixz6jMo533zrTWKGN2rY5PtRiTHsSmrQIsfKhUAnBxxjAHSjTEZxphKYCEwrV6bacACY1kJxIlIV/t17X3xIfZDf2O0Qxu+LSA0OIiBXTo02W54j1gKSqvIPFLmo8iUUo1xMnF0B+rWisiyt3nURkRcIrIBOAx8aIxZVafdXPvU1jwRafBPVRGZIyJrRWRtbq5O5QxUGzILGNqtA6HBTf8oDu8eB8DGrALng1JKNcnJxNHQLZD1Rw2NtjHG1BhjRgLJwBgRGWrvfwroi3UKKxt4tKGDG2OeMcakGWPSEhN/eH+A8r+qGjebDxxjZI+mT1MBDOgSQ6griE2aOJRq0nvvvceAAQPo168fDz30kCPHcDJxZAE96rxOBg62tI0xpgD4FJhiv86xk4obeBbrlJhqg3YeKqKi2s2IHrHNtg0NDmJQtw5szNIL5Eo1pqamhttuu413332Xbdu28corr7Bt2zavH8fJxLEGSBWR3iISCkwHltRrswSYZc+uGgccM8Zki0iiiMQBiEgEcA6ww37dtU7/y4AtDn4G5aANmQUAjPJgxAEwrHsHth8s1AvkSjVi9erV9OvXjz59+hAaGsr06dN5++23vX4cx4ocGmOqRWQu8D7gAuYZY7aKyM32/qeBZcAFQDpQClxnd+8KzLdnZgUBrxlj3rH3PSwiI7FOae0DfurUZ1DO2px1jI6RIfSIj/Co/YDOMRRVVJN9rJxucZ71Ucof7lu6lW0HC736noO7deAPFw9pss2BAwfo0eO7kzjJycmsWrWqiR6t42h1XHuq7LJ6256u89wAtzXQbxMwqpH3nOnlMJWfbMsuZEi3WI/LTvfvbFXH3ZVTpIlDqQY0NBp3YjkCLauu/KKqxs3OnCJmT0jxuE/dxHHmgCSHIlPqxDU3MnBKcnIymZnfTVTNysqiW7duXj+OlhxRfpGRW0JltZvBXZu+f6OujlGhJMaEsSvnxJe+VKo9OvXUU9m9ezd79+6lsrKShQsXcskll3j9ODriUH6xPds6/zu4m+eJA6B/52h25RQ5EZJSbV5wcDD//Oc/Of/886mpqeH6669nyBDvj340cSi/2JZdSGhwEH06RbWoX//OMSxcnYnbbQgK0qVklarvggsu4IILnC3hp6eqlF9sO1jIgM4xBDdSEbcx/TvHUFZVQ9ZRLT2ilL9o4lA+Z4xhe3Zhi65v1Kq9QL5TT1cp5TeaOJTP5RZVkF9SyaCuMS3u2y8pGoCMXL1ArpS/aOJQPlc7WhjQTEXchsRGhBAfFcq+/BJvh6WU8pAmDuVzOw/VJo6WjzgAUhIi2ZuniUMpf9HEoXxu56EiEmPCiI8KbVX/lE5RmjiU8iNNHMrnduUUMaBz60YbAH06RZFTWEFpZbUXo1Kq7bv++utJSkpi6NChzTc+AZo4lE+53YZdOcXHZ0e1Rop978e+vFJvhaVUuzB79mzee+89x4+jiUP5VObRUsqqahjQJbrV75GSYCcOvUCu1PdMmjSJ+Ph4x4+jd44rn/ruwnjLZ1TVqh1x6HUOFbDevRsObfbue3YZBlOdWdGvpXTEoXyqts5UalLrRxzRYcEkxYRp4lDKT3TEoXxqx6EiesRHEBV2Yj96KZ2i2KeJQwWqABkZOEVHHMqnTnRGVa3eCVF6jUMpP9HEoXymstpNRm5Jq2/8q6t3YhR5xZUUlld5ITKl2ocZM2Ywfvx4du7cSXJyMv/5z38cOY6eqlI+k5FXTLXbnNBU3FrHZ1bllTA8Oe6E30+p9uCVV17xyXEcHXGIyBQR2Ski6SJydwP7RUSesPdvEpHR9vZwEVktIhtFZKuI3FenT7yIfCgiu+2vHZ38DMp7TrTUSF29dWaVUn7jWOIQERfwJDAVGAzMEJHB9ZpNBVLtxxzgKXt7BXC2MWYEMBKYIiLj7H13A8uNManAcvu1agN25RQRHCT06dT6GVW1eiVEAnoToFL+4OSIYwyQbozJMMZUAguBafXaTAMWGMtKIE5Eutqva+tmh9gPU6fPfPv5fOBSBz+D8qKdh4rpkxhFaPCJ/9iFh7joHhfB3jwtr678wxjTfKM2oqWfxcnE0R3IrPM6y97mURsRcYnIBuAw8KExZpXdprMxJhvA/prU0MFFZI6IrBWRtbm5uSf6WZQX7Mwp9Mr1jVopnSLZm68jDuV74eHh5Ofnt4vkYYwhPz+f8PBwj/s4eXG8oQWh63+XG21jjKkBRopIHPCmiAw1xmzx9ODGmGeAZwDS0tLa/r9uG1dSUU3mkTJ+dEoPr71nSkIU72zK9tr7KeWp5ORksrKyaC9/lIaHh5OcnOxxeycTRxZQ97dEMnCwpW2MMQUi8ikwBdgC5Nins7JFpCvWiEQFuB32hfGBrVgutjG9O0VxrKyKoyWVdGxliXalWiMkJITevXv7Owy/cfJU1RogVUR6i0goMB1YUq/NEmCWPbtqHHDMTgiJ9kgDEYkAzgF21Olzrf38WuBtBz+D8pLt2YUArVoutjG1M6sydGaVUj7l2IjDGFMtInOB9wEXMM8Ys1VEbrb3Pw0sAy4A0oFS4Dq7e1dgvj0zKwh4zRjzjr3vIeA1EbkB+Ba4yqnPoLxne3YhMeHBdI+L8Np7fldevYRTeumsbKV8xdEbAI0xy7CSQ91tT9d5boDbGui3CRjVyHvmA5O9G6ly2o5DRQzq0gGRhi5rtU6PjpEECew/ohfIlfIlLTmiHOd2G3ZkF3r1NBVAaHAQ3eIi2K81q5TyKU0cynGZR0spqaxhkBcvjNdKSYhin07JVcqnNHEox23P9v6Mqlq9EiJ1xKGUj2niUI7bnl1IkOCVcur1pSREUVBaRUFppdffWynVME0cynHbswtJ6RRFRKjL6+9dW7Nqv56uUspnNHEox9XOqHLC8Sm5erpKKZ/RxKEcVVRexbdHSr0+o6pWz3gdcSjla5o4lKNq1+BwYkYVWFVyu8aG64hDKR/SxKEctd2BGlX1WTOrdMShlK9o4lCO2p5dSIfwYLrFel6yuaVSEqJ0Sq5SPqSJQzlqe3Yhg7p6t9RIfb0SosgrrqS4otqxYyilvqOJQznG7TbsPFTk2PWNWinHp+TqqEMpX9DEoRyTkVdMaWUNQ7o5mzh6JVhTcvU6h1K+oYlDOWZj5jEARvSIc/Q4Pe0Rh86sUso3NHEox2zKKiAy1EXfxGhHjxMdFkyn6DD25+mIQylf0MShHLMx6xhDu8fiCnLuwnitlIRIHXEo5SOaOJQjKqvdbMsuZERyrE+O1yshSq9xKOUjmjiUI3blFFFZ7WZ4cpxPjpeSEMmhwnLKKmt8cjylTmaOJg4RmSIiO0UkXUTubmC/iMgT9v5NIjLa3t5DRD4Rke0islVEbq/T514ROSAiG+zHBU5+BtU6G7MKABjho8TRyy52+K0uI6uU4xxLHCLiAp4EpgKDgRkiMrhes6lAqv2YAzxlb68G7jLGDALGAbfV6/uYMWak/fjemuYqMKzfX0BCVCg94iN8crwUnVmllM84OeIYA6QbYzKMMZXAQmBavTbTgAXGshKIE5GuxphsY8x6AGNMEbAd6O5grMrL1u4/QlpKR0fvGK+rV3ztvRyaOJRympOJozuQWed1Fj/85d9sGxFJAUYBq+psnmuf2ponIh29FrHyisNF5ezPLyWtV7zPjhkbGULHyBBdf1wpH3AycTT0p6ZpSRsRiQYWA3cYYwrtzU8BfYGRQDbwaIMHF5kjImtFZG1ubm4LQ1cnYt2+owCkpfg2p/fSYodK+YSTiSML6FHndTJw0NM2IhKClTReNsa8UdvAGJNjjKkxxriBZ7FOif2AMeYZY0yaMSYtMTHxhD+M8tyafUcJDwliSDffTMWtlZIQyT69CVApxzmZONYAqSLSW0RCgenAknptlgCz7NlV44BjxphssU6M/wfYboz5W90OItK1zsvLgC3OfQTVGmv3H2FkjzhCg30727tXQhQHj5VRUa1TcpVykmP/s40x1cBc4H2si9uvGWO2isjNInKz3WwZkAGkY40ebrW3nwbMBM5uYNrtwyKyWUQ2AWcBdzr1GVTLFZVXsfVgIaem+O76Rq2UTpEYA1lHy3x+bKVOJsFOvrk9VXZZvW1P13lugNsa6PclDV//wBgz08thKi9asSefGrfhtH6dfH7snnVmVjldH0upk5neOa686sv0PCJDXYzu6fvJbsfv5dDrHEo5ShOH8qovd+cxtne8z69vAMRHhRITFqwzq5RymCYO5TUHCsrIyCthYqp/ZrGJCL06Req9HEo5TBOH8povdln3y5ye6vvrG7V6JUSxN09HHEo5SROH8pqPtufQLTac1CT/XZju2ymKrKOlOiVXKQdp4lBeUVJRzee78zh/aBef1adqSN+kaNxG1x9XykmaOJRXfLYrl8pqN+cP6eLXOPp0skY7GbnFfo1DqfZME4fyive2HCI+KtQvN/7V1TvRupdjT65e51DKKR4lDhFZLCIXiogmGvUD5VU1fLLjMOcMSvLJ+uJNiQ4LpkuHcPboiEMpx3iaCJ4CfgLsFpGHRGSggzGpNuaDbTkUVVRz6cjAWDKlT2IUGTriUMoxHiUOY8xHxpirgdHAPuBDEflaRK6zq9iqk9iitZl0j4tgXJ8Ef4cCQN/EaPbkFmNVtFFKeZvHp55EJAGYDdwIfAM8jpVIPnQkMtUmZB8r48v0PK4Y3Z0gP5+mqtUnMYqi8mryiiv9HYpS7ZJHRQ5F5A1gIPAicLExJtve9aqIrHUqOBX4Fq3Nwhi4fHSyv0M5ro9d4HBPbjGJMWF+jkap9sfT6rjP2ZVujxORMGNMhTEmzYG4VBtQXlXDghX7OaN/IimdovwdznH97BsQ0w8XB8zpM6XaE09PVf2pgW0rvBmIanuWbDxIXnEFN53ex9+hfE+32HCiQl3szinydyhKtUtNjjhEpAvQHYgQkVF8t0ZGByDS4dhUAHO7Dc99kcHALjGc1i+w/qoXEfp1jmFXjk7JVcoJzZ2qOh/rgngyUHcJ1yLgdw7FpNqApZsOsiunmCdmjPJriZHG9E+K5pOduf4OQ6l2qcnEYYyZD8wXkSuMMYt9FJMKcJXVbh75YCdDunXgomFdm+/gB/07x7BoXRZHSyrpGBXq73CUaleaO1V1jTHmJSBFRH5Rf78x5m8NdFPt3IIV+8g8Usb864cFzBTc+lI7WxfId+UUMVYvkCvlVc1dHK+dKhMNxDTwaJKITBGRnSKSLiJ3N7BfROQJe/8mERltb+8hIp+IyHYR2Soit9fpEy8iH4rIbvur79coPYllHinl0Q92cfbAJCb5cd2N5qR2tn48dx3W6xxKeVtzp6r+bX+9r6VvLCIu4EngXCALWCMiS4wx2+o0mwqk2o+xWKVNxgLVwF3GmPUiEgOsE5EP7b53A8uNMQ/Zyehu4DctjU+1nDGGe97aQpDAHy8dGpDXNmp1iw0nOixYZ1Yp5QBPixw+LCIdRCRERJaLSJ6IXNNMtzFAujEmwxhTCSwEptVrMw1YYCwrgTgR6WqMyTbGrAcwxhQB27Fmd9X2mW8/nw9c6slnUCfuuS/28vmuXH4zdSDd4yL8HU6TRIR+SdHs0sShlNd5eh/HecaYQuAirNFDf+BXzfTpDmTWeZ3Fd7/8PW4jIinAKGCVvalz7Z3r9tekhg4uInNEZK2IrM3N1dk1J2rNviP85b0dTBnShZnjevk7HI8M6BzDzkNFWrNKKS/zNHHUFjK8AHjFGHPEgz4Nnceo/z+4yTYiEg0sBu6wE5fHjDHPGGPSjDFpiYmJLemq6kk/XMxNC9bSIz6Sv1w5PKBPUdU1qGsMR0uryCms8HcoSrUrniaOpSKyA0gDlotIIlDeTJ8soEed18nAQU/b2FV3FwMvG2PeqNMmR0S62m26Aoc9/AyqFfbnl3DtvNUEBwnzrxtDbETbKYY8qGsHALZnt+hvDqVUMzwtq343MB5IM8ZUASX88HpFfWuAVBHpLSKhwHRgSb02S4BZ9uyqccAxY0y2WH/S/gfY3sCU3yXAtfbza4G3PfkMquV2HCrkqqdXUFpZzQvXjaFnQtsqFjCom5U4tmniUMqrPC1yCDAI636Oun0WNNbYGFMtInOB9wEXMM8Ys1VEbrb3Pw0swzr9lQ6UAtfZ3U8DZgKbRWSDve13dqHFh4DXROQG4FvgqhZ8BuWh97Yc4hevbSA6LJiFc8YzoEuzs68DTofwEJI7RmjiUMrLPC2r/iLQF9gA1NibDU0kDgD7F/2yetuervPcALc10O9LGr7+gTEmH5jsSdyq5Uorq3lw2XZeWvktI3rE8czMU+jcIdzfYbXaoK4d9FSVUl7m6YgjDRhsdHpKu2WM4f2th7h/6TayC8uZM6kPd53Xn7Bgl79DOyGDunZg+fYcyipriAht259FqUDhaeLYAnQBsptrqNqetfuO8Od3d7Bu/1EGdI7hiRmjSEuJ93dYXjG4awxuAztzihjZI87f4SjVLniaODoB20RkNXB8bqMx5hJHolI+sTevhAeXbefDbTkkxYTx4GXD+FFaMsEuj1cUDnhDusUCsOXAMU0cSnmJp4njXieDUL51rKyKf368mxe+3keoK4hfntef6yf2JjK0JXMl2obkjhF0jAxhc9Yxf4eiVLvh0W8KY8xnItILSDXGfCQikVgzpVQb8/muXH65aCO5xRVcdUoyvzxvAElt+OJ3c0SEYclxbDqgiUMpb/G0VtVNwOvAv+1N3YG3HIpJOcAYwxPLdzNr3mpiI0J4+7bTePjKEe06adQa3j2WXTlFlFXWNN9YKdUsT09m34Z1b0UhgDFmN43UiFKBx+02/PaNzfztw11cPqo7S382keHJcf4Oy2eGJ8dS4zZ6P4dSXuJp4qiwK9wCYN8EqFNz2wBjDPe/s42FazK57ay+PPqjEYSHnFxnGWuT5KasAr/GoVR74Wni+ExEfgdEiMi5wCJgqXNhKW+Z99U+Xvh6HzdO7M0vzxvQZgoUelOX2HCSYsL0ArlSXuJp4rgbyAU2Az/Fuhv8904FpbxjQ2YBD727nXMHd+aeCwedlEmj1vDkODZkFvg7DKXaBU9nVblF5C3gLWOMLm7RBpRV1vDzV76hc4dwHrlyxEmdNABO6dWRj7bncKSkkvioUH+Ho1Sb1uSIw65ae6+I5AE7gJ0ikisi/+eb8FRrPflJOt8eKeXhK4cTG9l2SqE7JS3FWpp+3f6jfo5EqbavuVNVd2DNpjrVGJNgjInHWhP8NBG50+ngVOtk5Bbz78/3cPmo7kzo28nf4QSEYd1jCXEJa/d7sgaZUqopzSWOWcAMY8ze2g3GmAzgGnufCkCPfriLEFcQv71gkL9DaZ3qCqip8upbhoe4GNo9lnX7dMSh1Ilq7hpHiDEmr/5GY0yuvUKfCjDbswv536ZsbjurL4kxYf4Ox3NV5bD6Gdj8GhzabG1L6AdDr4QJP4Ow6BM+RFqvjsxfsZ+K6po2X/VXKX9qbsRR2cp9yk/+/tEuYsKCuen0Pv4OxXMH1sOTp8KH/w9CouCM38CZv4PYZPjsIXhyDOz/+oQPc0qveCqr3WzR8iNKnZDmRhwjRKSh220FaP+1KtqY/fklfLAth9vO7EdcZBuZObRtCbxxE0Qlwawl0OeM7+/PXA1v3QILLoUr58Ggi1p9qFPtC+QrM45wSq/2UTZeKX9ocsRhjHEZYzo08IgxxuipqgAz/+v9uESYOb6Xv0PxzM734PXroMtwmPPJD5MGQI8xcMOH0GUYLJoN+75q9eESosMY2CWGr/f84OyrUqoF2s/CCye54opqFq3N5IJhXdvGUq8Hv4FF11oJ4ZrFENXE7K/IeLjmdYjvDa9eDUf3tfqwE/p2Yu2+o5RXacFDpVrL0cQhIlNEZKeIpIvI3Q3sFxF5wt6/SURG19k3T0QOi8iWen3uFZEDIrLBflzg5GdoK5ZsOEhRRTWzT0vxdyjNK86FhddAZCf4ySII79B8n4iO8JNXwe2GxTdBTXWrDj2hbwIV1W6++bagVf2VUg4mDhFxAU8CU4HBwAwRGVyv2VQg1X7MAZ6qs+8FYEojb/+YMWak/Vjm1cDbqNfXZdK/czSjAn2VO2Ng6c+hJBemvwzRiZ73je8DF/0NslbDF4+26vBj+8TjChJW6OkqpVrNyRHHGCDdGJNhV9ZdCEyr12YasMBYVgJxItIVwBjzOaB3a3lgT24x678t4MpTkgO/tMiG/8LOZTD5/6DbyJb3H3YlDLsKPv8r5O5scfeY8BCGdY/ly3RNHEq1lpOJozuQWed1lr2tpW0aMtc+tTVPRDo21EBE5ojIWhFZm5vbvstrvbE+iyCBS0d68q3zo4Jv4d3fQK+JMO7W1r/P+X+G0ChYeoc1gmmhSf0T2ZBZwNESnVGuVGs4mTga+tO3/v9yT9rU9xTQFxgJZAMNnrMwxjxjjEkzxqQlJrbgdEgbY4zhrW8OcnpqYmCv5ud2w1u3AgYu/RcEncCPXnQinHsffPs1bH2zxd3PHpiE28Dnu9v3HxRKOcXJxJEF9KjzOhk42Io232OMyTHG1Bhj3MCzWKfETlqbso5xoKCMi0d083coTfvmRdj3BZz/IHT0wnThUTOh81D46F6rREkLDO8eS0JUKB/vOHzicSh1EnIycawBUkWkt4iEAtOBJfXaLAFm2bOrxgHHjDHZTb1p7TUQ22XAlsbangyWbckmOEg4d1Bnf4fSuNIj1i/4nhNgtJdKnAW54Nz7oWA/rH62ZV2DhDMGJPLZrlxq3LqQpVIt5VjiMMZUA3OB94HtwGvGmK0icrOI3Gw3WwZkAOlYo4fjJ75F5BVgBTBARLJE5AZ718MisllENgFnASdtlV5jDMs2Z3Nav06BXTp9+f1QfgwufAS8efG+32ToOxk+f9hKTi1w9sAkCkqrWP+tFj1UqqU8WsipteypssvqbXu6znMD3NZI3xmNbJ/pzRjbsq0HC8k8Usbcs/r5O5TGHVgH616wLoZ3HuL99z/vj/D0RPj8EZjyoMfdzuifSKgriPe2HOLUFC0/olRL6J3jbdhH23MQgXMC9TSVuwb+dxdEd4Yzf3D/p3d0HgIjfwJrnrVmbXkoJjyESf078e7mbEwrZmYpdTLTxNGGfbzjMKN6xJEQHaDl09fPt0qLnP+AZ3eHt9aZvwMEPn2oRd2mDu3KwWPluha5Ui2kiaONOlxYzqasY0wO1NFGST58dB+knA5Dr3D2WLHdYcxNsPEVOLzD427nDO5MiEt4d8shB4NTqv3RxNFGfbLTmkp69sAkP0fSiOX3QmUxXODlC+KNmfgLay2Pj//ocZfYiBBOT01k6caDOrtKqRbQxNFGfbzjMN1iwxnYJcbfofxQ5hpYv8C6IJ400DfHjEqwVgrc8Q5krfO42+Wju5N9rJwVe/IdDE6p9kUTRxtUVePmq/R8zhiQFHi1qWqqYdldENMNzvi1b489/lar4u7yez3ucs6gznQID2bx+izn4lKqndHE0QZtyCyguKKaM/o3sYaFv6x5DrI3WlNjw3w8GgqLgdPvgr2fw55PPOoSHuLi4hHdeHdLNkXlVQ4HqFT7oImjDfpiVy5BAuP7BljiKDwIH/8J+p0Lgy/1Twxp10NsD+umQw+n2V6V1oPyKjdvbWiy2o1SyqaJow36Ij2PkT3iiI0IsLvF3/stuKvggr/65oJ4Q0LCrXtGDq6H7Us96jIiOZZh3WN5ccU+vadDKQ9o4mhjjpVWsTGzgNNTA6zi7+4PYdtbMOlX1hKv/jR8OnTqb82w8mClQBFh1vhe7MopZmWGLgGjVHM0cbQxKzLycRuYmBpAp6mqyqw7xDsNgAk/93c04AqGs38Pebtg00KPulw8ohsdI0N4/qu9DgenVNuniaONWZmRT3hIECOS4/wdync+f8SqUnvhoxAc6u9oLIMugW6jrLvJq8qbbR4e4uKacb34YFsOu3OKfBCgUm2XJo42ZmVGPmm94gkNDpB/upyt8NXjMGIG9D7d39F8RwQm/wGOZcLaeR51ue603kSEuPjXp3scDk6pti1AfvsoTxSUVrIzp4ixvQOkmmtNFbx5M0TEwXkP+DuaH+p7FvSeBF88AmXNl0+Pjwrl6rE9WbLxIPvySnwQoFJtkyaONmT13iMYA+P6Jvg7FMvnj8ChTXDR3607twPReQ9YSWP5/R41nzOpD6GuIP76/k6HA1Oq7dLE0YaszDhCWHAQw5Nj/R0KHNxg/SU//Mcw6CJ/R9O4rsNh7M2w9nnIWtts86QO4dw0qQ//25ytizwp1QhNHG3Iqr35jO7ZkbBgl38DqSqzTlFFJcLUv/g3Fk+c9TuI6QLv3OHR9NyfTupDp+gw7l+6DbcWP1TqBzRxtBHHSqvYll3IuD4BcErovbshdztM+ydEdPR3NM0Li4EpD8GhzdaCT82ICgvmngsHsiGzgJdW7fdBgEq1LY4mDhGZIiI7RSRdRH6wBJxYnrD3bxKR0XX2zRORwyKypV6feBH5UER221/bwG+uE7dmn3V9Y2wfP18Y37LYWgp24p3Q7xz/xtISg6dZpVCW3w+5zV+/uHRkd05P7cTD7+3kQEGZDwJUqu1wLHGIiAt4EpgKDAZmiMjges2mAqn2Yw7wVJ19LwBTGnjru4HlxphUYLn9ut1bmZFPaHAQI3vE+S+IIxmw5HboMRbOusd/cbSGCFzyDwiJgNdvaPbeDhHhgUuHYYzh9le+obrG7aNAlQp8To44xgDpxpgMY0wlsBCYVq/NNGCBsawE4kSkK4Ax5nOgofoP04D59vP5wKVOBB9oVu09wqgecYSH+On6RmUJvDYLglxwxX/AFWB1sjzRoStc+hTkbIaP/tBs854JkTx4+TDW7j/K3z7c5YMAlWobnEwc3YHMOq+z7G0tbVNfZ2NMNoD9tcEl8ERkjoisFZG1ubm5LQo80BSWV7H14DHG+uv6htsNb91i3ex3xX8grod/4vCG/ufD2Ftg1dOwY1mzzaeN7M70U3vwr0/38NY3B3wQoFKBz8nE0VB51PpTVDxp0yrGmGeMMWnGmLTExAArCNhCa/cdwW1gnL+ub3z+MGx7G879I6S2oesajTn3Pug6At64yZpW3Iz7pw1lbO94fv36Jr5Kz3M+PqUCnJOJIwuo+6dpMlB/wQNP2tSXU3s6y/56+ATjDHirMo4Q6gpidE8/zAPY+iZ8+mcY8RMYf5vvj++E4DCY8ao1I+zlq+DoviabhwYH8e+Zp9AnMYob5q/h6z2aPNTJzcnEsQZIFZHeIhIKTAeW1GuzBJhlz64aBxyrPQ3VhCXAtfbza4G3vRl0IFqZkc+IHrG+v76x9wt4Y451Mfyix/y3xoYTOnSFaxZDTSW8dAWUNL3meFxkKC/dOJae8ZHMnreGxet0qVl18nIscRhjqoG5wPvAduA1Y8xWEblZRG62my0DMoB04Fng1tr+IvIKsAIYICJZInKDvesh4FwR2Q2ca79ut4rKq9hy0A/3b2RvgoU/gY69YcZCa4Gk9iZxgPXZCjLh+alwrOlk0Ck6jEU/nUBaSkfuWrSRR97fqTcIqpOSnAwrnqWlpZm1a5svNxGIPtl5mOueX8NLN4z13RocRzJg3hQICoYbPoDYZN8c11/2fmElybAYmPmmlVCaUFXj5v+9tYWFazI5b3Bn/nrViMBbjVEpLxCRdcaYtPrb9c7xALcq4wghLmF0rzjfHPBIBrxwkXUK55o32n/SAKsc/Oz/WdV+550Pez5psnmIK4g/Xz6M3184iI93HObCJ77gG61rpU4imjgC3MqMfIYnxxEZGuz8wfL3wPMXWrWorl0KSQOdP2ag6DrcGl1Fd4YXL4PlTS87KyLceHofXrt5PMbAVU+v4NnPM3TNcnVS0MQRwEoqqtl84Jhv1t/I32ONNKrL4dol0GWY88cMNPG94aZPYNTVVuXf+Rdb35cmjO7ZkWU/P52zBybxwLLt3Dh/LUdLKn0UsFL+oYkjgK3bf5Qat3H+wnheOrxwIdRUWCONkzFp1AqNhGlPwmXPQM4WeGoCfPn3JkcfsZEh/HvmKdx78WC+2J3HBU98wZp9DRU9UKp90MQRwFZm5OMKEk7p5eD9G3m77aRRBde+A12GOnestmTEj+G2VVYhx4/+AM+cCd+uarS5iDD7tN4svmUCocFBTH9mJU9+kq6nrlS7pIkjgK3ae4ThybFEhTl0fSN3l3V6yl1tjTQ6169BeZLr0A2mvww/ehHKjsC88+Ct26C48RI2w5JjeednE5k6tAt/fX8nv359kxZIVO2OJo4AVVpZzcbMAsb2dug0Ve5OmH8RmBqY/Y4mjaYMvgRuWw2n3QGbFsI/T4E1z4G7psHmMeEh/GPGKG6fnMqidVnc/NJ6yqsabqtUW6SJI0Ct23+UardxZv2NwzuskYYx1umppEHeP0Z7ExZt1bi65WurztX/7oJnz2p0OVoR4c5z+3PfJUNYviOHWfNWU1LR/OqDSrUFmjgC1Nd78gkOEk5N8XLiyEu3ZguBNdI4mabcekPiAJi1BK6cB8WH4blzYMnPGy1Zcu2EFP7+45Gs3XeEm19aR2W1nrZSbZ8mjgD19Z58RvSII9qb1zeO7oMFl4BxW0mjmTukVSNEYOgVMHcNTJgLG162Tl+tfd4qQV/PtJHdeejy4XyxO4+7Fm3UMiWqzdPEEYAKy6vYnFXAaX29eH3j2AFrpFFZArPe0qThDWExcN6f4OYvIWkIvHOHdQH9SMYPmv7o1B78ZspAlm48yH1Lt+psK9WmaeIIQKsyrPU3xvf1Um2qohxrpFFWADPfOLnv03BC0iBrBHfZM5C3C54+Hb552bqGVMfNZ/Thxom9mb9iPy+u3O+nYJU6cZo4AtDXe/IICw5iVM+4E3+zsqPw4qVQeBCuXgTdTznx91Q/JGLd+3HL19B1JLx9Kyy+0RrhHW8i/O6CQUwemMT9S7exKqPpUu5KBSpNHAFoxZ58Tk2JP/H1N6orYOHVkJ8OM16BnuO8E6BqXGyyVbLl7N/DlsXw3LnfO3UVFCQ8Nn0kPeMjue2/6zlYUObHYJVqHU0cASavuIIdh4oYf6LXN2rXCd//FVz6FPQ50yvxKQ8EuWDSr+Ca16HwgHXXeZ2Kux3CQ3hm1imUV7m55aV1eo+HanM0cQSYFXus0xcTTjRxLL/P+ov3nHth2JUnHphquX7nwJxPoUN3ePlK2Ljwu11JMTz6oxFszDrGA//b7r8YlWoFTRwB5us9+cSEBTOse2zr32TDK/DV3yHtButuZ+U/8b3h+veg1wR486fwxaPHL5qfP6QLcyb14cWV+1my8aCfA1XKc5o4AszXe/IY2yeeYFcr/2my1sLS26H3JJj6l/a1TnhbFR4LVy+GYVfB8vvhg98fTx6/On8Ap/TqyG8Xb2JPbrGfA1XKM5o4AsiBgjL255e2fhpuYbZ1MTymC1w1H1y6nGnACA61puuOmQMr/gnv/RaMIcQVxD9/MorQ4CBue3k9ZZV6vUMFPkcTh4hMEZGdIpIuInc3sF9E5Al7/yYRGd1cXxG5V0QOiMgG+3GBk5/Blz7fZVVdndivFYmjuhJemwkVRdYMqkgfLP6kWiYoCKY+DONuhVVPwbJfgdtN19gIHvvxSHbmFPGHJVv8HaVSzXJsPVIRcQFPAucCWcAaEVlijNlWp9lUINV+jAWeAsZ60PcxY8wjTsXuL5/uPEy32HD6d45ueeeP7oWsNXDVC9B5iLdDU94iAuc/aM28+vofVkn7C//GmQOSmHtWP/7xcTqnpsRzVVoPf0eqVKOcHHGMAdKNMRnGmEpgITCtXptpwAJjWQnEiUhXD/u2K5XVbr7cnccZA5KQll6X2L4UVj4JY34KQy5zJkDlPSJw7h9h4p2w7nmrVIkx3HFOf8b3SeD/vb2FnYeK/B2lUo1yMnF0BzLrvM6yt3nSprm+c+1TW/NEpMHl8URkjoisFZG1ubmNL7wTKNbuP0JJZQ1nDUhsWccje63FhbqNhvP+6ExwyvtEYPIfYOIvYP18ePc3uAQenzGS6LAQbnl5nZZhVwHLycTR0J/N9Su7Ndamqb5PAX2BkUA28GhDBzfGPGOMSTPGpCUmtvCXsR98ujOXEJdwWkuub1RXwKLZ1nfrquchOMyp8JQTRGDy/1nXPFb/Gz76A0nRYTwxYyT78kr43ZubtRiiCkiOXePAGiXUPVGbDNSfrN5Ym9DG+hpjcmo3isizwDveC9k/jDF8tC2Hsb0TWrZM7Pv3QPYGmP5f6JjiVHjKSbXXPKor4KvHITiCCWf9ll+c259HPtjFmN7xXD22l7+jVOp7nBxxrAFSRaS3iIQC04El9dosAWbZs6vGAceMMdlN9bWvgdS6DGjz01DSDxeTkVfC+UM6e95pyxuw5lkYPxcGXuhccMp5InDBIzDyGvjsIfjyMW49sx+T+idy35JtbDlwzN8RKvU9jiUOY0w1MBd4H9gOvGaM2SoiN4vIzXazZUAGkA48C9zaVF+7z8MisllENgFnAXc69Rl85f2thwA4d3AXzzrk77FWnUseY5UUUW1fUBBc8gQMvRI+upeg1U/z9x+PJD4qlFtfXs+Rkkp/R6jUcXIynENNS0sza9c2vDZ0ILjoH18Q4grizVtPa75xVZlVcbXwANz8hVWNVbUfNVXWdasd78BFf2d90qXMeGYlQ7p14OUbxxEReoIVk5VqARFZZ4xJq79d7xz3s6yjpWw5UMj5Qzwcbbz7G8jZDJc/o0mjPXKFwJXPQ+r58M6djD7yHo9PH8k3mQXcvvAbanTZWRUANHH4WW1xuwuGdm2mJdaqcuvnW1M4U891ODLlN8Gh8KMF0OcMePtWpvA1f7hoMB9sy+HeJbrsrPI/TRx+ZIzhzfUHSOvVkZ4JkU03zt4E//uFVbzwrHt8E6Dyn5Bwa7Zcj3Gw+CZmx2/lp3Yl3fuWbsOtIw/lR5o4/GhbdiG7Dxdz6aj690XWU1Zg1aGK6AhXzAOXk7OoVcAIjYKrX4Nuo2DRbO7us5cbJ/bmha/3cc9bmzV5KL/RxOFHb64/QIhLuHBYE6ep3G5482Y4lmVVvI0O/JsZlReFxcA1i6HLMOTVa7in+wbmntWPV1ZncteijVRWu/0doToJaeLwk/KqGhavz2LywM50jAptvOFXf4dd71o3ifUc67P4VACJiLPWMU+ZiLx9C7+M+YBfntefN785wE+eXcnhonJ/R6hOMpo4/OSdTdkcLa1i5vgm7gre9T58/EcYeoW1joM6eYXFwNWLYPA0+OD3zC17mn/8eDhbDh7jkn98xcbMAn9HqE4imjj85MUV++ibGNX42uLZm2DRddBlOFzyD13JT1m1yK58Hib8DNY8x8UbfsriawfhChKuenoFT326R6frKp/QxOEH6/YfZWPWMWaO69VwCfXCbPjvj61TFDMWWhdJlQJrHY/z/gSXPwsH1jFkyYUsvcTF2QOT+Mt7O7jq6a/J0CVolcM0cfjBE8t3Ex8V2vBiPWUF8N+roKIQfvIqdPDg/g518hn+I7j+PQgOJf61S3iq02Iev3Iw6YeLmfL4Fzz6wU5KK7Usu3KGJg4f25BZwGe7crnp9D4/rIRbXggvXQGHd1gzqLoM80+Qqm3oNgpu/hJOvRFZ9STTVlzJh9PcTB3ShX98nM7kRz/jrW8O6LRd5XWaOHzIGMMj7++kY2QIs+pfFK8ohv/+yCqT/qP5kHqOX2JUbUxoFFz4KMx8E4DOb0/n8ap7WXRlJ+KjQrnj1Q1MffwL3t2crQlEeY0mDh9atvkQX6bnccc5/b8/2ig9Ai9fCZmr4IrntEy6arm+Z8OtK2HKX+DgBk595zyWdPgrT5wZRFWNm1teXs/Ux7/g1TXfUl5V4+9oVRun1XF9pKi8inP/9jkJ0aEsmTsRV5B9UfxIBrx8FRR8C5f9G4Ze7tc4VTtQVgDrXoBV/4aig9R06MmSTjfy75xB7MivomNkCDPG9GTm+F50jY3wd7QqgDVWHVcThw8YY/jZK9+wbHM2r98ygdE97WXS938Nr14Dxg3TX4Fe4/0Wo2qHqith+xLY9Crs+RhTU82K8Im8EHQZHx7tQpAIZ/bvxKWje3DOoM5asl39QGOJQ4se+cCCFft5Z1M2vzp/gJU0qivh0wfhy79DfG/4ySLo1M/fYar2JjgUhl1pPUrykZ3/Y0LGp0zY+xCZofBSzWTe3jWR5TvziAqqYkrSUS7uI4zrk0h4h07WdPCIjhAeZ72XUjYdcTjsrW8OcOdrG5g8MIlnZqYRdHAdLL3DWlNj9Cw4/88QFu2X2NRJyhjI2w3ZG6nJ3siqvQW8dbgL75YOoIhIIihnQtA2zgzawJlBG+kRlAtBweAKsxJIcDi4Qq0bEl1h1hoirhAICrEKcAbVvg5uZLv9OjjC+tkPjYLQGPtrlLUtLBaiEqykpTe/+o2eqvJx4jDG8PxX+3hg2XbGpMTz/EWxhH/+J2tlt6gkuPhxGHiBT2NSqinlldWs2LaXT7dl8cneUr4tsrZ3C69iVIciRsYU0j+igD4hBXQPPkZQTQVUV4C7ylq50F1tf62CmmpMTRWl1cKR6lCOVIeRXx1Ofk0E+TVR5LujKDahVOOiygQThCFcKginkjgpoQtH6CJH6BJ0jK6RhpiYGIhMsB7RSdChu/WI7Q4dukFMNx0VOUAThw8Tx4GCMv64dBvvbT3EeT3cPBb1IlH7PoDQaDjt5zDuVh1lqIBmjGFvXgmf7cpl/bcFrN9/lAMFZcf3hwYHkRAVSlxkKLERwQSJYAzUuA2F5VUcLa3kaGlVo9V7w4KDiAkLJtQlBAcZ3G435dVuyqvcFFf9sH1ScCn9QvJJDTpIv5oMUt276ScHSaDQHpCInVC62Qkl+btHB/trdGdrbXflMb8kDhGZAjwOuIDnjDEP1dsv9v4LgFJgtjFmfVN9RSQeeBVIAfYBPzLGHG0qDl8kDmMMmzMLWPjVNhZvPoqYGu4IW8oc8zpBsd1h1NUw5qfW8FupNiivuIL0w8XszSthX14J+SWVFJRWUVhWhdsYgkQQgQ4RIXSMDKFjpJVY4qNCSIgKIyE69PjXyFBXw+V2gIrqGg4XVnCosJxDx8o5UFBG+uHi44/iiu/uiO8YBv1iqugXXkS/4BxSzX76Vu6gS/F2XFVF33/joBCrEkNsDzuh1CaYHlbCiU6CiHivrXdjjMFtwG0MbmMwBoJECHFJo5890Pg8cYiIC9gFnAtkAWuAGcaYbXXaXAD8DCtxjAUeN8aMbaqviDwMHDHGPCQidwMdjTG/aSqWVicOdw1UlUJV2XdfK0uhqpTiglw+3VPIjtwKthcEs7k4msM10YRSyWWur/hZ7Nck9x8JQy6HvmdZNYaUUifEGMOhwnJ25xSz+3gyKWL34WIKSr8bqriChC4xoXSPhuTwShJdRcS6C+hYnUvHimw6lB8grDSbMFNOKFWEYfWtwYU7PI7qiE7UhMfjjoinLCSeElcMxURSIpEUE0GJO4xidyjFNSEUVkFxFRRVQnGlm+JKQ1FFDcWVNTT06zU4SIgIdREZ6iIyNJiIEBfRYcFEhwcf/xoTFkzM8dchRNd5HRMeTESoi+CgIIKDhGCXWM9dQnCQd5OSP2ZVjQHSjTEZdgALgWnAtjptpgELjJW9VopInIh0xRpNNNZ3GnCm3X8+8CnQZOJotf/dBeueb3DXMZPA3Ip/4KKGvsG5jI86yOldDecMTCKu742Q+Fe9qKeUl4kIXWMj6BobwaT+3y1qZowhv6SS9MPFZOSWcKCglANHyzhQUMbKPCGvRKisjgaSgVFNH6QSKGw+lnBKiKGUGCkjhjKipYwkSomWMmIoJTqonBCpJgg3Aghu3LgoJZzS6jDKqsIpKQmnjDCKu47jcFEoGbnVFFdUU1ReTUUrF+lyBQlBAoI1Anx2Vtr3vlfe4GTi6A5k1nmdhTWqaK5N92b6djbGZAMYY7JFJKmhg4vIHKB2EYtiEdnZis/QCchreFchcBEAGcCHwBOtOMAJaCI2v9K4WkbjarlAjS0g4zrjgROKq8EFg5xMHA39uV1/4NZYG0/6NskY8wzwTEv61CciaxsapgWCQI1N42oZjavlAjW2kykuJ6cYZAF164YnAwc9bNNU3xz7dBb218NejFkppVQznEwca4BUEektIqHAdGBJvTZLgFliGQccs09DNdV3CXCt/fxa4G0HP4NSSql6HDtVZYypFpG5wPtYU2rnGWO2isjN9v6ngWVYM6rSsabjXtdUX/utHwJeE5EbgG+Bq5z6DJzgqS6HBWpsGlfLaFwtF6ixnTRxnRQ3ACqllPIevY1SKaVUi2jiUEop1SKaOOoQkX0isllENojIWntbvIh8KCK77a8d/RBXnIi8LiI7RGS7iIz3d1wiMsD+PtU+CkXkDn/HZcd2p4hsFZEtIvKKiIQHQlx2bLfbcW0VkTvsbT6PTUTmichhEdlSZ1ujcYjIb0UkXUR2isj5Po7rKvv75RaRtHrt/RnXX+3/k5tE5E0RifN1XE3E9kc7rg0i8oGIdPNqbMYYfdgPrNpXneptexi4235+N/AXP8Q1H7jRfh4KxAVCXHXicwGHsG4W8mtcWDeP7gUi7NevAbP9HZd93KHAFiASa2LKR0CqP2IDJgGjgS11tjUYBzAY2AiEAb2BPYDLh3ENAgZgVYlIq7Pd33GdBwTbz//ij+9XE7F1qPP858DT3oxNRxzNm4b1ixv766W+PLiIdMD6wfgPgDGm0hhT4O+46pkM7DHG7Ccw4goGIkQkGOuX9MEAiWsQsNIYU2qMqQY+Ay7zR2zGmM+BI/U2NxbHNGChMabCGLMXaxbkGF/FZYzZboxpqPKDv+P6wP53BFiJdb+ZT+NqIra6RVOi+O4Gaq/Eponj+wzwgYiss0uWQL0SJ0CDJU4c1AfIBZ4XkW9E5DkRiQqAuOqaDrxiP/drXMaYA8AjWFO1s7HuDfrA33HZtgCTRCRBRCKxpqL3CJDYaCKOxkoD+VsgxXU98K79PCDiEpEHRCQTuBr4P2/Gponj+04zxowGpgK3icgkfweE9dfzaOApY8wooATrNEJAsG/QvARY5O9YAOzz8tOwhuHdgCgRuca/UVmMMduxTml8CLyHdcqguslOgeGESwA5JCDiEpF7sP4dX67d1EAzn8dljLnHGNMDK6659mavxKaJow5jzEH762HgTawhnL9LnGQBWcaYVfbr17ESib/jqjUVWG+MybFf+zuuc4C9xphcY0wV8AYwIQDiAsAY8x9jzGhjzCSs0wu7AyW2JuLwpHyQP/g9LhG5Fqva6dXGvogQCHHV81/gCvu5V2LTxGETkSgRial9jnXhawt+LnFijDkEZIrIAHvTZKzy8oFSemUG352mAv/H9S0wTkQiRUSwvl/bAyAuAMSu5iwiPYHLsb53ARFbE3EsAaaLSJiI9Ma6oL/aD/HV59e4xFps7jfAJcaY0kCJy44ttc7LS4AdXo3NqSv9be2BdS1ho/3YCtxjb08AlmP9ZbgciPdDbCOBtcAm4C2gY4DEFQnkA7F1tgVCXPfZ/1G2AC9izSDxe1x2bF9gJf6NwGR/fc+wElY2UIX1V+gNTcUB3IM1A2cnMNXHcV1mP68AcoD3AySudKzrBRvsx9O+jquJ2BbbP/+bgKVAd2/GpiVHlFJKtYieqlJKKdUimjiUUkq1iCYOpZRSLaKJQymlVIto4lBKKdUimjjUSUlEauzKoRtFZL2ITLC3p9StMnqCx/i0tpqrfFd5eaNdrbSLN46hlD9o4lAnqzJjzEhjzAjgt8CffXDMs+zjrQV+V3eHWHzy/1FEXL44jmq/NHEoBR2Ao/U3irWOx/P2SOEbETmrme0RIrLQXgfhVSCikeN9DvSzRzfbReRfwHqgh4j8SkTW2O9xn/2+USLyP3u0skVEfmxvf0hEttltH7G3vSAiV9b5DMX21zNF5BMR+S+wWURcYq0nUXusn3rpe6lOAsH+DkApP4kQkQ1AONAVOLuBNrcBGGOGichArMrJ/ZvYfgtQaowZLiLDsZJBQy4CNtvPBwDXGWNuFZHzsEpAjMEqRrfELrSZCBw0xlwIICKxIhKPdUf1QGOMkTqLCDVhDDDUGLPXrv58zBhzqoiEAV+JyAfGKrWtVJN0xKFOVrWnqgYCU4AFdm2ruiZilSzBGLMD2A/0b2L7JOAle/smrHIPdX1iJ6sOfHdqbL8xZqX9/Dz78Q1W0hmIlUg2A+eIyF9E5HRjzDGgECgHnhORy4G6tZIas7pOYjgPmGXHswqr3EhqYx2VqktHHOqkZ4xZISKdsP6yr6uhEtRNbYemS1SfZYzJO/4m1iihpN77/tkY8+8fHFDkFKz1O/5sjwzuF5ExWEUcp2OVzT4bq7x3kN1HsFaMrFX/WD8zxrzfRLxKNUhHHOqkZ59ucmEVbKzrc6xFcLBPRfXEKgznyfahwPAWhvI+cL2IRNvv0V1EksRaL7rUGPMS1iJVo+02scaYZcAdWIUwwVr++BT7+TQgpIlj3SIiIbWfw64KrVSzdMShTla11zjA+uv7WmNMTb2zVf8CnhaRzVh/yc82xlTYF7Mb2v4U1kqNm7CqpbaoXLUx5gMRGQSssOMoBq4B+gF/FRE3VgXUW4AY4G0RCbfjv9N+m2ft7auxKtyW0LDngBRgvT0yycW/yw+rNkSr4yqllGoRPVWllFKqRTRxKKWUahFNHEoppVpEE4dSSqkW0cShlFKqRTRxKKWUahFNHEoppVrk/wOccIstss3EowAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.kdeplot(data = df, x = \"BloodPressure\", hue=\"Outcome\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There is no much of a difference in BP between people with diabetes and healthy people"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### INSULIN"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Insulin', ylabel='Density'>"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.kdeplot(data=df, x = \"Insulin\", hue=\"Outcome\")# k density plot of Insulin for different Outcome values "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "People with high Insulin seem to have Diabetes. We can use this for classification.\n",
    "\n",
    "The large number in the middle corresponds to NA values which we have imputed with median.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### BMI"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='BMI', ylabel='Density'>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.kdeplot(data=df,x=\"BMI\",hue=\"Outcome\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "People with high BMI have high chance of getting Diabities"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# MODEL TRAINING"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## TRAIN_TEST Split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "target=df.Outcome\n",
    "inputs=df.drop('Outcome',axis='columns',inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1\n",
       "1    0\n",
       "2    1\n",
       "3    0\n",
       "4    1\n",
       "Name: Outcome, dtype: int64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "target.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>148.0</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>35.00000</td>\n",
       "      <td>125.0</td>\n",
       "      <td>33.6</td>\n",
       "      <td>0.627</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>85.0</td>\n",
       "      <td>66.000000</td>\n",
       "      <td>29.00000</td>\n",
       "      <td>125.0</td>\n",
       "      <td>26.6</td>\n",
       "      <td>0.351</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8</td>\n",
       "      <td>183.0</td>\n",
       "      <td>64.000000</td>\n",
       "      <td>29.15342</td>\n",
       "      <td>125.0</td>\n",
       "      <td>23.3</td>\n",
       "      <td>0.672</td>\n",
       "      <td>32</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>89.0</td>\n",
       "      <td>66.000000</td>\n",
       "      <td>23.00000</td>\n",
       "      <td>94.0</td>\n",
       "      <td>28.1</td>\n",
       "      <td>0.167</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>137.0</td>\n",
       "      <td>75.095827</td>\n",
       "      <td>35.00000</td>\n",
       "      <td>168.0</td>\n",
       "      <td>43.1</td>\n",
       "      <td>2.288</td>\n",
       "      <td>33</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
       "0            1    148.0      72.000000       35.00000    125.0  33.6   \n",
       "1            1     85.0      66.000000       29.00000    125.0  26.6   \n",
       "2            8    183.0      64.000000       29.15342    125.0  23.3   \n",
       "3            1     89.0      66.000000       23.00000     94.0  28.1   \n",
       "4            0    137.0      75.095827       35.00000    168.0  43.1   \n",
       "\n",
       "   DiabetesPedigreeFunction  Age  \n",
       "0                     0.627   50  \n",
       "1                     0.351   31  \n",
       "2                     0.672   32  \n",
       "3                     0.167   21  \n",
       "4                     2.288   33  "
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "x_train,x_test,y_train,y_test=train_test_split(df,target,test_size=0.3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(537, 8)\n",
      "(537,)\n",
      "(231, 8)\n",
      "(231,)\n"
     ]
    }
   ],
   "source": [
    "print(x_train.shape)\n",
    "print(y_train.shape)\n",
    "print(x_test.shape)\n",
    "print(y_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.naive_bayes import GaussianNB\n",
    "model=GaussianNB()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GaussianNB()"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7359307359307359"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.score(x_test,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>482</th>\n",
       "      <td>4</td>\n",
       "      <td>85.0</td>\n",
       "      <td>75.095827</td>\n",
       "      <td>22.00000</td>\n",
       "      <td>49.0</td>\n",
       "      <td>27.800000</td>\n",
       "      <td>0.306</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>131</th>\n",
       "      <td>9</td>\n",
       "      <td>122.0</td>\n",
       "      <td>75.095827</td>\n",
       "      <td>29.15342</td>\n",
       "      <td>125.0</td>\n",
       "      <td>33.300000</td>\n",
       "      <td>1.114</td>\n",
       "      <td>33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>322</th>\n",
       "      <td>0</td>\n",
       "      <td>124.0</td>\n",
       "      <td>70.000000</td>\n",
       "      <td>20.00000</td>\n",
       "      <td>125.0</td>\n",
       "      <td>27.400000</td>\n",
       "      <td>0.254</td>\n",
       "      <td>36</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>145</th>\n",
       "      <td>0</td>\n",
       "      <td>102.0</td>\n",
       "      <td>75.000000</td>\n",
       "      <td>23.00000</td>\n",
       "      <td>125.0</td>\n",
       "      <td>32.457464</td>\n",
       "      <td>0.572</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>627</th>\n",
       "      <td>0</td>\n",
       "      <td>132.0</td>\n",
       "      <td>78.000000</td>\n",
       "      <td>29.15342</td>\n",
       "      <td>125.0</td>\n",
       "      <td>32.400000</td>\n",
       "      <td>0.393</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>268</th>\n",
       "      <td>0</td>\n",
       "      <td>102.0</td>\n",
       "      <td>75.095827</td>\n",
       "      <td>29.15342</td>\n",
       "      <td>125.0</td>\n",
       "      <td>25.100000</td>\n",
       "      <td>0.078</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>221</th>\n",
       "      <td>2</td>\n",
       "      <td>158.0</td>\n",
       "      <td>90.000000</td>\n",
       "      <td>29.15342</td>\n",
       "      <td>125.0</td>\n",
       "      <td>31.600000</td>\n",
       "      <td>0.805</td>\n",
       "      <td>66</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>582</th>\n",
       "      <td>12</td>\n",
       "      <td>121.0</td>\n",
       "      <td>78.000000</td>\n",
       "      <td>17.00000</td>\n",
       "      <td>125.0</td>\n",
       "      <td>26.500000</td>\n",
       "      <td>0.259</td>\n",
       "      <td>62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>451</th>\n",
       "      <td>2</td>\n",
       "      <td>134.0</td>\n",
       "      <td>70.000000</td>\n",
       "      <td>29.15342</td>\n",
       "      <td>125.0</td>\n",
       "      <td>28.900000</td>\n",
       "      <td>0.542</td>\n",
       "      <td>23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>292</th>\n",
       "      <td>2</td>\n",
       "      <td>128.0</td>\n",
       "      <td>78.000000</td>\n",
       "      <td>37.00000</td>\n",
       "      <td>182.0</td>\n",
       "      <td>43.300000</td>\n",
       "      <td>1.224</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin        BMI  \\\n",
       "482            4     85.0      75.095827       22.00000     49.0  27.800000   \n",
       "131            9    122.0      75.095827       29.15342    125.0  33.300000   \n",
       "322            0    124.0      70.000000       20.00000    125.0  27.400000   \n",
       "145            0    102.0      75.000000       23.00000    125.0  32.457464   \n",
       "627            0    132.0      78.000000       29.15342    125.0  32.400000   \n",
       "268            0    102.0      75.095827       29.15342    125.0  25.100000   \n",
       "221            2    158.0      90.000000       29.15342    125.0  31.600000   \n",
       "582           12    121.0      78.000000       17.00000    125.0  26.500000   \n",
       "451            2    134.0      70.000000       29.15342    125.0  28.900000   \n",
       "292            2    128.0      78.000000       37.00000    182.0  43.300000   \n",
       "\n",
       "     DiabetesPedigreeFunction  Age  \n",
       "482                     0.306   28  \n",
       "131                     1.114   33  \n",
       "322                     0.254   36  \n",
       "145                     0.572   21  \n",
       "627                     0.393   21  \n",
       "268                     0.078   21  \n",
       "221                     0.805   66  \n",
       "582                     0.259   62  \n",
       "451                     0.542   23  \n",
       "292                     1.224   31  "
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_test[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "482    0\n",
       "131    1\n",
       "322    1\n",
       "145    0\n",
       "627    0\n",
       "268    0\n",
       "221    1\n",
       "582    0\n",
       "451    1\n",
       "292    1\n",
       "Name: Outcome, dtype: int64"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 0, 0, 0, 0, 1, 1, 0, 1], dtype=int64)"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.predict(x_test[:10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.9881877 , 0.0118123 ],\n",
       "       [0.29186538, 0.70813462],\n",
       "       [0.97180491, 0.02819509],\n",
       "       [0.98242907, 0.01757093],\n",
       "       [0.93749057, 0.06250943],\n",
       "       [0.99082162, 0.00917838],\n",
       "       [0.06398798, 0.93601202],\n",
       "       [0.34955859, 0.65044141],\n",
       "       [0.94825577, 0.05174423],\n",
       "       [0.10639975, 0.89360025]])"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.predict_proba(x_test[:10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [07/Dec/2021 22:59:53] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [07/Dec/2021 22:59:53] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n",
      "127.0.0.1 - - [07/Dec/2021 23:00:36] \"\u001b[37mPOST /sub HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask,render_template,request\n",
    "\n",
    "app=Flask(__name__)\n",
    "\n",
    "@app.route(\"/\")\n",
    "def hello():\n",
    "    return render_template(\"Form.html\")\n",
    "@app.route(\"/sub\",methods=[\"POST\"])\n",
    "def submit():\n",
    "    if request.method=='POST':\n",
    "        \n",
    "        name=request.form[\"firstname\"]\n",
    "        age=int(request.form[\"age\"])\n",
    "        preg=int(request.form[\"preg\"])\n",
    "        glu=float(request.form[\"Glucose\"])\n",
    "        bp=float(request.form[\"bp\"])\n",
    "        thick=float(request.form['skin'])\n",
    "        ins=float(request.form['insulin'])\n",
    "        bmi=float(request.form['BMI'])\n",
    "        sc=float(request.form['score'])\n",
    "        new_input=[[preg,glu,bp,thick,ins,bmi,sc,age]]\n",
    "        new_output=int(model.predict(new_input))\n",
    "        if(new_output==0):\n",
    "            op='No'\n",
    "        else:\n",
    "            op='Yes'\n",
    "    return render_template(\"result.html\",na=name,ag=age,pr=preg,gl=glu,b=bp,thi=thick,insu=ins,bm=bmi,scr=sc,dia=op)\n",
    "if __name__==\"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
