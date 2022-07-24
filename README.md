# Email extractor
Extracts all emails from given urls in CSV `companies.csv` (with first field representing company name and the second field is the website of the company) and writes them in CSV `emails.csv` (with first field representing company name and the rest of the fields representing extracted emails).

## How to run
Assuming there is input CSV file `companies.csv`.

```
$ pip install -r requirements.txt
$ python3 main.py
```

Now you can find extracted emails in CSV file `emails.csv`.
