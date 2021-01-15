# Initial Standards of Documentation/Organization
-------------------------------------------------

The following information is intended to improve modularity and later integration. Documentation of code will be done by the software engineer who wrote it, but should be easily readable by other engineers. This information may be moved to a more permanent document later and will be updated as time goes on.

* At the beginning of a module as a header comment, the following must be included:
  * Name of the file
  * Class and date
  * Name of the team and principal programmer
  * General overview of the file's purpose

* For *every* function, both explicitly specified in the project handout and helpers, the following must be included in a block comment:
  * Description of the function - what does it do (and why if appropriate)
  * Input and Output form - for example, int list or a tuple of the form (int, string)
  * Any quirks of data expectations - for example, if it expects ints to be non-zero

* It is assumed that the functions explicitly described in the document will have the same signature as it appears in the document.

* The three files that will represent modules 3.1/3.2, 3.3, and 3.4 are all expected to contain only the explicitly described functions in the project description.
  * For each module, any helpers should be relegated to a single helper file for that module if possible (with a file name that reflects that purpose, for example preprocessing_helper.py helps preprocessing.py). This should help compartmentalize code and make it easier to check progress.
  * Tests for each module (every significant function should be tested) are expected to reside in a similarly named file (for example preprocessing_tests.py).

* If a module requires a library or package, documentation for how to install the library or package locally in the module header must be present (through pip, Anaconda, or wherever else) so the other engineers may configure their environments to match.
  * We will later collect this information into one place to describe how to run our code.

* It is assumed that we will be using Python 3.8 for the bulk of the project.


# Data Expectations
-------------------
* A time series will be a csv of the form (time0,magnitude0),(time1,magnitude1),...,(timeN,magnitudeN) where time and magnitude are both non-negative values.
  * Note: Logan and Jarett may have further input on this since Logan will be responsible for outputting data in this form and Jarett will be responsible for inputting data of this form. We may also get more info when we meet on the 1/19.
