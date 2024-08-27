# Member to Member Transfers

Program Overview


-----

## Contents

**Overview** 3

UX Run-Time Detail 3

Transferring to New or Previous Account 4

Editing or Deleting an Existing Transfer 5

Deleting a Saved Account 6

PowerOn Run-Time Detail 6

**Program Setup & Installation** 7

Required Files 7

Optional Files 7

Installation Steps 7

Configuration Letter File 8

**Database Interaction** 9

Data Sources 9

Transactions / File Maintenance Performed 9

**Additional Information** 11

Preference Access Requirement 11

Eligible Shares for Transfer Out 11

Daily Limits Management 12

External Account Records 12

Member to Member Transfers Report 12


-----

# Member to Member
 Transfers

This PowerOn allows the user to transfer funds to any credit union member providing they know

the other member's account number, the share or loan ID and the first three letters of the primary
member's last name (or business name). The user is also able to save, for later reuse, these alternate
account numbers which are stored in External Account records on the user's account.

### UX Run-Time Detail

Upon the user electing to run the program, the Banno UX displays an input form allowing the
following options:

#### • Create a new transfer to another account

 » Immediate, one-time transfer

 » Future dated, one-time transfer

 » Recurring transfer

 • Create a new transfer to a previously used (and saved) account

 • Edit or delete an existing, active, scheduled transfer previously created


-----

Member to Member Transfers

**Transferring to a New Account or Previously Used Account**

When setting up a transfer to another account the user is prompted for the first three letters of the

last name (or business name) associated with the target account, the member number, the targeted
type (share or loan) and the targeted share or loan ID.

Submitting the form will result in the PowerOn attempting to validate the entered account information.
If the validation fails, the user will be offered another opportunity to reenter the information.

Once the input has been validated, the transfer input form will be displayed. When setting up a
transfer to a previously used (and saved) member, the validation process is skipped over, and the user
is immediately presented with the transfer input form.


-----

Member to Member Transfers

The user enters the requested information and submits the information for final approval. Upon

approval by the user:

#### • One-time, immediate transfers are performed immediately

 • One-time, future dated and recurring transfers are set up with the creation of a share 

transfer record

**Editing or Deleting an Existing Transfer**

If the UX displays any previously created scheduled transfers, the user will have the opportunity of
selecting one to either delete or edit. Editing an existing transfer is limited to changing the amount,
frequency and/or date. Electing to delete the transfer results in the transfer being expired. Should the
user have inadvertently deleted a previously saved account, resulting in it being expired, manually
deleting the transfer record's expiration date will make it accessible to the user once more.


-----

Member to Member Transfers

**Deleting a Saved Account**

If the UX displays any previously saved accounts, the user will have the opportunity to delete the
saved account. The external account record will be expired, no longer accessible to the user through
the program. Should the user inadvertently delete a previously saved account, manually deleting the
external account record's expiration date will make it accessible to the user once more.

### PowerOn Run-Time Detail

When first run by the member, the program reads the various parameter settings from the Letter file,

builds a list of the member's eligible shares to transfer from, a list of existing transfers and a list of any
previously used member accounts the user had saved. It then passes this information to the Banno

UX to be presented to the member.

If the parameter settings to limit transfers and/or amounts to a daily limit is turned on, the information
passed to the UX will include the user's calculated daily count and amount limits along with the
current daily counts/amounts.

Once the member has made their selection (create a new transfer, edit an existing transfer, or delete
an existing transfer) those options are passed back to the PowerOn from the Banno UX and the
PowerOn then performs the appropriate file maintenance and/or transfer on the member's account.

#### • For a new transfer, a share transfer record, type 3, is created under the share to be debited.

 • When editing an existing transfer, the existing transfer is expired, and a new share transfer is

created with the user's revised options.

#### • When deleting a transfer, the existing transfer's effective date is cleared, and the expiration date

is set to the system date.


-----

Member to Member Transfers

### Program Setup & Installation

**Required Files**

#### • REPWRITERSPECS folder

 » BANNO.M2MTRANSFERS.V3.POW (Main PowerOn Program)

 » Main program support files

 • BNOLB.SLLISTBUILD.DEF

 • BNOLB.SLLISTBUILD.PRO

 » Standard PowerOn library include files which should already be in your system:

 • RD.GETDATA.DEF

 • RB.LISTEXPAND.DEF

 • RB.LISTEXPAND

 • LETTERSPECS folder

 » BANNO.M2MTRANSFERS.V3.CFG (Main program configuration Letter file)

**Optional Files**

#### • REPWRITERSPECS folder

 » BANNO.M2MTRANSFERS.RPT.BATCH (Member to Member Transfers Report)

**Installation Steps**

**1.** Upload files to their respective directories

#### » Recommend using Symitar PC Transfer.

**2.** Install the PowerOn programs for demand use

**3.** Add the Main PowerOn program name to SymXchange Common Parameters

**4.** In Device Control take SymXChange – Banno Off Host

**5.** Put SymXchange – Banno back On Host and verify Status = On Host

**6.** Update the settings in the configuration Letter file

#### » The configuration Letter file contains details for the various settings.


-----

Member to Member Transfers

**Configuration Letter File**

The configuration Letter file allows certain aspects of the program to be customized to better suit
your needs. Among the options which can be set are:

#### • Establish account eligibility.

 » Based upon account type(s) or warning code(s).

 • Establish transfer limits.

 » By transfer count and/or single or aggregate transfer amount(s) – globally or on an accountby-account basis.

#### • Determine whether to allow transfers from cross-accounts.

 • Establish whether transfers can be made from shares, loans, or both.

 • Determine whether transfers can be made to other member's clubs or certificates.

 • Determine whether the user can use the program to edit existing transfers not originally created

by the program.

#### • Establish a default share comment to be prepended to the comment added by the user for one
time immediate transfers.

#### • Modify member name and share/loan ID description that is displayed to members.

 • Indicate whether the program should be implemented in test mode.


-----

Member to Member Transfers

### Database Interaction

**Data Sources**

Data utilized by the program is pulled from the following sources:

#### • External Account Records are being utilized to track saved accounts by the member.

 • The member's Preference record is used to track transfer counts and amounts performed

on the system date by the member when transfer limitations are being utilized.

#### • Share transfer records are being utilized when the member is setting up recurring transfers.

**Transactions / File Maintenance Performed**

The program performs the following transactions and/or file maintenance.

#### • External Account Records

 » FINANCIALINSTITUTIONNAME

 • "M2M:" and the save name given by the user. The save name is limited to 20 characters.

 • Example – "M2M:Daughter's Checking"

 » PRIMARYACCOUNTHOLDERNAME

 • The first three letters of the last name or business name of the target account.

 » NUMBER

 • The account number and share/loan ID of the target account in the following format:

 » aaaaaaaaaabcccc where 'a' is the 10-digit account number, 'b'
is 'S' or 'L' for share or loan and 'c' is the share/loan ID.

#### » Example – "0000123456S0001" for account 000123456 Share 0001

 » STATUS

 • "Approved"

 » EXPIRATIONDATE

 • Set to the system date if member is 'deleting' the saved account.


-----

Member to Member Transfers

#### • Share Transfer Records

 » TYPE

 » ACCOUNTNUMBER

 » IDTYPE

 » ID

 » AMOUNT

 » EFFECTIVEDATE

 » NEXTDATE

 » FREQUENCY

 » DAY1

 » DAY2

 • Preference Records


Set to a type 3

Member number being credited by the transfer

Share (0) or loan (1) indicator

Share/Loan ID receiving the funds

Transfer amount

Effective date of the share transfer record

The next transfer date

Transfer frequency

Transfer day 1

Second transfer day of the month for semimonthly


If daily transfer amounts/counts are being tracked and enforced and the member is
performing the first transfer for the day, the following Preference record fields will be reset to
$0.00 or 0 depending on the field.

#### » XFERCOUNT

 » XFERAMOUNT

 » DEPCOUNT

 » DEPAMOUNT

 » WDCHECKCOUNT

 » WDCHECKAMOUNT

 » WDCASHCOUNT

 » WDCHECKAMOUNT

 » BILLPAYCOUNT

 » BILLPAYAMOUNT

 » LASTTRANDATE (set to system date)


-----

Member to Member Transfers

If daily transfer amounts/counts are being tracked and enforced, and upon a successful
transfer, the following fields will be updated in the member's Preference record:

#### » LASTTRANDATE

 • Updated to the system date

 » XFERCOUNT

 • Updated with the new count (previous count + 1)

 » XFERAMOUNT

 • Updated with the new daily total (previous value + transfer amount)

 • Transactions

 » One-time transfers are performed immediately by the program

### Additional Information

**Preference Access Requirement**

The user must have preference access type 3 (transfer to any account) on their account to
use the program.

**Eligible Shares for Transfer In/Out**

When the program validates the transfer to account information, the logic used to determine whether
a share is eligible to transfer funds to is determined by things such as the share IRS code equal to 0 as

well as service codes for transfer in values.

When the program builds a list of eligible shares for transfer out, the logic used to determine whether
a share is eligible to transfer funds from is determined by common PowerOn library procedures and
takes into consideration things such as cross-account access settings as well as service codes for
transfer out values.


-----

Member to Member Transfers

**Daily Limits Management**

Through settings in the configuration Letter file, daily transfer limiting can be turned on which would
limit the total number of transfers, total amount of transfers and the maximum single transfer amount
which can be originated by the user on the system date. The limits can be set on a global basis or on
an individual member by member basis. The global settings are established within the configuration
Letter file parameters and the individual limits would be set in the member's Preference record
settings. Individual member limitations will always override the global settings.

**External Account Records**

In addition to being created by the program, these records can be created manually or by batch
mode as long as the fields contain the correct data and are in the required format.

**Member to Member Transfers Report**

The Member to Member Transfers Report provides details about one-time immediate transfers, as well
as future-dated and recurring transfers that have been scheduled by members using the Member to
Member Transfers PowerOn. The report is generated by a batch PowerOn in Symitar.


-----

