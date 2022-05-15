output = []
n = int(input())
for i in range(n):
    arr = input().split(",")
    output.append(arr)

# print(output)

# "Vijay Kumar Mishra";;"+917879876977";"Saritamp16@gmail.com";"Saritamp16@gmail.com";"The_vijay_kumr";"Kumar vijay";"Not checked";"Not checked";"Checked";;;"https://drive.google.com/file/d/1-LpSbvia-Mku-R4Nn1z3UpFlzf3oCZcu/view?usp=drivesdk"
# "Shivom bhatt";;"8368792464";"shivombhatt1012@gmail.com";;"Shivombhatt010";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/1cbf906a33ee24cd372b85f1346c38e42818ec2ae87a7aa8b8776bb7399344b7";;
# "Murli Manohar";;"9305855616";"murlishukla86@gmail.com";;"7shuklamann";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/f10909f71f82dcca6dadd86f82e86d8a13d231265b3368e54faa6ba01821b737";;
# "Punyatoya Mishra";;"9861383475";"mishrapunyatoya2003@gmail.com";;"mishrapunyatoya";"Punyatoya Mishra";"Not checked";"Checked";"Not checked";;"https://drive.google.com/file/d/1Oy0dLDsydclpI5Q8dIbT1PGY0ud9d_9M/view?usp=drivesdk";
# "Aadi Jain";"21BCT0425";"7719484945";"tojainadi@gmail.com";"aadi.jain2021@vitstudent.ac.in";"n/a";;"Not checked";"Checked";"Not checked";;"https://drive.google.com/file/d/1ch17KNNEEfJnWQKlNET9Q4Smm6L1yniU/view?usp=drivesdk";
# "Saumya Shandilya";"21BCM0189";"7561997893";"saumya.shandilya2021@vitstudent.ac.in";"saumya.shandilya2021@vitstudent.ac.in";"_saumya.shandilya_";;"Not checked";"Not checked";"Checked";;;"https://drive.google.com/file/d/1rVUpCzskXwJ5DAIjUT8b9OoyYbTV4sWA/view?usp=drivesdk"
# "Tejasv Goyal";"21MIC0192";"8000757837";"tejasvgoyal2003@gmail.com";"tejasv.goyal2021@vitstudent.ac.in";"soul_9081";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/99b836199407dc6429ba67ca9b324b8125059c7517d6db8e470c23163ef12d4a";;
# "Vedant Bhargava";"21BAG0141";"9790208591";"vedantbhargava26@gmail.com";"vedant.bhargava2021@vitstudent.ac.in";"aadarsh_insaan";;"Not checked";"Not checked";"Checked";;;"https://drive.google.com/file/d/15rDOn9Ur5KYaMi-NPT1OYlmf8BexyzE2/view?usp=drivesdk"
# "Shreya Mangesh";"21BCI0122";"+919361926292";"cpsshreya216@gmail.com";"shreya.mangesh2021@vitstudent.ac.in";"shreyam_25";;"Not checked";"Checked";"Checked";;"https://drive.google.com/file/d/1j4VxAIGQA8EBD8S2x8Tg13CLcnPub_sy/view?usp=drivesdk";"https://drive.google.com/file/d/1ivWQry5VlCCDrQsd125b1VYaNutrECnv/view?usp=drivesdk"
# "rikkinmehta114@gmail.com";"rikkinpritesh.mehta2021@vitstudent.ac.in";"rikkin3012";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/7c95769dde919a59e2b890416955b7ad55eef0078947b8792fc13e4cf9bdf4ec";;
# "Priyanshu Tripathi";;"8920842716";"p.t.2001.14@gmail.com";;"@hehepriii";;"Checked";"Not checked";"Checked";"https://tripetto.app/attachment/c06cfa1282e5e2d7b2b8aeb37b14ee3b77836c4bbb55c77ec36d247044e81fa4";;"https://drive.google.com/file/d/1EeUKNID2kKodMFUyd4mhzUqTkumaDygE/view?usp=drivesdk"
# "Anngela Roy";"20MIS0186";"9971412924";"anngela.roy2020@vitstudent.ac.in";"anngela.roy2020@vitstudent.ac.in";"Anngela._._";"--";"Not checked";"Checked";"Not checked";;"https://drive.google.com/file/d/18S-f8CNdAWDFNhXtO9wG6E_K6Kzn0HUl/view?usp=drivesdk";
# "Devasish";;"09973261264";"kr.devasish.28@gmail.com";;"devasish.in";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/4de8a6e843db11d7ef99a4d6743aa1d0dd62d530a164ca0c5bd134e5b7fd9f65";;
# "Devasish Thakur";;"9973261264";"kr.devasish.28@gmail.com";;"devasish.in";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/039c3a121393082486ba2cc45cefd4e4f29674a2f48c815359a94e9d8b212c1c";;
# "Shristi Ghosh";;"8280130288";"sonu.shristi.0905@gmail.com";;"art.acquisitions.0905";"Shristi Ghosh";"Not checked";"Checked";"Not checked";;"https://www.instagram.com/tv/CQY_oQApGG3/?utm_medium=copy_link";
# "Arun Sagar";"NULL";"+91 72908 03860";"arunsagar207@gmail.com";"xyz.abc1234@abcdefgh.ac.in";"https://www.instagram.com/arun.sagar21/";;"Not checked";"Checked";"Not checked";;"https://drive.google.com/file/d/12WJeT_llfcLANjYnkwuPtm7q3WgGp67Y/view?usp=sharing";
# "Vijay Kumar Mishra";;"+917879876977";"Saritamp16@gmail.com";"Saritamp16@gmail.com";"The_vijay_kumr";"Kumar vijay";"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/e356ed7da35125850a2e88af0e48b3f58c812e412333756d0585da914b1d8266";;
# "Tanmay Jain";"20BBT0209";"+91 9004354466";"tanmayjaintommy@gmail.com";"tanmay.2020@vitstudent.ac.in";"tanmayjain_13";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/1a84adf9796fd1f72a5088834beeeeff3cf977dd45893ffd004f7bba5a6295bf";;
# "Atul kumar Srivastava";;"6306367183";"atulsrivastava.364@gmail.com";;"incomparable__atul___";;"Not checked";"Not checked";"Checked";;;"https://drive.google.com/file/d/1X1CjgwC4Ofy4igNkrzIO-YT56JZ428EB/view?usp=drivesdk"
# "Amina naaz";;"7095293754";"Naazamina113@gmail.com";;"harf_e_khamoshi";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/4190d06a25ffa21b3d3a55820db2ef76f2f81033fe06042922e5d873495e7e7a";;
# "Shruti Bansal";;"6399761577";"bansalshru142002@gmail.com";;"Expressinneru_667";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/c6ad702a81d73cbd0d9159a78a9420636685651afe29c1691b8d0247ba9eab1d";;
# "Khyati Priya Jain";"21BEC2194";"8130216859";"khyatipriya.jain2021@vitstudent.ac.in";"khyatipriya.jain2021@vitstudent.ac.in";"khyatipriyajain";;"Not checked";"Not checked";"Checked";;;"https://drive.google.com/file/d/1SCEh_Osjp6AcFro-oLEOoqr6UflNr2lc/view?usp=drivesdk"
# "D R VASUKI";"21BCM0048";"6362688716";"vasukisaibaba@gmail.com";"vasuki.dr2021@vitstudent.ac.in";"_vasuki_rajesh_";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/a623cc9eb570acc910c4263d30933dfac60a1e68f4d08898e5af1024f58b7266";;
# "अतुल कुमार श्रीवास्तव";;"6306367183";"atulsrivastava.364@gmail.com";;"incomparable__atul___";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/853e5ed6a00a143cf31c042e945513f5c0a94f93ebfcb83d590c82ad9a28f0bf";;
# "Khyati Priya Jain";"21BEC2194";"8130216859";"khyatipriya.jain2021@vitstudent.ac.in";"khyatipriya.jain2021@vitstudent.ac.in";"khyatipriyajain";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/774dc74da3bc01de80425ace056fcb0c6b21136c58b9c9cfbd97a6fa99d78135";;
# "Aditya Anand";"21BCE2285";"8210840130";"aditya1231anand@gmail.com";"aditya.anand2021@vitstudent.ac.in";"adiianand03";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/c8cb40d10a149e9eddc87a77b9b3d204da8c3b6b1432eeb03c396348c2fe133c";;
# ;"ABHINAV MADHAV JASRASARIA";"20BME0506";"6901771247";"abhinavm.jasrasaria@gmail.com";"abhinavmadhav.j2020@vitstudent.ac.in";"https://www.instagram.com/abhinavmadhavjasrasaria/";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/4d1b9a09da3aa835041825540d3d02456f859f1807b300c6160ddaac4769239b";;
# "Uttirna Dhar";;"7699171496";"uttirnadhr09@gmail.com";;"ud00001";"Uttirna Dhar";"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/661e224c2b160df4a4a2db8b30a5be59154bccd0ba20b98891aff5907d2134ba";;
# "TANNISTHA ROY";;"919836176700";"2025017@ksap.kiit.ac.in";;"tannistharoy01";"Tannistha Roy";"Not checked";"Checked";"Not checked";;"https://drive.google.com/file/d/1LKC9qnHwtgBuvtMjyhVGBX9as58JipXV/view?usp=drivesdk";
# "Devabathini Venkata Sai Kousik";"20BEC0355";"8247081967";"venkatasaikousik007@gmail.com";"venkata.saikousik2020@vitstudent.ac.in";"d.v.s.kousik";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/4094c564af7357bd719387848d033cddcb41414d1d6c609bacc14c3092a228f8";;
# "Prajapati Jha";;"9162842809";"jhaprajapati751@gmail.com";;"3165_Prajapati Jha";"Prajapati Jha";"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/8a32c503ea35acaa846c302347b21cd9f326d302127ddfba29c4210de977d869";;
# "Ayush Kumar Singh";;"9548306379";"cayush2001@gmail.com";;"_a.y.u.s.h_0";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/14053b4a5db091e61dbba2eba911d3cc0cd9aee77030b261c97a3984486463cb";;
# ;"Khyati Priya Jain";"21BEC2194";"8130216859";"khyatipriya.jain2021@vitstudent.ac.in";"khyatipriya.jain2021@vitstudent.ac.in";"khyatipriyajain";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/aa66dfb1c7b7b9180efa6066acc10acffc64f2ef6f87178fd5c8aab36def5f54";;
# "Aditya Anand";"21BCE2285";"8210840130";"aditya.anand2021@vitstudent.ac.in";"aditya.anand2021@vitstudent.ac.in";"adiianand03";;"Not checked";"Not checked";"Checked";;;"https://drive.google.com/file/d/1-8wn5XBZETC_MsFXN4MFR_4YHOitFi_4/view?usp=sharing"
# "Priyanshu Kumar";"21BBS0076";"8292367088";"priyanshu.kumar2021a@vitstudent.ac.in";"priyanshu.kumar2021a@vitstudent.ac.in";"priyanshu_yadav78";;"Checked";"Not checked";"Not checked";"https://tripetto.app/attachment/22a883d3c62cf056f713d18817c161e4652df54ec78e507c1bd1fe3fb556b220";;

for i in output:
    for j in i:
        print(j)

"Vijay Kumar Mishra"
"+917879876977"
"Saritamp16@gmail.com"
"Saritamp16@gmail.com"
"The_vijay_kumr"
"Kumar vijay"
"Not checked"
"Not checked"
"Checked"
"https://drive.google.com/file/d/1-LpSbvia-Mku-R4Nn1z3UpFlzf3oCZcu/view?usp=drivesdk"


"Shivom bhatt"
"8368792464"
"shivombhatt1012@gmail.com"
"Shivombhatt010"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/1cbf906a33ee24cd372b85f1346c38e42818ec2ae87a7aa8b8776bb7399344b7"


"Murli Manohar"
"9305855616"
"murlishukla86@gmail.com"
"7shuklamann"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/f10909f71f82dcca6dadd86f82e86d8a13d231265b3368e54faa6ba01821b737"


"Punyatoya Mishra"
"9861383475"
"mishrapunyatoya2003@gmail.com"
"mishrapunyatoya"
"Punyatoya Mishra"
"Not checked"
"Checked"
"Not checked"
"https://drive.google.com/file/d/1Oy0dLDsydclpI5Q8dIbT1PGY0ud9d_9M/view?usp=drivesdk"


"Aadi Jain"
"21BCT0425"
"7719484945"
"tojainadi@gmail.com"
"aadi.jain2021@vitstudent.ac.in"
"n/a"
"Not checked"
"Checked"
"Not checked"
"https://drive.google.com/file/d/1ch17KNNEEfJnWQKlNET9Q4Smm6L1yniU/view?usp=drivesdk"


"Saumya Shandilya"
"21BCM0189"
"7561997893"
"saumya.shandilya2021@vitstudent.ac.in"
"saumya.shandilya2021@vitstudent.ac.in"
"_saumya.shandilya_"
"Not checked"
"Not checked"
"Checked"
"https://drive.google.com/file/d/1rVUpCzskXwJ5DAIjUT8b9OoyYbTV4sWA/view?usp=drivesdk"


"Tejasv Goyal"
"21MIC0192"
"8000757837"
"tejasvgoyal2003@gmail.com"
"tejasv.goyal2021@vitstudent.ac.in"
"soul_9081"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/99b836199407dc6429ba67ca9b324b8125059c7517d6db8e470c23163ef12d4a"


"Vedant Bhargava"
"21BAG0141"
"9790208591"
"vedantbhargava26@gmail.com"
"vedant.bhargava2021@vitstudent.ac.in"
"aadarsh_insaan"
"Not checked"
"Not checked"
"Checked"
"https://drive.google.com/file/d/15rDOn9Ur5KYaMi-NPT1OYlmf8BexyzE2/view?usp=drivesdk"


"Shreya Mangesh"
"21BCI0122"
"+919361926292"
"cpsshreya216@gmail.com"
"shreya.mangesh2021@vitstudent.ac.in"
"shreyam_25"
"Not checked"
"Checked"
"Checked"
"https://drive.google.com/file/d/1j4VxAIGQA8EBD8S2x8Tg13CLcnPub_sy/view?usp=drivesdk"
"https://drive.google.com/file/d/1ivWQry5VlCCDrQsd125b1VYaNutrECnv/view?usp=drivesdk"


"rikkinmehta114@gmail.com"
"rikkinpritesh.mehta2021@vitstudent.ac.in"
"rikkin3012"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/7c95769dde919a59e2b890416955b7ad55eef0078947b8792fc13e4cf9bdf4ec"


"Priyanshu Tripathi"
"8920842716"
"p.t.2001.14@gmail.com"
"@hehepriii"
"Checked"
"Not checked"
"Checked"
"https://tripetto.app/attachment/c06cfa1282e5e2d7b2b8aeb37b14ee3b77836c4bbb55c77ec36d247044e81fa4"
"https://drive.google.com/file/d/1EeUKNID2kKodMFUyd4mhzUqTkumaDygE/view?usp=drivesdk"


"Anngela Roy"
"20MIS0186"
"9971412924"
"anngela.roy2020@vitstudent.ac.in"
"anngela.roy2020@vitstudent.ac.in"
"Anngela._._"
"--"
"Not checked"
"Checked"
"Not checked"
"https://drive.google.com/file/d/18S-f8CNdAWDFNhXtO9wG6E_K6Kzn0HUl/view?usp=drivesdk"


"Devasish"
"09973261264"
"kr.devasish.28@gmail.com"
"devasish.in"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/4de8a6e843db11d7ef99a4d6743aa1d0dd62d530a164ca0c5bd134e5b7fd9f65"


"Devasish Thakur"
"9973261264"
"kr.devasish.28@gmail.com"
"devasish.in"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/039c3a121393082486ba2cc45cefd4e4f29674a2f48c815359a94e9d8b212c1c"


"Shristi Ghosh"
"8280130288"
"sonu.shristi.0905@gmail.com"
"art.acquisitions.0905"
"Shristi Ghosh"
"Not checked"
"Checked"
"Not checked"
"https://www.instagram.com/tv/CQY_oQApGG3/?utm_medium=copy_link"


"Arun Sagar"
"NULL"
"+91 72908 03860"
"arunsagar207@gmail.com"
"xyz.abc1234@abcdefgh.ac.in"
"https://www.instagram.com/arun.sagar21/"
"Not checked"
"Checked"
"Not checked"
"https://drive.google.com/file/d/12WJeT_llfcLANjYnkwuPtm7q3WgGp67Y/view?usp=sharing"


"Vijay Kumar Mishra"
"+917879876977"
"Saritamp16@gmail.com"
"Saritamp16@gmail.com"
"The_vijay_kumr"
"Kumar vijay"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/e356ed7da35125850a2e88af0e48b3f58c812e412333756d0585da914b1d8266"


"Tanmay Jain"
"20BBT0209"
"+91 9004354466"
"tanmayjaintommy@gmail.com"
"tanmay.2020@vitstudent.ac.in"
"tanmayjain_13"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/1a84adf9796fd1f72a5088834beeeeff3cf977dd45893ffd004f7bba5a6295bf"


"Atul kumar Srivastava"
"6306367183"
"atulsrivastava.364@gmail.com"
"incomparable__atul___"
"Not checked"
"Not checked"
"Checked"
"https://drive.google.com/file/d/1X1CjgwC4Ofy4igNkrzIO-YT56JZ428EB/view?usp=drivesdk"


"Amina naaz"
"7095293754"
"Naazamina113@gmail.com"
"harf_e_khamoshi"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/4190d06a25ffa21b3d3a55820db2ef76f2f81033fe06042922e5d873495e7e7a"


"Shruti Bansal"
"6399761577"
"bansalshru142002@gmail.com"
"Expressinneru_667"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/c6ad702a81d73cbd0d9159a78a9420636685651afe29c1691b8d0247ba9eab1d"


"Khyati Priya Jain"
"21BEC2194"
"8130216859"
"khyatipriya.jain2021@vitstudent.ac.in"
"khyatipriya.jain2021@vitstudent.ac.in"
"khyatipriyajain"
"Not checked"
"Not checked"
"Checked"
"https://drive.google.com/file/d/1SCEh_Osjp6AcFro-oLEOoqr6UflNr2lc/view?usp=drivesdk"


"D R VASUKI"
"21BCM0048"
"6362688716"
"vasukisaibaba@gmail.com"
"vasuki.dr2021@vitstudent.ac.in"
"_vasuki_rajesh_"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/a623cc9eb570acc910c4263d30933dfac60a1e68f4d08898e5af1024f58b7266"


"अतुल कुमार श्रीवास्तव"
"6306367183"
"atulsrivastava.364@gmail.com"
"incomparable__atul___"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/853e5ed6a00a143cf31c042e945513f5c0a94f93ebfcb83d590c82ad9a28f0bf"


"Khyati Priya Jain"
"21BEC2194"
"8130216859"
"khyatipriya.jain2021@vitstudent.ac.in"
"khyatipriya.jain2021@vitstudent.ac.in"
"khyatipriyajain"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/774dc74da3bc01de80425ace056fcb0c6b21136c58b9c9cfbd97a6fa99d78135"


"Aditya Anand"
"21BCE2285"
"8210840130"
"aditya1231anand@gmail.com"
"aditya.anand2021@vitstudent.ac.in"
"adiianand03"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/c8cb40d10a149e9eddc87a77b9b3d204da8c3b6b1432eeb03c396348c2fe133c"


"ABHINAV MADHAV JASRASARIA"
"20BME0506"
"6901771247"
"abhinavm.jasrasaria@gmail.com"
"abhinavmadhav.j2020@vitstudent.ac.in"
"https://www.instagram.com/abhinavmadhavjasrasaria/"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/4d1b9a09da3aa835041825540d3d02456f859f1807b300c6160ddaac4769239b"


"Uttirna Dhar"
"7699171496"
"uttirnadhr09@gmail.com"
"ud00001"
"Uttirna Dhar"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/661e224c2b160df4a4a2db8b30a5be59154bccd0ba20b98891aff5907d2134ba"


"TANNISTHA ROY"
"919836176700"
"2025017@ksap.kiit.ac.in"
"tannistharoy01"
"Tannistha Roy"
"Not checked"
"Checked"
"Not checked"
"https://drive.google.com/file/d/1LKC9qnHwtgBuvtMjyhVGBX9as58JipXV/view?usp=drivesdk"


"Devabathini Venkata Sai Kousik"
"20BEC0355"
"8247081967"
"venkatasaikousik007@gmail.com"
"venkata.saikousik2020@vitstudent.ac.in"
"d.v.s.kousik"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/4094c564af7357bd719387848d033cddcb41414d1d6c609bacc14c3092a228f8"

"Prajapati Jha"

"9162842809"
"jhaprajapati751@gmail.com"
"3165_Prajapati Jha"
"Prajapati Jha"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/8a32c503ea35acaa846c302347b21cd9f326d302127ddfba29c4210de977d869"


"Ayush Kumar Singh"
"9548306379"
"cayush2001@gmail.com"
"_a.y.u.s.h_0"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/14053b4a5db091e61dbba2eba911d3cc0cd9aee77030b261c97a3984486463cb"

"Khyati Priya Jain"
"21BEC2194"
"8130216859"
"khyatipriya.jain2021@vitstudent.ac.in"
"khyatipriya.jain2021@vitstudent.ac.in"
"khyatipriyajain"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/aa66dfb1c7b7b9180efa6066acc10acffc64f2ef6f87178fd5c8aab36def5f54"


"Aditya Anand"
"21BCE2285"
"8210840130"
"aditya.anand2021@vitstudent.ac.in"
"aditya.anand2021@vitstudent.ac.in"
"adiianand03"
"Not checked"
"Not checked"
"Checked"
"https://drive.google.com/file/d/1-8wn5XBZETC_MsFXN4MFR_4YHOitFi_4/view?usp=sharing"


"Priyanshu Kumar"
"21BBS0076"
"8292367088"
"priyanshu.kumar2021a@vitstudent.ac.in"
"priyanshu.kumar2021a@vitstudent.ac.in"
"priyanshu_yadav78"
"Checked"
"Not checked"
"Not checked"
"https://tripetto.app/attachment/22a883d3c62cf056f713d18817c161e4652df54ec78e507c1bd1fe3fb556b220"
