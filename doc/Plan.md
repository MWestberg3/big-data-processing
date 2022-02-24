# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

* A detailed written description of the problem this program aims to solve.
  * Analyze a large csv file, and return certain data from the files. Data will be separated into 2 sections: a summary across all industries, and a summary of the software industry.
  * The file to be read is 493MB, therefore it will need to read smaller chunks at a time for optimal performance.
  * Create output that shows the desired data.
* Describe what a *good* solution looks like.
    * List what you already know how to do.
      * Searching a document for desired information.
      * Parsing through csv files.
      * Manipulating Strings.
      * Open files.
      * Open files line by line.
      * Closing files.
      * Creating lists.
      * Create new files based on old files.
    * Point out any challenges that you can foresee.
      * I don't know how to create a dictionary.
      * I'm not sure that I fully understand what data we are looking for.


## Phase 1: System Analysis *(10%)*

**Deliver:**

* List all of the data that is used by the program, making note of where it comes from.
  * What data do I need to collect?:
    * Area Fips (area_fips) (field #1) (data type: text)
    * Industry Code (industry_code) (field #3) (data type: text)
    * Own Code (own_code) (field #2) (data type: text)
    * Total Annual Wages (total_annual_wages) (field #16) (data type: Numeric)
    * Annual Average Employment Level (annual_avg_emplvl) (field #15) (data type: numeric)
    * Annual Average Establishments (annual_avg_estabs) (field # 14) (data type: numeric)
* Explain what form the output will take.
  * Output will be a string (when outputting the names of cities) and an integer (when outputting the numbers of fips and wages)
* Describe what algorithms and formulae will be used (but don't write them yet).
  * I will need to take the sum of all the wages
  * Count the amount of valid fip area codes

## Phase 2: Design *(30%)*

**Deliver:**

* Function signatures that include:
    * openAndCloseAlias(fileName)
    * openAndCloseAnnualFile(annualFileName, areaTitleDict, rpt)
* Pseudocode that captures how each function works.
    * openAndCloseAlias(fileName)
      * open file
      * create an empty dictionary
      * begin a while loop that will check each line (open file line by line) for data we want to add to dictionary
      * once we clear all the data we don't want, strip the quotes, the new lines, and split the data at the ",", and add it to the dictionary
      * return the dictionary

    * openAndCloseAnnualFile(annualFileName, areaTitleDict, rpt)
      * open the annualFileName
      * read the first line of the file (This will be the basis of the dictionary we create to assign the values to a 'key' that will identify the value desired)
      * strip the first line (keys) to get a bare string, and add it to an array (this array will account for the keys)
      * while loop
        * read the file one line at a time
        * if the line is empty, this signifies the end of the file, break out of the loop
        * strip the file to a bare string or int data type
        * if the fips area code does not match a fips area code in the area title list, continue to the next iteration (we don't want that data)
        * create a handle to decide where the data gets passed to (either the all industries, or the software industries) - this is decided based on the industry code and the own code
          * if the industry code and the own code don't match, we don't want this data, continue to the next loop iteration
        * add 1 to the successful fips area codes
        * add the total annual wages to the handle's total annual wages
        * test if the total annual wage is the max, if so, update the handle, and get the location
        * add the total establishments to the total estab handle (this gives you the total establishments)
        * test if the total establishments is the max by comparing to the current handle. If so, update the handle and get the location
        * add the total employees to the total employee handle (this updates the handle for the total employees)
        * test if the total employee is the max by comparing to the current handle. If the current iteration is larger than the current handle, get the value and the location 

## Phase 3: Implementation *(15%)*

**Deliver:**

*   (More or less) working code.
*   Note any relevant and interesting events that happened while you wrote the code.
    * I absolutely loved learning about dictionaries. I had no idea how to use them at all prior, and it was very interesting learning about them.
    * I think dictionaries are very useful to access data. I feel like you can do similar actions with lists and making constants, but it was very organized, and there were less items to change because I was using a list.
    
## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    * I ran a test on CT_combined, failed.
      * the total establishments was passing in the wrong data. I was passing in the actual number, rather than the area_fips. Caused an error where it couldn't find the desired fips area code.
      * fixed the code on line 108 to access the dictionary areaTitlesDict and specifically the area_fips in oneRowDict
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.


## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

**Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   Fill out the Assignment Reflection on Canvas.
