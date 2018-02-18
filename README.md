intelli-net

Not every company can afford a dedicated security engineer. We can use Watson to help fill in the gap!

What it does:
Automates and demystifies network security auditing and patching. Watson prompts the user to enter the IP address of the system, or IP range of the network to be tested. We use a shell script to run nmap scans, and then Watson queries CVE databases to make recommendations for patches or remediation. In only the most severe cases, Watson will recommend that the user consult with a security professional. This brings value to small and medium business customers who can't afford a dedicated SOC, and acts as a valuable introduction to network scanning and CVE research for the uninitiated. Over time, as Watson's available dataset grows, we should be able to execute predictive modeling for likely compromises, and eradicate those vectors before they become a serious issue.

How we built it:
Using Python, BASH, nmap, and a combination of IBM Cloud Services
