def calculate_simple_interest(principal, rate, time):
    # Calculate simple interest
    interest = principal * rate * time / 100
    total_amount = principal + interest
    return total_amount, interest

def calculate_compound_interest(principal, rate, time, compounding_frequency, include_leap_years=False):
    # Calculate compound interest with custom compounding frequency
    if include_leap_years:
        days_in_year = 366 if (time % 4 == 0 and (time % 100 != 0 or time % 400 == 0)) else 365
    else:
        days_in_year = 365

    rate_per_period = rate / (compounding_frequency * 100)
    n = compounding_frequency * time
    total_amount = principal * (1 + rate_per_period) ** (n * days_in_year / 365)
    interest = total_amount - principal
    return total_amount, interest

def main():
    # Print initial title
    print("Interest Calculator")
    
    # Continuously prompt user until valid input is provided
    while True:
        try:
            # Ask the user if they want Simple or Compound interest
            choice = int(input("Select the type of interest (1 for Simple, 2 for Compound): "))
            # Check if input is valid
            if choice not in (1, 2):
                raise ValueError("Invalid choice. Please enter 1 for Simple or 2 for Compound.")
            break
        except ValueError as e:
            # Print error message if input is invalid
            print(e)
    
    # Ask the user to choose a currency
    print("\nChoose currency:")
    print("1 - Dollars\n2 - Euros")
    
    # Get the user's choice for currency
    currency_choice = input("Your choice: ").strip()

    # Assign currency symbol based on user's choice
    if currency_choice == "1":
        currency_symbol = "$"
    elif currency_choice == "2":
        currency_symbol = "€"
    else:
        # Error if user provides an invalid choice
        raise ValueError("Invalid currency choice.")

    # Prompt user to input the principal amount with chosen currency symbol
    principal = float(input(f"Enter the principal amount ({currency_symbol}): "))

    # Let the user choose the time unit (years/months/days/weeks)
    print("\nChoose your time unit:")
    print("1 - Years\n2 - Months\n3 - Days\n4 - Weeks")
    
    # Read the time unit choice
    time_unit = input("Your choice: ").strip()

    # Convert user input into a number of years, based on choice
    if time_unit == "1":
        # Years
        time = float(input("Enter the number of years: "))
    elif time_unit == "2":
        # Months
        months = float(input("Enter the number of months: "))
        # Convert months to years
        time = months / 12.0
    elif time_unit == "3":
        # Days
        days = float(input("Enter the number of days: "))
        # Convert days to years (approximating 365 days)
        time = days / 365.0
    elif time_unit == "4":
        # Weeks
        weeks = float(input("Enter the number of weeks: "))
        # Convert weeks to years (approximating 52 weeks)
        time = weeks / 52.0
    else:
        # Raise an error for invalid time unit
        raise ValueError("Invalid time unit.")

    # Let the user choose the interest rate period (annual/daily/weekly/monthly)
    print("\nChoose your interest rate period:")
    print("1 - Annual\n2 - Monthly\n3 - Weekly\n4 - Daily")
    
    # Read the interest rate period choice
    rate_period = input("Your choice: ").strip()

    # Prompt user to input the interest rate
    rate = float(input("Enter the interest rate (%): "))

    # Convert the interest rate to an annual rate if necessary
    if rate_period == "2":
        rate = rate * 12  # Monthly to annual
    elif rate_period == "3":
        rate = rate * 52  # Weekly to annual
    elif rate_period == "4":
        rate = rate * 365  # Daily to annual
    elif rate_period != "1":
        raise ValueError("Invalid interest rate period.")

    # If user chose Simple Interest
    if choice == 1:
        # Calculate Simple Interest
        total_amount, interest = calculate_simple_interest(principal, rate, time)
        print("\nSimple Interest Calculation")
    # If user chose Compound Interest
    elif choice == 2:
        # Create a frequency dictionary mapping user choices to periods per year
        frequency_mapping = {
            "1": 365,  # daily
            "2": 52,   # weekly
            "3": 12,   # monthly
            "4": 4,    # quarterly
            "5": 2,    # semi-annually
            "6": 1     # annually
        }
        while True:
            try:
                # Ask user how often interest should be compounded
                print("\nEnter compounding frequency by number:")
                print("1 - Daily\n2 - Weekly\n3 - Monthly\n4 - Quarterly\n5 - Semi-annually\n6 - Annually")
                
                # Read user input for compounding frequency
                compounding_input = input("Your choice: ").strip()
                
                # Check validity of user choice
                if compounding_input not in frequency_mapping:
                    raise ValueError("Invalid choice. Please try again.")
                break
            except ValueError as e:
                # Print error and re-prompt if invalid input
                print(e)

        # Ask user if leap years should be included
        include_leap_years = input("Include leap years in calculations? (yes/no): ").strip().lower()
        # Convert to Boolean
        include_leap_years = (include_leap_years == "yes")

        # Calculate Compound Interest
        total_amount, interest = calculate_compound_interest(
            principal,
            rate,
            time,
            frequency_mapping[compounding_input],
            include_leap_years
        )
        # Print a label for Compound Interest
        print("\nCompound Interest Calculation")

    # Finally, display the results
    print(f"Principal Amount: {currency_symbol}{principal:.2f}")
    print(f"Annual Interest Rate: {rate}%")
    print(f"Time (in years): {time:.2f}")
    print(f"Total Amount: {currency_symbol}{total_amount:.2f}")
    print(f"Total Interest: {currency_symbol}{interest:.2f}")

if __name__ == "__main__":
    main()
