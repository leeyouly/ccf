function AdObj() {
  /* 参数表 */
  this.ADID        = 0;
  this.ADType      = 0;
  this.ADName      = "";
  this.ImgUrl      = "";
  this.ImgWidth    = 0;
  this.ImgHeight   = 0;
  this.FlashWmode  = 0;
  this.LinkUrl     = "";
  this.LinkTarget  = 0;
  this.LinkAlt     = "";
  this.Priority    = 0;
  this.CountView   = 0;
  this.CountClick  = 0;
  this.AdRoot     = "";
}

function BannerZone(_id) {
  /* 定义常量 */
  this.adNum       = 0;
  this.adDelay     = 10000;

  /* 公共参数 */
  this.ID          = _id;
  this.ZoneID      = 0;
  this.ZoneName    = "";
  this.ZoneWidth   = 0;
  this.ZoneHeight  = 0;
  this.ShowType    = 1;
  this.DivName     = "";
  this.Div         = null;

  /* 私有特性 */

  /* 定义广告实体 */
  this.AllAD       = new Array();
  this.ShowAD      = null;

  /* 相关函数 */
  this.AddAD       = BannerZone_AddAD;
  this.GetShowAD   = BannerZone_GetShowAD;
  this.Show        = BannerZone_Show;
  this.LoopShow    = BannerZone_LoopShow;

}

function BannerZone_AddAD(_AD) {
  this.AllAD[this.AllAD.length] = _AD;
}

function BannerZone_GetShowAD() {
  if (this.ShowType > 1 && this.ShowType < 4) {
    this.ShowAD = this.AllAD[0];
    return;
  }
  var num = this.AllAD.length;
  var sum = 0;
  for (var ii = 0; ii < num; ii++) {
    sum = sum + this.AllAD[ii].Priority;
  }
  if (sum <= 0) {return ;}
  var rndNum = Math.random() * sum;
  ii = 0;
  jj = 0;
  while (true) {
    jj = jj + this.AllAD[ii].Priority;
    if (jj >= rndNum) {break;}
    ii++;
  }
  this.adNum=ii;
  this.ShowAD = this.AllAD[ii];
}

function BannerZone_Show() {
  if (!this.AllAD) {
    return;
  } else {
    this.GetShowAD();
  }

  if (this.ShowAD == null) return false;
  this.DivName = "BannerZone_Div" + this.ZoneID;
  if (!this.ShowAD.ImgWidth) this.ShowAD.ImgWidth = this.ZoneWidth
  if (!this.ShowAD.ImgHeight) this.ShowAD.ImgHeight = this.ZoneHeight
  if (this.ShowType >= 3) {
   document.write("<div id='" + this.DivName + "' style='visibility:visible; z-index:1; width:" + this.ZoneWidth + "px; height:" + this.ZoneHeight + "px; filter: revealTrans(duration=2,transition=20);'>" + AD_Content(this.ShowAD) + "</div>");
  } else {
   document.write("<div id='" + this.DivName + "' style='visibility:visible; z-index:1; width:" + this.ZoneWidth + "px; height:" + this.ZoneHeight + "px;'>" + AD_Content(this.ShowAD) + "</div>");

    //if (this.ShowAD.CountView) {
    // document.write ("<scr"+"ipt src='" + this.ShowAD.AdRoot + "/go.php?type=view&adid=" + this.ShowAD.ADID + "'></" + "scr"+"ipt>")
    //}
  }
  this.Div = document.getElementById(this.DivName);
  if (this.ShowType >= 3) this.LoopShow(); //循环显示
}



function BannerZone_LoopShow() { //循环显示代码
  var ie_flag=0;
	if(navigator.userAgent.indexOf("MSIE")>0){
    //ie_flag=1;//ie下不要效果
  } 
  if(ie_flag){
  	this.Div.filters.revealTrans.Transition=Math.floor(Math.random()*23); 
    this.Div.filters.revealTrans.apply(); 
  } 
  if (this.AllAD[this.adNum].ImgWidth) this.AllAD[this.adNum].ImgWidth = this.ZoneWidth
  if (this.AllAD[this.adNum].ImgHeight) this.AllAD[this.adNum].ImgHeight = this.ZoneHeight
  
  //一次刷新页面 循环一周 只是第一个循环展示次数加一(展示到的图片才加一)
  if (this.ShowAD.CountView) {
    loopNum++;
    //if(loopNum<=this.AllAD.length)
    	//$("body").append("<scr"+"ipt src='" + this.ShowAD.AdRoot + "/go.php?type=view&adid=" + this.AllAD[this.adNum].ADID + "'></" + "scr"+"ipt>");
  	this.Div.innerHTML=AD_Content(this.AllAD[this.adNum]);
  }
  	
  if(ie_flag){
    this.Div.filters.revealTrans.play();
  }
  if(this.AllAD[this.adNum].Delaytime>0){  
    this.Div.timer=setTimeout(this.ID+".LoopShow()",this.AllAD[this.adNum].Delaytime*1000);
  }else{
    this.Div.timer=setTimeout(this.ID+".LoopShow()",this.adDelay);
  }
  if(this.adNum<this.AllAD.length-1) this.adNum++ ; 
  else this.adNum=0; 
}

function AD_Content(o) {

  var str = "";
  if(o.ADType == 1 || o.ADType == 2) {
    tmpurl = o.ImgUrl.toLowerCase();
    if (tmpurl.indexOf("http://") == - 1) o.ImgUrl = o.AdRoot + o.ImgUrl;
    if (tmpurl.indexOf(".swf") !=  - 1) {
	    if (o.LinkUrl) {
        if (o.CountClick) o.LinkUrl = o.AdRoot + "/go.php?type=click&adid=" + o.ADID ;
      }

      if(o.LinkUrl && o.FlashWmode){
        str ="<div style='POSITION:relative;left:0;top:0;Z-INDEX:2;width:" + o.ImgWidth + "px;height:"+ o.ImgHeight +"px'>";
      }
      str += "<object classid='clsid:D27CDB6E-AE6D-11cf-96B8-444553540000' codebase='http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,0,0'";
      str += " name='AD_" + o.ADID + "' id='AD_" + o.ADID + "'";
      str += " width='" + o.ImgWidth + "'";
      str += " height='" + o.ImgHeight + "'";
      if (o.style) str += " style='" + o.style + "'";
      if (o.extfunc) str += " " + o.extfunc + " ";
      str += ">";
      str += "<param name='movie' value='" + o.ImgUrl + "'>";
      str += "<param name='allowScriptAccess' value='always' />";
      //if (o.FlashWmode == 1) 
      str += "<param name='wmode' value='transparent'>";
      if (o.play) str += "<param name='play' value='" + o.play + "'>";
      if (typeof(o.loop) != "undefined") str += "<param name='loop' value='" + o.loop + "'>";
      str += "<param name='quality' value='autohigh'>";
      str += "<embed ";
      str += " name='AD_" + o.ADID + "' id='AD_" + o.ADID + "'";
      str += " width='" + o.ImgWidth + "'";
      str += " height='" + o.ImgHeight + "'";
      if (o.style) str += " style='" + o.style + "'";
      if (o.extfunc) str += " " + o.extfunc + " ";
      str += " src='" + o.ImgUrl + "'";
      //if (o.FlashWmode == 1) 
      str += " wmode='transparent'";
      if (o.play) str += " play='" + o.play + "'";
      if (typeof(o.loop) != "undefined") str += " loop='" + o.loop + "'";
      str += " quality='autohigh'";
      str += " allowScriptAccess='always'";
      str += " pluginspage='http://www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash' type='application/x-shockwave-flash'></embed>";
      str += "</object>";
      if(o.LinkUrl && o.FlashWmode){
        //str += "<div style='background-color:yellow;POSITION:absolute;left:0;top:0;Z-INDEX:3;width:"+ o.ImgWidth +"px;height:"+ o.ImgHeight +"px'><OBJECT classid='clsid:D27CDB6E-AE6D-11cf-96B8-444553540000' codebase='http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,0,0' ID='button"+o.ADID+"' WIDTH='"+ o.ImgWidth +"' HEIGHT='"+ o.ImgHeight +"'><PARAM NAME='movie' VALUE='"+ o.AdRoot +"/blank.swf'><PARAM NAME='Wmode' VALUE='Transparent'><EMBED src='"+ o.AdRoot +"/blank.swf' WMODE='Transparent' WIDTH='"+ o.ImgWidth +"' HEIGHT='"+ o.ImgHeight +"' TYPE='application/x-shockwave-flash' name='button"+o.ADID+"'></EMBED></OBJECT></div>";
        var target_str="";
        if(o.LinkTarget==1) target_str="target=_blank";
        str += "<a href='"+o.LinkUrl+"'"+target_str+" title='"+o.LinkAlt+"' style='display:inline-block;opacity:0;filter:alpha(opacity=0);background:red;POSITION:absolute;left:0;top:0;Z-INDEX:3;width:"+ o.ImgWidth +"px;height:"+ o.ImgHeight +"px'></a>";
        str += "</div>";
        //str += "<SCR"+"IPT LANGUAGE='VBScript'>\nSub button"+ o.ADID +"_FSCommand(ByVal Command,ByVal args)\n Call button"+ o.ADID +"_DoFSCommand(command,args)\n End Sub\n</SCR"+"IPT>";
        str += "<SCR"+"IPT LANGUAGE='JavaScript'>function button"+ o.ADID +"_DoFSCommand(command,args){window.open('"+o.LinkUrl+"');}</SCR"+"IPT>";
      }
    } else if (tmpurl.indexOf(".gif") !=  - 1 || tmpurl.indexOf(".jpg") !=  - 1 || tmpurl.indexOf(".jpeg") !=  - 1 || tmpurl.indexOf(".bmp") !=  - 1 || tmpurl.indexOf(".png") !=  - 1) {
      if (o.LinkUrl) {
        if (o.CountClick) o.LinkUrl = o.AdRoot + "/go.php?type=click&adid=" + o.ADID
        str += "<a href='" + o.LinkUrl + "' target='" + ((o.LinkTarget == 0) ? "_self" : "_blank") + "' title='" + o.LinkAlt + "'>";
      }
      str += "<img ";
      str += " name='AD_" + o.ADID + "' id='AD_" + o.ADID + "'";
      if (o.style) str += " style='" + o.style + "'";
      if (o.extfunc) str += " " + o.extfunc + " ";
      str += " src='" + o.ImgUrl + "'";
      if (o.ImgWidth) str += " width='" + o.ImgWidth + "'";
      if (o.ImgHeight) str += " height='" + o.ImgHeight + "'";
      str += " border='0'>";
      if (o.LinkUrl) str += "</a>";
    }
  } else if (o.ADType == 3 || o.ADType == 4) {
    str = o.ADIntro
  } else if (o.ADType == 5) {
    str = "<iframe id='" + "AD_" + o.ADID + "' marginwidth=0 marginheight=0 hspace=0 vspace=0 frameborder=0 scrolling=no width=100% height=100% src='" + o.ADIntro + "'>wait</iframe>";
  }

  return str;
}


	    //广告位初始化

	    var AdZone_106 = new BannerZone("AdZone_106");
	    AdZone_106.ZoneID      = 106;
	    AdZone_106.ZoneWidth   = 300;
	    AdZone_106.ZoneHeight  = 180;
	    AdZone_106.ShowType    = 4;

	//当前时间戳
  var timestamp_cur=new Date().getTime();
  //广告初始化

var objAD_1012 = new AdObj();
      		objAD_1012.ADID           = 1012;  //广告ID
      		objAD_1012.ADType         = 1;  //广告类型
      		objAD_1012.ADName         = "第十届中国杭州纤维素纤维（粘胶）产业链论坛_copy";  //广告名称
      		objAD_1012.ImgUrl         = "/ggimg/201602/20160216040446.jpg";    //图片路径
      		objAD_1012.ImgWidth       = 300;    //图片宽度
      		objAD_1012.ImgHeight      = 180;    //图片高度
      		objAD_1012.FlashWmode     = 0;    //flash是否透明
      		objAD_1012.ADIntro        = " "; //文本或代码广告
      		objAD_1012.LinkUrl        = "http://viscose.ccf.com.cn/2016/";    //链接指向
      		objAD_1012.LinkTarget     = "1";    //target
      		objAD_1012.LinkAlt        = "第十届中国杭州 纤维素纤维（粘胶）产业链论坛";   //alt
      		objAD_1012.Delaytime       = 10;    //时间
      		objAD_1012.Priority       = 1;    //权重
      		objAD_1012.CountView      = 1;   //统计显示
      		objAD_1012.CountClick     = 1;   //统计点击
      		objAD_1012.AdRoot     = "http://www.ccf.com.cn/gg";     //广告目录
      		AdZone_106.AddAD(objAD_1012);



//一次刷新页面 循环一周 只是第一个循环展示次数加一(展示到的图片才加一) 用于控制第一次的变量
		var loopNum=0;

		AdZone_106.Show(); 