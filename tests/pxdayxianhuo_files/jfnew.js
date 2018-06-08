simptext='<a href="javascript:void(0);" onClick="Switchj_Time();" title="这是简体"><span>简体</span></a>';
twtext='<a href="javascript:void(0);" onClick="Switchf_Time();" title="這是繁體"><span>繁體</span></a>';
window.onload=BodyLoad;//为网页加载注册一个事件
function BodyLoad(){
	if(getCookie("wwwccfcom")=="ft")
	{
	Switchf_Time();
	}
}

function Switchf_Time(){
setTimeout("Switchf_1()",50);
setCookie("wwwccfcom","ft");
}

function Switchj_Time()
{
setTimeout("Switchj_1()",50);
setCookie("wwwccfcom","del"); //改写值为删除
}

function Switchf_1()
	
{
	document.getElementById("switch").innerHTML=simptext;
	window.document.title=SwitchBig(window.document.title);
	
	Switchf(document.body,document.getElementsByTagName("img"));
	if(IsIframe){
   		Switchf_iframe()
   		}
   		
}


function Switchj_1()
{
document.getElementById("switch").innerHTML=twtext;
window.document.title=SwitchGb(window.document.title);
Switchj(document.body,document.getElementsByTagName("img"));
if(IsIframe)
{
   Switchj_iframe()
}
}

function Switchf(obj,str)
{

   SwitchTxtf(obj);  
   SwitchImgf(str);
  
}
function Switchj(obj,str)
{ 

   SwitchTxtj(obj);   
   SwitchImgj(str);
}
//-------------增加了对框架页的转换--------------
function IsIframe()
{
	if(document.frames.length>0)
	{
	   return true;
	}
	else{
	   return false;
	}
}

function Switchf_iframe()
{
var num=document.frames.length;
for(var i=1;i<num;i++)
{
   var obj=document.frames[i];
   Switchf(obj.document.body,obj.document.getElementsByTagName("img"));  
}
}
function Switchj_iframe()
{
var num=document.frames.length;
for(var i=1;i<num;i++)
{
   var obj=document.frames[i];
   Switchj(obj.document.body,obj.document.getElementsByTagName("img"));  
}
}

//------------下面是转换函数------------------------
function SwitchTxtf(fobj) 
{
	if(typeof(fobj)=="object"){var obj=fobj.childNodes}
	else
	{
  	 return; 
	}
	for(var i=0;i<obj.length;i++) 
	{
	   var aa=obj[i];
	   //if(aa.tagName=="TEXTAREA")continue;
	   //if(aa.tagName=="SELECT")continue;
	
	   if(aa.title!=""&&aa.title!=null)aa.title=SwitchBig(aa.title);
	   if(aa.alt!=""&&aa.alt!=null)aa.alt=SwitchBig(aa.alt);
	   
	   
	   /* 这段转换Input里面的值 还是不转了
	   对于不想转换的块设置一个过滤name值obj.childNodes[0].name||obj.childNodes[0].id
	   if(aa.tagName=="INPUT"&&aa.value!=""&&aa.type!="hidden")
	   {
	    aa.value=SwitchBig(aa.value); 
	   }
	   */
	   if(aa.nodeType==3) //这是转换文本的值 
	   {
	    aa.nodeValue=SwitchBig(aa.nodeValue); 
	   }
	   else
	   {
	    SwitchTxtf(aa);  
	   }
	}
}
function SwitchImgf(str) 
{
var Imgobj=str; 
var objRegexp=/gb2312/; 
for(var i=0;i<Imgobj.length;i++)
{
   var gg=Imgobj[i].getAttributeNode("src").nodeValue;
   if(objRegexp.test(gg))  
   {
    Imgobj[i].getAttributeNode("src").nodeValue=gg.replace("gb2312","big5");
   } 
}

}

function SwitchTxtj(fobj) 
{
if(typeof(fobj)=="object"){var obj=fobj.childNodes}
else
{
   return; 
}
for(var i=0;i<obj.length;i++) 
{
   var aa=obj[i];
   if(aa.tagName=="TEXTAREA")continue;
   if(aa.title!=""&&aa.title!=null)aa.title=SwitchGb(aa.title);
   if(aa.alt!=""&&aa.alt!=null)aa.alt=SwitchGb(aa.alt);
   if(aa.tagName=="INPUT"&&aa.value!=""&&aa.type!="hidden")
   {
    aa.value=SwitchGb(aa.value); 
   }
   if(aa.nodeType==3)  
   {
    aa.nodeValue=SwitchGb(aa.nodeValue); 
   }
   else
   {
    SwitchTxtj(aa);  
   }
}
}
function SwitchImgj(str) 
{
var Imgobj=str; 
var objRegexp=/big5/;
for(var i=0;i<Imgobj.length;i++)
{
   var gg=Imgobj[i].getAttributeNode("src").nodeValue;
   if(objRegexp.test(gg))  
   {
    Imgobj[i].getAttributeNode("src").nodeValue=gg.replace("big5","gb2312");
   } 
}

}

function SwitchBig(strGb)  
{


var strBig=""; 
var ss=JTPYStr();
var tt=FTPYStr(); 
for(var i=0;i<strGb.length;i++)
{
   if(strGb.charCodeAt(i)>10000&&ss.indexOf(strGb.charAt(i))!=-1)
    { 
      strBig+=tt.charAt(ss.indexOf(strGb.charAt(i)));
    }
   else
    {
     strBig+=strGb.charAt(i); 
    }
}
return strBig; 
}

function SwitchGb(strBig)  
{
var strGb=""; 
var ss=JTPYStr();
var tt=FTPYStr();
for(var i=0;i<strBig.length;i++)
{
   if(strBig.charCodeAt(i)>10000&&tt.indexOf(strBig.charAt(i))!=-1)
    { 
      strGb+=ss.charAt(tt.indexOf(strBig.charAt(i)));//开始转换 
    }
   else
    {
     strGb+=strBig.charAt(i); //否则不予以转换
    }
}
return strGb;  
}


//-------------下面是简繁体对照表---------------------------
function JTPYStr()
{return '皑蔼碍爱翱袄奥坝罢摆败颁办绊帮绑镑谤剥饱宝报鲍辈贝钡狈备惫绷笔毕毙闭边编贬变辩辫鳖瘪濒滨宾摈饼拨钵铂驳卜补参蚕残惭惨灿苍舱仓沧厕侧册测层诧搀掺蝉馋谗缠铲产阐颤场尝长偿肠厂畅钞车彻尘陈衬撑称惩诚骋痴迟驰耻齿炽冲虫宠畴踌筹绸丑橱厨锄雏础储触处传疮闯创锤纯绰辞词赐聪葱囱从丛凑窜错达带贷担单郸掸胆惮诞弹当挡党荡档捣岛祷导盗灯邓敌涤递缔点垫电淀钓调迭谍叠钉顶锭订东动栋冻斗犊独读赌镀锻断缎兑队对吨顿钝夺鹅额讹恶饿儿尔饵贰发罚阀珐矾钒烦范贩饭访纺飞废费纷坟奋愤粪丰枫锋风疯冯缝讽凤肤辐抚辅赋复负讣妇缚该钙盖干赶秆赣冈刚钢纲岗皋镐搁鸽阁铬个给龚宫巩贡钩沟构购够蛊顾剐关观馆惯贯广规硅归龟闺轨诡柜贵刽辊滚锅国过骇韩汉阂鹤贺横轰鸿红后壶护沪户哗华画划话怀坏欢环还缓换唤痪焕涣黄谎挥辉毁贿秽会烩汇讳诲绘荤浑伙获货祸击机积饥讥鸡绩缉极辑级挤几蓟剂济计记际继纪夹荚颊贾钾价驾歼监坚笺间艰缄茧检碱硷拣捡简俭减荐槛鉴践贱见键舰剑饯渐溅涧浆蒋桨奖讲酱胶浇骄娇搅铰矫侥脚饺缴绞轿较秸阶节茎惊经颈静镜径痉竞净纠厩旧驹举据锯惧剧鹃绢杰洁结诫届紧锦仅谨进晋烬尽劲荆觉决诀绝钧军骏开凯颗壳课垦恳抠库裤夸块侩宽矿旷况亏岿窥馈溃扩阔蜡腊莱来赖蓝栏拦篮阑兰澜谰揽览懒缆烂滥捞劳涝乐镭垒类泪篱离里鲤礼丽厉励砾历沥隶俩联莲连镰怜涟帘敛脸链恋炼练粮凉两辆谅疗辽镣猎临邻鳞凛赁龄铃凌灵岭领馏刘龙聋咙笼垄拢陇楼娄搂篓芦卢颅庐炉掳卤虏鲁赂禄录陆驴吕铝侣屡缕虑滤绿峦挛孪滦乱抡轮伦仑沦纶论萝罗逻锣箩骡骆络妈玛码蚂马骂吗买麦卖迈脉瞒馒蛮满谩猫锚铆贸么霉没镁门闷们锰梦谜弥觅绵缅庙灭悯闽鸣铭谬谋亩钠纳难挠脑恼闹馁腻撵捻酿鸟聂啮镊镍柠狞宁拧泞钮纽脓浓农疟诺欧鸥殴呕沤盘庞国爱赔喷鹏骗飘频贫苹凭评泼颇扑铺朴谱脐齐骑岂启气弃讫牵扦钎铅迁签谦钱钳潜浅谴堑枪呛墙蔷强抢锹桥乔侨翘窍窃钦亲轻氢倾顷请庆琼穷趋区躯驱龋颧权劝却鹊让饶扰绕热韧认纫荣绒软锐闰润洒萨鳃赛伞丧骚扫涩杀纱筛晒闪陕赡缮伤赏烧绍赊摄慑设绅审婶肾渗声绳胜圣师狮湿诗尸时蚀实识驶势释饰视试寿兽枢输书赎属术树竖数帅双谁税顺说硕烁丝饲耸怂颂讼诵擞苏诉肃虽绥岁孙损笋缩琐锁獭挞抬摊贪瘫滩坛谭谈叹汤烫涛绦腾誊锑题体屉条贴铁厅听烃铜统头图涂团颓蜕脱鸵驮驼椭洼袜弯湾顽万网韦违围为潍维苇伟伪纬谓卫温闻纹稳问瓮挝蜗涡窝呜钨乌诬无芜吴坞雾务误锡牺袭习铣戏细虾辖峡侠狭厦锨鲜纤咸贤衔闲显险现献县馅羡宪线厢镶乡详响项萧销晓啸蝎协挟携胁谐写泻谢锌衅兴汹锈绣虚嘘须许绪续轩悬选癣绚学勋询寻驯训讯逊压鸦鸭哑亚讶阉烟盐严颜阎艳厌砚彦谚验鸯杨扬疡阳痒养样瑶摇尧遥窑谣药爷页业叶医铱颐遗仪彝蚁艺亿忆义诣议谊译异绎荫阴银饮樱婴鹰应缨莹萤营荧蝇颖哟拥佣痈踊咏涌优忧邮铀犹游诱舆鱼渔娱与屿语吁御狱誉预驭鸳渊辕园员圆缘远愿约跃钥岳粤悦阅云郧匀陨运蕴酝晕韵杂灾载攒暂赞赃脏凿枣灶责择则泽贼赠扎札轧铡闸诈斋债毡盏斩辗崭栈战绽张涨帐账胀赵蛰辙锗这贞针侦诊镇阵挣睁狰帧郑证织职执纸挚掷帜质钟终种肿众诌轴皱昼骤猪诸诛烛瞩嘱贮铸筑驻专砖转赚桩庄装妆壮状锥赘坠缀谆浊兹资渍踪综总纵邹诅组钻致钟么为只凶准启板里雳余链泄';
}
function FTPYStr()
{return '皚藹礙愛翺襖奧壩罷擺敗頒辦絆幫綁鎊謗剝飽寶報鮑輩貝鋇狽備憊繃筆畢斃閉邊編貶變辯辮鼈癟瀕濱賓擯餅撥缽鉑駁蔔補參蠶殘慚慘燦蒼艙倉滄廁側冊測層詫攙摻蟬饞讒纏鏟産闡顫場嘗長償腸廠暢鈔車徹塵陳襯撐稱懲誠騁癡遲馳恥齒熾沖蟲寵疇躊籌綢醜櫥廚鋤雛礎儲觸處傳瘡闖創錘純綽辭詞賜聰蔥囪從叢湊竄錯達帶貸擔單鄲撣膽憚誕彈當擋黨蕩檔搗島禱導盜燈鄧敵滌遞締點墊電澱釣調叠諜疊釘頂錠訂東動棟凍鬥犢獨讀賭鍍鍛斷緞兌隊對噸頓鈍奪鵝額訛惡餓兒爾餌貳發罰閥琺礬釩煩範販飯訪紡飛廢費紛墳奮憤糞豐楓鋒風瘋馮縫諷鳳膚輻撫輔賦複負訃婦縛該鈣蓋幹趕稈贛岡剛鋼綱崗臯鎬擱鴿閣鉻個給龔宮鞏貢鈎溝構購夠蠱顧剮關觀館慣貫廣規矽歸龜閨軌詭櫃貴劊輥滾鍋國過駭韓漢閡鶴賀橫轟鴻紅後壺護滬戶嘩華畫劃話懷壞歡環還緩換喚瘓煥渙黃謊揮輝毀賄穢會燴彙諱誨繪葷渾夥獲貨禍擊機積饑譏雞績緝極輯級擠幾薊劑濟計記際繼紀夾莢頰賈鉀價駕殲監堅箋間艱緘繭檢堿鹼揀撿簡儉減薦檻鑒踐賤見鍵艦劍餞漸濺澗漿蔣槳獎講醬膠澆驕嬌攪鉸矯僥腳餃繳絞轎較稭階節莖驚經頸靜鏡徑痙競淨糾廄舊駒舉據鋸懼劇鵑絹傑潔結誡屆緊錦僅謹進晉燼盡勁荊覺決訣絕鈞軍駿開凱顆殼課墾懇摳庫褲誇塊儈寬礦曠況虧巋窺饋潰擴闊蠟臘萊來賴藍欄攔籃闌蘭瀾讕攬覽懶纜爛濫撈勞澇樂鐳壘類淚籬離裏鯉禮麗厲勵礫曆瀝隸倆聯蓮連鐮憐漣簾斂臉鏈戀煉練糧涼兩輛諒療遼鐐獵臨鄰鱗凜賃齡鈴淩靈嶺領餾劉龍聾嚨籠壟攏隴樓婁摟簍蘆盧顱廬爐擄鹵虜魯賂祿錄陸驢呂鋁侶屢縷慮濾綠巒攣孿灤亂掄輪倫侖淪綸論蘿羅邏鑼籮騾駱絡媽瑪碼螞馬罵嗎買麥賣邁脈瞞饅蠻滿謾貓錨鉚貿麽黴沒鎂門悶們錳夢謎彌覓綿緬廟滅憫閩鳴銘謬謀畝鈉納難撓腦惱鬧餒膩攆撚釀鳥聶齧鑷鎳檸獰甯擰濘鈕紐膿濃農瘧諾歐鷗毆嘔漚盤龐國愛賠噴鵬騙飄頻貧蘋憑評潑頗撲鋪樸譜臍齊騎豈啓氣棄訖牽扡釺鉛遷簽謙錢鉗潛淺譴塹槍嗆牆薔強搶鍬橋喬僑翹竅竊欽親輕氫傾頃請慶瓊窮趨區軀驅齲顴權勸卻鵲讓饒擾繞熱韌認紉榮絨軟銳閏潤灑薩鰓賽傘喪騷掃澀殺紗篩曬閃陝贍繕傷賞燒紹賒攝懾設紳審嬸腎滲聲繩勝聖師獅濕詩屍時蝕實識駛勢釋飾視試壽獸樞輸書贖屬術樹豎數帥雙誰稅順說碩爍絲飼聳慫頌訟誦擻蘇訴肅雖綏歲孫損筍縮瑣鎖獺撻擡攤貪癱灘壇譚談歎湯燙濤縧騰謄銻題體屜條貼鐵廳聽烴銅統頭圖塗團頹蛻脫鴕馱駝橢窪襪彎灣頑萬網韋違圍爲濰維葦偉僞緯謂衛溫聞紋穩問甕撾蝸渦窩嗚鎢烏誣無蕪吳塢霧務誤錫犧襲習銑戲細蝦轄峽俠狹廈鍁鮮纖鹹賢銜閑顯險現獻縣餡羨憲線廂鑲鄉詳響項蕭銷曉嘯蠍協挾攜脅諧寫瀉謝鋅釁興洶鏽繡虛噓須許緒續軒懸選癬絢學勳詢尋馴訓訊遜壓鴉鴨啞亞訝閹煙鹽嚴顔閻豔厭硯彥諺驗鴦楊揚瘍陽癢養樣瑤搖堯遙窯謠藥爺頁業葉醫銥頤遺儀彜蟻藝億憶義詣議誼譯異繹蔭陰銀飲櫻嬰鷹應纓瑩螢營熒蠅穎喲擁傭癰踴詠湧優憂郵鈾猶遊誘輿魚漁娛與嶼語籲禦獄譽預馭鴛淵轅園員圓緣遠願約躍鑰嶽粵悅閱雲鄖勻隕運蘊醞暈韻雜災載攢暫贊贓髒鑿棗竈責擇則澤賊贈紮劄軋鍘閘詐齋債氈盞斬輾嶄棧戰綻張漲帳賬脹趙蟄轍鍺這貞針偵診鎮陣掙睜猙幀鄭證織職執紙摯擲幟質鍾終種腫衆謅軸皺晝驟豬諸誅燭矚囑貯鑄築駐專磚轉賺樁莊裝妝壯狀錐贅墜綴諄濁茲資漬蹤綜總縱鄒詛組鑽緻鐘麼為隻兇準啟闆裡靂餘鍊洩';
}
//-------------------Cookie操作---------------------------------------
function setCookie(name, value,expires,Cookie_path)//写Cookie
{
   if((typeof expires)=="undefined")
   {
    var expires_data=1; 
   }
   else
   { if(expires==null)
    {
     var expires_data=1;
    }else
    {
     if(expires<0)
     {
      var expires_data=0;//负数时,页面立即过期
     }
     else
     {
      var expires_data=expires;
     }
    }
   }
   var data = new Date ();
   data.setTime(data.getTime() + (expires_data*1000*3600*24));
   var expires_str = ";expires=" + data.toUTCString(); 
  
   if((typeof Cookie_path)=="undefined")
   {
    Cookie_path="/";  
   }
   else if(Cookie_path==null)
   {
    Cookie_path="/";
   }
   var Cookie_path_str=";path=" + Cookie_path;  

document.cookie = name + "=" +escape(value)+expires_str+Cookie_path_str;

}

function getCookie(name)   //读取Cookie值
{  
     var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");
         if(arr=document.cookie.match(reg)) return unescape(arr[2]);
         else return null;
}

function delCookie(name)   //让Cookie   过期
{
     var data = new Date();
         data.setTime(data.getTime() - 1);
     var cval=getCookie(name);
         if(cval!=null) document.cookie= name + "="+escape(cval)+";expires="+data.toGMTString();
}




if(getCookie("wwwccfcom")=="ft"){
var _alert = window.alert; 
window.alert = function(s) {
  _alert(SwitchBig(s)); 
}
var _confirm = window.confirm;
window.confirm = function(s) { 
  _confirm(SwitchBig(s)); 
} 
var _prompt = window.prompt; 
window.prompt = function(s,i){ 
  _prompt( SwitchBig(s) ,SwitchBig(i));
}
}