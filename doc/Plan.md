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
      * 
    * Industry Code (industry_code) (field #3) (data type: text)
    * Own Code (own_code) (field #2) (data type: text)
    * Total Annual Wages (total_annual_wages) (field #16) (data type: Numeric)
    * Annual Average Employment Level (annual_avg_emplvl) (field #15) (data type: numeric)
    * Annual Average Establishments (annual_avg_estabs) (field # 14) (data type: numeric)
* Explain what form the output will take.
* Describe what algorithms and formulae will be used (but don't write them yet).


## Phase 2: Design *(30%)*

**Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.


## Phase 3: Implementation *(15%)*

**Deliver:**

*   (More or less) working code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
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
