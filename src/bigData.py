#!/usr/bin/env python                                               	         	  

#                         ~                                         	         	  
#                        (o)<  DuckieCorp Software License          	         	  
#                   .____//                                         	         	  
#                    \ <' )   Copyright (c) 2022 Erik Falor         	         	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	  
#                                                                   	         	  
# Permission is NOT granted, to any person who is NEITHER an employee NOR     	  
# customer of DuckieCorp, to deal in the Software without restriction,        	  
# including without limitation the rights to use, copy, modify, merge,        	  
# publish, distribute, sublicense, and/or sell copies of the Software, and to 	  
# permit persons to whom the Software is furnished to do so, subject to the   	  
# following conditions:                                             	         	  
#                                                                   	         	  
# The above copyright notice and this permission notice shall be included in  	  
# all copies or substantial portions of the Software.               	         	  
#                                                                   	         	  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    	  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 	  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      	  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     	  
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS	  
# IN THE SOFTWARE.                                                  	         	  

import time                                                         	         	  
import sys                                                          	         	  
from Report import Report                                           	         	  


rpt = Report(year=2020)


def openAndReadAlias(fileName):
    file = open(fileName, "r")
    areaTitlesDict = {}
    done = False
    while not done:
        readOneLine = file.readline()
        if readOneLine == "":
            done = True
        elif readOneLine.startswith("\"area_fips\""):
            continue
        elif readOneLine.startswith("\"US"):
            continue
        elif readOneLine.find("000\",\"") != -1:
            continue
        elif readOneLine.startswith("\"C"):
            continue
        else:
            readOneLine = readOneLine.lstrip("\"")
            readOneLine = readOneLine.rstrip("\n")
            readOneLine = readOneLine.rstrip("\"")
            oneLineArray = readOneLine.split("\",\"")
            areaTitlesDict[oneLineArray[0]] = oneLineArray[1]

    return areaTitlesDict

def openAndReadAnnualFile(annualFileName, areaTitlesDict, rpt):
    file = open(annualFileName, "r")
    readKeys = file.readline()
    readKeys = readKeys.lstrip("\"")
    readKeys = readKeys.rstrip("\n")
    readKeys = readKeys.rstrip("\"")
    keyArray = readKeys.split("\",\"")

    forever = True
    while forever:
        valueOneLine = file.readline()
        if valueOneLine == "":
            break

        valueOneLine = valueOneLine.replace("\"", "")
        valueOneLine = valueOneLine.rstrip("\n")
        valueArray = valueOneLine.split(",")
        oneRowDict = dict(zip(keyArray, valueArray))

        # if area fip is undesired data, skip past it
        if oneRowDict["area_fips"] not in areaTitlesDict.keys():
            continue

        rptHandle = None
        if oneRowDict["industry_code"] == "10" and oneRowDict["own_code"] == "0":
            rptHandle = rpt.all
        elif oneRowDict["industry_code"] == "5112" and oneRowDict["own_code"] == "5":
            rptHandle = rpt.soft

        # if industry code and own code do NOT match up, undesired data, so skip it
        if rptHandle is None:
            continue

        # number of areas
        rptHandle.num_areas += 1

        # annual wages
        totalAnnualWages = int(oneRowDict["total_annual_wages"])
        rptHandle.total_annual_wages += totalAnnualWages
        if totalAnnualWages > rptHandle.max_annual_wage[1]:
            rptHandle.max_annual_wage[1] = totalAnnualWages
            rptHandle.max_annual_wage[0] = areaTitlesDict[oneRowDict["area_fips"]]




if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("No file given")
        sys.exit(1)

    print("Reading the databases...", file=sys.stderr)              	         	  
    before = time.time()                                            	         	  

    fileName = sys.argv[1] + "/area_titles.csv"
    areaTitlesDict = openAndReadAlias(fileName)

    annualFileName = sys.argv[1] + "/2020.annual.singlefile.csv"
    openAndReadAnnualFile(annualFileName, areaTitlesDict, rpt)
    print("TODO: if opening the file 'sys.argv[1]/2020.annual.singlefile.csv' fails, let your program crash here")  # DELETE ME
    print("TODO: Collect information from 'sys.argv[1]/2020.annual.singlefile.csv', place into the Report object rpt")  # DELETE ME

    after = time.time()                                             	         	  
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)	         	  

    # print("TODO: Fill in the report for all industries")  # DELETE ME
    # rpt.all.num_areas           = 1337
    #
    # rpt.all.total_annual_wages  = 13333337
    # rpt.all.max_annual_wage     = ["Trantor", 123456]
    #
    # rpt.all.total_estab         = 42
    # rpt.all.max_estab           = ["Terminus", 12]
    #
    # rpt.all.total_empl          = 987654
    # rpt.all.max_empl            = ["Anacreon", 654]
    #
    #
    # print("TODO: Fill in the report for the software publishing industry")  # DELETE ME
    # rpt.soft.num_areas          = 1010
    #
    # rpt.soft.total_annual_wages = 101001110111
    # rpt.soft.max_annual_wage    = ["Helicon", 110010001]
    #
    # rpt.soft.total_estab        = 1110111
    # rpt.soft.max_estab          = ["Solaria", 11000]
    #
    # rpt.soft.total_empl         = 100010011
    # rpt.soft.max_empl           = ["Gaia", 10110010]
    #
    #
    # Print the completed report                                    	         	  
    print(rpt)                                                      	         	  

    print("\n\nTODO: did you delete all of these TODO messages?")  # DELETE ME	  
