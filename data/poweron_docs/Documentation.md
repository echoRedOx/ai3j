# PowerOn Language Developer Guide

## Table of Contents

1. [Introduction](#1-introduction)
   - 1.1 [Overview](#11-overview)

2. [Syntax and Structure](#2-syntax-and-structure)
   - 2.1 [Keywords](#21-keywords)
   - 2.2 [Operators](#22-operators)
   - 2.3 [Variables](#23-variables)
   - 2.4 [Data Types](#24-data-types)
   - 2.5 [Comments](#25-comments)

3. [File Structure](#3-file-structure)
   - 3.1 [File Extensions](#31-file-extensions)
   - 3.2 [File Format](#32-file-format)

4. [Code Blocks and Sections](#4-code-blocks-and-sections)
   - 4.1 [DEFINE Section](#41-define-section)
   - 4.2 [SETUP Section](#42-setup-section)
   - 4.3 [SELECT Section](#43-select-section)
   - 4.4 [SORT Section](#44-sort-section)
   - 4.5 [PRINT Statement](#45-print-statement)

5. [Control Flow Statements](#5-control-flow-statements)
   - 5.1 [IF Statements](#51-if-statements)
   - 5.2 [WHILE Statements](#52-while-statements)
   - 5.3 [FOR EACH Statements](#53-for-each-statements)

6. [Termination](#6-termination)
   - 6.1 [TERMINATE Statement](#61-terminate-statement)

7. [Limitations and Constraints](#7-limitations-and-constraints)
   - 7.1 [Character Limit](#71-character-limit)
   - 7.2 [Tree-Based Relations](#72-tree-based-relations)

8. [Error Handling](#8-error-handling)
   - 8.1 [Error Messages](#81-error-messages)
   - 8.2 [Exception Handling](#82-exception-handling)

9. [Additional Resources](#9-additional-resources)
   - 11.1 [Reference Documentation](#111-reference-documentation)
   - 11.2 [Community Forums](#112-community-forums)


 
# Introduction

## 1.1 Overview

PowerOn is a scripting language designed for creating specfiles that generate custom reports and interact with the system. It empowers developers to extract specific information from the database by manipulating and presenting selected records.

### Common Tasks Achieved with PowerOn:

- **Produce Demand Inquiries**
- **Perform File Maintenance:**
  Modify fields in the system database efficiently (refer to File Maintenance Specfiles).
  
- **Validate Data Entry:**
  Implement data validation as users type into fields (refer to Validation Specfiles).
  
- **Control Printer Features:**
  Manage laser printer fonts and special features (refer to Laser Printer Use).
  
- **Compute and Print Loan Projections:**
  Generate custom loan projections and disclosures.
  
- **Post Transactions:**
  Post fees, insurance premiums, and comment transactions (refer to Posting Specfiles).

### Outputs and Use Cases:

- **Daily Reports, Forms, Notices:**
  Many routine outputs are generated using specfiles.
  
- **Period-End Assessments:**
  Assess fees based on specfile output during period-end processing.
  
- **Database Updates:**
  Perform database updates seamlessly using specfile output.

PowerOn is a versatile language, providing developers with a powerful toolset to manipulate and extract valuable information from the Symitar system. Mastering PowerOn allows for the creation of efficient, customized reports and the automation of various database-related tasks.

# 2. Syntax and Structure

### 2.1 Keywords
  following are the PowerOn keyword that cannot be used as variables :

  *ABS, ACROSS, ALL, AND, ANY, ANYSERVICE, ANYWARNING, ARRAY, BELL, BLINK, BRIGHT, CALL, CAPITALIZE, CHARACTER, CHARACTERREAD, CHARACTERSEARCH, CHRARRAY, CODEREAD, COL, CTRLCHR, DATAFILE, DATASIZE, DATE, DATEOFFSET, DATEREAD, DATEVALUE, DAY, DAYOFWEEK, DEFINE, DIALOGCLOSE, DIALOGDISPLAY, DIALOGENDGROUPING, DIALOGINTROTEXT, DIALOGNEWCOLUMN, DIALOGPROMPTCHAR, DIALOGPROMPTCODE, DIALOGPROMPTCOMBOEND, DIALOGPROMPTCOMBOOPTION, DIALOGPROMPTCOMBOSTART, DIALOGPROMPTDATE, DIALOGPROMPTLISTEND, DIALOGPROMPTLISTOPTION, DIALOGPROMPTLISTSTART, DIALOGPROMPTMONEY, DIALOGPROMPTNUMBER, DIALOGPROMPTPASSWORD, DIALOGPROMPTRATE, DIALOGPROMPTYESNO, DIALOGSTART, DIALOGSTARTGROUPBOX, DIALOGSTARTGROUPING, DIALOGTEXTLISTEND, DIALOGTEXTLISTOPTION, DIALOGTEXTLISTSTART, DIM, DIVPROJECTCALC, DIVPROJECTINIT, DO, EACH, ELSE, EMAILLINE, EMAILSEND, EMAILSTART, END, ENTERCHARACTER, ENTERCODE, ENTERDATE, ENTERDELIMITER, ENTERLINE, ENTERMONEY, ENTERNUMBER, ENTERRATE, ENTERYESNO, EVERY, EXECUTE, EXP, FILEARCHIVEADD, FILEARCHIVEEXTRACT, FILECLOSE, FILECREATE, FILEDECRYPT, FILEDELETE, FILEENCRYPT, FILEGETPOS, FILELISTCLOSE, FILELISTOPEN, FILELISTREAD, FILEOPEN, FILEREAD, FILEREADLINE, FILESETPOS, FILEWRITE, FILEWRITELINE, FLOAT, FLOATVALUE, FLOOR, FMPERFORM, FOR, FORMAT, FORMLENGTH, FTPCLOSE, FTPCMD, FTPGET, FTPLOGIN, FTPOPEN, FTPPUT, FULLYEAR, GETDATACHAR, GETDATACHARACTER, GETDATADATE, GETDATAMONEY, GETDATANUMBER, GETDATARATE, GETFIELDDATAMAX, GETFIELDDATATYPE, GETFIELDHELPFILE, GETFIELDMNEMONIC, GETFIELDNAME, GETFIELDNUMBER, HEADER, HEADERS, HOUR, HPBOXDRAW, HPESC, HPFONT, HPLINEDRAW, HPLINESPERINCH, HPRESET, HPSETUP, HPUNDERLINE, HPXPOS, HPYPOS, HTMLVIEWDISPLAY, HTMLVIEWLINE, HTMLVIEWOPEN, IF, INITCREDITREPORT, INITSUBROUTINE, INT, LABELS, LEFT, LENGTH, LETTER, LOANPROJECTCALC, LOANPROJECTINIT, LOG, LOWERCASE, MINUTE, MOD, MONEY, MONEYREAD, MONTH, NEWLINE, NEWPAGE, NONANSISTANDARD, NONE, NOT, NUMBER, NUMBERREAD, OR, OUTPUTCLOSE, OUTPUTOPEN, OUTPUTSWITCH, POPUPMESSAGE, PRINT, PRINTCONTROL, PROCEDURE, PULLCREDITREPORT, PWR, RATE, RATECHANGE, RATECHANGES, RATEREAD, REPEATCHR, REPORTCATEGORY, RIGHT, SCREENXYPOS, SEGMENT, SELECT, SERVICEMESSAGE, SETUP, SORT, STARTING, STOPBLINK, SUBTOTAL, SUPPRESS, SUPPRESSNEWLINE, TARGET, TERMINATE, THEN, TITLE, TOTAL, TRAILERS, TRANPERFORM, UNTIL, UPPERCASE, VALUE, VARARRAY, WHILE, WHILELIMIT, WIDTH, WINDDECONNECT, WINDDEDISCONNTECT, WINDDEEXECUTE, WINDDEPOKEDATA, WINDOWSSEND, WINMESSAGEFIELD, WINMESSAGESEND, WINMESSAGESTART, WINMODETEXT, WINMODEWINDOWS, WITH, YEAR, YESNOPROMPT, YESNOREAD*

### 2.2 Operators

Operators in PowerOn perform logical operations. Key operators include logical operators like `AND`, `OR`, and `NOT`.

### 2.3 Variables

Variables are containers for storing data. Predefined variables in PowerOn are identified by the "@" symbol at the beginning. There's no requirement to declare these predefined variables within the DEFINE division. Instead, you configure the values of the @ variables in the SETUP division of your PowerOn specfile.

### 2.4 Data Types

The data type in PowerOn serves to define a specific category of data, encompassing its potential values, permissible operations, and the manner in which those values are stored.

CHARACTER Data Type:
The CHARACTER data type encompasses upper and lowercase letters, digits, spaces, and specific symbols.

CODE Data Type:
The CODE data type comprises a system-specified number of digits.

DATE Data Type:
The DATE data type is designed for storing and manipulating dates.

FLOAT Data Type:
The FLOAT data type represents numbers expressed in scientific notation.

MONEY Data Type:
The MONEY data type is used to identify a dollar amount.

NUMBER Data Type:
The NUMBER data type characterizes numeric data, specifically whole numbers, excluding dollar amounts or rates.

RATE Data Type:
The RATE data type represents a percentage.

### 2.5 Comments
 Use brackets [ ] for comments, anything inside brackets PowerOn treats it as a Comment and ignores it.


# 3. File Structure

Understanding the file structure in PowerOn is crucial for effective development. Key components include:

### 3.1 File Extensions

PowerOn files are distinguished by specific extensions, each serving a unique purpose:

- **.po:** PowerOn language file.
- **.def:** Definition file.
- **.pro:** Program file.
- **.setup:** Setup file.

### 3.2 File Format
  *Add image here for account records*

# 4. Code blocks and sections

### 4.1 DEFINE Section

The `DEFINE` section in PowerOn is used for declaring variables. It's the place where you specify the variables that will be used in your program. Here's an example:

```poweron
DEFINE
  TRUE = 1
  FALSE = 0
  FOUND = NUMBER
END
```

In this example:
- `TRUE` and `FALSE` are declared as constants with values 1 and 0, respectively.
- `FOUND` is declared as a variable of type `NUMBER`. This variable will be used later in the program.

The `END` statement marks the conclusion of the `DEFINE` section.

### 4.2 SETUP Section

The `SETUP` section is where you assign values to the variables declared in the `DEFINE` section. It's essentially the initialization phase of your program. Here's an example:

```poweron
SETUP
  FOUND = TRUE
END
```

In this example:
- The value of `FOUND` is set to `TRUE`. This setup is preparing the program for subsequent logic that may depend on the value of `FOUND`.

The `END` statement marks the end of the `SETUP` section.

### 4.3 SELECT Section

The `SELECT` section is used for filtering records based on specified conditions. It determines which records will be considered in subsequent operations. Here's an example:

```poweron
SELECT
  ACCOUNT:CLOSEDATE='--/--/--'
END
```

In this example:
- Only accounts with a `CLOSEDATE` of `--/--/--` will be selected for further processing.

The `END` statement marks the end of the `SELECT` section.

### 4.4 SORT Section

The `SORT` section is employed for sorting records based on a specified field. It defines the order in which records will be processed or displayed. Here's an example:

```poweron
SORT
  ACCOUNT:OPENDATE
END
```

In this example:
- Accounts will be sorted based on the `OPENDATE` field.

The `END` statement marks the end of the `SORT` section.

Got it, thank you for the clarification. Let's adjust the explanation for the `PRINT` statement and the `PRINT TITLE` section accordingly:

### 4.5 PRINT Statement

The `PRINT` statement in PowerOn is used to display output. It is often used to print text, including variable values, to the output. Here's an example:

```poweron
PRINT "HELLO WORLD"
```

In this example:
- The `PRINT` statement is used to display the text "HELLO WORLD" in the output.

### 4.6 PRINT TITLE Section

The `PRINT TITLE` section in PowerOn is similar to the `body` section in HTML code. It's used to structure and organize the content that will be printed. Here's an example:

```poweron
PRINT TITLE="REPORT"
  PRINT "Hello World"
END
```

In this example:
- The `PRINT TITLE` statement sets the title of the report to "REPORT".
- The subsequent `PRINT "Hello World"` statement is within the body of the report.

The `END` statement marks the conclusion of the `PRINT TITLE` section.

Certainly! Let's dive deeper into the Control Flow Statements section of the PowerOn Language Developer Guide.

---

## 5. Control Flow Statements

Control flow statements in PowerOn provide the ability to conditionally execute code or loop through sets of records. This section covers the following key control flow statements:

### 5.1 IF Statements

The `IF` statement in PowerOn is used for conditional branching. It allows the execution of a block of code if a specified condition is true. The basic structure is as follows:

```poweron
IF condition THEN
  DO
    // Code to execute when the condition is true
  END
```

You can also include an `ELSE` block to specify code that executes when the condition is false:

```poweron
IF condition THEN
  DO
    // Code to execute when the condition is true
  END
ELSE
  DO
    // Code to execute when the condition is false
  END
```

Additionally, you can use an `ELSE IF` block for multiple condition checks:

```poweron
IF condition1 THEN
  DO
    // Code to execute when condition1 is true
  END
ELSE IF condition2 THEN
  DO
    // Code to execute when condition2 is true
  END
ELSE
  DO
    // Code to execute when all conditions are false
  END
```

### 5.2 WHILE Statements

The `WHILE` statement in PowerOn is used for creating loops that execute a block of code while a specified condition is true. The structure is as follows:

```poweron
WHILE condition
  DO
    // Code to execute while the condition is true
  END
```

The code inside the `DO...END` block will continue to execute as long as the specified condition remains true.

### 5.3 FOR EACH Statements

The `FOR EACH` statement is used for iterating through a set of records that match a specified condition. It's often used to process records in a database-like structure. The basic structure is as follows:

```poweron
FOR EACH record IN dataset WITH condition
  DO
    // Code to execute for each matching record
  END

Example :
 FOR EACH ACCOUNT WITH ACCOUNT:NUMBER = 00010
  DO
    // Code to execute for each matching record
  END
```
```poweron
FOR record IN dataset condition
  DO
    // Code to execute for each matching record
  END

Example :
 FOR ACCOUNT ACCOUNT:NUMBER
  DO
    // Code to execute for each matching record
  END
```

In this statement:
- `record` represents the current record being processed.
- `dataset` is the dataset (e.g., `ACCOUNT`, `LOAN`) to iterate through.
- `condition` is an optional condition that the records must satisfy.

You can include multiple conditions in the `WITH` clause to narrow down the set of records.

# 6. TERMINATE Statement:

The `TERMINATE` statement in PowerOn is used to gracefully exit the application based on a specified condition. When the condition evaluates to true, the program terminates immediately. This is particularly useful for ending the execution of a PowerOn script once a specific goal or condition is met.

**Example:**
```poweron
IF PROCESS_SUCCESSFUL = TRUE THEN
 DO
  TERMINATE;
 END;
```

## 7. Limitations and Constraints

### 7.1 Character Limit

In the PowerOn language, one notable constraint is the character limit for each line of code. The maximum number of characters allowed on a single line is 132. This limitation is in place to ensure readability and adherence to coding standards.

**Example:**

```poweron
PRINT "This is a PowerOn code line with 132 characters .........................................................."
```

### 7.2 Tree-Based Relations

PowerOn utilizes a tree-based relational structure for organizing and representing data relationships. This approach involves organizing data in a hierarchical tree format, which can include parent-child relationships.

#### Key Points:

- **Hierarchy:** Data is structured hierarchically, with parent nodes and child nodes forming a tree structure.  
- **Relations:** The relations between different elements are represented in a tree format, allowing for efficient querying and manipulation.

Great, let's incorporate the information about error handling, specifically error messages and exception handling, into the developer guide for the PowerOn language.

---

## 8. Error Handling

### 8.1 Error Messages

In PowerOn, error messages play a crucial role in debugging and understanding the flow of your application. One common method for displaying custom messages is through the `POPUPMESSAGE` function. This function is particularly useful when you want to inspect the value of a variable during runtime.

**Example:**

```poweron
POPUPMESSAGE(0, "STRING: " + FORMAT("#9", FOUND))
```

In this example, the `POPUPMESSAGE` function displays a popup with the concatenated string "STRING: " and the formatted value of the `FOUND` variable. The `FORMAT("#9", FOUND)` part converts the numeric value of `FOUND` to a character value (string) for better readability.

### 8.2 Exception Handling

PowerOn does not have native support for traditional exception handling like try-catch blocks in some other languages. However, the `POPUPMESSAGE` function can be strategically used for similar purposes. By strategically placing `POPUPMESSAGE` calls in critical sections of your code, you can effectively create checkpoints for debugging.

**Example:**

```poweron
IF FOUND = TRUE THEN
  DO
    POPUPMESSAGE(0, "Debug Point: Inside IF Statement")
    PRINT "HELLO WORLD"
  END
ELSE
  DO
    POPUPMESSAGE(0, "Debug Point: Inside ELSE Statement")
    PRINT "HELL MIAMI"
  END
```
In this example, `POPUPMESSAGE` is used to create debug points inside conditional statements. When the condition is met (`FOUND = TRUE`), a popup displays "Debug Point: Inside IF Statement," and similarly for the else branch.
---