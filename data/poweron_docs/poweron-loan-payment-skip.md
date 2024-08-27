# Loan Payment Skip

Program Overview


-----

## Contents

**Overview**

UX Run-Time Detail

PowerOn Run-Time Detail

**Program Setup & Installation**

Required Files

Installation Steps

Configuration Letter File

**Database Interaction**

Data Sources

Transactions / File Maintenance Performed

**Additional Information**

Loan Tracking Records

Shares Eligible for Fees

Test Mode

SKIPPAYMENT.XXX


-----

# Loan Payment Skip

This PowerOn allows the user to select one or more eligible loans and, for a fee, have the loan due

date and loan maturity date advanced by either one month (28 days for payment frequencies 6, 7, 8,
9, 11 or 12) or 1 payment cycle.

### UX Run-Time Detail

Upon the member electing to run the program, the Banno UX displays a list of eligible loans the
member can elect to skip. For each open eligible loan, the current amount due and due date are
displayed. For open loans which are not eligible, the reason for the loan's ineligibility is displayed.
Upon selecting an eligible loan, the member is prompted for the share which will be used for the fees.

A summary screen is then displayed for the member to view and approve. Upon approval the skip is

_immediately performed._


-----

Loan Payment Skip

### PowerOn Run-Time Detail

When first run by the member, the program reads the various parameter settings from the Letter file,

looks for loan tracking records pertaining to skip payments and based upon these settings and values,

determines whether the account is eligible to perform a loan payment skip (account eligibility). If the
account is eligible, the program then generates a list of eligible and ineligible loans as well as a list
of shares eligible to be used for the skip payment fee. This data, along with the fee amount and the
terms and conditions is then passed to the Banno UX for display to the member.

Once the member has made their selections and those selections are passed back to the PowerOn
by the Banno UX, the program performs the payment skip.

### Program Setup & Installation

**Required Files**

#### • REPWRITERSPECS folder

 » BANNO.LOANPAYMENT.SKIP.V1.POW (Main PowerOn Program)

 » Standard PowerOn library include files which should already be in your system:

 • RB.LISTEXPAND.DEF

 • RB.LISTEXPAND

 • LETTERSPECS folder

 » BANNO.LOANPAYMENT.SKIP.CFG (Main program configuration Letter file)

**Installation Steps**

**1.** Upload files to their respective directories

#### » Recommend using Symitar PC Transfer.

**2.** Install the PowerOn programs for demand use

**3.** Add the Main PowerOn program name to SymXchange Common Parameters

**4.** In Device Control take SymXchange – Banno Off Host


-----

Loan Payment Skip

**5.** Put SymXchange – Banno back On Host and verify Status = On Host

**6.** Update the settings in the configuration Letter file

#### » The configuration Letter file contains details for the various settings.

**7.** Add the program to Banno People

**Configuration Letter File**

The configuration Letter file allows certain aspects of the program to be customized to better suit

your needs. Among the options which can be set are:

#### • Determine program availability by calendar dates.

 • Determine member eligibility by account warning code(s).

 • Determine loan eligibility by loan type(s), loan service code(s), minimum and/or maximum

payment amounts, loan warning code(s), loan seasoning, time since last skip, maximum skips
allowed per loan, per year, or time since last skip, past due status, number of DQ payments per
payment types, and payment frequency type.

#### • Establish how the due date and maturity date are to be advanced: by a set amount (28 days or

1 month) or based upon the loan payment frequency.

#### • Utilize a test function to facilitate testing newer changes in a production environment.

### Database Interaction

**Data Sources**

Data utilized by the program is pulled from the following sources:

#### • Member's open loan records

**Transactions / File Maintenance Performed**

The program updates the following fields in the loan record:



#### • DUEDATE

 • MATURITYDATE


The new due date

The new loan maturity date


-----

Loan Payment Skip

If the update of the loan fields was successful, then the program creates a loan tracking record
under the loan for which the payment was skipped. The loan tracking record contains the
following information:



#### • USERDATE1

 • USERDATE2

 • USERDATE3

 • USERDATE4

 • USERDATE5

 • USERAMOUNT1

 • USERAMOUNT2


The system date

The loan's original due date

The loan's new calculated due date

The loan's original maturity date

The loan's new calculated maturity date

The calculated fee amount for this payment skip

The loan payment amount (LOAN:PAYMENT)


If the creation of the loan tracking record was successful, then the program debits the selected share
for the skip payment fee.

### Additional Information

**Loan Tracking Records**

The program uses the existence of these tracking records (regardless of whether it's expired or not)

along with the date value in the USERDATE1 field to determine the number of skips performed in the
prior rolling year, when the last skip was and how long it's been since the last skip for any given loan.

There will be a loan tracking record created under each loan each time a skip is performed against

that given loan.

**Shares Eligible for Fees**

The program looks for shares which are not closed, not charged-off which are a valid share type

based upon the Letter file configuration settings and which have an available balance sufficient to

cover the anticipated fee to be charged.


-----

Loan Payment Skip

**Test Mode**

To facilitate testing in a live environment, with test mode turned on and at least one member number

listed in the corresponding "Test Member List" parameter setting, any programming changes in this
most recent version will only be implemented when being run by members listed in the Test Member
List parameter. With Test Mode turned off, full program functionality will be used for all members.

**SKIPPAYMENT.XXX**

This Banno PowerOn program is not designed to work with the SKIPPAYMENT.XXX Symitar on-demand

program from Symitar Professional Services.


-----

