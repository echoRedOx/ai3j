# Loan Payoff

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

**Additional Information**

Loan Tracking Records

Fee PowerOn


-----

# Loan Payoff

This PowerOn allows the user to request a loan payoff amount including interest and late fees for

a selected date.

Loan payoffs are only available on in-house loans. The payoff option will not display for any thirdparty loans. Credit card loans will not display the interest rate as they typically have different interest
rates for different portions of the balance.

### UX Run-Time Detail

Upon the member electing to run the program, the Banno UX displays the loan selected and Payoff
Date. The Payoff Date defaults to today, but the member may click the link to select a future payoff
date from a calendar. Customizable Terms and Conditions verbiage will also display to the member.

Upon selecting Calculate, a Loan Payoff screen is displayed for the member to view the calculated
payoff amount and details.


-----

Loan Payoff

### PowerOn Run-Time Detail

When first run by the member, Banno passes back to the PowerOn the account and loan ID the
member is requesting payoff for. The program takes this information, reads the various parameter
settings from the configuration Letter file and determines account eligibility. The PowerOn will pass
back to the UX if the loan is eligible, the number of days in the future a payoff can be requested, and
the terms and conditions. If eligible, once the member selects the desired payoff date, that date is
passed back to the PowerOn from the Banno UX and the PowerOn then calculates the loan payoff
amount. It then passes this information to the Banno UX to be presented to the member.

### Program Setup & Installation

**Required Files**

#### • REPWRITERSPECS folder

 » BANNO.LOAN.PAYOFF.V1.POW (Main PowerOn Program)

 » BANNO.LOAN.PAYOFF.FEES.POW (Optional – subroutine PowerOn responsible for returning
additional fees)

#### » Standard PowerOn library include files which should already be in your system:

 • RD.GETDATA.DEF

 • RB.LISTEXPAND.DEF

 • RB.LISTEXPAND

 • LETTERSPECS folder

 » BANNO.LOAN.PAYOFF.V1.CFG (Main program configuration Letter file)

**Installation Steps**

**1.** Upload files to their respective directories

#### » Recommend using Symitar PC Transfer.

**2.** Install the PowerOn programs for demand use

**3.** Add the Main PowerOn program name to SymXchange Common Parameters


-----

Loan Payoff

**4.** In Device Control take SymXChange – Banno Off Host

**5.** Put SymXchange – Banno back On Host and verify Status = On Host

**6.** Update the settings in the configuration Letter file

#### » The configuration Letter file contains details for the various settings.

**7.** Add the program to Banno People

**Configuration Letter File**

The configuration Letter file allows certain aspects of the program to be customized to better suit

your needs. Among the options which can be set are:

#### • Determine member eligibility by account warning code(s).

 • Determine loan eligibility by loan type(s), loan warning code(s).

 • Determine the number of days in the future for which a loan payoff can be requested.

 • Determine home loan, boat loan, vehicle loan, and secured loan types to identify collateral for

display.

#### • Set Terms and Conditions to be displayed to the member regarding the payoff.

 • Set fee PowerOn name if additional loan payoff fees should be included/displayed.

The configuration Letter file contains full instructions on setting these run-time parameters. Do

pay close attention when selecting your options making sure to set each option within the
required parameters.

### Database Interaction

**Data Sources**

Data utilized by the program is pulled from the following sources:

#### • Member's open internal loan records

 • Loan Tracking records

 • Loan Name records

 • Loan Pledge records


-----

Loan Payoff

### Additional Information

**Loan Tracking Records**

The program uses these tracking records to store boat and vehicle collateral information. The credit

union can specify in the configuration Letter file which loan tracking types to use and which field(s)
contain collateral information.

**Fee PowerOn**

Subroutine PowerOn can be modified to return up to 10 custom fee amounts and descriptions to the
Banno UX for display. Custom fee logic must be added directly to this program. (No actual fees are
posted by this PowerOn. The return data is for display only.)


-----

