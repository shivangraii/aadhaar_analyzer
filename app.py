def get_data_source(choice):
    if choice == 1:
        paths = [
            "data/saved/enrolment.csv",
            "data/saved/biometrics.csv",
            "data/saved/demographic.csv"
        ]
    else:
        paths = input("Enter CSV paths (comma separated): ").split(",")
    
    return load_multiple_csv(paths)
