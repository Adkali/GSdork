# GSdork
A Google dorking program for searching inside google with the dorking method, retrieves links back to you. Google is the encyclopedia of the internet as we already know, and many of us using it on our day, so why now using the dorking way which is more powerful. Before i made this program, i wanted to practice on my bs skils, than from here i decided to make a little dorking-search for google dorking. Using the special operators, you can make searching easy with better results.

Gsdork is designed to automate the process of performing Google dorking searches By providing search terms and special operators. the program generates complex search queries that are sent to Google, and The results are then analyzed and filtered, presenting the user with relevant links and information.<br>

<img src="https://github.com/Adkali/GSdork/assets/90532971/366ad8c1-45d4-4b0c-a125-a6c15e6579a5">
<img src=https://github.com/Adkali/GSdork/assets/90532971/bb4a7129-d6bd-4435-8484-85fc5b2a2f91>

# Google Operators Examples:
<pre>
#1. site:exmaple.com filetype:pdf <b>[ Filetype looks for the type of file you want inside the site you spesificed ]</b>
#2. inurl:[cyber] inbody:threat <b>[ search for URLs that contain a specified keyword ]</b>
#3. passwords filetype:docx site:example.com <b>[ look for password docx file with all listed url  for the specified site )</b>
#4. allintext:hacking <b>[ Search for spesific text inside webpage ]</b>
#5. how to * website <b>[ '*' used to search pages contains anything before your word ]</b>
#6. allintext:username filetype:log <b>[ This parameter searches for user-specified text in a webpage ]</b>
#7. intitle:index of django/admin site:.* <b>[ Pages containing login portals ]</b>
#8. intext:"#mysql dump" filetype:sql <b>[ text containing spesific strings ]</b>
</pre>
<b>Note: Make a search, find more Google-Dork lists you can use.</b>
# Usage:
<pre>
1. clone with git clone [ repository name ] 
2. install requirements.txt
3. python3 [ FileName.py ] 
4. Happy dorking.
</pre>

# Caution 
Please be advised that this code has only been tested on a Kali machine and no issues were encountered during the testing phase. Given the appropriate timeline, I intend to incorporate additional features to enhance its searching capabilities. Kindly note that this code is intended for educational purposes only and should not be used for any other purpose.

### Updates
- code improvement using threads for faster results.
- Better output handle

![צילום מסך 2022-07-16 221720](https://user-images.githubusercontent.com/90532971/179369098-dfded351-fda7-432c-8753-71baf5513286.png)
