# Project: Time Calculator
# Course: Scientific Computing with Python (freeCodeCamp)
# Programming language: Python
# Developer: Valeriy B.

def add_time(start, duration, *day):
    
    # Creating final variable
    new_time = ""
    
    # Splitting start time
    time_now = start.split()[0]
    time_now_hours = time_now.split(":")[0]
    time_now_minutes = time_now.split(":")[1]
    meridiem = start.split()[1]

    # Splitting duration time
    durations_hours = duration.split(":")[0]
    duration_minutes = duration.split(":")[1]

    # Creating resulting variables for hours and minutes
    resulted_minutes = 0
    resulted_hours = 0

    # Creating resulted meridiem variable
    resulted_meridiem = ""

    # Creating 'days after' variable
    days_after = ""

    # Creating 'day of the week' variable
    day_of_the_week = ""

    # Creating a week list
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Minutes logic calculation
    if int(time_now_minutes) + int(duration_minutes) < 60:
        resulted_minutes += (int(time_now_minutes) + int(duration_minutes))
    else:
        resulted_minutes += (int(time_now_minutes) + int(duration_minutes) - 60)
        resulted_hours += 1

    # Hours logic calculation      
    day_counter = 0
    if int(time_now_hours) + int(durations_hours) < 12:
        resulted_hours += (int(time_now_hours) + int(durations_hours))
    else:
        total_hours = int(time_now_hours) + int(durations_hours)
        while total_hours > 12:
            temp_hours_variable = total_hours - 12
            day_counter += 1
            total_hours = temp_hours_variable
        resulted_hours += total_hours

    # Creating string minutes variable
    resulted_minutes_str = ""
    if resulted_minutes < 10:
        resulted_minutes_str = "0" + str(resulted_minutes)
    else:
        resulted_minutes_str = str(resulted_minutes)

    # Calculating the total number of days
    hours_total = 0
    if int(time_now_minutes) + int(duration_minutes) > 60:
        hours_total += 1
    hours_total += int(time_now_hours) + int(durations_hours)
    days_total = hours_total / 12

    # Resulted meridiem variable logic
    if days_total < 1:
        resulted_meridiem = meridiem
    elif days_total < 2:
        if meridiem == "PM":
            resulted_meridiem = "AM"
        else:
            resulted_meridiem = "PM"
    elif days_total >= 2:
        if int(days_total) % 2 == 0:
            resulted_meridiem = meridiem
        else:
            if meridiem == "PM":
                resulted_meridiem = "AM"
            else:
                resulted_meridiem = "PM"

    # 'Days after' parameter calculation logic
    calculation_days_after = days_total / 2
    if meridiem == "PM" and days_total > 1:
        if calculation_days_after <= 1:
            days_after = " (next day)"
        else:
            days_after = f" ({int(calculation_days_after) + 1} days later)"
    elif meridiem == "AM" and calculation_days_after >= 1:
        if calculation_days_after <= 1.5:        
            days_after = " (next day)"
        else:
            days_after = f" ({int(calculation_days_after) + 1} days later)"
            
    # 'Day of the week' parameter logic
    if day:
        week_day_index = week.index(str(day[0]).capitalize())
        week_day_final = ""
        if calculation_days_after <= 1:
            week_day_final = week[week_day_index]
        else:
            counting_days = 0
            temp_days_count = 0
            
            # Verifying if number of days is bigger than 7
            if int(calculation_days_after) + 1 > 7:   
                days_of_the_week = int(calculation_days_after) + 1
                while days_of_the_week % 7 != 0:
                    temporary_days_variable = days_of_the_week - 1
                    temp_days_count += 1
                    days_of_the_week = temporary_days_variable
                counting_days += temp_days_count
            else:
                if calculation_days_after < 1.5:
                    counting_days = int(calculation_days_after)
                else:
                    counting_days = int(calculation_days_after) + 1

            # Searching for the new index in the 'week' list           
            week_remaining_days = 6 - week_day_index
            if (week_day_index + counting_days + 1) > week_remaining_days:
                new_day_index = counting_days - week_remaining_days 
                week_day_final = week[new_day_index - 1]
            else:
                week_day_final = week[week_day_index + counting_days]

        # Resulted 'day of the week' variable
        day_of_the_week = ", " + str(week_day_final)

    # Resulted variable
    new_time = str(resulted_hours) + ":" + resulted_minutes_str + " " + resulted_meridiem + day_of_the_week + days_after
    
    return new_time