# Overdraft Tolerance Opt-In / Opt-Out

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

Share Tracking Records


-----

# Overdraft Tolerance  Opt-In / Opt-Out

This PowerOn allows the user to acknowledge the credit union's terms and fees and opt-in or out

of overdraft services on their account. The member may opt-in or opt-out on a share-by-share

basis. The status of any given share and the date last set will be recorded by the program in a share
tracking record.

### UX Run-Time Detail

Upon running the program, the Banno UX displays a list of the eligible shares for which the user can
change the Overdraft Tolerance (ODT) settings.

The shares which the user has already opted in for will be preselected. The user can opt out of those

shares by deselecting them. The user can also select additional shares to opt in.


-----

Overdraft Tolerance Opt-In / Opt-Out

Upon submitting the form, the Terms and Conditions will be displayed for the member to accept.

A summary screen is then displayed for the member to view and confirm. Upon confirming the ODT

settings are immediately updated.


-----

Overdraft Tolerance Opt-In / Opt-Out

### PowerOn Run-Time Detail

When first run by the member, the program reads the various parameter settings from the Letter
file, and based upon these settings and values, determines whether the account is eligible to update
the share ODT settings. If the account is eligible, the program looks for the share tracking record
pertaining to ODT settings and then generates a list of eligible shares identifying the opt-in or opt-out
status for each share. This data is then passed to the Banno UX for display to the member.

Once the member has made their selections and those selections are passed back to the PowerOn
by the Banno UX, the program reads the Letter file to obtain the Terms and Conditions. This data is
then passed to the Banno UX for display for the member to view and approve.

Upon approval, the PowerOn will update the member's share and create/update the related share
tracking record as needed.

### Program Setup & Installation

**Required Files**

#### • REPWRITERSPECS folder

 » BANNO.ODTOPTIN.V1.POW (Main PowerOn Program)

 • Standard PowerOn library include files which should already be in your system:

 » RD.GETDATA.DEF

 » RB.LISTEXPAND.DEF

 » RB.LISTEXPAND

 • LETTERSPECS folder

 » BANNO.ODTOPTIN.V1.CFG (Main program configuration Letter file)

**Installation Steps**

**1.** Upload files to their respective directories

#### » Recommend using Symitar PC Transfer.

**2.** Install the PowerOn programs for demand use


-----

Overdraft Tolerance Opt-In / Opt-Out

**3.** Add the Main PowerOn program name to SymXchange Common Parameters

**4.** In Device Control take SymXChange – Banno Off Host

**5.** Put SymXchange – Banno back On Host and verify Status = On Host

**6.** Update the settings in the configuration Letter file

#### » The configuration Letter file contains details for the various settings.

**7.** Add the program to Banno People

**Configuration Letter File**

The configuration Letter file allows certain aspects of the program to be customized to better meet

your specific needs. Among the options which can be set are:

#### • Identify the share tracking type used to store the current ODT status for each share.

 • Determine which account and share types are ineligible.

 • Determine which account and share level warning codes to exclude.

 • Determine if the program should update the share's ODT Auth/Fee Option 1 and ODT Source

Code List 1 fields at the same time the share is updated and if so, identify the value each should
be set to if the member opts in or opts out.

#### • Determine if the program will set the share's Overdraw Tolerance amount by share type.

 • Set the Terms & Conditions, fee disclosure, revocation instructions, service instructions, Opt-in

information, and Opt-out information verbiage.

The configuration Letter file contains full instructions on setting these run-time parameters. Do

pay close attention when selecting your options making sure to set each option within the
required parameters.

### Database Interaction

**Data Sources**

Data utilized by the program is pulled from the following sources:

#### • Member's open share records

 • ODT share tracking records


-----

Overdraft Tolerance Opt-In / Opt-Out

**Transactions / File Maintenance Performed**

#### • The program updates the following fields in the share record:


AUTHFEEOPTION:1

ODTAUTHFEESRCCODELIST:1

OVERDRAFTTOLERANCE


ODT Auth/Fee Option

ODT Source Code List

Overdraw Tolerance Amount



#### • The program creates and/or updates the ODT share tracking record. The share tracking record

contains the following information:


USERCODE1

USERDATE1


ODT Status

Date of ODT Status Update


### Additional Information

**Share Tracking Records**

The program uses the existence of these tracking records along with the AUTHFEEOPTION:1 and

ODTAUTHFEESRCCODELIST:1 fields on the share record to identify/update the ODT settings for
the share. There will be a share tracking record created under each share once the share is set as
opted in or out.


-----

