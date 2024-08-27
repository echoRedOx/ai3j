# Withdraw By Check

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

Address Verification

Check Record


-----

# Withdraw By Check

This PowerOn allows the user to withdraw funds in the form of a check, from an eligible share or loan

and have the check mailed to them. The program will use the system calculated member address
(ACCOUNT:PAYEELINE:[1-6]) as the address to which the check will be mailed.

### UX Run-Time Detail

Upon running the program, the Banno UX displays the selected share/loan details, check amount
input field, mailing address for the check, and the custom Terms and Conditions verbiage. Once the
member enters the amount they are requesting for the check withdrawal, they hit submit to complete
the transaction.

Upon submitting, a recap is provided, and the check withdrawal is processed.


-----

Withdraw By Check

### PowerOn Run-Time Detail

When first run by the member, Banno passes back to the PowerOn the account and share/loan ID the
member has selected for the check withdrawal. The program takes this information, reads the various
parameter settings from the configuration Letter file, and determines account eligibility. The PowerOn
will pass back to the UX if the share/loan is eligible, the share/loan details, the mailing address for the
check withdrawal, and the Terms and Conditions.

Once the member has entered the check amount, the amount is passed back to the PowerOn. The
PowerOn takes this information, reads the various parameter settings from the configuration Letter
file, determines transaction eligibility, and completes an address verification. It then passes the
success or failure message to the Banno UX.

### Program Setup & Installation

**Required Files**

#### • REPWRITERSPECS folder

 » BANNO.CHECK.WITHDRAW.V1.POW (Main PowerOn Program)

 » Standard PowerOn library include files which should already be in your system:

 • RD.GETDATA.DEF

 • RB.LISTEXPAND.DEF

 • RB.LISTEXPAND

 • LETTERSPECS folder

 » BANNO.CHECK.WITHDRAW.V1.CFG (Main program configuration Letter file)

**Installation Steps**

**1.** Upload files to their respective directories

#### » Recommend using Symitar PC Transfer.

**2.** Install the PowerOn programs for demand use

**3.** Add the Main PowerOn program name to SymXchange Common Parameters


-----

Withdraw By Check

**4.** In Device Control take SymXChange – Banno Off Host

**5.** Put SymXchange – Banno back On Host and verify Status = On Host

**6.** Update the settings in the configuration Letter file

#### » The configuration Letter file contains details for the various settings.

**7.** Add the program to Banno People

**Configuration Letter File**

The configuration Letter file allows certain aspects of the program to be customized to better suit

your needs. Among the options to be set are:

#### • Determine which share and loan types are eligible.

 • Determine which account, share, or loan warning codes to exclude.

 • Determine the minimum and/or maximum withdrawal amount for shares.

 • Determine the cash advance limit for loans.

 • Determine if checks withdrawn via Banno are subject to Reg D.

 • Set the Terms & Conditions verbiage, which the user must accept to process the transaction.

The configuration Letter file contains full instructions on setting these run-time parameters. Do

pay close attention when selecting your options making sure to set each option within the
required parameters.

### Database Interaction

**Data Sources**

Data utilized by the program is pulled from the following sources:

#### • Member's open share and loan records

 • Name records at the account level


-----

Withdraw By Check

**Transactions / File Maintenance Performed**

#### • A check withdrawal transaction is performed for withdrawals from shares.

 • A check advance transaction is performed for withdrawals from loans.

 • A check record is created within Check Manager.

### Additional Information

**Address Verification**

Upon hitting submit the program looks at the account record field "Payee Name Record Locator"
for which Name Record Locator is used by Symitar for the mailing address. Then it verifies that the
address has everything that is needed, i.e. Street, Zip, etc. See account record fields in Symitar eDocs
for more information regarding the Payee Name Record Locator.

**Check Record**

The transaction creates the check record, and the credit union would use their standard process to

print and mail the checks. For additional information, contact Symitar Application Support.


-----

