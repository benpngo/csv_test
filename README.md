# Test script for demo

Written in python 2.7

1. Grabs CSV url from given github url
2. Reads CSV content
3. Sorts list by first name
4. Adds 2 extra fields for a Password and UPN. Password is 8 character length with mixed upper and lower case letters, symbols, and numbers. 
UPN is first name + last name + domain
5. Writes out to a local csv file

Run file using
```bash
python csv_test.py
```