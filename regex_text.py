import re
from numpy import mat

from soupsieve import match
from sympy import mobius #导入 正则表达式库,还有其他的乱七八糟的不被调用的库

# # 正则表达式,匹配查找
# massage = "hi there ~ my name is william jiamin and my wechat id is WilliamJiamin,\
# you can call me at (86)-18888888888 which name is William ace,if it doesn't work you can call\
# 86-16666666666"

# # find_my_phone_number = re.compile(r"(\(\d\d\))-(\d\d\d\d\d\d\d\d\d\d\d)")   # "\d"表示一位数字,()用于对查找的数据进行分组,\(\)用于对括号的查找
# # find_my_phone_number_1 = re.compile(r'(\((\d){2}\))-((\d){11})')            #利用后面使用的(){n}形式简化,虽然。。。
# # match_object = find_my_phone_number.search(massage)                 #在massage中查找符合条件的<<第一个>>对象
# # match_findall = find_my_phone_number.findall(massage)               #在massage中查找所有符合条件的对象
# # print(match_object)                                 #打印查找的对象所在位置，和值
# # print(match_object.group())                         #打印查找到的对象
# # print(match_object.group(1))                        #打印被括号包起来的国家码
# # print(match_object.group(2))                        #打印查找对象的第二组数据
# # print(match_findall)                                #打印所有符合的对象

# williamRegax = re.compile(r'William(jiamin| ace| teacher| fintech)')    #通常使用Regex表示正则表达式的
# mo = williamRegax.search(massage)
# print(mo.group())

# message_1 = "I am Monkey luffy. I am the king of the sea!"
# luffy_Regex = re.compile(r'Monkey (D )?luffy')          #()?表示可有可无
# mo = luffy_Regex.search(message_1)
# print(mo)
# print(mo.group())

# text = "I am so happy now! yeah~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
# happy_Regex = re.compile(r'yeah(~)*')                      #()*表示匹配括号里的重复字符可以不包含括号内字符,()+表示匹配时必须包含括号中的字符
# happy_Regex_1 = re.compile(r'yeah(~){3}')                  #(){n,m}表示括号内字符须要重复出现n至m次(n<m),默认greedy match.(){n,m}? 表示nongreedy match
# mo = happy_Regex_1.search(text)

# print(mo)
# if( mo!= None ):                                           #讨厌在visual code里出现报错信息，然后要f5退出debug模式
#     print(mo.group())
# else:
#     print("error")

text = """
<!DOCTYPE html>
<html>
  <head>
<meta http-equiv="Content-Type" content="text/html; charset=gbk">
<title>网易</title>
<meta name="model_url" content="http://corp.163.com/special/00832V22/gbcontactus.html" />
<base target="_blank" />
<!-- 公用css -->
<style type="text/css">
body {font-family:"Microsoft YaHei","微软雅黑","宋体","Arial";background:#ffffff;}
body,div,dl,dt,dd,ul,ol,li,h1,h2,h3,h4,h5,h6,pre,code,
form,fieldset,legend,input,button,textarea,p,blockquote,th,td {
    margin:0;
    padding:0;
}
ol,ul{list-style:none;}
address,caption,cite,code,dfn,em,strong,th,var,optgroup {
    font-style:normal;
}
input,button,textarea,select,optgroup,option {
    font-family:inherit;
    font-size:inherit;
    font-style:inherit;
    font-weight:inherit;
    *font-size:100%;
}
fieldset,img,a img,:link img,:visited img{border:0;}
a{text-decoration:none;}
a:hover {text-decoration:none;}
:focus {outline:0;}
table{border-collapse:collapse;border-spacing:0;}
caption,th {text-align:left;}
sup,sub {font-size:100%;vertical-align:baseline;}
blockquote,q {quotes:none;}
blockquote:before,blockquote:after,q:before,q:after{content:'';content:none;}
.clear,.clearfix:after {clear:both;height:0;overflow:hidden;display:block;}
.clearfix:after {visibility:hidden;content:".";}
.clearfix{*zoom:1;}
.cm_page{width: 1200px;margin:0px auto 80px auto;}
</style>
<link rel="stylesheet" href="https://static.ws.126.net/163/f2e/commonnav2019/css/commonnav_headcss-e017654fb2.css">
</head>
<body>
<div class="ntes_wap">
        <!-- 顶部导航 开始-->
    <style type="text/css">
    .cm_ntes_topnav{height: 87px;overflow: hidden;border-top: 5px #b81c22 solid;
        background: url(http://static.ws.126.net/img09/netease/nav_bg2.png) left bottom repeat-x;}
    .cm_ntes_topnav .logo{width: 125px;height: 42px;float: left;background: url(http://cms-bucket.ws.126.net/2019/12/19/cf143f1465dc403c86cb7dc5e86a2c90.png) no-repeat 0px 8px;overflow: hidden;line-height: 300px;margin:20px 0px 0px 60px;display: inline;}
    .cm_ntes_topnav .navlist{float: left;display: inline;margin:31px 0px 0px 100px;}
    .cm_ntes_topnav .navlist li{float: left;display: inline;font-size: 18px;margin-right: 80px;}
    .cm_ntes_topnav .navlist a{color: #888888;}
    .cm_ntes_topnav .navlist .current a{color: #333333;position: relative;}
     .cm_ntes_topnav .navlist .current a:after{content: '';position:absolute;width: 4px;height: 8px;display: block;background: url(http://cms-bucket.ws.126.net/2019/12/19/cf143f1465dc403c86cb7dc5e86a2c90.png) no-repeat -141px -1px;right: -14px;top:8px;}
    </style>
    <div class="cm_ntes_topnav">
        <a href="http://www.163.com/" class="logo">网易</a>
        <ul class="navlist">
            <li ><a href="https://corp.163.com/gb/about/overview.html">公司简介</a></li>
            <li ><a href="https://corp.163.com/gb/about/management.html">管理团队</a></li>
            <li ><a href="http://corp.163.com/special/008397SO/neteasenews.html ">公司新闻</a></li>
            <li><a href="https://netease.gcs-web.com">投资者关系</a></li>
            <li class="current"><a href="https://corp.163.com/gb/contactus.html">联系我们</a></li>
        </ul>
    </div>    <!-- 顶部导航 结束 -->
    <style type="text/css">
    .page{width: 1200px;margin:0px auto 80px auto;line-height: 24px;}
    .page_tb{
        margin-top: 30px;
    }
    .page_tb tr{height: 26px;}
    .page_tb p,.page_tb td,.page_tb .inewsbody{
        font-size: 14px;
    }
    </style>
    <!-- 内容 开始 -->
    <div class="page">
    	<div class="page_tb">
        <table>
        	<tr>
        		<td>
        			<table width="100%"  border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td style="padding:5px;">
                <!-- 网易客户服务 -->
                  <p>&nbsp;</p>
                  <p><br>
                    <span class="inewsbody"><b><font color="#990000">网易</font>客户服务</b> 
                    </span> </p>
                   <table border="0" cellspacing="0" cellpadding="4">
                    <tr> 
                      <td valign="top" class="inewsbody" width="100">客服热线:</td>
                      <td width="2">&nbsp;</td>
                      <td valign="top" class="inewsbody">95163234</td>
                    </tr>
                    <tr> 
                      <td valign="top" class="inewsbody" width="100">服务时间:</td>
                      <td width="2">&nbsp;</td>
                      <td valign="top" class="inewsbody">08：00 - 24：00</td>
                    </tr>
                  </table>
                  <!-- 游戏客服 -->
                  <p>&nbsp;</p>
                  <p><br>
                    <span class="inewsbody"><b><font color="#990000">网易</font>游戏客服</b> 
                    </span> </p>
                  <table border="0" cellspacing="0" cellpadding="4">
                    <tr> 
                      <td valign="top" class="inewsbody" width="120">游戏客服总机电话:</td>
                      <td width="2">&nbsp;</td>
                      <td valign="top" class="inewsbody">95163000</td>
                    </tr>
                    <tr> 
                      <td valign="top" class="inewsbody" width="120">大话西游客服电话:</td>
                      <td width="2">&nbsp;</td>
                      <td valign="top" class="inewsbody">95163555</td>
                    </tr>
                    <tr> 
                      <td valign="top" class="inewsbody" width="120">梦幻西游客服电话:</td>
                      <td width="2">&nbsp;</td>
                      <td valign="top" class="inewsbody">95163999</td>
                    </tr>
                    <tr> 
                      <td valign="top" class="inewsbody" width="120">天下叁客服电话:</td>
                      <td width="2">&nbsp;</td>
                      <td valign="top" class="inewsbody">95163777</td>
                    </tr>
                    <TR height="27">
                            <TD height="22" colspan="3"><p class="STYLE1">&nbsp;</p></TD>
                    </TR>
                    <tr> 
                      <td height="27" colspan="3"><span class="STYLE1">如果您需要反馈问题，可优先使用游戏内的客服中心咨询或拨打上述客服热线。</span></td>
                    </tr>
                  </table>
                  
                  <!-- 有道 -->
                  <p>&nbsp;</p>
                  <p><br>
                    <span class="inewsbody"><b><font color="#990000">网易</font>有道客服</b> 
                    </span> </p>
                  <table border="0" cellspacing="0" cellpadding="4">
                    <tr> 
                      <td valign="top" class="inewsbody" width="100">有道精品课:</td>
                      <td width="2">&nbsp;</td>
                      <td valign="top" class="inewsbody">400-867-1360</td>
                    </tr>
                    <tr> 
                      <td valign="top" class="inewsbody" width="100">有道智能硬件:</td>
                      <td width="2">&nbsp;</td>
                      <td valign="top" class="inewsbody">400-800-4163</td>
                    </tr>
                    <TR height="27">
                            <TD height="22" colspan="3"><p class="STYLE1">&nbsp;</p></TD>
                    </TR>
                    <tr> 
                      <td height="27" colspan="3"><span class="STYLE1">为尽快解决您的问题，建议您根据使用的平台在“意见反馈”提交您的问题。</span></td>
                    </tr>
                  </table>
                  <!-- 严选 -->
                  <p>&nbsp;</p>
                  <p><br>
                    <span class="inewsbody"><b><font color="#990000">网易</font>严选</b> 
                    </span> </p>
                  <table border="0" cellspacing="0" cellpadding="4">
                    <tr> 
                      <td valign="top" class="inewsbody" width="100">客服热线:</td>
                      <td width="2">&nbsp;</td>
                      <td valign="top" class="inewsbody">400-0368-163</td>
                    </tr>
                  </table>
                  <!-- 网易邮箱 -->
                  <p>&nbsp;</p>
                  <p><br>
                    <span class="inewsbody"><b><font color="#990000">网易</font>邮箱</b> 
                    </span> </p>
                  <table border="0" cellspacing="0" cellpadding="4">
                    <tr> 
                      <td valign="top" class="inewsbody" width="100">在线客户服务:</td>
                      <td width="1">&nbsp;</td>
                      <td valign="top" class="inewsbody">http://help.mail.163.com</td>
                    </tr>
                  </table>
                  
                  <p>&nbsp;</p>
                  <p><span class="inewsbody"><b><font color="#990000">网易</font>北京公司</b> 
                  </span> </p>
                  <table border="0" cellspacing="0" cellpadding="4">
                  <tr>
                    <td width="125" valign="top" class="inewsbody">地址:</td>
                    <td width="1">&nbsp;</td>
                      <td width="490" valign="top" class="inewsbody">北京市海淀区西北旺东路10号院 中关村软件园二期西区7号</td>
                  </tr>
                  <tr>
                    <td valign="top" class="inewsbody">邮编:</td>
                    <td></td>
                      <td valign="top" class="inewsbody">100084</td>
                  </tr>
                  <tr>
                    <td valign="top" class="inewsbody">电话:</td>
                    <td></td>
                      <td valign="top" class="inewsbody"><span class="inewsbody">(+8610)-82558163</span></td>
                  </tr>
                  <tr>
                      <td valign="top" class="inewsbody">广告销售部电话:</td>
                    <td></td>
                      <td valign="top" class="inewsbody"><span class="inewsbody">(+8610)-8255 8163 转88118</span></td>
                  </tr>
                  <tr>
                      <td valign="top" class="inewsbody">服务时间:</td>
                    <td></td>
                      <td valign="top" class="inewsbody"><span class="inewsbody">工作日（09:30-12:00 14:00-18:30）</span></td>
                  </tr>
                  <tr>
                    <td valign="top" class="inewsbody">市场部电话:</td>
                    <td></td>
                      <td valign="top" class="inewsbody"><span class="inewsbody">(+8610)-82558147</span></td>
                  </tr>
                </table>
                  <p>&nbsp;</p>
                  <p><span class="inewsbody"><br>
                    <b><font color="#990000">网易</font>上海公司</b> </span> </p>
                  <table border="0" cellspacing="0" cellpadding="4">
                    <tr>
                      <td width="125" valign="top" class="inewsbody">地址:</td>
                      <td width="1">&nbsp;</td>
                        <td width="490" valign="top"><span class="inewsbody">中国上海市虹口区溧阳路735号半岛湾创意产业园区2号楼3楼
                        </span></td>
                    </tr>
                    <tr>
                      <td valign="top" class="inewsbody">邮编:</td>
                      <td></td>
                        <td valign="top" class="inewsbody">200080</td>
                    </tr>
                    <tr>
                      <td valign="top" class="inewsbody">电话:</td>
                      <td></td>
                        <td valign="top"><span class="inewsbody">(+8621)-61947163</span></td>
                    </tr>
                    <tr>
                      <td valign="top" class="inewsbody">市场部电话:</td>
                      <td></td>
                        <td valign="top"><span class="inewsbody">(+8621)-61947163-7279</span></td>
                    </tr>
                  </table>
                  <p>&nbsp;</p>
                  <p><br>
                    <span class="inewsbody"><b><font color="#990000">网易</font>广州公司</b> 
                    </span> </p>
                  <table border="0" cellspacing="0" cellpadding="4">
                    <tr> 
                      <td width="125" valign="top" class="inewsbody">地址:</td>
                      <td width="1">&nbsp;</td>
                      <td width="490" valign="top"><span class="inewsbody">广东省广州市天河区思蕴路1、3、5号</span></td>
                    </tr>
                    <tr> 
                      <td valign="top" class="inewsbody">邮编:</td>
                      <td></td>
                      <td valign="top" class="inewsbody">510665</td>
                    </tr>
                    <tr> 
                      <td valign="top" class="inewsbody">电话:</td>
                      <td></td>
                      <td valign="top"><span class="inewsbody">(+8620)-85105163</span></td>
                    </tr>
                    <tr> 
                      <td height="25" valign="top" class="inewsbody">广告销售部电话:</td>
                      <td></td>
                      <td valign="top"><span class="inewsbody">(+8620)-85105163</span></td>
                    </tr>
                    <tr> 
                      <td valign="top" class="inewsbody">广告销售部电话:</td>
                      <td></td>
                      <td valign="top"><span class="inewsbody">(+8620)-8510 5291/6684</span></td>
                    </tr>
                    <tr> 
                      <td valign="top" class="inewsbody"><span class="inewsbody">服务时间:</span></td>
                      <td></td>
                      <td valign="top"><span class="inewsbody">工作日（09:30-12:00 14:00-18:30）</span></td>
                    </tr>
                  </table>
                  <!-- 杭州 -->
                  <p>&nbsp;</p>
                  <p><span class="inewsbody"><br>
                    <b><font color="#990000">网易</font>杭州公司</b> </span> </p>
                  <table border="0" cellspacing="0" cellpadding="4">
                    <tr>
                      <td width="125" valign="top" class="inewsbody">地址:</td>
                      <td width="1">&nbsp;</td>
                        <td width="490" valign="top"><span class="inewsbody">杭州市滨江区网商路599号
                        </span></td>
                    </tr>
                    <tr>
                      <td valign="top" class="inewsbody">邮编:</td>
                      <td></td>
                        <td valign="top" class="inewsbody">310052</td>
                    </tr>
                    <tr>
                      <td valign="top" class="inewsbody">电话:</td>
                      <td></td>
                        <td valign="top"><span class="inewsbody">(+0571)89852163</span></td>
                    </tr>
                  </table>
                  <!--  -->
                  <p>&nbsp;</p>
                  <p><span class="inewsbody"><br></span> </p>
                  <table border="0" cellspacing="0" cellpadding="4">
                    <tr>
                      <td width="125" valign="top" class="inewsbody">投资者关系部网站:</td>
                      <td width="1">&nbsp;</td>
                        <td width="490" valign="top"><span class="inewsbody">http://ir.netease.com/
                        </span></td>
                    </tr>
                  </table>
                </td>
            </tr>
          </table>
        		</td>
        	</tr>
        </table>
        </div>
    </div>
    <!-- 内容 结束 -->
    <!-- 底部导航条 -->
    <div class="N-nav-bottom">
    <div class="N-nav-bottom-main">
        <div class="ntes_foot_link">
            <span class="N-nav-bottom-copyright"><span class="N-nav-bottom-copyright-icon">&copy;</span> 1997-2022 网易公司版权所有</span>
            <a href="https://corp.163.com/">About NetEase</a> |
            <a href="https://corp.163.com/gb/about/overview.html">公司简介</a> |
            <a href="https://corp.163.com/gb/contactus.html">联系方法</a> |
            <a href="https://corp.163.com/gb/job/job.html">招聘信息</a> |
            <a href="https://help.163.com/">客户服务</a> |
            <a href="https://corp.163.com/gb/legal.html">隐私政策</a> |
            <a href="http://emarketing.163.com/">广告服务</a> |
           <!--  <a ne-role="feedBackLink" ne-click="handleFeedBackLinkClick()" href="http://www.163.com/special/0077450P/feedback_window.html" class="ne_foot_feedback_link">意见反馈</a> | -->
            <a href="http://jubao.aq.163.com/">不良信息举报 Complaint Center</a> |
            <a href="https://jubao.163.com/">廉正举报</a>
        </div>
    </div>
</div>
<script>
if (/closetie/.test(window.location.search)) {
  function addNewStyle(newStyle) {
    var styleElement = document.getElementById('styles_js');
    if (!styleElement) {
      styleElement = document.createElement('style');
      styleElement.type = 'text/css';
      styleElement.id = 'styles_js';
      document.getElementsByTagName('head')[0].appendChild(styleElement);
    }
    styleElement.appendChild(document.createTextNode(newStyle));
  }
  addNewStyle('.tie-area, .comment-wrap, .ep-tie-top {display: none !important;} .post_comment {opacity: 0;padding: 0;margin: 0;min-height: 0px !important;} .post_tie_top {opacity: 0;} .js-tielink {display: none;}');
}
</script>
</div>
</body>
</html>"""

phone_number_Regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phone_number_Regex.findall(text)
print(mo)