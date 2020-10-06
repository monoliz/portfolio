{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Задание 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Выберите один верный ответ. “Коэффициент корреляции между количеством сна и уровнем счастья равен нулю” - это..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "  +1) Нулевая гипотеза\n",
    "   2) Альтернативная гипотеза\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Задание 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Выберите один верный ответ. Если уровень значимости 0.10, а p-значение равно 0.7, то необходимо..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " 1)отвергнуть нулевую гипотезу\n",
    "+2)не отвергать нулевую гипотезу\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Задание 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Выберите все подходящие ответы. Что из перечисленного является \n",
    "статистической гипотезой?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "+1)  Случайная величина X имеет \n",
    "     нормальное распределение\n",
    " 2)  Среднее арифметическое \n",
    "     признака A равно 52.5\n",
    "+3)  Средний вес упаковки яблок составляет 1300 г.\n",
    " 4)  Дисперсия случайной величины X \n",
    "     не больше 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Задание 4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Парфюмерная компания хочет узнать возраст женщин, которые являются их покупательницами. Ранее уже было изучено, что средний возраст  был 37, а среднеквадратичное отклонение равно 3.4. Размер выборки - 200 человек. Рассчитайте 95% доверительный интервал для среднего возраста. Представьте все необходимые вычисления."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Нижняя граница: 36.52878404101728 , Верхняя граница: 37.47121595898272 . С вероятностью 0.95  можно утверждать, что среднее значение при выборке большего объема не выйдет за пределы найденного интервала, т.е. средний возраст покупательниц парфюмерии будет оставаться примерно таким же\n"
     ]
    }
   ],
   "source": [
    "\n",
    "X=37 #средний возраст\n",
    "s=3.4  # стандартное отклонение\n",
    "n=200  #выборка\n",
    "z=1.96 #т.к n>30, то определяем значение z по таблицам функции Лапласа, ищем значение  \n",
    "       #(0.95/2=0.475), \n",
    "       #z= (0.475) = 1.96\n",
    "    #формула\n",
    "mean_low=X-z*(s/(n**0.5))\n",
    "mean_high=X+z*(s/(n**0.5))\n",
    "print( 'Нижняя граница:', mean_low ,', ''Верхняя граница:',mean_high,\n",
    "      '. ''С вероятностью 0.95  можно утверждать, что среднее значение при выборке '\n",
    "      'большего объема не выйдет за пределы найденного интервала, т.е. средний возраст'\n",
    "      ' покупательниц парфюмерии будет' \n",
    "      ' оставаться примерно таким же' )\n",
    " \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Задание 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Перед Вами данные результатов экзаменов для детей средней школы."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
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
       "      <th>gender</th>\n",
       "      <th>race</th>\n",
       "      <th>parenteducation</th>\n",
       "      <th>lunch</th>\n",
       "      <th>testprepcourse</th>\n",
       "      <th>mathscore</th>\n",
       "      <th>readingscore</th>\n",
       "      <th>writingscore</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>female</td>\n",
       "      <td>group A</td>\n",
       "      <td>some high school</td>\n",
       "      <td>standard</td>\n",
       "      <td>completed</td>\n",
       "      <td>78</td>\n",
       "      <td>83</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>female</td>\n",
       "      <td>group C</td>\n",
       "      <td>some high school</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>69</td>\n",
       "      <td>71</td>\n",
       "      <td>78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>bachelor's degree</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>completed</td>\n",
       "      <td>58</td>\n",
       "      <td>65</td>\n",
       "      <td>71</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>female</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>69</td>\n",
       "      <td>72</td>\n",
       "      <td>70</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>female</td>\n",
       "      <td>group C</td>\n",
       "      <td>high school</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>67</td>\n",
       "      <td>72</td>\n",
       "      <td>67</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>995</th>\n",
       "      <td>male</td>\n",
       "      <td>group A</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>68</td>\n",
       "      <td>60</td>\n",
       "      <td>55</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>996</th>\n",
       "      <td>male</td>\n",
       "      <td>group C</td>\n",
       "      <td>associate's degree</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>none</td>\n",
       "      <td>76</td>\n",
       "      <td>70</td>\n",
       "      <td>66</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>997</th>\n",
       "      <td>male</td>\n",
       "      <td>group B</td>\n",
       "      <td>some high school</td>\n",
       "      <td>standard</td>\n",
       "      <td>completed</td>\n",
       "      <td>50</td>\n",
       "      <td>43</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>998</th>\n",
       "      <td>male</td>\n",
       "      <td>group D</td>\n",
       "      <td>some college</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>none</td>\n",
       "      <td>34</td>\n",
       "      <td>28</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999</th>\n",
       "      <td>male</td>\n",
       "      <td>group E</td>\n",
       "      <td>associate's degree</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>none</td>\n",
       "      <td>97</td>\n",
       "      <td>79</td>\n",
       "      <td>73</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1000 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     gender     race     parenteducation         lunch testprepcourse  \\\n",
       "0    female  group A    some high school      standard      completed   \n",
       "1    female  group C    some high school      standard           none   \n",
       "2    female  group B   bachelor's degree  free/reduced      completed   \n",
       "3    female  group C        some college      standard           none   \n",
       "4    female  group C         high school      standard           none   \n",
       "..      ...      ...                 ...           ...            ...   \n",
       "995    male  group A        some college      standard           none   \n",
       "996    male  group C  associate's degree  free/reduced           none   \n",
       "997    male  group B    some high school      standard      completed   \n",
       "998    male  group D        some college  free/reduced           none   \n",
       "999    male  group E  associate's degree  free/reduced           none   \n",
       "\n",
       "     mathscore  readingscore  writingscore  \n",
       "0           78            83            85  \n",
       "1           69            71            78  \n",
       "2           58            65            71  \n",
       "3           69            72            70  \n",
       "4           67            72            67  \n",
       "..         ...           ...           ...  \n",
       "995         68            60            55  \n",
       "996         76            70            66  \n",
       "997         50            43            44  \n",
       "998         34            28            22  \n",
       "999         97            79            73  \n",
       "\n",
       "[1000 rows x 8 columns]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df=pd.read_csv('examscore.csv')\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Обработайте данные на предмет пропусков и проверьте гипотезу о том, что между средними оценками по математике для мальчиков и девочек нет статистических различий. Представьте все необходимые вычисления и содержательную интерпретацию."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "gender\n",
      "female    62.851546\n",
      "male      68.469903\n",
      "Name: mathscore, dtype: float64\n",
      "gender\n",
      "female    485\n",
      "male      515\n",
      "Name: mathscore, dtype: int64\n",
      "Чтобы оценить, насколько далеко попадает наша наблюдаемая разность от наших ожиданийпо нулевой гипотезе, мы считаем z-статистику\n",
      "gender\n",
      "female    248.254775\n",
      "male      306.440240\n",
      "Name: mathscore, dtype: float64\n",
      "gender\n",
      "female    15.756103\n",
      "male      17.505435\n",
      "Name: mathscore, dtype: float64\n",
      "t= -5.339575429638625\n",
      "t  крит по табличному значению =1.96, t вычисленное по модулю больше, это значит,что статистические различия все таки есть\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "#Проверка на наличие значения NaN (пропусков и пустых значений)\n",
    "df.isnull().values.any()\n",
    "\n",
    "#Поиск средних значений по математике:\n",
    "print(df.groupby('gender')['mathscore'].mean())\n",
    "\n",
    "#считаем выборку\n",
    "print(df.groupby('gender')['mathscore'].count())\n",
    "\n",
    "print('Чтобы оценить, насколько далеко попадает наша наблюдаемая разность от наших ожиданий'\n",
    "      'по нулевой гипотезе, мы считаем z-статистику')\n",
    "# дисперсия\n",
    "print(df.groupby('gender')['mathscore'].var()) \n",
    "\n",
    "#отклонения для каждой выборки\n",
    "print(df.groupby('gender')['mathscore'].std())\n",
    "\n",
    "\n",
    "v=998 #степени свободы \n",
    "print('t=',(62.8515-68.469)/(((15.75**2)/485)+((17.51**2)/515))**0.5)\n",
    "print('t  крит по табличному значению =1.96, t вычисленное по модулю больше, это значит,' \n",
    "       'что статистические различия все таки есть') \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Задание 6"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Вам предложены данные A/B теста. Проанализируйте, есть ли статистически значимая разница для конверсии в контрольной и экспериментальной группе."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Данные содержат 5 признаков:\n",
    "    \n",
    "* user_id - ID пользователя\n",
    "* timestamp - Временная отметка\n",
    "* group - К какой группе относится пользователь (контрольная или экспериментальная)\n",
    "* landing_page - Какой дизайн показали пользователю {old_page, new_page}\n",
    "* converted - Конверсия (0=not converted, 1=converted)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Не забудьте проверить и подготовить данные, сделать всю необходимую предобработку."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "кол-во: group\n",
      "control      147202\n",
      "treatment    147276\n",
      "Name: converted, dtype: int64\n",
      "ст отклонение: group\n",
      "control      0.325429\n",
      "treatment    0.323695\n",
      "Name: converted, dtype: float64\n",
      "среднее: group\n",
      "control      0.120399\n",
      "treatment    0.118920\n",
      "Name: converted, dtype: float64\n",
      " Получаем значение t_dfab  1.7519749611392352\n",
      "t крит 1.96 больше, чем t полученная,это означает, чторазницы конверсии в экспереминатльной группе и контрольной нет\n"
     ]
    }
   ],
   "source": [
    "dfab = pd.read_csv('ab_data.csv')\n",
    "#проверка на пустые значения\n",
    "dfab.isnull().values.any() \n",
    "\n",
    "#Cформируем гипотезы\n",
    "\n",
    "#H0=разницы для конверсии в контрольной и экспериментальной группе нет\n",
    "#H1=разница для конверсии в контрольной и экспериментальной группе есть\n",
    "#считаем выборку\n",
    "print('кол-во:', dfab.groupby('group')['converted'].count())\n",
    "\n",
    "#вычисляем среднее значение для каждой выборки\n",
    "print('среднее:',dfab.groupby('group')['converted'].mean())\n",
    "\n",
    "#вычисляем среднее отклонение для каждой выборки\n",
    "print('ст отклонение:',dfab.groupby('group')['converted'].std())\n",
    "\n",
    "#вычислим эмпирическое значение критерия\n",
    "t_dfab=(0.120399-0.118920)/(((0.325429**2)/147202)+((0.323695**2)/147276)**0.5)\n",
    "\n",
    "#находим число степеней свободы для нахождения t крит из таблицы\n",
    "v=147202+147276-2 #t крит =1.96\n",
    "\n",
    "print(' Получаем значение t_dfab ',t_dfab)\n",
    "print('t крит 1.96 больше, чем t эмп ,это означает, что' \n",
    "       'разницы конверсии в экспереминатльной группе и контрольной нет')"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
