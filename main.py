import re
import csv

import bs4
import requests


EMAIL_REGEX = re.compile('[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}')


def main():
    emails = {}
    companies = []

    # name,website
    with open("companies.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            companies.append(tuple(row))

    for name, url in companies:
        kwargs = {}
        if url.startswith("https"):
            kwargs["verify"] = False

        response = requests.get(url, **kwargs)
        body = response.content.decode("utf-8")

        text = bs4.BeautifulSoup(body, "html.parser").get_text()
        emails[name] = [elem.group(0) for elem in EMAIL_REGEX.finditer(text) if elem]

    # name,email1,email2,...
    with open("emails.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        for name, emails in emails.items():
            writer.writerow([name] + emails)


if __name__ == "__main__":
    main()
