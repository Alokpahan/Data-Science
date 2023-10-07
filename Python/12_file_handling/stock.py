# stocks.csv contains stock price, earnings per share and book value.
# You are writing a stock market application that will process this file and create a new file with
# financial metrics such as pe ratio and price to book ratio. These are calculated as,
#
# pe ratio = price / earnings per share
# price to book ratio = price / book value


# Open the "stocks.csv" file for reading and "output.csv" file for writing.
with open("stocks.csv", "r") as f, open("output.csv", "w") as out:
    # Write a header line to the output file.
    out.write("Company Name,PE Ratio, PB Ratio\n")

    # Skip the first line in the input file, which is a header.
    next(f)

    # Iterate through each line in the input file.
    for line in f:
        # Split the line into a list of tokens using "," as the delimiter.
        tokens = line.split(",")
        # Uncomment the line below for debugging purposes to see the tokens.
        # print(tokens)

        # Extract relevant information from the tokens.
        stock = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])

        # Calculate the Price-to-Earnings (PE) ratio and round it to 2 decimal places.
        pe = round(price / eps, 2)

        # Calculate the Price-to-Book (PB) ratio and round it to 2 decimal places.
        pb = round(price / book, 2)

        # Write the company name, PE ratio, and PB ratio to the output file.
        out.write(f"{stock},{pe},{pb}\n")
