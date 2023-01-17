# eti_test

Selenium Browser automation testing for internship at Qinetics

## Features

- Tests basic functionalities on page
- Tests cross element functionalities on a page
- Tests cross page functionalities

## Built with:

- Selenium 4.6.0 Python

## Problems with this testsuite:

Other than being incomplete, there are still some issues

- Too much junk data is created since only on account create can we bypass the captcha
- Accounts cannot be reused, thus actual dashboard functionalities' tests will make even more junk data
- If not, it simply cannot be tested like many features locked behind "existing account"
- The flow will get longer and longer the further we go (step1-step4 of payment is unavoidable, but the dashboard can avoid redoin step1-step4 if captcha is skippable)
-

## Recommendation:

- Adding a secret key to allow testing software to bypass captcha or remove captcha from staging completely to reduce the amount of junk accounts created and allow reuse of test data

## TODO:

1. test redirect for forgets
2. testing payment gateway (setup wait):

- samsung pay testable?
- test credit card form
- test reset form
- payment on click should show progress indicators?

3. satisfaction survey
4. Dashboard can be accessed after payment, can test the below

- The online domains should appear in the dashboard, whereas the offline ones WILL appear in email
- note that since these actually work, there will be a lot of junk data - ask for permission before proceeding

## WIP:

testing step 3:

- check boxes (single, multi)
- check all (single, multi)
- modify (single, multi) - nothing much to test, just click inside and change for each?
  - Currently left on trying to implement adaptive locators for modify form to ensure robustness
- test variations with (no addons, WHOIS only, DNSSEC only, Both), should be reflected in this step's summary

testing step 4:

- payment (nothing much to check actually, maybe check amount of checks and number of items in receipt and VAT)
- check box alert
