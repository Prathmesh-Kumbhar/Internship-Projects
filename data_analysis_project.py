import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename):
    try:
        # Changed the hardcoded path to use the 'filename' argument
        df = pd.read_csv(filename)
        print("Data loaded successfully\n")
        print(df.head())
        return df
    except Exception as e:
        print("Error loading file:", e)
        return None

def clean_data(df):
    try:
        df = df.drop_duplicates()

        df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

        choice = input("Handle missing salary? (drop/fill): ")

        if choice.lower() == "drop":
            df = df.dropna(subset=["Salary"])
        else:
            avg_salary = df["Salary"].mean()
            df["Salary"].fillna(avg_salary, inplace=True)

        print("\nData cleaned successfully\n")
        return df
    except Exception as e:
        print("Error cleaning data:", e)
        return df

def filter_data(df):
    try:
        print("\n--- Filtered Data ---")

        print("\nEmployees with Salary > 60000:")
        print(df[df["Salary"] > 60000])

        print("\nIT Department Employees:")
        print(df[df["Department"] == "IT"])

        print("\nEmployees with Experience > 5:")
        print(df[df["Experience"] > 5])

    except Exception as e:
        print("Error filtering data:", e)

def analyze_data(df):
    try:
        print("\n----- Summary Statistics -----")
        print(df.describe())

        print("\n----- Average Salary by Department -----")
        dept_avg = df.groupby("Department")["Salary"].mean()
        print(dept_avg)

        print("\n----- Employee Count by Department -----")
        dept_count = df["Department"].value_counts()
        print(dept_count)

        print("\n----- Highest Salary -----")
        print(df.loc[df["Salary"].idxmax()])

        print("\n----- Lowest Salary -----")
        print(df.loc[df["Salary"].idxmin()])

        return dept_avg
    except Exception as e:
        print("Error analyzing data:", e)

def plot_data(df, dept_avg):
    try:
        plt.figure()
        dept_avg.plot(kind="bar")
        plt.title("Average Salary by Department")
        plt.xlabel("Department")
        plt.ylabel("Salary")
        plt.show()

        plt.figure()
        df["Salary"].plot(kind="hist")
        plt.title("Salary Distribution")
        plt.xlabel("Salary")
        plt.ylabel("Frequency")
        plt.show()

        plt.figure()
        plt.scatter(df["Experience"], df["Salary"])
        plt.title("Experience vs Salary")
        plt.xlabel("Experience")
        plt.ylabel("Salary")
        plt.show()

    except Exception as e:
        print("Error plotting data:", e)

def main():
    file_path = input("Enter CSV file path: ")
    df = load_data(file_path)

    if df is not None:
        df = clean_data(df)
        filter_data(df)
        dept_avg = analyze_data(df)

        choice = input("\nDo you want to see graphs? (yes/no): ")
        if choice.lower() == "yes":
            plot_data(df, dept_avg)

if __name__ == "__main__":
    main()
