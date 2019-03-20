# cac_keepalive

### Purpose

One fine day, I noticed my VMs on CAC just never came back. They routinely go down, sometimes for a day and normally come back up. After checking with them, they confirmed that they nuked the VMs because nobody logged on in over 6 months to their portal. While being ridiculous, I knew that I was not going to remember to log in at least every few months. So I wrote this simple script to log in daily or at an interval of your choosing via contab. I suggest a more gentle interval of every 2 weeks.

### Installation
- Clone this repo
- Install required packages:  
`pip3 install requests`
- Update `settings.json` with your username and password, and the logfile output
- Test script by running it manually:  
`python3 cac_keepalive.py`
- Check the logfile, which by default is saved in the current directory from where the python script is launched from. The default is: `./cloudatcost-keepalive.log`
- You may wish to disable email notification in the CAC Portal, or you will get email each time this script runs successfully

### TODO:
- Add setup.py
- Add a requirements.txt file
- Add command line argument parser to display logging data to STDOUT
- Understand and fix why the session cause an email from CAC, but does not occur via a browser... Cookies not loading correctly?
- PEX file?
