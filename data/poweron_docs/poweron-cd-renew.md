# CD Renew

Program Overview


-----

## Contents

**Overview** 3

UX Run-Time Detail 3

PowerOn Run-Time Detail 5

**Program Setup & Installation** 6

Required Files 6

Installation Steps 6

Configuration Letter File 6

**Database Interaction** 7

Data Sources 7

Transactions / File Maintenance Performed 7

Increase Balance and Renew Certificate 7

Change Certificate Term 8

Transfer Balance and Close Certificate 8

Renew Certificate 8

Disburse Funds by Check 8

Suspend Certificate 9

**Additional Information** 9

Single or Multiple Changes 9

Eligible Shares for Transfer In (Transfer at Maturity) 10

Eligible Shares for Transfer Out (Increase Balance at Maturity) 10


-----

# CD Renew

This PowerOn allows the user to determine what action should automatically be taken upon

maturity of their CD.

### UX Run-Time Detail

Upon the user electing to run the program, the Banno UX displays an input form allowing the user to
select, from a list of options, what will happen to their CD upon maturity.

#### • Increase balance and renew certificate

 • Change certificate term

 • Transfer balance and close certificate

 • Renew certificate

 • Disburse funds by check

 • Suspend certificate


-----

CD Renew

Depending upon the option selected by the user, another user input screen may be shown:


-----

CD Renew

Once a selection has been made and any required input completed, a confirmation screen will be
presented with an overview of the option selected and the input received for final verification. Upon
acceptance, the necessary actions will be completed based upon the request. For example – if the
user elected to transfer funds out:

### PowerOn Run-Time Detail

When first run by the member, Banno passes back to the PowerOn the account and share ID the
member is reviewing options for. The program takes this information, reads the various parameter
settings from the configuration Letter file and compiles information which is then passed to the
Banno UX for display to the member. The data passed includes details about the chosen certificate:
term, maturity date, minimum balance, current maturity renewal option, current share transfers set
up and so on. Also passed to the UX are the certificate maturity options which the member will be

able to select from.

Once the member has made their selection and based upon that selection, the PowerOn will update
the member's certificate and any related transfer record(s) as needed.


-----

CD Renew

### Program Setup & Installation

**Required Files**

#### • REPWRITERSPECS folder

 » BANNO.CDRENEW.V1.POW (Main PowerOn Program)

 » Standard PowerOn library include files which should already be in your system:

 • RD.GETDATA.DEF

 • RB.LISTEXPAND.DEF

 • RB.LISTEXPAND

 • LETTERSPECS folder

 » BANNO.CDRENEW.V1.CFG (Main program configuration Letter file)

**Installation Steps**

**1.** Upload files to their respective directories

#### » Recommend using Symitar PC Transfer.

**2.** Install the PowerOn programs for demand use

**3.** Add the PowerOn program name to SymXchange Common Parameters

**4.** In Device Control take SymXchange – Banno Off Host

**5.** Put SymXchange – Banno back On Host and verify Status = On Host

**6.** Update the settings in the configuration Letter file

#### » The configuration Letter file contains details for the various settings.

**7.** Add the program to Banno People

**Configuration Letter File**

The configuration Letter file allows certain aspects of the program to be customized to better suit

your needs. Among the options which can be set are:


-----

CD Renew

#### • Allow which CD Renew options will be presented to the user to select from based upon the

Share type and modify the option descriptors, if desired.

#### • Determine account eligibility by account type(s) and / or account level warning code(s).

 • Determine share eligibility based on share warning code(s).

 • Limit the user to a single change or allow multiple changes to their selections.

 • Determine eligible share types which the user can transfer funds from or to upon maturity.

 • Determine whether existing transfers should be expired or deleted upon selection update.

 • Determine eligibility by share IRS code.

 • Set the payee terms, suspend message, review message, ineligible IRS code message, and

cross-account maturity changes not allowed verbiage.

The configuration Letter file contains full instructions on setting these run-time parameters. Do

pay close attention when selecting your options making sure to set each option within the
required parameters.

### Database Interaction

**Data Sources**

Data utilized by the program is pulled from the following sources:

#### • Share and Loan record(s)

 • Share and Loan Transfer record(s)

**Transactions / File Maintenance Performed**

Based upon the member's selected option, the following actions will be taken by the program:

**Increase balance and renew certificate**

#### • Any existing share transfers type 2 (maturity) currently under the certificate will be expired or

deleted (depending on the configuration parameter setting).

#### • A new share transfer type 3 (auto share transfer) will be created under the debit share and for

the requested amount with the transfer date being set for the day before the certificate is set to
mature.


-----

CD Renew

#### • The maturity post code of the certificate will be set to 0 (renew).

 • If the limit changes parameter is set to 1, a share note record will be added to the certificate.

**Change certificate term**

#### • Because of the potential complexities regarding changing the original terms of a renewing

certificate, should the member elect this option, program output will refer them to contact their
credit union representative.

**Transfer balance and close certificate**

#### • Any existing share transfers type 2 (maturity) currently under the certificate will be expired or

deleted (depending on the configuration parameter setting).

#### • A new share transfer type 2 (maturity) will be created under the certificate pointing to the

desired account and share or loan to be credited on the maturity date of the certificate.

#### • Any existing share transfers type 3 (auto share transfer) to the certificate may be expired or

deleted (depending on the configuration parameter setting).

#### • The maturity post code of the certificate will be set to 2 (transfer).

 • If the limit changes parameter is set to 1, a share note record will be added to the certificate.

**Renew certificate**

#### • Any existing share transfers type 2 (maturity) currently under the certificate will be expired or

deleted (depending on the configuration parameter setting).

#### • Any existing share transfers type 3 (auto share transfer) to the certificate may be expired or

deleted (depending on the configuration parameter setting).

#### • The maturity post code of the certificate will be set to 0 (renew).

 • If the limit changes parameter is set to 1, a share note record will be added to the certificate.

**Disburse funds by check**

#### • Any existing share transfers type 2 (maturity) currently under the certificate will be expired or

deleted (depending on the configuration parameter setting).

#### • Any existing share transfers type 3 (auto share transfer) to the certificate may be expired or

deleted (depending on the configuration parameter setting).

#### • The maturity post code of the certificate will be set to 1 (by check).

 • If the limit changes parameter is set to 1, a share note record will be added to the certificate.


-----

CD Renew

**Suspend certificate**

#### • Any existing share transfers type 2 (maturity) currently under the certificate will be expired or

deleted (depending on the configuration parameter setting).

#### • Any existing share transfers type 3 (auto share transfer) to the certificate may be expired or

deleted (depending on the configuration parameter setting).

#### • The maturity post code of the certificate will be set to 3 (suspend).

 • If the limit changes parameter is set to 1, a share note record will be added to the certificate.

### Additional Information

**Single or Multiple Changes**

One of the settings in the parameter configuration Letter file is the ability to determine whether
the user is allowed to make multiple changes to their certificate maturity option or just one time. If
the parameter is set to limit the user change to just one time, the program will add a note record to
the certificate.

Should the member attempt to change their maturity option at some point in the future, they will be
given a polite request to contact the credit union. Deleting the note record under the certificate will
also allow the user to register their selection once more.


-----

CD Renew

**Eligible shares for transfer in (transfer at maturity)**

The program will use the "TRANSFER CERTIFICATE FUNDS TO SHARE TYPES" parameter setting

in the configuration Letter file and will evaluate service code(s) for transfer in (as determined
by SymXchange parameter settings) to determine which shares the user can transfer funds
to at maturity.

**Eligible shares for transfer out (increase balance at maturity)**

The program will use the "TRANSFER FUNDS IN TO CERTIFICATE FROM SHARE TYPES" parameter

setting in the configuration Letter file and will evaluate service code(s) for transfer out (as determined
by SymXchange parameter settings) to determine which shares the user can pull funds from at
maturity to increase the balance.


-----

