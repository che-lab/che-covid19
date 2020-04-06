

import requests
import os
import subprocess

# Switch to directory you want the downloaded folder to reside
os.chdir('/Users/geoffreyhughes/Projects/Work/COVID-19/che-covid19/data')

# Grab new files from github
p = subprocess.Popen("svn checkout https://github.com/CSSEGISandData/COVID-19/trunk/csse_covid_19_data/csse_covid_19_daily_reports",
 stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()

# Print revisions done
print "Revision is", output
