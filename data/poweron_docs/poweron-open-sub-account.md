# Open Sub Account

Program Overview


-----

## Contents

**Overview**

UX Run-Time Detail

PowerOn Run-Time Detail

**Program Setup & Installation**

Required Files

Installation Steps

On-Demand Configuration PowerOn

**Database Interaction**

Data Sources

Transactions / File Maintenance Performed

**Additional Information**

Eligible Shares for Funding the New Share

Minimum Funding Amount Management

Allow Name Record Addition

Terms and Conditions Letter Files

Fee PowerOn


-----

# Open Sub Account

This PowerOn allows the end-user to open new shares whenever it's convenient for them. While

creating their new share, the member can easily add existing or new names to the share and also
transfer funds.

### UX Run-Time Detail

Upon running the program, the Banno UX displays a list of eligible account types (share groups) the
member can select to open. Once the member selects the account type, they are presented with a
list of eligible share types that they can open.

Once the member selects the specific share type, the Terms and Conditions will be displayed for the
member to accept.


-----

Open Sub Account

Upon accepting, a screen requesting how the new share will be funded is displayed. Then the user
will select the transferring account and enter the opening deposit amount.

Once the funding of the new share has been determined, the user is presented with a screen they can
easily copy existing or add new names to the share.


-----

Open Sub Account

Once the user determines any name additions, a screen is then displayed for the member to view and
confirm. Upon confirming the new share is immediately created and funded.

### PowerOn Run-Time Detail

When first run by the member, the program reads the various parameter settings from the
configuration program, and based upon these settings and values, determines what account
types (share groups) and share types can be opened. This data is then passed to the Banno UX for
display to the member.

Once the member has selected the account and share type, that selection is passed back to the
PowerOn by the UX.

The PowerOn obtains the Terms and Conditions from the Letter Files, along with the funding

parameters and copy/add name parameters from the configuration program. This data is then
passed to the Banno UX for display for the member to view, approve, enter funding information, and
determine if name(s) will be copied and/or newly added.

Upon submission, the PowerOn will create the new share, complete the transfer for the opening
balance, and copy and/or add new names if applicable.


-----

Open Sub Account

### Program Setup & Installation

**Required Files**

#### • REPWRITERSPECS folder

 » BANNO.NEWSUBCREATE.V1.POW (Main PowerOn Program)

 » BANNO.NEWSUBCREATE.V1.CONFIG (On-Demand Configuration PowerOn Program)

 » BANNO.NEWSUBCREATE.FEES.V1.POW (Optional – subroutine PowerOn responsible for
charging fees upon share creation)

#### » Standard PowerOn library include files which should already be in your system:

 • RD.GETDATA.DEF

 • RB.LISTEXPAND.DEF

 • RB.LISTEXPAND

**Installation Steps**

**1.** Upload files to their respective directories

#### » Recommend using Symitar PC Transfer.

**2.** Install the PowerOn programs for demand use

**3.** Add the Main PowerOn program name to SymXchange Common Parameters

**4.** In Device Control take SymXChange – Banno Off Host

**5.** Put SymXchange – Banno back On Host and verify Status = On Host

**6.** Run the configuration program (BANNO.NEWSUBCREATE.V1.CONFIG) from Account Manager

#### » The configuration program saves your desired options to a datafile (BANNO.

NEWSUBCREATE.V1.CFG) which is used by the PowerOn program at run-time.

#### » The configuration program also creates, as necessary, Terms and Conditions Letter

files with sample text. The text can be updated as needed from Letter File Control for
each of the share groups you are making available for members to select from.

**7.** Add the program to Banno People


-----

Open Sub Account

**On-Demand Configuration PowerOn**

Included in the PowerOn files is a configuration tool which is an on-demand PowerOn to be run from
any account in Account Manager. Among the options which can be set are:

#### • Determine which account types and warning codes to exclude.

 • Determine if funding the new share will be required.

 • Determine if the addition of a name record will be allowed.

 » Determine if copying existing name(s) associated with the account or creating new names
will be allowed.

#### » Determine where the name record will be added (account or share level).

 » Identify the number of new names allowed.

 » Identify Safe and Unsafe Name types and Tracking Record to be used for unsafe names.

 • Determine if internal email will be used when name record discrepancies are identified when

copying existing names.

#### • Determine if interest rates will be displayed.

 • Determine if the individual rate for fill-ins will be set with new share creation.

 • Indicate whether the program should be implemented in test mode.

 • Identify the Share Group(s).

 » Account Type(s) (i.e. Certificate of Deposit, Checking, Club, Savings, Money Market), Share
Type(s), and Share ID Range(s) allowed for the new share.

#### • Identify max limit of how many shares can be opened of each share type.

 • Modify error message wording that is displayed to users.

The program contains a built-in help file explaining each setting and how it can be used. Do pay close

attention when selecting your options making sure to set each option within the required parameters.


-----

Open Sub Account

### Database Interaction

**Data Sources**

Data utilized by the program is pulled from the following sources:

#### • Member's open share records

 • Account name records

 • Share / Loan level name records

 • Share defaults

 • Dividend type parameters

**Transactions / File Maintenance Performed**

#### • The program creates a new share record for the new share based on the share type defaults.

 • Any new name records created or copied are added to the share.

 • If the creation of the share record was successful, then the program debits the selected share to

fund the new share.

### Additional Information

**Eligible Shares for Funding the New Share**

When the program builds a list of eligible shares to fund the new share, the logic used to determine
whether a share is eligible to transfer from is determined by common PowerOn library procedures
and takes into consideration things such as cross-account access settings as well as service codes for
transfer out values.

**Minimum Funding Amount Management**

Through settings in the configuration PowerOn and the minimum balance field on the share

record the minimum funding amount can be set. The program looks at the minimum funding
parameter and compares that to the minimum balance amount in the share defaults for the
selected new share type and it forces the higher amount as the minimum funding amount for the
new share. Should a share have a minimum balance requirement that is greater than any eligible
share's available balance then the member will not see that share type as an option to open. open.


-----

Open Sub Account

**Allow Name Record Addition**

Through settings in the configuration PowerOn the user can copy existing names from the account's

shares and loans or create new name records to be added to the new share. If the "Copying existing
names" option is selected, the PowerOn will display existing share and loan name types according
to the parameters. The user can select which one(s) they would like to add to the new share. If the

"Creating new names" option is selected, the PowerOn will allow the user to input new name record(s)

to be added to the share. "Safe name types" will be added to the share upon creation. "Unsafe name
types" will require credit union review. The unsafe name information will be added to a tracking record
for credit union review. Any name records at the account level will display to the user but cannot be
modified as they will automatically apply to the new share. The configuration PowerOn contains a
built-in help file explaining each setting and how it can be used.

**Terms and Conditions Letter Files**

The configuration program creates, as necessary, the Terms and Conditions Letter files (BANNO.

NEWSUBACCT.TERMS.00-19). The letter files provide formatting requirements and sample verbiage.

**Fee PowerOn**

The subroutine PowerOn (BANNO.NEWSUBCREATE.FEES.V1.POW) can be used to charge the member

a fee upon share creation. The PowerOn can be used to determine the scenario in which a fee should

be charged, the amount of the fee, the fee description, and the GL to use for the fee posting. If you
need additional information or assistance with updating this PowerOn, please open a case.


-----

