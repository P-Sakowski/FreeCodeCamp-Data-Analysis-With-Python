import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', header=0)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    df_men = df[df['sex'] == 'Male']
    average_age_men = df_men['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    df_bachelors = df[df['education'] == 'Bachelors']
    bachelors_count = df_bachelors.shape[0]
    df_count = df.shape[0]
    percentage_bachelors = round(bachelors_count / df_count * 100.0, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    df_higher_edu = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    df_higher_edu_rich = df_higher_edu[df_higher_edu['salary'] == '>50K']
    higher_edu_count = df_higher_edu.shape[0]
    higher_edu_rich_count = df_higher_edu_rich.shape[0]
  
    # What percentage of people without advanced education make more than 50K?
    df_lower_edu = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]
    df_lower_edu_rich = df_lower_edu[df_lower_edu['salary'] == '>50K']
    lower_edu_count = df_lower_edu.shape[0]
    lower_edu_rich_count = df_lower_edu_rich.shape[0]

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df_higher_edu
    lower_education = df_lower_edu

    # percentage with salary >50K
    higher_education_rich = round(higher_edu_rich_count / higher_edu_count * 100.0, 1)
    lower_education_rich = round(lower_edu_rich_count / lower_edu_count * 100.0, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_min_workers = df[df['hours-per-week'] == df['hours-per-week'].min()]
    num_min_workers = df_min_workers.shape[0]
    df_min_workers_rich = df_min_workers[df_min_workers['salary'] == '>50K']
    min_workers_rich_count = df_min_workers_rich.shape[0]
    rich_percentage = round(min_workers_rich_count / num_min_workers * 100.0, 1)

    # What country has the highest percentage of people that earn >50K?
    ppl_per_country = df.groupby(by=['native-country']).count()
    rich_ppl_per_country = df[df['salary'] == '>50K'].groupby(by=['native-country']).count()
    rich_country_percentage = rich_ppl_per_country / ppl_per_country * 100.0
    df_highest_earning_country = rich_country_percentage.nlargest(1, 'age')
    highest_earning_country = df_highest_earning_country.index[0]
    highest_earning_country_percentage = round(rich_country_percentage.loc[highest_earning_country].iloc[0], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    df_india = df[df['native-country'] == 'India']
    rich_occupation = df_india[df_india['salary'] == '>50K'].groupby(by=['occupation']).count()
    top_IN_occupation = rich_occupation.nlargest(1, 'age').index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
