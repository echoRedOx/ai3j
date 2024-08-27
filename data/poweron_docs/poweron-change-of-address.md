# Change of Address

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

Name Record

Note Record

Banno Conversations

Tracking Record 8 Cleanup

Tracking Record 8 Matching

Tracking Record 8 Matching Installation


-----

# Change of Address

This PowerOn allows the user to submit an address change to the credit union. The change will either

immediately update the member's address in Episys, or if the member meets any of the ineligibility

criteria, will start a conversation in Banno. The program allows for submitting changes to the following
address fields: Street Address, Extra Address, City, State, and Zip Code.

### UX Run-Time Detail

Upon selecting "Edit Address" from the user's Profile, if the password was not entered immediately
prior to launch, the Banno UX displays the password confirmation box. Once the password is
confirmed the UX displays an input form allowing the following update options: Street Address, Street
Address 2, City, State, Zip Code, and a field to add notes (optional).

Once the member enters the updates, they hit save to complete the address change.

### PowerOn Run-Time Detail

Once the member has entered and saved their updates, the account and address information is
passed back to the PowerOn from the Banno UX. The PowerOn takes this information, reads the
various parameter settings from the configuration Letter file, determines account and warning code

eligibility, and performs the appropriate file maintenance on the account and name record(s). It then
passes the success or pending address change message to the Banno UX.


-----

Change of Address

### Program Setup & Installation

**Required Files**

#### • REPWRITERSPECS folder

 » BANNO.CHANGE.ADDR.V1.POW (Main PowerOn Program)

 » Standard PowerOn library include files which should already be in your system:

 • RD.GETDATA.DEF

 • RB.LISTEXPAND.DEF

 • RB.LISTEXPAND

 • LETTERSPECS folder

 » BANNO.CHANGE.ADDR.V1.CFG (Main program configuration Letter file)

**Installation Steps**

**1.** Upload files to their respective directories

#### » Recommend using Symitar PC Transfer.

**2.** Install the PowerOn programs for demand use

**3.** Add the Main PowerOn program name to SymXchange Common Parameters

**4.** In Device Control take SymXchange – Banno Off Host

**5.** Put SymXchange – Banno back On Host and verify Status = On Host

**6.** Update the settings in the configuration Letter file

#### » The configuration Letter file contains details for the various settings.

**7.** Update setting in Banno People to enable PowerOn (must be completed by Jack Henry)


-----

Change of Address

**Configuration Letter File**

The configuration Letter file allows certain aspects of the program to be customized to better suit

your needs. Among the options which can be set are:

#### • Determine which account types are ineligible.

 • Determine which account level warning codes to exclude.

 • Determine if an account level warning code should be cleared upon updating the address

record.

#### • Determine if an account level warning code should be set upon updating the address record.

 • If setting an account level warning code, determine the number of days the warning code

should be set to expire.

#### • Determine if entering a PO Box will be restricted.
 » If entering a PO Box is restricted, identify the various PO Box character combinations the
program should check for, i.e. P.O. Box, PO Box, etc.

#### • Determine what account tree levels should be updated if the address on the Name Record

matches the address being changed.

#### » If left blank (not using name level matching) then the PowerOn will make the address
change based on the user information stored in the Tracking Record 8. See Additional
_Information below._

#### » If account tree levels are used, identify what name types to include in the level matching.

 • Determine if a confirmation email will be sent to the member upon successful address change.

(Episys SENDMAIL functionality must be enabled).

#### » If using the confirmation email, identify the email type, email subject, email from, and email
text.

The configuration Letter file contains full instructions on setting these run-time parameters. Do

pay close attention when selecting your options making sure to set each option within the
required parameters.


-----

Change of Address

### Database Interaction

**Data Sources**

Data utilized by the program is pulled from the following sources:

#### • Name records at the account, share, IRS, loan, pledge, EFT, card, and external loan levels

**Transactions / File Maintenance Performed**

#### • Name record(s) updated based on configuration Letter file setup

 • Note record created with the address change details

 • Account warning codes updated (cleared or set based on configuration Letter file setup)

 • Send the confirmation email if enabled

### Additional Information

**Name Record**

When the address change is successful, the name record(s) will immediately update in Episys. If
name level matching is enabled in the configuration Letter file, the program will find all the allowed
name records / name types with an address that matches the one being changed and changes
them all at once.

**Note Record**

When saving an address change a note record is added to the member's account regardless of
status. The note will include address change status (successful, attempt, or error), Name Locator(s)
updated, and reason for the attempt or error.


-----

Change of Address

**Banno Conversations**

Depending on account eligibility and the configuration Letter file setup, the address change may
not immediately update in Episys, but rather start a conversation in Banno. The conversation to the
credit union will include the member's updated address, plus any notes the member added with the
expectation the credit union staff will manually update the member's record in Episys.

**Tracking Record 8 Cleanup**

For credit unions using the Address Change PowerOn with Tracking Record 8 linking that are moving
to the name level matching version, there are two items that need to be done in addition to enabling
name level matching in the configuration Letter file. The first is to uninstall the Database Check
PowerOn (BANNO.DATABASE.CHECK.V1.POW). That program connects a Banno user to a definitive

name record, where the connection is stored in the (NetTeller) tracking type 8 record. The second is
to upload and run the Tracking 8 Cleanup batch program (BANNO.TRACKING8.FM). This job creates
an FM report to update, expire, or delete account level Tracking Type 8 records depending on user
prompt selections. Then changes can be posted to the account with FM Processing.

**Tracking Record 8 Matching**

If name level matching is not enabled in the configuration Letter file, the program will revert to linking
the address changes based on Tracking Record 8. The credit union will need to refer to the required
files and installation instructions below.


-----

Change of Address

**Tracking Record 8 Matching Installation**

**Required files when using Tracking Record 8 Linking**

#### • REPWRITERSPECS folder

 » BANNO.CHANGE.ADDR.V1.POW (Main PowerOn Program)

 » BANNO.DATABASE.CHECK.V1.POW (Secondary PowerOn Program)

 • This file can be obtained from the link-user-to-episys-name-record section of the Banno

GitHub repository.

#### » Standard PowerOn library include files which should already be in your system:

 • RD.GETDATA.DEF

 • RB.LISTEXPAND.DEF

 • RB.LISTEXPAND

 • LETTERSPECS folder

 » BANNO.CHANGE.ADDR.V1.CFG (Main program configuration Letter file)

**Installation Steps**

**1.** Upload files to their respective directories

**2.** Install the PowerOn programs (Main and Secondary) for demand use

**3.** Add the PowerOn program names (Main and Secondary) to SymXchange Common Parameters

**4.** In Device Control take SymXchange – Banno Off Host

**5.** Put SymXchange – Banno back On Host and verify Status = On Host

**6.** Update the settings in the configuration Letter file

#### » The configuration Letter file contains details for the various settings.

**7.** Update setting in Banno People to enable PowerOn (must be completed by Jack Henry)


-----

