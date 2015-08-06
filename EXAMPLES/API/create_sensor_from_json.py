
"""
Export a sensor object to a JSON file, adding ' API TEST' to the name of the sensor before exporting the JSON file and deleting any pre-existing sensor with the same (new) name, then create a new sensor object from the exported JSON file
"""

import os
import sys
sys.dont_write_bytecode = True

# Determine our script name, script dir
my_file = os.path.abspath(sys.argv[0])
my_dir = os.path.dirname(my_file)

# determine the pytan lib dir and add it to the path
parent_dir = os.path.dirname(my_dir)
pytan_root_dir = os.path.dirname(parent_dir)
lib_dir = os.path.join(pytan_root_dir, 'lib')
path_adds = [lib_dir]

for aa in path_adds:
    if aa not in sys.path:
        sys.path.append(aa)


# connection info for Tanium Server
USERNAME = "Tanium User"
PASSWORD = "T@n!um"
HOST = "172.16.31.128"
PORT = "444"

# Logging conrols
LOGLEVEL = 2
DEBUGFORMAT = False

import tempfile

import pytan
handler = pytan.Handler(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    loglevel=LOGLEVEL,
    debugformat=DEBUGFORMAT,
)

print handler

# set the attribute name and value we want to add to the original object (if any)
attr_name = "name"
attr_add = " API TEST"

# delete object before creating it?
delete = True

# setup the arguments for getting an object to export as json file
get_kwargs = {}
get_kwargs["objtype"] = u'sensor'
get_kwargs["id"] = 381


# get objects to use as an export to JSON file
orig_objs = handler.get(**get_kwargs)

# if attr_name and attr_add exists, modify the orig_objs to add attr_add to the attribute
# attr_name
if attr_name:
    for x in orig_objs:
        new_attr = getattr(x, attr_name)
        new_attr += attr_add
        setattr(x, attr_name, new_attr)
        if delete:
            # delete the object in case it already exists
            del_kwargs = {}
            del_kwargs[attr_name] = new_attr
            del_kwargs['objtype'] = u'sensor'
            try:
                handler.delete(**del_kwargs)
            except Exception as e:
                print e

# export orig_objs to a json file
json_file, results = handler.export_to_report_file(
    obj=orig_objs,
    export_format='json',
    report_dir=tempfile.gettempdir(),
)

# create the object from the exported JSON file
create_kwargs = {'objtype': u'sensor', 'json_file': json_file}
response = handler.create_from_json(**create_kwargs)


print ""
print "Type of response: ", type(response)

print ""
print "print of response:"
print response

print ""
print "print the object returned in JSON format:"
print response.to_json(response)


'''Output from running this:
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: Not yet determined!
2015-08-06 14:56:10,732 INFO     pytan.handler: Deleted 'Sensor, id: 3874'
2015-08-06 14:56:10,733 INFO     pytan.handler: Report file '/var/folders/dk/vjr1r_c53yx6k6gzp2bbt_c40000gn/T/SensorList_2015_08_06-10_56_10-EDT.json' written with 15857 bytes
2015-08-06 14:56:10,791 INFO     pytan.handler: New Sensor, name: 'Folder Name Search with RegEx Match API TEST', id: 3876 (ID: 3876) created successfully!

Type of response:  <class 'taniumpy.object_types.sensor_list.SensorList'>

print of response:
SensorList, len: 1

print the object returned in JSON format:
{
  "_type": "sensors", 
  "sensor": [
    {
      "_type": "sensor", 
      "category": "File System", 
      "creation_time": "2015-08-06T14:56:10", 
      "delimiter": ",", 
      "description": "Finds the specified folder and provides the full path if the folder exists on the client machine. Takes regular expression to match.\nExample: C:\\WINDOWS\\System32", 
      "exclude_from_parse_flag": 1, 
      "hash": 839342978, 
      "hidden_flag": 0, 
      "id": 3876, 
      "ignore_case_flag": 1, 
      "last_modified_by": "Tanium User", 
      "max_age_seconds": 600, 
      "metadata": {
        "_type": "metadata", 
        "item": [
          {
            "_type": "item", 
            "admin_flag": 0, 
            "name": "defined", 
            "value": "McAfee"
          }
        ]
      }, 
      "modification_time": "2015-08-06T14:56:10", 
      "name": "Folder Name Search with RegEx Match API TEST", 
      "parameter_definition": "{\"parameters\":[{\"label\":\"Search for Folder Name\",\"maxChars\":0,\"restrict\":null,\"validationExpressions\":[{\"helpString\":\"Value must be at least 3 characters\",\"expression\":\"\\\\S{3}\",\"flags\":\"\",\"model\":\"com.tanium.models::ValidationExpression\",\"parameterType\":\"com.tanium.models::ValidationExpression\"}],\"value\":\"\",\"helpString\":\"Enter the folder name to search for\",\"promptText\":\"e.g Program Files\",\"defaultValue\":\"\",\"key\":\"dirname\",\"model\":\"com.tanium.components.parameters::TextInputParameter\",\"parameterType\":\"com.tanium.components.parameters::TextInputParameter\"},{\"label\":\"Regular Expression\",\"maxChars\":0,\"restrict\":null,\"validationExpressions\":[{\"helpString\":\"Value must be at least 3 characters\",\"expression\":\"\\\\S{3}\",\"flags\":\"\",\"model\":\"com.tanium.models::ValidationExpression\",\"parameterType\":\"com.tanium.models::ValidationExpression\"}],\"value\":\"\",\"helpString\":\"Enter the regular expression to search for.\",\"promptText\":\"e.g. test*.exe\",\"defaultValue\":\"\",\"key\":\"regexp\",\"model\":\"com.tanium.components.parameters::TextInputParameter\",\"parameterType\":\"com.tanium.components.parameters::TextInputParameter\"},{\"label\":\"Case sensitive?\",\"values\":[\"No\",\"Yes\"],\"value\":\"\",\"helpString\":\"Enter Yes/No for case sensitivity of search.\",\"requireSelection\":true,\"promptText\":\"\",\"defaultValue\":\"\",\"key\":\"casesensitive\",\"model\":\"com.tanium.components.parameters::DropDownParameter\",\"parameterType\":\"com.tanium.components.parameters::DropDownParameter\"},{\"label\":\"Global\",\"values\":[\"No\",\"Yes\"],\"value\":\"\",\"helpString\":\"Enter Yes/No whether the search is global.\",\"requireSelection\":true,\"promptText\":\"\",\"defaultValue\":\"\",\"key\":\"global\",\"model\":\"com.tanium.components.parameters::DropDownParameter\",\"parameterType\":\"com.tanium.components.parameters::DropDownParameter\"}],\"model\":\"com.tanium.components.parameters::ParametersArray\",\"parameterType\":\"com.tanium.components.parameters::ParametersArray\"}", 
      "queries": {
        "_type": "queries", 
        "query": [
          {
            "_type": "query", 
            "platform": "Windows", 
            "script": "&#039;========================================\n&#039; Folder Name Search with RegEx Match\n&#039;========================================\n&#039;@INCLUDE=utils/SensorRandomization/SensorRandomizationFunctions.vbs\nOption Explicit\n\nSensorRandomize()\n\nDim Pattern,strRegExp,strGlobalArg,strCaseSensitiveArg\nDim bGlobal,bCaseSensitive\n\nPattern = unescape(&quot;||dirname||&quot;)\nstrRegExp = Trim(Unescape(&quot;||regexp||&quot;))\nstrGlobalArg = Trim(Unescape(&quot;||global||&quot;))\nstrCaseSensitiveArg = Trim(Unescape(&quot;||casesensitive||&quot;))\n\nbGlobal = GetTrueFalseArg(&quot;global&quot;,strGlobalArg)\nbCaseSensitive = GetTrueFalseArg(&quot;casesensitive&quot;,strCaseSensitiveArg)\n\nConst SYSTEM_FOLDER = 1, TEMP_FOLDER = 2, FOR_READING = 1\n\nDim FSO, WshShell, Drives, Drive, TextStream, OutputFilename, strLine\n\nSet FSO = CreateObject(&quot;Scripting.FileSystemObject&quot;)\nSet WshShell = CreateObject(&quot;WScript.Shell&quot;)\n\nOutputFilename = TempName() &#039; a temporary file in system&#039;s temp dir\n\n&#039; Go through file system, refresh output file for filename\nIf Not FSO.FileExists(OutputFilename) Then\n\t\n\tIf FSO.FileExists(OutputFilename) Then FSO.DeleteFile OutputFilename\n\n\t&#039; Get the collection of local drives.\n\tSet Drives = FSO.Drives\n\tFor Each Drive in Drives\n\t\tIf Drive.DriveType = 2 Then &#039; 2 = Fixed drive\n\t\t\t&#039; Run the Dir command that looks for the filename pattern.\n\t\t\tRunCommand &quot;dir &quot; &amp;Chr(34)&amp; Drive.DriveLetter &amp; &quot;:\\&quot; &amp; Pattern &amp; Chr(34)&amp;&quot; /a:D /B /S&quot;, OutputFilename, true\n\t\tEnd If\n\tNext\nEnd If\n\n&#039; Open the output file, echo each line, and then close and delete it.\nSet TextStream = FSO.OpenTextFile(OutputFileName, FOR_READING)\nDo While Not TextStream.AtEndOfStream\n\tstrLine = TextStream.ReadLine()\n\tIf RegExpMatch(strRegExp,strLine,bGlobal,bCaseSensitive) Then\n\t\tWScript.Echo strLine\n\tEnd If\nLoop\n\n\nTextStream.Close()\n \nIf FSO.FileExists(OutputFileName) Then\n\tOn Error Resume Next\n\tFSO.DeleteFile OutputFileName, True\n\tOn Error Goto 0\nEnd If\n\nFunction RegExpMatch(strPattern,strToMatch,bGlobal,bIsCaseSensitive)\n\n\tDim re\n\tSet re = New RegExp\n\tWith re\n\t  .Pattern = strPattern\n\t  .Global = bGlobal\n\t  .IgnoreCase = Not bIsCaseSensitive\n\tEnd With\n\t\n\tRegExpMatch = re.Test(strToMatch)\n\nEnd Function &#039;RegExpMatch\n\n\nFunction GetTrueFalseArg(strArgName,strArgValue)\n\t&#039; Checks for valid values, will fail with error message\n\t\n\tDim bArgVal\n\tbArgVal = False\n\tSelect Case LCase(strArgValue)\n\t\tCase &quot;true&quot;\n\t\t\tbArgVal = True\n\t\tCase &quot;yes&quot;\n\t\t\tbArgVal = True\n\t\tCase &quot;false&quot;\n\t\t\tbArgVal = False\n\t\tCase &quot;no&quot;\n\t\t\tbArgVal = False\n\t\tCase Else\n\t\t\tWScript.Echo &quot;Error: Argument &#039;&quot;&amp;strArgName&amp;&quot;&#039; must be True or False, quitting&quot;\n\t\t\tPrintUsage\n\tEnd Select\n\tGetTrueFalseArg = bArgVal\n\nEnd Function &#039;GetTrueFalseArg\n\n\n&#039; Returns the name of a temporary file in the Temp directory.\nFunction TempName()\n\tDim Result\n\tDo\n \t\tResult = FSO.BuildPath(FSO.GetSpecialFolder(TEMP_FOLDER), FSO.GetTempName())\n\t\tWScript.Sleep 200 &#039;avoid potential busy loop\n\tLoop While FSO.FileExists(Result)\n\t\n\tTempName = Result\nEnd Function &#039;TempName\n\n&#039; Runs a command with Cmd.exe and redirects its output to a temporary\n&#039; file. The function returns the name of the temporary file that holds\n&#039; the command&#039;s output.\nFunction RunCommand(Command, OutputFilename, b64BitNecessary)\n\t&#039; 64BitNecessary true when you need to examine the 64-bit areas like system32\n\tDim CommandLine,WshShell,strPRogramFilesx86,strDOSCall,objFSO\n\tSet objFSO = CreateObject(&quot;Scripting.FileSystemObject&quot;)\n\tSet WshShell = CreateObject(&quot;WScript.Shell&quot;)\n\t\n\tstrDOSCall = &quot;%ComSpec% /C &quot;\n\t\n\t&#039; if 64-bit OS *and* we must examine in 64-bit mode to avoid FS Redirection\n\tstrProgramFilesx86=WshShell.ExpandEnvironmentStrings(&quot;%ProgramFiles%&quot;)\n\tIf objFSO.FolderExists(strProgramFilesx86) And b64BitNecessary Then &#039; quick check for x64\n\t\tstrDOSCall = FixFileSystemRedirectionForPath(WshShell.ExpandEnvironmentStrings(strDOSCall))\n\tEnd If\n\t\t\n\tCommandLine = WshShell.ExpandEnvironmentStrings(strDOSCall &amp; Command &amp; &quot; &gt;&gt; &quot;&quot;&quot; &amp; OutputFileName &amp; &quot;&quot;&quot;&quot;)\n\tWshShell.Run CommandLine, 0, True\nEnd Function &#039;RunCommand\n\nFunction FixFileSystemRedirectionForPath(strFilePath)\n&#039; This function will fix a folder location so that\n&#039; a 32-bit program can be passed the windows\\system32 directory\n&#039; as a parameter.\n&#039; Even if the sensor or action runs in 64-bit mode, a 32-bit\n&#039; program called in a 64-bit environment cannot access\n&#039; the system32 directory - it would be redirected to syswow64.\n&#039; you would not want to do this for 64-bit programs.\n\t\n\tDim objFSO, strSystem32Location,objShell\n\tDim strProgramFilesx86,strNewSystem32Location,strRestOfPath\n\tSet objFSO = CreateObject(&quot;Scripting.FileSystemObject&quot;)\n\tSet objShell = CreateObject(&quot;Wscript.Shell&quot;)\n\n\tstrProgramFilesx86=objShell.ExpandEnvironmentStrings(&quot;%ProgramFiles%&quot;)\n\n\tstrFilePath = LCase(strFilePath)\n\tstrSystem32Location = LCase(objFSO.GetSpecialFolder(1))\n\tstrProgramFilesx86=objShell.ExpandEnvironmentStrings(&quot;%ProgramFiles(x86)%&quot;)\n\t\n\tIf objFSO.FolderExists(strProgramFilesx86) Then &#039; quick check for x64\n\t\tIf InStr(strFilePath,strSystem32Location) = 1 Then\n\t\t\tstrRestOfPath = Replace(strFilePath,strSystem32Location,&quot;&quot;)\n\t\t\tstrNewSystem32Location = Replace(strSystem32Location,&quot;system32&quot;,&quot;sysnative&quot;)\n\t\t\tstrFilePath = strNewSystem32Location&amp;strRestOfPath\n\t\tEnd If\n\tEnd If\n\tFixFileSystemRedirectionForPath = strFilePath\n\t\n\t&#039;Cleanup\n\tSet objFSO = Nothing\nEnd Function &#039;FixFileSystemRedirectionForPath\n&#039;------------ INCLUDES after this line. Do not edit past this point -----\n&#039;- Begin file: utils/SensorRandomization/SensorRandomizationFunctions.vbs\n&#039;&#039; -- Begin Random Sleep Functions -- &#039;&#039;\n\nDim bSensorRandomizeDebugOutput : bSensorRandomizeDebugOutput = False\n\nFunction SensorRandomizeLow()\n    Dim intSensorRandomizeWaitLow : intSensorRandomizeWaitLow = 10\n    SensorRandomizeRandomSleep(intSensorRandomizeWaitLow)\nEnd Function &#039; SensorRandomizeLow\n\nFunction SensorRandomize()\n    Dim intSensorRandomizeWaitMed : intSensorRandomizeWaitMed = 20\n    SensorRandomizeRandomSleep(intSensorRandomizeWaitMed)\nEnd Function &#039; SensorRandomize\n\nFunction SensorRandomizeHigh()\n    Dim intSensorRandomizeWaitHigh : intSensorRandomizeWaitHigh = 30\n    SensorRandomizeRandomSleep(intSensorRandomizeWaitHigh)\nEnd Function &#039; SensorRandomize\n\nFunction SensorRandomizeRandomSleep(intSleepTime)\n&#039; sleeps for a random period of time, intSleepTime is in seconds\n&#039; if the sensor randomize flag is on\n&#039; RandomizeScalingFactor is a multiplier on the values hardcoded in the sensor\n&#039; not typically set but can adjust timings per endpoint, optionally\n\tDim intSensorRandomizeWaitTime\n\tDim objShell,intRandomizeFlag,strRandomizeRegPath,intRandomizeScalingPercentage\n\tstrRandomizeRegPath = SensorRandomizeGetTaniumRegistryPath&amp;&quot;\\Sensor Data\\Random Sleep&quot;\n\t\n\tSet objShell = CreateObject(&quot;WScript.Shell&quot;)\n\tOn Error Resume Next\n\tintRandomizeFlag = objShell.RegRead(&quot;HKLM\\&quot;&amp;strRandomizeRegPath&amp;&quot;\\SensorRandomizeFlag&quot;)\n\tintRandomizeScalingPercentage = objShell.RegRead(&quot;HKLM\\&quot;&amp;strRandomizeRegPath&amp;&quot;\\SensorRandomizeScalingPercentage&quot;)\n\tOn Error Goto 0\n\tIf intRandomizeFlag &gt; 0 Then\n\t\tIf intRandomizeScalingPercentage &gt; 0 Then\n\t\t\tintSleepTime = intRandomizeScalingPercentage * .01 * intSleepTime\n\t\t\tSensorRandomizeEcho &quot;Randomize scaling percentage of &quot; _ \n\t\t\t\t&amp; intRandomizeScalingPercentage &amp; &quot; applied, new sleep time is &quot; &amp; intSleepTime\n\t\tEnd If\n\t\tintSensorRandomizeWaitTime = CLng(intSleepTime) * 1000 &#039; convert to milliseconds\n\t\t&#039; wait random interval between 0 and the max\n\t\tRandomize(SensorRandomizeTaniumRandomSeed)\n\t\t&#039; assign random value to wait time max value\n\t\tintSensorRandomizeWaitTime = Int( ( intSensorRandomizeWaitTime + 1 ) * Rnd )\n\t\tSensorRandomizeEcho &quot;Sleeping for &quot; &amp; intSensorRandomizeWaitTime &amp; &quot; milliseconds&quot;\n\t\tWScript.Sleep(intSensorRandomizeWaitTime)\n\t\tSensorRandomizeEcho &quot;Done sleeping, continuing ...&quot;\n\tElse \n\t\tSensorRandomizeEcho &quot;SensorRandomize Not Enabled - No Op&quot;\n\tEnd If\nEnd Function &#039;SensorRandomizeRandomSleep\n\nFunction SensorRandomizeTaniumRandomSeed\n&#039; for randomizing sensor code, the default seed is not random enough\n\tDim timerNum\n\ttimerNum = Timer()\n\tIf timerNum &lt; 1 Then\n\t\tSensorRandomizeTaniumRandomSeed = (SensorRandomizeGetTaniumComputerID / Timer() * 10 )\n\tElse\n\t\tSensorRandomizeTaniumRandomSeed = SensorRandomizeGetTaniumComputerID / Timer\n\tEnd If\nEnd Function &#039;SensorRandomizeTaniumRandomSeed\n\nFunction SensorRandomizeGetTaniumRegistryPath\n&#039;SensorRandomizeGetTaniumRegistryPath works in x64 or x32\n&#039;looks for a valid Path value\n\n\tDim objShell\n\tDim keyNativePath, keyWoWPath, strPath, strFoundTaniumRegistryPath\n\t  \n    Set objShell = CreateObject(&quot;WScript.Shell&quot;)\n    \n\tkeyNativePath = &quot;Software\\Tanium\\Tanium Client&quot;\n\tkeyWoWPath = &quot;Software\\Wow6432Node\\Tanium\\Tanium Client&quot;\n    \n    &#039; first check the Software key (valid for 32-bit machines, or 64-bit machines in 32-bit mode)\n    On Error Resume Next\n    strPath = objShell.RegRead(&quot;HKLM\\&quot;&amp;keyNativePath&amp;&quot;\\Path&quot;)\n    On Error Goto 0\n\tstrFoundTaniumRegistryPath = keyNativePath\n \n  \tIf strPath = &quot;&quot; Then\n  \t\t&#039; Could not find 32-bit mode path, checking Wow6432Node\n  \t\tOn Error Resume Next\n  \t\tstrPath = objShell.RegRead(&quot;HKLM\\&quot;&amp;keyWoWPath&amp;&quot;\\Path&quot;)\n  \t\tOn Error Goto 0\n\t\tstrFoundTaniumRegistryPath = keyWoWPath\n  \tEnd If\n  \t\n  \tIf Not strPath = &quot;&quot; Then\n  \t\tSensorRandomizeGetTaniumRegistryPath = strFoundTaniumRegistryPath\n  \tElse\n  \t\tSensorRandomizeGetTaniumRegistryPath = False\n  \t\tWScript.Echo &quot;Error: Cannot locate Tanium Registry Path&quot;\n  \tEnd If\nEnd Function &#039;SensorRandomizeGetTaniumRegistryPath\n\nFunction SensorRandomizeGetTaniumComputerID\n&#039;&#039; This function gets the Tanium Computer ID\n\tDim objShell\n\tDim intClientID,strID,strKeyPath,strValueName\n\t\n    strKeyPath = SensorRandomizeGetTaniumRegistryPath\n    strValueName = &quot;ComputerID&quot;\n    Set objShell = CreateObject(&quot;WScript.Shell&quot;)\n    On Error Resume Next\n    intClientID = objShell.RegRead(&quot;HKLM\\&quot;&amp;strKeyPath&amp;&quot;\\&quot;&amp;strValueName)\n    If Err.Number &lt;&gt; 0 Then\n    \tSensorRandomizeGetTaniumComputerID = 0\n    Else\n\t\tSensorRandomizeGetTaniumComputerID = SensorRandomizeReinterpretSignedAsUnsigned(intClientID)\n\tEnd If\n\tOn Error Goto 0\nEnd Function &#039;SensorRandomizeGetTaniumComputerID\n\nFunction SensorRandomizeReinterpretSignedAsUnsigned(ByVal x)\n\t  If x &lt; 0 Then x = x + 2^32\n\t  SensorRandomizeReinterpretSignedAsUnsigned = x\nEnd Function &#039;SensorRandomizeReinterpretSignedAsUnsigned\n\nSub SensorRandomizeEcho(str)\n\tIf bSensorRandomizeDebugOutput = true Then WScript.Echo str\nEnd Sub &#039;SensorRandomizeEcho\n&#039; -- End Random Sleep Functions --&#039;\n&#039;- End file: utils/SensorRandomization/SensorRandomizationFunctions.vbs", 
            "script_type": "VBScript"
          }, 
          {
            "_type": "query", 
            "platform": "Linux", 
            "script": "#!/bin/bash\n#||dirname||||regexp||||casesensitive||||global||\necho Windows Only\n", 
            "script_type": "UnixShell"
          }, 
          {
            "_type": "query", 
            "platform": "Mac", 
            "script": "#!/bin/bash\n#||dirname||||regexp||||casesensitive||||global||\necho Windows Only\n", 
            "script_type": "UnixShell"
          }
        ]
      }, 
      "source_id": 0, 
      "string_count": 0, 
      "value_type": "String"
    }
  ]
}

'''
