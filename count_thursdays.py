from datetime import datetime, timedelta


def count_thursdays(start_date, end_date, first_day):
    # Convert the start and end dates to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Define a timedelta of one day
    one_day = timedelta(days=1)

    # Find the first Thursday after the start date
    while start_date.strftime("%A") != first_day:
        start_date += one_day

    # Count the number of Thursdays
    count = 0
    while start_date <= end_date:
        if start_date.strftime("%A") == "Thursday":
            count += 1
        start_date += timedelta(days=7)

    return count


# Example usage
start_date = "2022-01-01"
end_date = "2022-12-31"
first_day = "Saturday"

thursday_count = count_thursdays(start_date, end_date, first_day)
print(thursday_count)
