from tkinter import *
from tkinter import messagebox
import sys

#
#This is the section with the HTML strings
#
gradSols_STR = """
  <!DOCTYPE HTML PUBLIC"-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Email Signature</title>
<meta content="text/html; charset=utf-8"http-equiv="Content-Type">
</head>
<body>

<table style="width: 490px; font-size: 9pt; font-family: Arial,sans-serif; line-height:normal;" cellpadding="0" cellspacing="0">
<tbody>
 <tr>	
  <td style="width:76px; vertical-align:top;" valign="top">
   <a href="https://www.iwantmydiploma.com" target="_blank"><img border="0" alt="Logo" height="76" width="76" style="width:76px; height:76px; border:0;" src="{4}"></a>
   
  </td>
  

  <td style="width:44px; ; text-align:center; vertical-align:top;" valign="top">
   <img border="0" alt="Logo" width="13" style="width:13px; height:86px; border:0;" src="https://bit.ly/3Cf6S3H">
  </td>
  <td style="width:490px; vertical-align:top;" valign="top">
   <table cellpadding="0" cellspacing="0">
   <tbody>
    <tr>
     <td style="font-size:14pt; font-family: Arial, sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{0}</span></td>
    </tr>
    <tr>
     <td style="font-size:12pt; font-family: Arial,sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{1}</span></td>
    </tr>
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"></a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;<span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">T: </span>(480) 689-5999 EXT: {5}</span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span><span style="font-family: Arial, sans-serif; color:#3c3c3b"><span style="font-weight:bold;">M: </span>{2}</span>
     </td>
    </tr>				
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">E: </span>{3}</span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span>
     <span><a href="http://iwantmydiploma.com" target="_blank"><span style="font-family: Arial, sans-serif; color:#1793d2">iwantmydiploma.com</span></a></span>
     </td>
    </tr>				
    <tr>
     
<td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span><a href="https://bit.ly/3pn4xjA" target="_blank"><img alt="location icon" border="0" width="10" height="10" style="border:0; height:10px; width:10px" src="https://bit.ly/3G4ER0W"></a>&nbsp;</a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;">1440 S Clearview Ave </span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span><span style="font-family: Arial, sans-serif; color:#3c3c3b">Mesa, AZ 85209</span>
     </td>
    </tr>				
    <tr>
     <td style="padding-top:5px; vertical-align: bottom;"><span style="display:inline-block; height:30px;"><span><a href="https://www.facebook.com/gradsolutionsllc/" target="_blank"><img alt="Facebook icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3DUq7Qe"></a>&nbsp;

</span><span><a href="https://www.instagram.com/iwantmydiploma/" target="_blank"><img alt="Instagram icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3nbWSSr"></a>&nbsp;

</span><span><a href="https://www.linkedin.com/school/grad-solutions/" target="_blank"><img alt="LinkedIn icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3vvliK9"></a>&nbsp;

</span><span><a href="https://twitter.com/iwantmydiploma" target="_blank"><img alt="Twitter icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/2ZewqPR"></a>&nbsp;

</span><span><a href="https://www.youtube.com/channel/UCTsetZr0xHhffaGkwGsc7vQ" target="_blank"><img alt="Youtube icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3G7KawE"></a>&nbsp;</a></span></span>
     </td>
    </tr>
   </tbody>
   </table>
  </td>
 </tr>
 <tr>
  <td style="width:490px; padding-top:16px;" colspan="3" width="490"><span style="display:inline-block; height:50px;"><img src="spacer.png" height="1px" width="15px"></span><span><a href="https://www.smartschoolsusa.org" target="_blank"><img alt="SmartSchoolsUSA Icon" border="0" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3pik18n"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

</span><span><a href="https://www.lumosarts.com" target="_blank"><img alt="LumosArts Icon" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3jmkLFz"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

<span><a href="https://www.welcomehomelearning.com" target="_blank"><img alt="Welcome Home Learning Logo" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3aV46Et"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

<span><a href="https://www.studentswin.org" target="_blank"><img alt="StudentsFirst Icon" border="0" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/2XsBJua"></a></span></span>
</td>
 </tr>	
</tbody>
</table>
 
</body>
</html>


"""

gradSols_STR_noPhone = """
  <!DOCTYPE HTML PUBLIC"-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Email Signature</title>
<meta content="text/html; charset=utf-8"http-equiv="Content-Type">
</head>
<body>

<table style="width: 490px; font-size: 9pt; font-family: Arial,sans-serif; line-height:normal;" cellpadding="0" cellspacing="0">
<tbody>
 <tr>	
  <td style="width:76px; vertical-align:top;" valign="top">
   <a href="https://www.iwantmydiploma.com" target="_blank"><img border="0" alt="Logo" height="76" width="76" style="width:76px; height:76px; border:0;" src="{4}"></a>
   
  </td>
  

  <td style="width:44px; ; text-align:center; vertical-align:top;" valign="top">
   <img border="0" alt="Logo" width="13" style="width:13px; height:86px; border:0;" src="https://bit.ly/3Cf6S3H">
  </td>
  <td style="width:490px; vertical-align:top;" valign="top">
   <table cellpadding="0" cellspacing="0">
   <tbody>
    <tr>
     <td style="font-size:14pt; font-family: Arial, sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{0}</span></td>
    </tr>
    <tr>
     <td style="font-size:12pt; font-family: Arial,sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{1}</span></td>
    </tr>
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"></a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;<span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">T: </span>(480) 689-5999 EXT: {2}</span>
     </td>
    </tr>				
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">E: </span>{3}</span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span>
     <span><a href="http://iwantmydiploma.com" target="_blank"><span style="font-family: Arial, sans-serif; color:#1793d2">iwantmydiploma.com</span></a></span>
     </td>
    </tr>				
    <tr>
     
<td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span><a href="https://bit.ly/3pn4xjA" target="_blank"><img alt="location icon" border="0" width="10" height="10" style="border:0; height:10px; width:10px" src="https://bit.ly/3G4ER0W"></a>&nbsp;</a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;">1440 S Clearview Ave </span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span><span style="font-family: Arial, sans-serif; color:#3c3c3b">Mesa, AZ 85209</span>
     </td>
    </tr>				
    <tr>
     <td style="padding-top:5px; vertical-align: bottom;"><span style="display:inline-block; height:30px;"><span><a href="https://www.facebook.com/gradsolutionsllc/" target="_blank"><img alt="Facebook icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3DUq7Qe"></a>&nbsp;

</span><span><a href="https://www.instagram.com/iwantmydiploma/" target="_blank"><img alt="Instagram icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3nbWSSr"></a>&nbsp;

</span><span><a href="https://www.linkedin.com/school/grad-solutions/" target="_blank"><img alt="LinkedIn icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3vvliK9"></a>&nbsp;

</span><span><a href="https://twitter.com/iwantmydiploma" target="_blank"><img alt="Twitter icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/2ZewqPR"></a>&nbsp;

</span><span><a href="https://www.youtube.com/channel/UCTsetZr0xHhffaGkwGsc7vQ" target="_blank"><img alt="Youtube icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3G7KawE"></a>&nbsp;</a></span></span>
     </td>
    </tr>
   </tbody>
   </table>
  </td>
 </tr>
 <tr>
  <td style="width:490px; padding-top:16px;" colspan="3" width="490"><span style="display:inline-block; height:50px;"><img src="spacer.png" height="1px" width="15px"></span><span><a href="https://www.smartschoolsusa.org" target="_blank"><img alt="SmartSchoolsUSA Icon" border="0" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3pik18n"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

</span><span><a href="https://www.lumosarts.com" target="_blank"><img alt="LumosArts Icon" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3jmkLFz"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

<span><a href="https://www.welcomehomelearning.com" target="_blank"><img alt="Welcome Home Learning Logo" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3aV46Et"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

<span><a href="https://www.studentswin.org" target="_blank"><img alt="StudentsFirst Icon" border="0" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/2XsBJua"></a></span></span>
</td>
 </tr>	
</tbody>
</table>
 
</body>
</html>


"""

gradSols_STR_noExt = """
  <!DOCTYPE HTML PUBLIC"-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Email Signature</title>
<meta content="text/html; charset=utf-8"http-equiv="Content-Type">
</head>
<body>

<table style="width: 490px; font-size: 9pt; font-family: Arial,sans-serif; line-height:normal;" cellpadding="0" cellspacing="0">
<tbody>
 <tr>	
  <td style="width:76px; vertical-align:top;" valign="top">
   <a href="https://www.iwantmydiploma.com" target="_blank"><img border="0" alt="Logo" height="76" width="76" style="width:76px; height:76px; border:0;" src="{4}"></a>
   
  </td>
  

  <td style="width:44px; ; text-align:center; vertical-align:top;" valign="top">
   <img border="0" alt="Logo" width="13" style="width:13px; height:86px; border:0;" src="https://bit.ly/3Cf6S3H">
  </td>
  <td style="width:490px; vertical-align:top;" valign="top">
   <table cellpadding="0" cellspacing="0">
   <tbody>
    <tr>
     <td style="font-size:14pt; font-family: Arial, sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{0}</span></td>
    </tr>
    <tr>
     <td style="font-size:12pt; font-family: Arial,sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{1}</span></td>
    </tr>
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"></a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;<span style="font-family: Arial, sans-serif; color:#3c3c3b"><span style="font-weight:bold;">M: </span>{2}</span>
     </td>
    </tr>				
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">E: </span>{3}</span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span>
     <span><a href="http://iwantmydiploma.com" target="_blank"><span style="font-family: Arial, sans-serif; color:#1793d2">iwantmydiploma.com</span></a></span>
     </td>
    </tr>				
    <tr>
     
<td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span><a href="https://bit.ly/3pn4xjA" target="_blank"><img alt="location icon" border="0" width="10" height="10" style="border:0; height:10px; width:10px" src="https://bit.ly/3G4ER0W"></a>&nbsp;</a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;">1440 S Clearview Ave </span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span><span style="font-family: Arial, sans-serif; color:#3c3c3b">Mesa, AZ 85209</span>
     </td>
    </tr>				
    <tr>
     <td style="padding-top:5px; vertical-align: bottom;"><span style="display:inline-block; height:30px;"><span><a href="https://www.facebook.com/gradsolutionsllc/" target="_blank"><img alt="Facebook icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3DUq7Qe"></a>&nbsp;

</span><span><a href="https://www.instagram.com/iwantmydiploma/" target="_blank"><img alt="Instagram icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3nbWSSr"></a>&nbsp;

</span><span><a href="https://www.linkedin.com/school/grad-solutions/" target="_blank"><img alt="LinkedIn icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3vvliK9"></a>&nbsp;

</span><span><a href="https://twitter.com/iwantmydiploma" target="_blank"><img alt="Twitter icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/2ZewqPR"></a>&nbsp;

</span><span><a href="https://www.youtube.com/channel/UCTsetZr0xHhffaGkwGsc7vQ" target="_blank"><img alt="Youtube icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3G7KawE"></a>&nbsp;</a></span></span>
     </td>
    </tr>
   </tbody>
   </table>
  </td>
 </tr>
 <tr>
  <td style="width:490px; padding-top:16px;" colspan="3" width="490"><span style="display:inline-block; height:50px;"><img src="spacer.png" height="1px" width="15px"></span><span><a href="https://www.smartschoolsusa.org" target="_blank"><img alt="SmartSchoolsUSA Icon" border="0" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3pik18n"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

</span><span><a href="https://www.lumosarts.com" target="_blank"><img alt="LumosArts Icon" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3jmkLFz"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

<span><a href="https://www.welcomehomelearning.com" target="_blank"><img alt="Welcome Home Learning Logo" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3aV46Et"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

<span><a href="https://www.studentswin.org" target="_blank"><img alt="StudentsFirst Icon" border="0" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/2XsBJua"></a></span></span>
</td>
 </tr>	
</tbody>
</table>
 
</body>
</html>


"""

smartSchools_STR = """
 <!DOCTYPE HTML PUBLIC"-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Email Signature</title>
<meta content="text/html; charset=utf-8"http-equiv="Content-Type">
</head>
<body>

<table style="width: 490px; font-size: 9pt; font-family: Arial,sans-serif; line-height:normal;" cellpadding="0" cellspacing="0">
<tbody>
 <tr>	
  <td style="width:76px; vertical-align:top;" valign="top">
   <a href="https://www.smartschoolsusa.org" target="_blank"><img border="0" alt="Logo" height="76" width="76" style="width:76px; height:76px; border:0;" src="{4}"></a>
   
  </td>
  

  <td style="width:44px; ; text-align:center; vertical-align:top;" valign="top">
   <img border="0" alt="Logo" width="13" style="width:13px; height:86px; border:0;" src="https://bit.ly/3Cf6S3H">
  </td>
  <td style="width:490px; vertical-align:top;" valign="top">
   <table cellpadding="0" cellspacing="0">
   <tbody>
    <tr>
     <td style="font-size:14pt; font-family: Arial, sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{0}</span></td>
    </tr>
    <tr>
     <td style="font-size:12pt; font-family: Arial,sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{1}</span></td>
    </tr>
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"></a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;<span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">T: </span>(480) 689-5999 EXT: {5}</span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span><span style="font-family: Arial, sans-serif; color:#3c3c3b"><span style="font-weight:bold;">M: </span>{2}</span>
     </td>
    </tr>				
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">E: </span>{3}</span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span>
     <span><a href="http://smartschoolsusa.org" target="_blank"><span style="font-family: Arial, sans-serif; color:#1793d2">smartschoolsusa.org</span></a></span>
     </td>
    </tr>				
    <tr>
     
<td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span><a href="https://bit.ly/3pn4xjA" target="_blank"><img alt="location icon" border="0" width="10" height="10" style="border:0; height:10px; width:10px" src="https://bit.ly/3G4ER0W"></a>&nbsp;</a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;">1440 S Clearview Ave </span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span><span style="font-family: Arial, sans-serif; color:#3c3c3b">Mesa, AZ 85209</span>
     </td>
    </tr>				
    <tr>
     <td style="padding-top:5px; vertical-align: bottom;"><span style="display:inline-block; height:30px;"><span><a href="https://www.facebook.com/smartschoolsusa/" target="_blank"><img alt="Facebook icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3DUq7Qe"></a>&nbsp;

</span><span><a href="https://www.instagram.com/smartschoolsusa/?hl=en" target="_blank"><img alt="Instagram icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3nbWSSr"></a>&nbsp;

</span><span><a href="https://twitter.com/smartschoolsusa?lang=en" target="_blank"><img alt="Twitter icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/2ZewqPR"></a>&nbsp;


     </td>
    </tr>
   </tbody>
   </table>
  </td>
 </tr>
 <tr>
  <td style="width:490px; padding-top:16px;" colspan="3" width="490"><span style="display:inline-block; height:50px;"><img src="spacer.png" height="1px" width="15px"></span><span><a href="https://www.iwantmydiploma.com" target="_blank"><img alt="GSIcon" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/2Zdy1p5"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

</span><span><a href="https://www.lumosarts.com" target="_blank"><img alt="LumosArts Icon" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3jmkLFz"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

<span><a href="https://www.welcomehomelearning.com" target="_blank"><img alt="Welcome Home Learning Logo" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3aV46Et"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

<span><a href="https://www.studentswin.org" target="_blank"><img alt="StudentsFirst Icon" border="0" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/2XsBJua"></a></span></span>
</td>
 </tr>	
</tbody>
</table>
 
</body>
</html>

"""

smartSchools_STR_noPhone = """
 <!DOCTYPE HTML PUBLIC"-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Email Signature</title>
<meta content="text/html; charset=utf-8"http-equiv="Content-Type">
</head>
<body>

<table style="width: 490px; font-size: 9pt; font-family: Arial,sans-serif; line-height:normal;" cellpadding="0" cellspacing="0">
<tbody>
 <tr>	
  <td style="width:76px; vertical-align:top;" valign="top">
   <a href="https://www.smartschoolsusa.org" target="_blank"><img border="0" alt="Logo" height="76" width="76" style="width:76px; height:76px; border:0;" src="{4}"></a>
   
  </td>
  

  <td style="width:44px; ; text-align:center; vertical-align:top;" valign="top">
   <img border="0" alt="Logo" width="13" style="width:13px; height:86px; border:0;" src="https://bit.ly/3Cf6S3H">
  </td>
  <td style="width:490px; vertical-align:top;" valign="top">
   <table cellpadding="0" cellspacing="0">
   <tbody>
    <tr>
     <td style="font-size:14pt; font-family: Arial, sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{0}</span></td>
    </tr>
    <tr>
     <td style="font-size:12pt; font-family: Arial,sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{1}</span></td>
    </tr>
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"></a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;<span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">T: </span>(480) 689-5999 EXT: {2}</span>
     </td>
    </tr>				
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">E: </span>{3}</span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span>
     <span><a href="http://smartschoolsusa.org" target="_blank"><span style="font-family: Arial, sans-serif; color:#1793d2">smartschoolsusa.org</span></a></span>
     </td>
    </tr>				
    <tr>
     
<td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span><a href="https://bit.ly/3pn4xjA" target="_blank"><img alt="location icon" border="0" width="10" height="10" style="border:0; height:10px; width:10px" src="https://bit.ly/3G4ER0W"></a>&nbsp;</a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;">1440 S Clearview Ave </span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span><span style="font-family: Arial, sans-serif; color:#3c3c3b">Mesa, AZ 85209</span>
     </td>
    </tr>				
    <tr>
     <td style="padding-top:5px; vertical-align: bottom;"><span style="display:inline-block; height:30px;"><span><a href="https://www.facebook.com/smartschoolsusa/" target="_blank"><img alt="Facebook icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3DUq7Qe"></a>&nbsp;

</span><span><a href="https://www.instagram.com/smartschoolsusa/?hl=en" target="_blank"><img alt="Instagram icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3nbWSSr"></a>&nbsp;

</span><span><a href="https://twitter.com/smartschoolsusa?lang=en" target="_blank"><img alt="Twitter icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/2ZewqPR"></a>&nbsp;


     </td>
    </tr>
   </tbody>
   </table>
  </td>
 </tr>
 <tr>
  <td style="width:490px; padding-top:16px;" colspan="3" width="490"><span style="display:inline-block; height:50px;"><img src="spacer.png" height="1px" width="15px"></span><span><a href="https://www.iwantmydiploma.com" target="_blank"><img alt="GSIcon" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/2Zdy1p5"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

</span><span><a href="https://www.lumosarts.com" target="_blank"><img alt="LumosArts Icon" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3jmkLFz"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

<span><a href="https://www.welcomehomelearning.com" target="_blank"><img alt="Welcome Home Learning Logo" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3aV46Et"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

<span><a href="https://www.studentswin.org" target="_blank"><img alt="StudentsFirst Icon" border="0" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/2XsBJua"></a></span></span>
</td>
 </tr>	
</tbody>
</table>
 
</body>
</html>

"""

smartSchools_STR_noExt = """
 <!DOCTYPE HTML PUBLIC"-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Email Signature</title>
<meta content="text/html; charset=utf-8"http-equiv="Content-Type">
</head>
<body>

<table style="width: 490px; font-size: 9pt; font-family: Arial,sans-serif; line-height:normal;" cellpadding="0" cellspacing="0">
<tbody>
 <tr>	
  <td style="width:76px; vertical-align:top;" valign="top">
   <a href="https://www.smartschoolsusa.org" target="_blank"><img border="0" alt="Logo" height="76" width="76" style="width:76px; height:76px; border:0;" src="{4}"></a>
   
  </td>
  

  <td style="width:44px; ; text-align:center; vertical-align:top;" valign="top">
   <img border="0" alt="Logo" width="13" style="width:13px; height:86px; border:0;" src="https://bit.ly/3Cf6S3H">
  </td>
  <td style="width:490px; vertical-align:top;" valign="top">
   <table cellpadding="0" cellspacing="0">
   <tbody>
    <tr>
     <td style="font-size:14pt; font-family: Arial, sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{0}</span></td>
    </tr>
    <tr>
     <td style="font-size:12pt; font-family: Arial,sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{1}</span></td>
    </tr>
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"></a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;<span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">T: </span>(480) 689-5999</span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span><span style="font-family: Arial, sans-serif; color:#3c3c3b"><span style="font-weight:bold;">M: </span>{2}</span>
     </td>
    </tr>				
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">E: </span>{3}</span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span>
     <span><a href="http://smartschoolsusa.org" target="_blank"><span style="font-family: Arial, sans-serif; color:#1793d2">smartschoolsusa.org</span></a></span>
     </td>
    </tr>				
    <tr>
     
<td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span><a href="https://bit.ly/3pn4xjA" target="_blank"><img alt="location icon" border="0" width="10" height="10" style="border:0; height:10px; width:10px" src="https://bit.ly/3G4ER0W"></a>&nbsp;</a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;">1440 S Clearview Ave </span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span><span style="font-family: Arial, sans-serif; color:#3c3c3b">Mesa, AZ 85209</span>
     </td>
    </tr>				
    <tr>
     <td style="padding-top:5px; vertical-align: bottom;"><span style="display:inline-block; height:30px;"><span><a href="https://www.facebook.com/smartschoolsusa/" target="_blank"><img alt="Facebook icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3DUq7Qe"></a>&nbsp;

</span><span><a href="https://www.instagram.com/smartschoolsusa/?hl=en" target="_blank"><img alt="Instagram icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3nbWSSr"></a>&nbsp;

</span><span><a href="https://twitter.com/smartschoolsusa?lang=en" target="_blank"><img alt="Twitter icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/2ZewqPR"></a>&nbsp;


     </td>
    </tr>
   </tbody>
   </table>
  </td>
 </tr>
 <tr>
  <td style="width:490px; padding-top:16px;" colspan="3" width="490"><span style="display:inline-block; height:50px;"><img src="spacer.png" height="1px" width="15px"></span><span><a href="https://www.iwantmydiploma.com" target="_blank"><img alt="GSIcon" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/2Zdy1p5"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

</span><span><a href="https://www.lumosarts.com" target="_blank"><img alt="LumosArts Icon" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3jmkLFz"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

<span><a href="https://www.welcomehomelearning.com" target="_blank"><img alt="Welcome Home Learning Logo" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3aV46Et"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

<span><a href="https://www.studentswin.org" target="_blank"><img alt="StudentsFirst Icon" border="0" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/2XsBJua"></a></span></span>
</td>
 </tr>	
</tbody>
</table>
 
</body>
</html>

"""

lumos_STR = """
 <!DOCTYPE HTML PUBLIC"-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Email Signature</title>
<meta content="text/html; charset=utf-8"http-equiv="Content-Type">
</head>
<body>

<table style="width: 490px; font-size: 9pt; font-family: Arial,sans-serif; line-height:normal;" cellpadding="0" cellspacing="0">
<tbody>
 <tr>	
  <td style="width:76px; vertical-align:top;" valign="top">
   <a href="https://www.lumosarts.com" target="_blank"><img border="0" alt="Logo" height="76" width="76" style="width:76px; height:76px; border:0;" src="{3}"></a>
   
  </td>
  

  <td style="width:44px; ; text-align:center; vertical-align:top;" valign="top">
   <img border="0" alt="Logo" width="13" style="width:13px; height:86px; border:0;" src="https://bit.ly/3Cf6S3H">
  </td>
  <td style="width:490px; vertical-align:top;" valign="top">
   <table cellpadding="0" cellspacing="0">
   <tbody>
    <tr>
     <td style="font-size:14pt; font-family: Arial, sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{0}</span></td>
    </tr>
    <tr>
     <td style="font-size:12pt; font-family: Arial,sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{1}</span></td>
    </tr>
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"></a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;<span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">T: </span>(480) 272-1129</span>
     </td>
    </tr>				
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">E: </span>{2}</span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span>
     <span><a href="http://lumosarts.com" target="_blank"><span style="font-family: Arial, sans-serif; color:#1793d2">lumosarts.com</span></a></span>
     </td>
    </tr>				
    <tr>
     
<td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span><a href="https://bit.ly/3ndF1uf" target="_blank"><img alt="location icon" border="0" width="10" height="10" style="border:0; height:10px; width:10px" src="https://bit.ly/3G4ER0W"></a>&nbsp;</a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;">2055 S Power Rd</span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span><span style="font-family: Arial, sans-serif; color:#3c3c3b">Mesa, AZ 85209</span>
     </td>
    </tr>				
    <tr>
     <td style="padding-top:5px; vertical-align: bottom;"><span style="display:inline-block; height:30px;"><span><a href="https://www.facebook.com/LumosArtsAcademy/" target="_blank"><img alt="Facebook icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3DUq7Qe"></a>&nbsp;

</span><span><a href="https://www.instagram.com/lumosartsacademy/?hl=en" target="_blank"><img alt="Instagram icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3nbWSSr"></a>&nbsp;


</span><span><a href="https://www.youtube.com/channel/UCpqJDoQox2YQ7L2nLGgWULg" target="_blank"><img alt="Youtube icon" border="0" width="30" height="30" style="border:0; height:30px; width:30px" src="https://bit.ly/3G7KawE"></a>&nbsp;</a></span></span>
     </td>
    </tr>
   </tbody>
   </table>
  </td>
 </tr>
 <tr>
  <td style="width:490px; padding-top:16px;" colspan="3" width="490"><span style="display:inline-block; height:50px;"><img src="spacer.png" height="1px" width="15px"></span><span><a href="https://www.iwantmydiploma.com" target="_blank"><img alt="GSIcon" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/2Zdy1p5"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

</span><span><a href="https://www.smartschoolsusa.org" target="_blank"><img alt="SmartSchoolsUSA Icon" border="0" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3pik18n"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">


<span><a href="https://www.welcomehomelearning.com" target="_blank"><img alt="Welcome Home Learning Logo" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3aV46Et"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

<span><a href="https://www.studentswin.org" target="_blank"><img alt="StudentsFirst Icon" border="0" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/2XsBJua"></a></span></span>
</td>
 </tr>	
</tbody>
</table>
 
</body>
</html>

"""

archway_STR = """
 <!DOCTYPE HTML PUBLIC"-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Email Signature</title>
<meta content="text/html; charset=utf-8"http-equiv="Content-Type">
</head>
<body>

<table style="width: 490px; font-size: 9pt; font-family: Arial,sans-serif; line-height:normal;" cellpadding="0" cellspacing="0">
<tbody>
 <tr>	
  <td style="width:76px; vertical-align:top;" valign="top">
   <a href="https://archwayonline.com" target="_blank"><img border="0" alt="Logo" height="76" width="76" style="width:76px; height:76px; border:0;" src="{4}"></a>
   
  </td>
  

  <td style="width:44px; ; text-align:center; vertical-align:top;" valign="top">
   <img border="0" alt="Logo" width="13" style="width:13px; height:86px; border:0;" src="https://bit.ly/3Cf6S3H">
  </td>
  <td style="width:490px; vertical-align:top;" valign="top">
   <table cellpadding="0" cellspacing="0">
   <tbody>
    <tr>
     <td style="font-size:14pt; font-family: Arial, sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{0}</span></td>
    </tr>
    <tr>
     <td style="font-size:12pt; font-family: Arial,sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{1}</span></td>
    </tr>
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"></a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;<span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-family: Arial, sans-serif; color:#3c3c3b"><span style="font-weight:bold;">M: </span>{2}</span>
     </td>
    </tr>				
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">E: </span>{3}</span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span>
     <span><a href="http://archwayonline.com" target="_blank"><span style="font-family: Arial, sans-serif; color:#1793d2">archwayonline.com</span></a></span>
     </td>
    </tr>				
    <tr>
     
<td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span><a href="https://bit.ly/3pn4xjA" target="_blank"><img alt="location icon" border="0" width="10" height="10" style="border:0; height:10px; width:10px" src="https://bit.ly/3G4ER0W"></a>&nbsp;</a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;">1440 S Clearview Ave </span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span><span style="font-family: Arial, sans-serif; color:#3c3c3b">Mesa, AZ 85209</span>
     </td>
    </tr>				
    <tr>


     </td>
    </tr>
   </tbody>
   </table>
  </td>
 </tr>
 <tr>
  <td style="width:490px; padding-top:16px;" colspan="3" width="490"><span style="display:inline-block; height:50px;"><img src="spacer.png" height="1px" width="15px">
</span><span><a href="https://www.iwantmydiploma.com" target="_blank"><img alt="GSIcon" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/2Zdy1p5"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

</span><span><a href="https://www.smartschoolsusa.org" target="_blank"><img alt="SmartSchoolsUSA Icon" border="0" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3pik18n"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

</span><span><a href="https://www.lumosarts.com" target="_blank"><img alt="LumosArts Icon" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3jmkLFz"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

<span><a href="https://www.welcomehomelearning.com" target="_blank"><img alt="Welcome Home Learning Logo" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3aV46Et"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

<span><a href="https://www.studentswin.org" target="_blank"><img alt="StudentsFirst Icon" border="0" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/2XsBJua"></a></span></span>
</td>
 </tr>	
</tbody>
</table>
 
</body>
</html>

"""

welcomeHomeLearning_STR = """
 <!DOCTYPE HTML PUBLIC"-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Email Signature</title>
<meta content="text/html; charset=utf-8"http-equiv="Content-Type">
</head>
<body>

<table style="width: 490px; font-size: 9pt; font-family: Arial,sans-serif; line-height:normal;" cellpadding="0" cellspacing="0">
<tbody>
 <tr>	
  <td style="width:76px; vertical-align:top;" valign="top">
   <a href="https://welcomehomelearning.com" target="_blank"><img border="0" alt="Logo" height="76" width="76" style="width:76px; height:76px; border:0;" src="{4}"></a>
   
  </td>
  

  <td style="width:44px; ; text-align:center; vertical-align:top;" valign="top">
   <img border="0" alt="Logo" width="13" style="width:13px; height:86px; border:0;" src="https://bit.ly/3Cf6S3H">
  </td>
  <td style="width:490px; vertical-align:top;" valign="top">
   <table cellpadding="0" cellspacing="0">
   <tbody>
    <tr>
     <td style="font-size:14pt; font-family: Arial, sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{0}</span></td>
    </tr>
    <tr>
     <td style="font-size:12pt; font-family: Arial,sans-serif; font-weight: bold; color: #3d3c3f; padding-bottom:5px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;">{1}</span></td>
    </tr>
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"></a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;<span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">T: </span>{2}</span><span style="font-family: Arial, sans-serif; color:#3c3c3b">  
     </td>
    </tr>				
    <tr>
     <td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span style="font-family: Arial, sans-serif; color:#3c3c3b;"><span style="font-weight:bold;">E: </span>{3}</span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> 
     </td>
    </tr>				
    <tr>
     
<td style="font-size:10pt; font-family: Arial, sans-serif; color: #9b9b9b; padding-bottom:1px;"><span><a href="https://bit.ly/3pn4xjA" target="_blank"><img alt="location icon" border="0" width="10" height="10" style="border:0; height:10px; width:10px" src="https://bit.ly/3G4ER0W"></a>&nbsp;</a></span></span><span style="font-family: Arial, sans-serif; color:#3c3c3b;">1440 S Clearview Ave </span><span style="font-family: Arial, sans-serif; color:#3c3c3b"> | </span><span style="font-family: Arial, sans-serif; color:#3c3c3b">Mesa, AZ 85209</span>
     </td>
    </tr>				
    <tr>


     </td>
    </tr>
   </tbody>
   </table>
  </td>
 </tr>
 <tr>
  <td style="width:490px; padding-top:16px;" colspan="3" width="490"><span style="display:inline-block; height:50px;"><img src="spacer.png" height="1px" width="15px">
</span><span><a href="https://www.iwantmydiploma.com" target="_blank"><img alt="GSIcon" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/2Zdy1p5"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

</span><span><a href="https://www.smartschoolsusa.org" target="_blank"><img alt="SmartSchoolsUSA Icon" border="0" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3pik18n"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">

</span><span><a href="https://www.lumosarts.com" target="_blank"><img alt="LumosArts Icon" border="10" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/3jmkLFz"></a>&nbsp;<img src="spacer.png" height="1px" width="15px">


<span><a href="https://www.studentswin.org" target="_blank"><img alt="StudentsFirst Icon" border="0" width="50" height="50" style="border:0; height:50px; width:50px" src="https://bit.ly/2XsBJua"></a></span></span>
</td>
 </tr>	
</tbody>
</table>
 
</body>
</html>

"""
#
#Window creation and initialize
#
window = Tk()
window.title("Signature Creator")
window.geometry("750x250")

options = [
    "phone",
    "extension",
    "both"
    ]
    
entityOptions = [
    "GS",
    "SS",
    "L",
    "WHL",
    "AW"
    ]

entityClicked = StringVar()
entityClicked.set("GS")

clicked = StringVar()
clicked.set("phone")

userEntity = OptionMenu(window, entityClicked, *entityOptions)
userEntity.config(font=("ariel", 14))
userPic = Entry(window, font=("ariel", 14))
userName = Entry(window, font=("ariel", 14))
userTitle = Entry(window, font=("ariel", 14))
userPhone = Entry(window, font=("ariel", 14))
userExtension = Entry(window, font=("ariel", 14))
userEmail = Entry(window, font=("ariel", 14))
userQuestion = OptionMenu(window, clicked, *options)
userQuestion.config(font=("ariel", 14))

menuSizeChange = window.nametowidget(userEntity.menuname)
menuSizeChange.config(font=("ariel", 14))

menuSizeChangeTwo = window.nametowidget(userQuestion.menuname)
menuSizeChangeTwo.config(font=("ariel", 14))

finishedEntity = "chicken"
finishedPic = "chicken"
finishedName = "chicken"
finishedTitle = "chicken"
finishedPhone = "chicken"
finishedExtension = "chicken"
finishedEmail = "chicken"
finishedQuestion = "chicken"

entityLabel = Label(window, text="Choose your entity from the dropdown:", font=("ariel", 14))
picLabel = Label(window, text="Enter URL of your picture", font=("ariel", 14))
nameLabel = Label(window, text="Enter Name", font=("ariel", 14))
titleLabel = Label(window, text="Enter Title", font=("ariel", 14))
phoneLabel = Label(window, text="Enter Phone Number", font=("ariel", 14))
extensionLabel = Label(window, text="Enter Extension", font=("ariel", 14))
emailLabel = Label(window, text="Enter Email Address", font=("ariel", 14))
peQuestionsLabel = Label(window, text="Choose your contact type from the dropdown:", font=("ariel", 14))


#
#This is where we place the questions in the window
#
def initQuestions():
    picLabel.grid(row=1, column=0)
    nameLabel.grid(row=2, column=0)
    titleLabel.grid(row=3, column=0)
    emailLabel.grid(row=6, column=0)

    userPic.grid(row=1, column=1)
    userName.grid(row=2, column=1)
    userTitle.grid(row=3, column=1)
    userEmail.grid(row=6, column=1)

def initExtensionQuestions():
    picLabel.grid(row=1, column=0)
    nameLabel.grid(row=2, column=0)
    titleLabel.grid(row=3, column=0)
    extensionLabel.grid(row=5, column=0)
    emailLabel.grid(row=6, column=0)

    userPic.grid(row=1, column=1)
    userName.grid(row=2, column=1)
    userTitle.grid(row=3, column=1)
    userExtension.grid(row=5, column=1)
    userEmail.grid(row=6, column=1)

def initPhoneQuestions():
    picLabel.grid(row=1, column=0)
    nameLabel.grid(row=2, column=0)
    titleLabel.grid(row=3, column=0)
    phoneLabel.grid(row=4, column=0)
    emailLabel.grid(row=6, column=0)

    userPic.grid(row=1, column=1)
    userName.grid(row=2, column=1)
    userTitle.grid(row=3, column=1)
    userPhone.grid(row=4, column=1)
    userEmail.grid(row=6, column=1)

def initFullQuestions():
    picLabel.grid(row=1, column=0)
    nameLabel.grid(row=2, column=0)
    titleLabel.grid(row=3, column=0)
    phoneLabel.grid(row=4, column=0)
    extensionLabel.grid(row=5, column=0)
    emailLabel.grid(row=6, column=0)

    userPic.grid(row=1, column=1)
    userName.grid(row=2, column=1)
    userTitle.grid(row=3, column=1)
    userPhone.grid(row=4, column=1)
    userExtension.grid(row=5, column=1)
    userEmail.grid(row=6, column=1)

def peEntityVariationLogic(passed_Html):
    if finishedEntity.upper() == "GS" :
        if finishedQuestion == "phone" :
            passed_Html.write(gradSols_STR_noExt.format(finishedName, finishedTitle, finishedPhone, finishedEmail, finishedPic))
        elif finishedQuestion == "extension" :
            passed_Html.write(gradSols_STR_noPhone.format(finishedName, finishedTitle, finishedExtension, finishedEmail, finishedPic))
        elif finishedQuestion == "both" :
            passed_Html.write(gradSols_STR.format(finishedName, finishedTitle, finishedPhone, finishedEmail, finishedPic, finishedExtension))
        else :
            print("Failure in peEntity method under GS entity logic.")
            sys.exit()
    elif finishedEntity.upper() == "SS" :
        if finishedQuestion == "phone" :
            passed_Html.write(smartSchools_STR_noExt.format(finishedName, finishedTitle, finishedPhone, finishedEmail, finishedPic))
        elif finishedQuestion == "extension" :
            passed_Html.write(smartSchools_STR_noPhone.format(finishedName, finishedTitle, finishedExtension, finishedEmail, finishedPic))
        elif finishedQuestion == "both" :
            passed_Html.write(smartSchools_STR.format(finishedName, finishedTitle, finishedPhone, finishedEmail, finishedPic, finishedExtension))
        else:
            print("Failutre in peEntity method under SS entity logic")
            sys.exit()
            
    else :
        print("Failure in peEntity method under another the catch all")
        sys.exit()
    
#
#This is where the HTML file is created with the user input data
#
def htmlCreatorMethod():
    Html_file= open(finishedName + " Signature.html","w")

    if finishedEntity.upper() == "GS" or finishedEntity.upper() == "SS" :
        peEntityVariationLogic(Html_file)
    elif finishedEntity.upper() == "L" :
        Html_file.write(lumos_STR.format(finishedName, finishedTitle, finishedEmail, finishedPic))
    elif finishedEntity.upper() == "AW" :
        Html_file.write(archway_STR.format(finishedName, finishedTitle, finishedPhone, finishedEmail, finishedPic))
    elif finishedEntity.upper() == "WHL" :
        Html_file.write(welcomeHomeLearning_STR.format(finishedName, finishedTitle, finishedPhone, finishedEmail, finishedPic))
    else:
        print(finishedEntity)
        print(finishedQuestion)
        print("You have failed the simple entity task.")
        sys.exit()
        
    #Html_file.write(.format(userName, userTitle, userPhone, userEmail))

    Html_file.close()


#
#Assigned gloabl finished variables with user input data
#
def signatureCreatorPopup():
    #things = userName.get()
    #label.configure(text=things)
    
    global finishedPic 
    finishedPic = str(userPic.get())
    global finishedName 
    finishedName = str(userName.get())
    global finishedTitle 
    finishedTitle = str(userTitle.get())
    global finishedEmail 
    finishedEmail = str(userEmail.get())
    
    global finishedPhone
    global finishedExtension

    if finishedQuestion == "phone" :
        finishedPhone = str(userPhone.get())
    elif finishedQuestion == "extension" :
        finishedExtension = str(userExtension.get())
    elif finishedQuestion == "both" :
        finishedPhone = str(userPhone.get())
        finishedExtension = str(userExtension.get())
    
    htmlCreatorMethod()
    
    messagebox.showinfo("Alert", "it has been done")
    window.destroy()

def followUpMethod():
    userButton = Button(window, text='submit', command=signatureCreatorPopup, font=("ariel", 12))
    userButton.grid(row=7, column=0)

def phoneFollowUpMethod():
    initPhoneQuestions()
    followUpMethod()

def noPEFollowUpMethod():
    initQuestions()
    followUpMethod()

def questionInitiator():
    global finishedQuestion 
    finishedQuestion = clicked.get()
    
    if finishedQuestion == "phone" :
        initPhoneQuestions()
    elif finishedQuestion == "extension" :
        initExtensionQuestions()
    elif finishedQuestion == "both" :
        initFullQuestions()
    else:
        messagebox.showinfo("Alert", "You have failed the simple pe question")
        window.destroy()
        print("You have failed the simple pe question task.")
        sys.exit()

    userQuestion.destroy()
    userFirst.destroy()
    peQuestionsLabel.destroy()

    followUpMethod()

def peQuestionInitiator():
    global finishedEntity 
    finishedEntity = entityClicked.get()

    entityLabel.destroy()
    userEntity.destroy()
    entityButton.destroy()

    if finishedEntity.upper() == "GS" or finishedEntity.upper() == "SS" :
        peQuestionsLabel.grid(row=0, column=0)
        userQuestion.grid(row=0, column=1)
        
        userFirst.grid(row=1, column=0)
    elif finishedEntity.upper() == "L" :
        noPEFollowUpMethod()
    elif finishedEntity.upper() == "WHL" or finishedEntity.upper() == "AW" :
        phoneFollowUpMethod()
    else:
        #
        #Error handling for wrong entity input
        #
        messagebox.showinfo("Alert", "You have failed the Entity Input questions")
        window.destroy()
        print("You have failed the simple entity question task.")
        sys.exit()


#
#Ask for entity first, then ask for phone/extension
#
entityLabel.grid(row=0, column=0)
userEntity.grid(row=0, column=1)

entityButton = Button(window, text="submit", command=peQuestionInitiator, font=("ariel", 12))
entityButton.grid(row=1, column=0)

userFirst = Button(window, text="submit", command=questionInitiator, font=("ariel", 12))

window.mainloop()



