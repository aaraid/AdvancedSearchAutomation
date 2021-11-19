import sys
from Functions import *


class CN_01_AdvSearch:
    BrowserSetup('https://github.com/')
    SearchRepository('react')
    SearchRefinement('JavaScript', '>45', '>50', 'bsl-1.0')
    CheckResult('1 repository result', 'mvoloskov/decider')
    PrintReadMe(300)
    TearDown()