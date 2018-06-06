#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: clawer_test.py
@time: 2018/6/1 13:50
@desc:
'''

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    html_doc = """
    <!DOCTYPE html>
<html><head>
    <meta content="jVXZ05o5vR" name="baidu-site-verification"/>
    <title>
微步在线 | 威胁情报分析平台-ThreatBook-多引擎在线扫描、恶意软件在线检测
</title>
    <!-- <meta charset="utf-8"> -->
    <meta charset="utf-8"/>
    <meta content="text/html; charset=utf-8" http-equiv="Content-type"/>
    <meta content="no-cache" http-equiv="Pragma"/>
    <meta content="no-store" http-equiv="Pragma"/>
    <meta content="-1" http-equiv="Expires"/>
    <meta x-ms-format-detection="none"/>
    <meta content="telephone=no" name="format-detection"/>
    <meta content="微步,微步在线,北京微步,免费杀毒,在线查毒,云查杀, 多引擎在线杀毒,在线扫描,病毒扫描,威胁检测,威胁分析,安全分析,安全分析师,大数据,APT,威胁情报,MRTI,开源威胁情报,OSINT,溯源分析,事件响应,VirusTotal,VirScan,恶意软件,查杀木马,企业杀毒,沙箱,间谍软件,在线病毒扫描,恶意软件,扫描, 在线, 免费, 系统劫持, 木马, 特洛伊, 垃圾邮件, 杀毒软件, 小红伞, 大蜘蛛, 卡巴斯基, 熊猫卫士, 趋势, rootkit, avast, avg, bitdefender, clamav, drweb, f-secure, kaspersky, nod32,  panda antivirus,  trend micro" name="keywords"/>
    <meta content="virusbook提供免费多引擎在线扫描服务,免费病毒扫描结果,动态沙箱结果,免费安全工具,威胁情报的基础数据提供" name="description"/>
    <meta content="webkit" name="renderer"/>
    <meta content="IE=edge,Chrome=1" http-equiv="X-UA-Compatible"/>
    <meta content="date=no" name="format-detection"/>
    <meta content="address=no" name="format-detection"/>
    <meta content="telephone=no" name="format-detection"/>
    <meta content="ip=no" name="format-detection"/>
    <!-- <meta name="viewport" content="width=device-width, initial-scale=1"> -->
    <meta content="initial-scale=1.0,user-scalable=no" name="viewport"/>
    <link href="/static/css/bootstrap.min.css" media="screen" rel="stylesheet"/>
    <link href="/static/css/new-common.css" rel="stylesheet" type="text/css"/>
    <link href="/static/css/new-custom.css" rel="stylesheet" type="text/css"/>
    <link href="/static/css/new-form.css" rel="stylesheet" type="text/css"/>
    <link href="/static/css/loading.css" media="screen" rel="stylesheet"/>
    <link href="/static/css/new-common-body.css" rel="stylesheet" type="text/css"/>
    <!--[if IE 8 ]>
    <link rel="stylesheet" type="text/css" href="/static/css/ie8.css" />
    <![endif]-->

<link href="/static/css/vote.css" rel="stylesheet" type="text/css"/>
<link href="/static/css/jquery.qtip.css" rel="stylesheet" type="text/css"/>
<style type="text/css">
    #share_domain_table td {
        width: 50%;
    }

    #his_domain_table tbody td:first-child {
        width: 120px;
    }
</style>

    <!--[if lt IE 9]>
    <script src="/static/js/respond.min.js"></script>
    <script src="/static/js/html5shiv.min.js"></script>
    <![endif]-->
    <script charset="utf-8" src="/static/js/jquery.min.js" type="text/javascript"></script>
    <script charset="utf-8" src="/static/js/bootstrap.min.js" type="text/javascript"></script>

    <script charset="utf-8" src="/static/js/jquery.cookie.js" type="text/javascript"></script>
    <script charset="utf-8" src="/static/js/lang.js" type="text/javascript"></script>
    <script charset="utf-8" src="/static/js/ajaxfileupload.js" type="text/javascript"></script>
    <script charset="utf-8" src="/static/js/base.js" type="text/javascript"></script>
    <script charset="utf-8" src="/static/js/strings.js" type="text/javascript"></script>
    <script charset="utf-8" src="/static/js/action.js" type="text/javascript"></script>
    <script charset="utf-8" src="/static/js/main.js" type="text/javascript"></script>
    <script charset="utf-8" src="/static/js/common.js" type="text/javascript"></script>

    <script src="/static/js/moment.js" type="text/javascript"></script>
    <script charset="utf-8" src="/static/js/dragEvent.js" type="text/javascript"></script>
    <script type="text/javascript">
        function triggerLoading() {
            //check is null
            var val = $("#q").val()
            if (val == "") {
                return false
            } else {
                var screenHeight = window.screen.availHeight
                var screenWidth = window.screen.availWidth
                var innerHeight = window.innerHeight
                var innerWidth = window.innerWidth
                if (isIE("9.0")) {
                    $("#loading_conflict").css({
                        "top": innerHeight / 2 - 50,
                        "left": innerWidth / 2 - 50
                    })
                    $("#modal_loading_conflict").modal()
                } else if (isIE("8.0")) {
                    $("#loading_conflict").css({
                        "top": screenHeight / 2 - 50,
                        "left": screenWidth / 2 - 50
                    })
                    $("#modal_loading_conflict").modal()
                } else {
                    //loading
                    $("#load").css({
                        "top": innerHeight / 2,
                        "left": innerWidth / 2
                    })
                    $('#modal_loading main').removeClass("hidden")
                    $('#modal_loading').modal("show")
                }
            }
        }

        function IsPC() {
            var userAgentInfo = navigator.userAgent;
            var Agents = ["Android", "iPhone",
                "SymbianOS", "Windows Phone",
                "iPad", "iPod"
            ];
            var flag = true;
            for (var v = 0; v < Agents.length; v++) {
                if (userAgentInfo.indexOf(Agents[v]) > 0) {
                    flag = false;
                    break;
                }
            }
            return flag;
        }


        function openLoginDlg() {
            showDlg("/login", function() {
                var ForThirdPartUserBindType  = localStorage.getItem("oauth_bind_type");
                localStorage.removeItem("oauth_bind_type");
                if (ForThirdPartUserBindType == "register") {
                    $("#tag-a-login").removeClass("active");
                    $("#tag-a-register").addClass("active");
                    $(".js-login").addClass("hidden");
                    $(".js-register").removeClass("hidden");
                    showRecaptchaImageTo('Register');
                } else {
                    $("#tag-a-login").addClass("active");
                    $("#tag-a-register").removeClass("active");
                    $(".js-login").removeClass("hidden");
                    $(".js-register").addClass("hidden");
                    showRecaptchaImageTo('Login');
                }
                console.log("next: " + _loginRedirectURL);
                if (_loginRedirectURL) {
                    next_url = _loginRedirectURL;
                }
            });
        }
        function openRegisterDlg() {
            showDlg("/login", function() {
                $("#tag-a-login").removeClass("active");
                $("#tag-a-register").addClass("active");
                $(".js-login").addClass("hidden");
                $(".js-register").removeClass("hidden");
                showRecaptchaImageTo('Register');
                console.log("next: " + _loginRedirectURL);
                if (_loginRedirectURL) {
                    next_url = _loginRedirectURL;
                }
            });

        }
        // function openRegDlg() {
        //     showDlg("/registration", function() {});
        // }

        function openVoteDlg(ipDomainHash) {
                            openVoteDlg4Login(ipDomainHash, false, "请登录后再进行本操作！");
                }

        // function setLangWhenLoad() {
        //   $(".lang").html(getLang() == "zh" ? "English" : "中文");
        // }

        function dealLoginEffect(img, src) {
            $(img).attr("src", src)
        }
        function dealHoverEffect($img, srcIn, srcOut) {
            $img.mousemove(function() {
                $(this).attr("src", srcIn)
            }).mouseleave(function() {
                $(this).attr("src", srcOut)
            })
        }

        function resetFileInput(id) {
            var $el = $(id);
            $el.wrap('<form>').closest('form').get(0).reset();
            $el.unwrap();
        }
        var _loginRedirectURL = "";
        function checkQuery() {
            if ($("#q").val() == "") {
                searchAlert("请输入要搜索的内容！");
                return false;
            }
            return true;
        }

        function resetFileInput(id) {
            var $el = $(id);
            $el.wrap('<form>').closest('form').get(0).reset();
            $el.unwrap();
        }

        var uploadDlgHtml = "";

        function saveUploadDlgHtml() {
            uploadDlgHtml = $("#upload_progress_dialog").html();
        }

        function restoreUploadDlgHtml() {
            $("#upload_progress_dialog").html(uploadDlgHtml);
        }
        function saveVoteResultCallback(result) {
            if (result)
            {
                alertModal("情报保存成功，等待审核。感谢您的参与！",1);
            }
            else
            {
                alertModal("情报保存失败！",0);
            }
            loadVoteSummary();
        }
        
        function addNickname(){
            /*debugger*/
            var name = $("#nickname").val()
            var res = /[0-9a-zA-Z\u4e00-\u9fa5\-_\|]{2,9}/.test(name)
            if (res) {
                //
                $.post('/setUserNickName',{nickName:name},function(data){
                    var res = JSON.parse(data)
                    if (res.response_code == 0) {
                        //success
                        $("#add_nickname").modal('hide')
                        // $this.text("提交")
                        $(".info-tip").html("提交成功")
                        $(".info-img").removeClass("error").addClass("success")
                        $("#intelli_info").html("昵称保存成功,请重新提交内容")
                        $("#common-modal").modal('show')
                        setTimeout(function(){$("#common-modal").modal('hide')},3000)
                        // submitUserIntelli()
                    } else if (res.response_code == -4) {
                        //nickname exists
                        $(".nick-error").text("该昵称已被占用")
                        $(".nick-error").removeClass("hidden")
                    } else if (res.response_code == -5) {
                        //invalid
                        $(".nick-error").text('不包含特殊字符，长度在5个汉字或10个英文字符内，可包括"-"、"_"')
                        $(".nick-error").removeClass("hidden")
                    } else if (res.response_code == -6) {
                        //contain sensitive
                        $(".nick-error").text("你提交的内容中包含敏感词")
                        $(".nick-error").removeClass("hidden")
                    } else {
                        //error
                        console.warn("error:addNickname")
                    }
                })
            } else {
                $(".nick-error").text('不包含特殊字符，长度在5个汉字或10个英文字符内，可包括"-"、"_"')
                $(".nick-error").removeClass("hidden")
            }

        }
    </script>
    <script type="text/javascript">
        function openNicknameDlg(){
            $("#add_nickname").modal()
        }
        function autoIframeHeight(id, parentId) {
            var oFrm = document.getElementById(id)
            var wrapIframe = document.getElementById(parentId)
            if(!oFrm || !wrapIframe){
                return
            }
            var context = oFrm.contentDocument
            var h1= Math.max(context.body.clientHeight, context.documentElement.clientHeight)
            var h2= Math.max(context.body.scrollHeight, context.documentElement.scrollHeight)
            var ifrmHeight = Math.max(h1,h2)
            oFrm.style.height = ifrmHeight + 'px'
            wrapIframe.style.minHeight = ifrmHeight + 'px'
        }

        $(function() {
            initBodyMinHeight();
            $('#addNickname').click(window.addNickname)
            var oFrm = document.getElementById('iframe_vb4');
            $(document).on('click', function () {
                autoIframeHeight('iframe_vb4', 'v4_container')
            })

            if(oFrm) {
                oFrm.onload = function(){
                    autoIframeHeight('iframe_vb4', 'v4_container')
                    window.islogin = false
                                    oFrm.contentWindow.postMessage({
                        isLoggedIn: window.islogin
                    }, '*')
                }
            }
            var time = -1;
            time = setInterval(function(){
                autoIframeHeight('iframe_vb4', 'v4_container')
            }, 1000);
            setTimeout(function() {
                if(time !== -1) {
                    clearInterval(time)
                }
            }, 100000)
            /*$('#logout').click(function(e) {
                e.preventDefault()
                oFrm.contentWindow.postMessage({
                  isLoggedIn: false
                }, '*')
                var d = {url: function() { return '/logout'; },method: 'POST'}			window.location.href = d.url()
		})*/
            /*window.addEventListener('message', function(event) {
                var origin = event.origin || event.originalEvent.origin
                console.warn(origin)
                console.warn(event.data)
                <!-- debugger -->
                <!-- if(origin.indexOf('/article')!= -1) { -->
                <!-- debugger -->
                    var shouldRefreshIfrmHeight = event.data.shouldRefreshIfrmHeight
                    var addHeight = event.data.addHeight
                    if(shouldRefreshIfrmHeight) {
                        var curHeight = parseInt(oFrm.style.height)
                        var newHeight = curHeight + addHeight
                        oFrm.style.height = newHeight + 'px'
                        $('#test').height(newHeight)
                        console.warn('refreshed')
                    }
                <!-- } -->

              <!-- if (origin.indexOf('/list')!= -1 || origin.indexOf('/launch')!= -1 || origin.indexOf('/uCenter')!= -1|| origin.indexOf('/article')!= -1) {  -->
                var shouldOpenLogin = event.data.shouldOpenLogin
                var shouldAddNickname = event.data.shouldAddNickname
                if(shouldOpenLogin) {
                    openLoginDlg()
                } else if(shouldAddNickname) {
                    openNicknameDlg()
                }
              <!-- } -->
            });*/
            $(window).on('message', function (event) {
                var origin = event.origin || event.originalEvent.origin
                console.warn(origin)
                console.warn(event.data)
                var shouldRefreshIfrmHeight = event.data.shouldRefreshIfrmHeight
                var addHeight = event.data.addHeight
                if(shouldRefreshIfrmHeight) {
                    var curHeight = parseInt(oFrm.style.height)
                    var newHeight = curHeight + addHeight
                    oFrm.style.height = newHeight + 'px'
                    $('#test').height(newHeight)
                    console.warn('refreshed')
                }
                var shouldOpenLogin = event.data.shouldOpenLogin
                var shouldAddNickname = event.data.shouldAddNickname
                if(shouldOpenLogin) {
                    openLoginDlg()
                } else if(shouldAddNickname) {
                    openNicknameDlg()
                }
            })
            window.loginurl = {url: function() { return '/login'; },method: 'POST'}.url()
            // setLangWhenLoad();

            var langCookie = getLang()
            if (langCookie == "zh") {
                $('#lang').text("中文");
            } else if (langCookie == "en") {
                $('#lang').text("English");
            } else {
                $('#lang').text("中文");
            }

            $(".list-lang a").click(function() {
                var val = $(this).attr("value");
                setLang(val);

                window.location.reload();
            });
            if (IsPC()) {
                $(".nav-new .q").attr("placeholder", "IP、域名、文件HASH(MD5/SHA1/SHA256)");
            } else {
                $(".nav-new .q").attr("placeholder", "IP、域名、文件HASH");
            }
            // initBodyMinHeight()
            var ie_version = window.browser ? window.browser['version'] : undefined
            if (ie_version !== undefined && ie_version < 10) {
                $(".soutu-drop").css({"display": "none"});
                $(".soutu-wrap").css({"height": 90});
            }
            var screenHeight = window.screen.availHeight
            var screenWidth = window.screen.availWidth
            //upload tooltip
            $("span.ipt_photo,span.vb-help-info").tooltip({
                template: '<div class="tooltip" role="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>',
                trigger: 'hover',
                placement: 'bottom'
            });
            $("span.ipt_photo").click(function() {
                $(this).tooltip('hide')
            });
            var login = $("a.login")
            login.mousemove(function() {
                dealLoginEffect($(this).find("img"), "/static/img/user.png")
            });
            login.mouseleave(function() {
                dealLoginEffect($(this).find("img"), "/static/img/visitor.png")
            });
            $(".upload-pic").change(function() {
                var path, name;
                path = $(this).val(); 
                name = path.substring(path.lastIndexOf("\\") + 1)
                $('#no_file_info').addClass("hidden");
                $(".forFile").val(name);
            });
            $("input.forFile").change(function() {
                if ($(this).val() == "") {
                    $('#no_file_info').removeClass("hidden");
                } else {
                    $('#no_file_info').addClass("hidden");
                }
            });
            $("a.soutu-close").click(function() {
                $("#form_file").addClass("hidden");
                $("#form_search").removeClass("hidden");
                $("span.placeholder").removeClass("hidden");
                return false;
            });
            $("span.ipt_photo").click(function() {
                $("#form_search").addClass("hidden");
                $("#form_file").removeClass("hidden");
                $("span.placeholder").addClass("hidden");
            });
            $(window).resize(function() {
                initBodyMinHeight();
            });
            $('.modal').on('show.bs.modal', function(e) {
                $("body").css({
                    "overflow-y": "scroll"
                });
            });
            $("a.vote-advance").mouseenter(function() {
                $("#vote_advance_img").attr("src", "/static/img/vote_advance_hover.png");
            }).mouseleave(function() {
                $("#vote_advance_img").attr("src", "/static/img/vote_advance.png");
            });
            $("#wechat_container").mouseenter(function() {
                $("#two_d_code").css({
                    "top": $(this).offset().top - 65,
                    "left": $(this).offset().left + 35
                });
                $("#two_d_code").removeClass("hidden");
            }).mouseleave(function() {
                $("#two_d_code").addClass("hidden");
            });

            resetFileInput("input#file_input");
            $("#q").focus();
            $("#q").focus(searchAlertHide);
            $('form#form_search>span>span.warn-info.search-wrong').click(function(){
                $('#q').focus();
            });
            $("#scan_file_btn").click(scanFile);
            $("input#file_input").change(selectFile);

            resetFileInput("input#file_input");
            $("a.clear").click(function() {
                $("#q").val("")
            });

            // IE single click to invoid file selection
            if (!isCookiesEnabled()) {
                alert(getString("cookie_prompt"));
            };
            $('[data-toggle=tooltip]').on('hidden.bs.tooltip', function () {
                $(this).attr("delay",0)
            });

            $('.slidebttn').hover(
                    function() {
                        var $this = $(this);
                        var $slidelem = $this.prev();
                        $slidelem.stop().animate({
                            'width': '235px'
                        }, 300);
                        $slidelem.find('span').stop(true, true).fadeIn();
                        $this.addClass('button_c');
                    },
                    function() {
                        var $this = $(this);
                        var $slidelem = $this.prev();
                        $slidelem.stop().animate({
                            'width': '0px'
                        }, 200);
                        $slidelem.find('span').stop(true, true).fadeOut();
                        $this.removeClass('button_c');
                    }
            );

            // if(isIE("8.0")){
            //   $("#ana_detect_ul").css("margin-left",25)
            // }
            saveUploadDlgHtml();
            // if ($.browser.msie) {
            //     $('input:checkbox').click(function () {
            //         this.blur();
            //         this.focus();
            //     });
            // };
        
            if ($.isSafari()) {
                //unload not func,use pagehide
                window.addEventListener("pagehide", function(){
                    $('#modal_loading').modal('hide')
                    $('#modal_loading main').addClass("hidden")
                    $("span.placeholder").css("display","block");
                }, false);
            }
        });
    </script>

    <script type="text/javascript">
        var username = "";
        var _vds = _vds || [];
        window._vds = _vds;
        (function(){
            _vds.push(['setAccountId', '93c2f45e22af239e']);
                            (function() {
                var vds = document.createElement('script');
                vds.type='text/javascript';
                vds.async = true;
                vds.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'dn-growing.qbox.me/vds.js';
                var s = document.getElementsByTagName('script')[0];
                s.parentNode.insertBefore(vds, s);
            })();
                })();
    </script>
</head>

<body class="vb" data-offset="0" data-spy="scroll" data-target="#scroll_container">
<header>
    <nav class="nav-new">
        <a class="navbar-brand" href="/" id="logo_container"><img alt="VirusBook" src="/static/img/logo_big.png"/></a>
        <div class="dropdown" style="display:inline-block;float:left;">
            <a class="chg-lang dropdown" data-toggle="dropdown">
                    <span class="lang" id="lang">
                    Language
                    </span>
                <span class="glyphicon glyphicon-triangle-bottom">
                    </span>
            </a>
            <ul class="dropdown-menu gray-border no-borderRadius vb-menu list-lang">
                <li>
                    <a class="active" href="#" value="zh">中文</a>
                </li>
                <li>
                    <a href="#" value="en">English</a>
                </li>
            </ul>
        </div>
                <div class="center-block hidden-xs hidden-sm" id="search_container">
            <form action="/query" class="form-inline" id="form_search" method="post" name="f" onsubmit="triggerLoading();return checkQuery();">
                    <span class="user-input">
                      <span class="ipt_photo" data-placement="bottom" id="upload_btn" style="display: block;" title="上传文件">
                      </span>
                      <input autocomplete="off" class="q form-control" id="q" maxlength="255" name="q" placeholder="IP、域名、文件HASH(MD5/SHA1/SHA256)" value=""/>
                      <a class="quickdelete" href="javascript:;" id="quickdelete" style="top: 0px; right: 0px; display: none;" title="清空"></a>
                      <span class="warn-info hidden search-wrong"></span>
                    </span>
                <input class="btn btn-default btn-search text-center form-control" id="ana" type="submit" value="分析"/>
            </form>
            <form action="/scan_file" class="form-inline hidden" id="form_file" name="f">
                    <span class="user-input">
                      <input autocomplete="off" class="form-control forFile" disabled="" maxlength="255" value=""/>
                      <span class="warn-info file-info hidden" id="no_file_info">您还没有上传检测文件</span>
                    </span>
                <input class="btn btn-default btn-search text-center form-control" id="scan_file_btn" type="button" value="检测"/>
                <div>
                    <div class="soutu-wrap">
                        <div class="soutu-hr">
                            <div class="soutu-drop"><span class="soutu-drop-tip">拖拽文件到这里</span><i class="soutu-icon soutu-drop-icon center-block"></i></div>
                            <div class="upload-wrap">
                                <input class="upload-pic" data-nolog="1" id="file_input" name="file" type="file" value="本地上传文件"/>
                                <span class="soutu-icon upload-icon"></span>
                                <span class="upload-text ">本地上传文件</span>
                            </div>
                            <a class="soutu-icon soutu-close pull-right" data-nolog="1" href="javascript:void(0);"></a>
                        </div>
                    </div>
                </div>
            </form>
        </div>
            <ul class="nav navbar-nav hidden-xs hidden-sm" id="idx_menu">
            <!--li><a href="/communityMainPage">情报</a></li-->
            <!--li><a href="/api" target="_blank">API</a></li-->
            <!--li><a href="/about" target="_blank">关于</a></li-->
        </ul>
        <div class="pull-right" id="nav_right">
            <div class="dropdown hidden" id="menu_container">
                <a class="menu" data-toggle="dropdown" id="more_menu">
                      <span class="glyphicon glyphicon-th">
                  </span>
                </a>
                <ul aria-labelledby="more_menu" class="dropdown-menu gray-border no-borderRadius vb-menu" id="list_menu">
                    <li>
                        <a class="active" href="/" title="首页">首页</a>
                    </li>
                    <li>
                        <a href="/guide" title="向导">向导</a>
                    </li>
                    <li>
                        <a href="/user/rightsInterests" title="权益">权益</a>
                    </li>
                    <li>
                        <a href="/api" title="API">API</a>
                    </li>
                    <li>
                        <a href="/about" title="关于">关于</a>
                    </li>
                                    <li class="hidden-md hidden-lg">
                        <a href="javascript:openLoginDlg();" id="login" title="登录">登录</a>
                    </li>
                    <li class="hidden-md hidden-lg">
                        <a href="/user/register" target="_blank">注册</a>
                    </li>
                                 </ul>
            </div>
            <div class="hidden-xs hidden-sm" id="user_container">
                            <a class="btn login" href="javascript:openLoginDlg();" id="login" title="登录"><img class="pull-left" src="/static/img/visitor.png"/>登录</a>
                <a class="hook hook-reg btn btn-default reg" href="javascript:openRegisterDlg();" id="register">注册</a>
                                    </div>
        </div>
    </nav>
</header>

﻿




<script>
    function showIpTab() {
        $('#tabs a[href="#ip"]').tab('show');
    }

    var nodes_4;
    var edges_4;

    $(function () {
        $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
            //console.log(e.target.href);
            if (e.target.href.indexOf("#chart") >= 0) {
                //console.log("chart");
                buildChart();
            }
        });

        var href = window.location.hash;
        if (href === "#community_put") {
            $("#tabs li").removeClass("active");
            $("div .tab-pane").removeClass("active");
            $('#intell_community_tab').addClass("active");
            $("#intell_community").addClass("active");
        }

    });

    var chartBuilt = false;
    function buildChart() {
        if (chartBuilt) {
            console.log("The chart has already been built.");
            return;
        }

        chartBuilt = true;

        var nodes = [
        
            {
                data: {
                    id: '80.82.78.50',
                    name: '80.82.78.50',
                    type: 'IP',
                }
            },
        
        ];

        var edges = [
        
        ];

        if (nodes_4) {
            console.log("nodes_4 length:" + nodes_4.length);
            console.log("before add:" + nodes.length);

            $.merge(nodes, nodes_4);

            console.log("after add:" + nodes.length);
        }

        if (edges_4) {
            $.merge(edges, edges_4);
        }

        var data = {root: '80.82.78.50', nodes: nodes, edges: edges};

        var tags = [
        
            
        
        ];

        createGraph(data, "cy", "ip", tags);
    }

</script>

<div class="container main_body">
    <input id="ipDomainHash" type="hidden" value="80.82.78.50"/>
    <div class="this-title clearfix">
        <h3>80.82.78.50
            <small>IP信息</small>
        </h3>
    </div>
    <div class="panel domain-head-panel clearfix">
        <div class="col-md-9 col-lg-9 col-xs-12 col-sm-12">
            <table class="table table-condensed table-borderless pull-left res-brief">
                <tbody>
                <tr>
                    <th>IP地址</th>
                    <td>80.82.78.50
                        <a class="hidden" href="javascript:showIpTab();void(0);" id="domain_count_info">
                            <span class="blue">（共有 <span id="domain_count"></span> 个域名共用此地址）</span>
                        </a>
                    </td>
                </tr>
                <tr>
                    <th>地理位置</th>
                    <td>
                    荷兰,北荷兰省,阿姆斯特丹
                    
                        (quasinetworks.com)
                    
                    </td>
                </tr>
                <tr>
                    <th>ASN</th>
                
                
                    <td>
                    29073
                        
                             <span>（QUASINETWORKS, NL） </span>
                        
                    </td>
                    
                
                </tr>
                
                <tr>
                    <th>微步情报</th>
                    <td>
                        
                            
                                
                                
                                    
                                    
                                        <span class="tag non-clickable-tag neutral">IDC服务器</span>
                                    
                                
                            
                        

                        
                            
                        
                    </td>
                </tr>

                
                <tr>
                    <th>社区用户情报</th>
                    <td class="vote"></td>
                </tr>
                </tbody>
            </table>
        </div>
        <div class="col-md-3 col-lg-3 hidden-xs hidden-sm">
        <style type="text/css">
	#c_center{
		width: 16px;
  	height: 16px;
		border-radius: 50%;
		background-color: #3fa9f5;
		display: inline-block;
		margin: auto;
		margin-top: 80px;
  	margin-left: 80px;
		position: relative;

		-ms-transform: rotate(-135deg); /* IE 9 */
    -webkit-transform: rotate(-135deg); /* Chrome, Safari, Opera */
    transform: rotate(-135deg);

    -ms-transition-duration:1s;
    -ms-transition-timing-function:ease-in;

    -webkit-transition-duration:1s;
    -webkit-transition-timing-function:ease-in;

    transition-duration:1s;
    transition-timing-function:ease-in;
	}
	#c_center:before{
		content: "";
    width: 0;
    height: 0;
    border-bottom: 60px solid #3fa9f5;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    display: inline-block;
    left: 3.5px;
    position: absolute;
    bottom: 10px;
	}
	#heat_bg{
		width: 180px;
		height: 150px;
		background-image: url('../../static/img/community/heat_bg.png');
		position: relative;
	}
	#heat_bg span{
		display: inline-block;
    position: absolute;
    bottom: 15px;
    left: 0;
    color: #3fa9f5;
    font-weight: bold;
    width: 100%;
    text-align: center;
	}
</style>
<div class="pull-right hidden-xs hidden-sm" id="heat_bg">
	<div id="c_center">
		
	</div>
	<span>
		查询热度
	</span>
</div>
<script type="text/javascript">
	$(function(){
		//change rotate
		var level = "5"
		var deg = -135+level * 54
		var hot = $("#c_center")[0]
		hot.style.webkitTransform = 'rotate('+deg+'deg)'; 
    hot.style.mozTransform    = 'rotate('+deg+'deg)'; 
    hot.style.msTransform     = 'rotate('+deg+'deg)'; 
    hot.style.oTransform      = 'rotate('+deg+'deg)'; 
    hot.style.transform       = 'rotate('+deg+'deg)'; 
	})
</script>
        </div>
    </div>

    <ul class="nav nav-tabs text-center res-tab" id="tabs" role="tablist">
        <li class="active" role="presentation">
            <a class="hook hook-tab" data-toggle="tab" href="#ti" role="tab">威胁情报</a>
        </li>
        <li role="presentation">
            <a class="hook hook-tab" data-toggle="tab" href="#port" role="tab">端口与服务</a>
        </li>
        <li role="presentation">
            <a class="hook hook-tab" data-toggle="tab" href="#ip" role="tab">反查域名</a>
        </li>
        <li role="presentation">
            <a class="hook hook-tab" data-toggle="tab" href="#ca" role="tab">数字证书</a>
        </li>
        <li role="presentation">
            <a class="hook hook-tab" data-toggle="tab" href="#chart" role="tab">可视分析</a>
        </li>
        <li class="intelli-entrance hidden-xs hidden-sm" id="intell_community_tab" role="presentation">
            <a class="hook hook-tab" data-toggle="tab" href="#intell_community" role="tab">社区情报</a>
        </li>
    </ul>

    <div class="tab-content">
        <div class="tab-pane active" id="ti" role="tabpanel">
            <div class="panel panel-default" id="intelli_tag">
                <div class="panel-heading">
                    <h3 class="panel-title">威胁情报检测</h3>
                </div>
                <p class="no-data hidden" id="no_data_ti">无匹配数据</p>
                <table class="table hidden table-vertical" id="intelli_table">
                    <thead>
                    <tr><th>情报源</th>
                    <th>发现时间</th>
                    <th>情报类型</th>
                    </tr></thead>
                    <tbody>
                    
                        
                        <tr style="color: #B5BCC4">
                            <td>开源情报</td>
                            <td>2016-06-29</td>
                            <td style="padding-top: 6px; padding-bottom: 2px">扫描 <span class="arrow-left"></span><span class="rectangle">已过期</span></td>
                        </tr>
                        
                        
                    
                        
                        <tr style="color: #B5BCC4">
                            <td>ThreatBook Labs</td>
                            <td>2016-06-15</td>
                            <td style="padding-top: 6px; padding-bottom: 2px">垃圾邮件 <span class="arrow-left"></span><span class="rectangle">已过期</span></td>
                        </tr>
                        
                        
                    
                        
                        <tr style="color: #B5BCC4">
                            <td>ThreatBook Labs</td>
                            <td>2016-06-15</td>
                            <td style="padding-top: 6px; padding-bottom: 2px">垃圾邮件 <span class="arrow-left"></span><span class="rectangle">已过期</span></td>
                        </tr>
                        
                        
                    
                        
                        
                        <tr>
                            <td>ThreatBook Labs</td>
                            <td>2016-05-17</td>
                            <td>IDC服务器</td>
                            <!--td>[Ljava.lang.String;@592428a4</td-->
                        </tr>
                        
                    
                        
                        <tr style="color: #B5BCC4">
                            <td>开源情报</td>
                            <td>2016-04-15</td>
                            <td style="padding-top: 6px; padding-bottom: 2px">可疑 <span class="arrow-left"></span><span class="rectangle">已过期</span></td>
                        </tr>
                        
                        
                    
                        
                        <tr style="color: #B5BCC4">
                            <td>开源情报</td>
                            <td>2015-11-27</td>
                            <td style="padding-top: 6px; padding-bottom: 2px">扫描 <span class="arrow-left"></span><span class="rectangle">已过期</span></td>
                        </tr>
                        
                        
                    
                    </tbody>
                </table>
                <div class="text-right hidden" id="intelli_btn_container"><span class="vb-badge" id="intelli_badge"></span>
                    <button class="btn btn-secondary" type="button">显示更多</button>
                    <div class="clearfix"></div>
                </div>
            </div>

            <div class="panel panel-default">
                <div class="panel-heading">
                    <h3 class="panel-title">相关事件</h3>
                </div>
            
                <table class="table table-vertical" id="relateEvent_table">
                    <thead>
                    <tr><th>相关网址</th>
                    <th class="time-width">收录时间</th>
                    </tr></thead>
                    <tbody>
                        
                        <tr>
                            <td>
                                <a class="url" href="/show_blog/47414" title="https://x.threatbook.cn/nodev4/vb4/article?threatInfoID=530">https://x.threatbook.cn/nodev4/vb4/article?threatInfoID=530</a>
                            </td>
                            <td>
                            2018-05-28
                            </td>
                        </tr>
                        
                        <tr>
                            <td>
                                <a class="url" href="/show_blog/46460" title="https://x.threatbook.cn/nodev4/vb4/article?threatInfoID=464">https://x.threatbook.cn/nodev4/vb4/article?threatInfoID=464</a>
                            </td>
                            <td>
                            2018-04-11
                            </td>
                        </tr>
                        
                    </tbody>
                </table>
                <div class="text-right hidden" id="relateEvent_btn_container"><span class="vb-badge" id="relateEvent_badge"></span>
                    <button class="btn btn-secondary" type="button">显示更多</button>
                    <div class="clearfix"></div>
                </div>
            
            
            </div>

        <script src="/static/js/baiduTemplate.js" type="text/javascript"></script>
<script id="sus_list" type="text/template">
  <!for(var i=0;i<items.length;i++){!>
    <tr>
      <td>
        <!if(items[i].hash){!>
          <a href="/report/<!=items[i].hash!>" target="_blank" title="<!=items[i].url!>"><!=formatUrl(items[i].url,70)!></a>
        <!}else{!>
          <!=formatUrl(items[i].url,70)!>
        <!}!>
      </td>
      <td><!=items[i].file_size!></td>
      <td><!=items[i].scan_result!></td>
      <td><!=items[i].collect_time!></td>
    </tr>
  <!}!>
</script>
<div class="panel panel-default" id="sus_url_tag">
  <div class="panel-heading">
    <h3 class="panel-title">该地址上的可疑URL</h3>
  </div>
  <div class="loading">
    <img alt="loading" src="/static/img/wait.gif"/>
    <span>加载中...</span>
  </div>
  <p class="no-data hidden">无匹配数据</p>
  <table class="table hidden table-vertical" id="sus_url_table">
    <thead>
      <tr><th>URL</th>
      <th class="time-width">文件大小</th>
      <th class="time-width">扫描结果</th>
      <th class="time-width">收录时间</th>
    </tr></thead>
    <tbody>
    </tbody>
  </table>
  <div class="text-right hidden" id="sus_url_btn_container"><span class="vb-badge" id="sus_url_badge"></span><button class="btn btn-secondary" type="button">显示更多</button><div class="clearfix"></div></div>
</div>
<script src="/static/js/common/suspicousUrl.js" type="text/javascript"></script>

            <!--Begin: 鐩稿叧甯栧瓙-->
        
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h3 class="panel-title">情报社区相关讨论</h3>
                </div>
                <table class="table table-vertical table-hover" id="vb4_tag_table">
                    <thead>
                    <tr><th>帖子标题</th>
                    <th>社区用户情报</th>
                    </tr></thead>
                    <tbody>
                        
                        <tr>
                            <td style="max-width: 400px">
                                <a href="/nodev4/vb4/article?threatInfoID=530" target="_blank" title="求大佬指教 80.82.78.50 这个IP的行为是什么骚操作？">求大佬指教 80.82.78.50 这个...</a>
                            </td>
                            <td>
                                
                                    <span class="vb4-tag voted">求分析</span>
                                

                            </td>
                        </tr>
                        
                    </tbody>
                </table>
                <div class="text-right hidden" id="vb4_tag_btn_container"><span class="vb-badge" id="vb4_tag_badge"></span>
                    <button class="btn btn-secondary" type="button">显示更多</button>
                    <div class="clearfix"></div>
                </div>
            </div>
        
            <!--Begin: 鐩稿叧甯栧瓙-->

            <div class="panel panel-default" id="malware_tag">
            
            
                <div class="loading" id="samples_loading">
                    <img alt="loading" src="/static/img/wait.gif"/>
                    <span>加载中...</span>
                </div>
            
            </div>
        </div>

        <div class="tab-pane" id="ip" role="tabpanel">
            <!-- Begin: Current Domains Panel -->
            <div class="panel panel-default" id="share_domain_list">
                <div class="panel-heading">
                    <h3 class="panel-title">指向该IP的域名</h3>
                </div>
            <div class="loading" id="cur_domains_loading">
  <img alt="loading" src="/static/img/wait.gif"/>
  <span>加载中...</span>
</div>
<div id="cur_domains">
</div>
<script type="text/javascript">
function loadDomains(ip, isOnlyCheck, isUsePoint) {
  $("#cur_domains_loading").removeClass("hidden");
  var route = {url: function(args) { var pattern = '/7e2935f1ac5e47fd8ae79305f36200c8/ipcontroller/ip_cur_domains?isUsePoint=:isUsePoint&d=:ip&onlyCheck=:onlyCheck'; for (var key in args) { pattern = pattern.replace(':'+key, args[key] || ''); } return pattern; },method: 'GET'};
  var url = encodeURI(route.url({ip: ip, onlyCheck: isOnlyCheck, isUsePoint: isUsePoint}));

  $("#cur_domains").load(url, function(response, status, xhr) {
  $("#cur_domains_loading").addClass("hidden");
    console.log("Current domains info load status: " + status);

    if (status && status.indexOf("error") >= 0) {
      console.log("Failed to fetch history domains info, error: " + response);
      $("#cur_domains").html("");
    }
  });
}
  
$(function(){
  window.setTimeout(function() {
    loadDomains("80.82.78.50", true);
  }, 1500);
})
</script>
            </div>
            <!-- End: Current Domains Panel -->

            <!-- Begin: History Domains Panel -->
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h3 class="panel-title">历史域名记录</h3>
                </div>
                <div id="his_domains">
                    <div class="loading" id="his_domains_loading">
                        <img alt="loading" src="/static/img/wait.gif"/>
                        <span>加载中...</span>
                    </div>
                </div>
            </div>
            <!-- End: History Domains Panel -->
            <!-- Begin: rdns Panel -->
            <div class="panel panel-default" id="rdns_tag">
                <div class="panel-heading">
                    <h3 class="panel-title">该IP的 rdns 记录</h3>
                </div>
                <div class="loading">
                    <img alt="loading" src="/static/img/wait.gif"/>
                    <span>加载中...</span>
                </div>
                <p class="no-data hidden">无匹配数据</p>
                <table class="table hidden table-vertical" id="rdns_table">
                    <thead>
                    <tr><th>rdns名称</th>
                    <th class="time-width">收录时间</th>
                    </tr></thead>
                    <tbody>
                    </tbody>
                </table>
                <div class="text-right hidden" id="rdns_btn_container"><span class="vb-badge" id="rdns_badge"></span>
                    <button class="btn btn-secondary" type="button">显示更多</button>
                    <div class="clearfix"></div>
                </div>
            </div>
            <!-- End: rdns Panel -->
        </div>
    <script src="/static/js/baiduTemplate.js" type="text/javascript"></script>

<link href="/static/css/ip_port_shodan.css" rel="stylesheet" type="text/css"/>


<script id="port_list" type="text/template">
    <!for(var i=0;i<port_list.length;i++){!>
    <tr>
        <td><!=port_list[i].potocol!> <!=port_list[i].port!></td>
        <td><!=port_list[i].status=="0"?"开放":"关闭"!></td>
        <td><!=port_list[i].banner!></td>
        <td><!=port_list[i].get_time!></td>
    </tr>
    <!}!>
</script>

<!--NEW 端口数据-->
<script id="port_basic" type="text/template">
    <div class="port-info" >
        <div class="col3 last-update" id="last_update" >
            <span>更新时间：&nbsp;<!=last_update!></span>
        </div>
        <div class="col3 all-trigger" id="port_btn_container">
            <span class="vb-badge"></span>
            <button class="btn btn-secondary" type="button">全部展开</button>
            <div class="clearfix"></div>
        </div>
        <div class="col3 number" id="port_number" >
            <span>共<!=port_count!>个端口</span>
        </div>

    </div>
</script>

<script id="port_detail" type="text/template">
    <!for(var i=0; i<portsDetail.length; i++) {!>
    <div class="row-wrapper">
        <div class="port-detail-row js-row" >
            <div class="row-content row-content1">
                <span class="port"><!=portsDetail[i].port!></span>
                <span class="proto"><!=portsDetail[i].module!></span>
            </div>
            <div class="row-content row-content2">
                <!if (portsDetail[i].product == null) {!>
                <p class="application">N/A</p>
                <p class="version"></p>
                <!} else {!>
                <p class="application"><!=portsDetail[i].product!></p>
                    <!if (portsDetail[i].version == null) {!>
                        <p class="version"></p>
                    <!} else {!>
                        <p class="version">version&nbsp;<!=portsDetail[i].version!></p>
                    <!}!>
                <!}!>
            </div>
            <div class="row-content row-content3">
                <div class="detail-info">
                    <!for (var j=0; j<portsDetail[i].detail.length; j++) {!>
                    <p><!=portsDetail[i].detail[j]!> </p>
                    <!}!>
                </div>
                <div class="blank-detail"></div>
                <! if (portsDetail[i].collapseFlag == true) {!>
                <div class="more-wrapper" id="more_wrapper">
                    <div class="blank-top"></div>
                    <div class="more-trigger closed light"></div>
                    <div class="blank-bottom"></div>
                </div>
                <!}!>
            </div>
        </div>
    </div>
    <!}!>
</script>



<!--
<script id='os_list' type="text/template">
    <!for(var i=0;i<os_list.length;i++){!>
    <tr>
        <td><!=os_list[i].os!></td>
        <td><!=os_list[i].get_time!></td>
    </tr>
    <!}!>
</script>
-->

<!-- 把前端模板写在这里原因：other_info.js中包含了渲染rdns前端的代码，并且请求数据也使用和port相同的接口） -->
<script id="rdns_list" type="text/template">
    <!for(var i=0;i<rdns_list.length;i++){!>
    <tr>
        <td><!=rdns_list[i].rdns!></td>
        <td><!=rdns_list[i].get_time!></td>
    </tr>
    <!}!>
</script>


<style type="text/css">

</style>


<div class="tab-pane" id="port" role="tabpanel">
    <div class="panel panel-default" id="port_tag">
        <div class="panel-heading">
            <h3 class="panel-title">端口开放信息</h3>
        </div>
        <div class="loading">
            <img alt="loading" src="/static/img/wait.gif"/>
            <span>加载中...</span>
        </div>
        <p class="no-data hidden">无匹配数据</p>
        <!--数据内容起始-->
        <div id="port_info_detail_div">

        </div>
        <!--数据内容终止-->
    </div>
</div>

<script>

    $("#port_info_detail_div").delegate(".more-trigger", "click", function () {
        if ($(this).hasClass("closed")) {
            //console.log("closed->opened");
            $(this).removeClass("closed").addClass("opened");
            $(this).parents('.js-row').css({height:'auto'});
            checkIsAll("opened");
            return;
        }
        if ($(this).hasClass("opened")) {
            //console.log("opened->closed");
            $(this).removeClass("opened").addClass("closed");
            $(this).parents('.js-row').css({height:'154px'});
            checkIsAll("closed");
            return;
        }
    });


    function checkIsAll(actionType) {

        if (actionType == "closed") {
            var flag = true;
            $('.more-trigger').each(function () {
                if ($('.more-trigger').hasClass('opened')) {
                    flag = false;
                }
            });
            if (flag){
                var btn = $("#"+"port_btn_container").find("button");
                if (btn.html() == getString("expand_all")) {
                    return;
                }
                //alert("closed");
                buttonAllClickEvent("port_btn_container");
            }
        }
        if (actionType == "opened") {
            var flag = true;
            $('.more-trigger').each(function () {
                if ($('.more-trigger').hasClass('closed')) {
                    flag = false;
                }
            });
            if (flag) {
                var btn = $("#"+"port_btn_container").find("button");
                if (btn.html() == getString("collapse_all")) {
                    return;
                }
                //alert("opened");
                buttonAllClickEvent("port_btn_container");
            }
        }
    }

    $("#port_info_detail_div").delegate('.js-row',"mouseenter", function () {
        $(this).find('div.more-trigger').removeClass("light");
    });
    $("#port_info_detail_div").delegate('.js-row',"mouseleave", function () {
        $(this).find('div.more-trigger').addClass("light");
    });


    $("#port_info_detail_div").delegate("#port_btn_container","click", function () {
        buttonAllClickEvent("port_btn_container");
    });


    function buttonAllClickEvent(btn_container_id) {
        var btn = $("#"+btn_container_id).find("button");
        console.log(btn_container_id);
        if (btn.html() == getString("expand_all")) {
            console.log("expand_all");
            btn.addClass("less");
            btn.html(getString("collapse_all"));
            $('.more-trigger').removeClass("closed").addClass("opened");
            $('.js-row').css({height:'auto'});
            return;
        }
        if (btn.html() == getString("collapse_all")) {
            console.log("collapse_all");
            btn.removeClass("less");
            btn.html(getString("expand_all"));
            $('.more-trigger').removeClass("opened").addClass("closed");
            $('.js-row').css({height:'154px'});
            return;
        }
    }


</script>

<script src="/static/js/ip/other_info.js" type="text/javascript"></script>

        <div class="tab-pane" id="ca" role="tabpanel">

            <div class="ca-container" id="ca_container">
                <div class="loading" id="ca_loading">
                    <img alt="loading" src="/static/img/wait.gif"/>
                    <span>加载中...</span>
                </div>
            </div>

        </div>

        <div class="tab-pane" id="chart" role="tabpanel">
            <div class="graph-box-container">
                <table>
                    <tbody>
                    <tr>
                        <td class="graph-box-td">
                            <div class="graph-box" id="cy"></div>
                        </td>
                        <td class="graph-legend-td hidden-xs hidden-sm">
                            <div><div class="fieldContainer">
	<fieldset class="data-container">
    <legend align="center">基础数据信息</legend>
    <ul class="data ul-base-data">
      <li class="domain">
        <span></span>域名
      </li>
      <li class="sample">
        <span></span>样本HASH
      </li>
      <li class="ip">
        <span></span>IP
      </li>
      <li class="whois-email">
        <span></span>whois注册邮箱
      </li>
      <li class="whois-nickname">
        <span></span>whois注册名
      </li>
    </ul>
	</fieldset>
	<fieldset class="data-container">
    <legend align="center" class="threat-legend">威胁情报数据</legend>
    <ul class="data ul-threat-data">
      <li class="domain">
        <span></span>域名
      </li>
      <li class="file-hash">
        <span></span>样本HASH
      </li>
      <li class="url">
        <span></span>URL
      </li>
      <li class="ip">
        <span></span>IP
      </li>
      <li class="other">
        <span></span>其它
      </li>
    </ul>
	</fieldset>
	<dl class="tip">
		<dt class="sm-font-size">提示</dt>
		<dd class="xs-font-size"><span class="dot"></span>分类数据最大显示结点数：50</dd>
		<dd class="xs-font-size"><span class="dot"></span>点击图标，查看详细内容并访问链接</dd>
	</dl>
</div></div>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="tab-pane" id="intell_community" role="tabpanel">
            <div class="panel panel-default" id="intelli_tag">
                <div class="panel-heading">
                    <h3 class="panel-title">社区用户情报</h3>
                </div>
            <link href="/static/css/intell_community.css" rel="stylesheet" type="text/css"/>

<!--提示信息框，内容在显示时通过JS填充-->
<div class="modal fade" id="common-modal" role="dialog" tabindex="-1">
    <div class="modal-dialog modal-sm">
        <div class="modal-content">
            <div class="modal-body clearfix">
                <div class="header">
                    <div class="back-info"><span class="info-tip"></span><span class="info-img"></span></div>
                    <p class="info-content" id="intelli_info"></p>
                </div>
                <a class="btn btn-default center-block" data-dismiss="modal">知道了</a>
            </div>
        </div>
    </div>
</div>

<!--对于没有昵称的用户，提示其输入昵称-->
<div class="modal fade" id="add_nickname" role="dialog" tabindex="-1">
    <div class="modal-dialog modal-sm">
        <div class="modal-content">
            <div class="modal-body clearfix">
                <div class="header">
                    <p class="info-content">
                        <span>设置社区用户名</span>
                        <input class="form-control" id="nickname" maxlength="20" placeholder='不包含特殊字符，长度在5个汉字或10个英文字符内，可包括"-"、"_"' type="text"/>
                        <span class="error nick-error hidden"></span>
                    </p>
                </div>
                <a class="btn btn-default center-block" id="addNickname">提交</a>
            </div>
        </div>
    </div>
</div>

<div class="vb-panelBody" id="comment">
    <div class="user hidden">
        <!--可供选择的标签列表-->
        <div class="vote-container vote vote-list"></div>

        <!--暂无情报，我要提交一条。 或者已经有情报时，我要提供情报…-->
        <div class="comment-make row">
            <div class="col-md-10 col-lg-10 col-sm-9 col-xs-9">
                <input class="form-control" id="comment_input" placeholder="暂无情报提交，我要提交一条!" type="text"/>
            </div>
            <div class="col-md-2 col-lg-2 col-sm-3 col-xs-3 text-right">
                <button class="btn btn-default submit-comment" id="submit_tags">提交</button>
            </div>
        </div>
        <div class="comment-make row hidden" id="comment_area">
            <div class="col-md-12 col-lg-12 col-sm-12 col-xs-12">
                <textarea class="form-control" id="comment_textarea" maxlength="800" placeholder="暂无情报提交，我要提交一条!"></textarea>
                <div class="pull-right" id="infoLength_comment">(0 /800)</div>
            </div>
            <div class="col-md-offset-8 col-lg-offset-8 col-sm-offset-6 col-xs-offset-4 col-md-4 col-lg-4 col-sm-6 col-xs-8 text-right">
                <!--取消输入评论-->
                <button class="btn vb-cancel" id="comment_cancel">取消</button>
                <!--提交情报-->
                <button class="btn btn-default submit-comment" id="submit_comment">提交</button>
            </div>
        </div>
        <div class="checkbox ck-item opts" id="anoym_container">
            <input id="anoym" type="checkbox"/>
            <label for="anoym">匿名评论</label>
        </div>
    </div>

    <!--显示评论列表-->
    <div class="comment-display row"></div>

    <!--评论列表的翻页方式，瀑布-->
    <div class="pagi-container">
        <button class="btn show more center-block hidden">显示更多</button>
    </div>
</div>
<script src="/static/js/auto_complete.js" type="text/javascript"></script>

<script type="text/javascript">
    $(function(){
        dealRedPoint();
        $("a[href=#intell_community]").click(function(){
            localStorage.setItem("redPoint","disappear");
            dealRedPoint()
        });

        $("#nickname").focus(function(){
            $("span.nick-error").addClass("hidden")
        });
        $(".intelli-mine").click(function(){
            $(".exists").addClass("hidden");
            $(".user").removeClass("hidden")
        });
        $("#comment_input").focus(function(){
            $(this).parents(".comment-make").addClass("hidden");
            $("#comment_area").removeClass("hidden");
            $("#comment_textarea").focus()
        });
        $("#comment_cancel").click(function(){
            //cancel , clear textarea
            // $("#comment_textarea").val("")
            $("#comment_area").addClass("hidden");
            $("#comment_area").siblings(".comment-make").removeClass("hidden")
        });
        $(".submit-comment").click(function(){
        
            openLoginDlg();
        
        
        });
        $("#addNickname").click(addNickname);
        //限制输入文字长度
        var $textAera = $('#comment_textarea');
        detectInput($textAera,checkCanSubmitWithComments);
        loadData()
    })
</script>

<script type="text/javascript">
    /*record:user select tag len*/
    var selectedTagLen = 0;
    //input/textarea等输入控件监听
    function detectInput($tar,dealFunc){
        if (window.addEventListener) { //先执行W3C
            $tar.get(0).addEventListener("input", dealFunc, false);
        }else{
            $tar.get(0).attachEvent("onpropertychange", dealFunc);
        }
        if (window.VBArray && window.addEventListener) { //IE9
            //ie11 edge模式也会进入该方法
            //通过.attachEvent去掉ie11 edge
            if ($tar.get(0).attachEvent) {
                $tar.get(0).attachEvent("onkeydown", function() {
                    var key = window.event.keyCode;
                    (key == 8 || key == 46) && dealFunc(); //处理回退与删除
                });
                $tar.get(0).attachEvent("oncut", dealFunc); //处理粘贴
            }
        }
    }

    // 加载特别多的数据
    function loadData() {
        $.ajax({
            url: "/getUserTags",
            type: "POST",
            data: {"d": $("#ipDomainHash").val()},
            beforeSend: function () {
//                $("td.vote").html('<img alt="loading" src="/static/img/wait.gif"/>');
                $(".vote-list").html('<div class="loader center-block"><div class="loader-inner line-scale-pulse-out-rapid"><div></div><div></div><div></div><div></div><div></div></div></div>');
                $(".comment-display").html('<div class="loader center-block"><div class="loader-inner line-scale-pulse-out-rapid"><div></div><div></div><div></div><div></div><div></div></div></div>')
            },
            error: function (e) {
                console.warn("comment list load error:");
                $(".info-tip").html("提交失败");
                $(".info-img").removeClass("success").addClass("error");
                $("#intelli_info").html("加载失败");
                $("#common-modal").modal()
            },
            success: function (data) {
//                console.log("/getUserTags: " + data);
                var curUserInfo = null;
                var data = JSON.parse(data);
                $(".comment-display").html('');
                var lists = data.tag_user_list;//lt 11
                var listsLength = lists ? lists.length : 0;
                var imgPath = '/vb4/getUserImg?t=';
                if (listsLength > 0) {
                    $("#comment_input,#comment_textarea").prop("placeholder", "为标签添加备注...");
                    //fill list include fill own
                    var oFragment = document.createDocumentFragment();
                    for (var i = 0; i < listsLength; i++) {
                        var cur = lists[i];
                        var comments_list = cur.Comments_list;
                        var id = "list" + cur.id;
                        var imgName = cur.userImage;

                        var imgSrc = imgPath + imgName;
                        //get cur user info:include comments && tags
                        if (cur.isOwner) {
                            //curUserInfo = cur; // we allow add more than one tag for one object.
                        }

                        var showname = cur.userName;

                        var date = cur.create_time;

                        var content = htmlEncodeByJquery(cur.comments).replace(/(https:\/\/x.threatbook.cn\/nodev4\/vb4\/article\?threatInfoID\=)(\d+)/g, "<a href=$1$2 target=_blank>$1$2</a>");

                        var tags = cur.tag_list;

                        var ilike = cur.isPraiser ? "liked" : "";
                        var likenum = cur.praise_count;

                        var reportto = cur.reportTo;

                        var ireportto = cur.isReporter ? "reported" : "";
                        var reportnum = cur.report_count;

                        var commentnum = cur.comments_count;
                        var tagHtml = "";
                        var tagFragment = document.createDocumentFragment();
                        var mineTagLen = tags.length > 5 ? 5 : tags.length;
                        for (var j = 0; j < mineTagLen; j++) {
                            var tag = $('<span class="vote-tag voted"></span>');
                            tagFragment.appendChild(tag[0]);
                            tag.html(htmlEncodeByJquery(tags[j].tag_name))
                        }

                        var list = $('<div class="list clearfix"></div>');
                        list.prop("id", id);
                        var imgPare = $('<div class="col-md-1 col-lg-1 col-sm-2 hidden-xs portrait"></div>');
                        var img = $('<img style="width: 60px;height: 60px"/>');
                        img.prop("src", imgSrc);
                        img.appendTo(imgPare);
                        imgPare.appendTo(list);

                        var contentConta = $('<div class="col-md-11 col-lg-11 col-sm-10 col-xs-12 content"></div>');

                        var nameConta = $('<div class="col-md-12 col-lg-12 col-sm-12 col-xs-12 name-container"></div>');
                        var nicknameConta = $('<span class="mystrong"></span>');
                        nicknameConta.html(htmlEncodeByJquery(showname));
                        nicknameConta.appendTo(nameConta);

                        var dateConta = $('<span class="date"></span>');
                        dateConta.text(date);
                        dateConta.appendTo(nameConta);
                        nameConta.appendTo(contentConta);

                        var commentConta = $('<div class="col-md-9 col-lg-9 col-sm-12 col-xs-12 content"></div>');
                        var shortSpan = $('<span class="cut-text"></span>');
                        var shortenObj = getShrotenText(content, 200);
                        if (shortenObj.needShorten) {
                            shortSpan.html(shortenObj.res.replace(/\n/g, "<br/>").concat("... ").concat('<a class="intell-all" href="#">' + "显示更多" + '</a>'));
                            var wholeSpan = $('<span class="whole-text hidden"></span>');
                            wholeSpan.html(content.replace(/\n/g, "<br/>").concat(' <a class="intell-part" href="#">' + "收起" + '</a>'));
                            shortSpan.appendTo(commentConta);
                            wholeSpan.appendTo(commentConta)
                        } else {
                            commentConta.html(content.replace(/\n/g, "<br/>"))
                        }
                        commentConta.appendTo(contentConta);

                        var tagConta11 = $('<div class="vote-container vote text-right"></div>');
                        tagConta11[0].appendChild(tagFragment);
                        var tagConta1 = $('<div class="col-md-3 col-lg-3 col-sm-12 col-xs-12"></div>');
                        tagConta11.appendTo(tagConta1);
                        tagConta1.appendTo(contentConta);

                        var operConta = $('<div class="col-md-12 col-lg-12 col-sm-12 col-xs-12 oper-container"><div class="oper like ' + ilike + '"><i class="glyphicon glyphicon-thumbs-up" aria-hidden="true"></i>点赞(<span class="num">' + likenum + '</span>)</div><div class="oper to-comment"><i class="glyphicon glyphicon-comment" aria-hidden="true"></i>评论(<span class="num">' + commentnum + '</span>)</div><div class="oper report-to ' + ireportto + '">举报(<span class="num">' + reportnum + '</span>)</div></div></div>');
                        operConta.appendTo(contentConta);

                        contentConta.appendTo(list);
                        oFragment.appendChild(list[0])
                    }
                    $(".comment-display")[0].appendChild(oFragment);

                    $('.list a.intell-all').click(function (e) {
                        e.preventDefault();
                        $(this).parent(".cut-text").addClass("hidden");
                        $(this).parent(".cut-text").next(".whole-text").removeClass("hidden");
                    });
                    $('.list a.intell-part').click(function (e) {
                        e.preventDefault();
                        $(this).parent(".whole-text").addClass("hidden");
                        $(this).parent(".whole-text").prev(".cut-text").removeClass("hidden");
                    });
                    $(".to-comment").click(function () {
                        var hasComments = Number($(this).find("span.num").text()) !== 0;
                        if (hasComments) {
                            var hasCollasped = $(this).hasClass("collapsed");
                            $(".to-comment").removeClass("collapsed").parents(".oper-container").next("div").remove();
                            if (hasCollasped) {
                                //评论(*)
                                //remove
                                $(this).parents(".oper-container").next("div").remove();
                                $(this).removeClass("collapsed")
                            } else {
                                //收起评论
                                //add
                                var id = $(this).parents("div.list").prop("id").substring(4);
                                loadReply(id, 1, true)
                            }
                        } else {
                            var hasCollasped = $(this).hasClass("collapsed");
                            $(".to-comment").removeClass("collapsed").parents(".oper-container").next("div").remove();
                            if (hasCollasped) {
                                //评论(*)
                                //remove
                                $(this).parents(".oper-container").next("div").remove();
                                $(this).removeClass("collapsed")
                            } else {
                                //收起评论
                                //add
                                var reply = '<div class="reply-make row"><div class="col-md-10 col-lg-10 col-sm-9 col-xs-9"><input type="text" class="form-control reply-area"></div><div class="col-md-2 col-lg-2 col-sm-3 col-xs-3 text-right"><button class="btn btn-default submit-sub" disabled id="submit_tags">' + "提交" + '</button></div></div><div class="reply-make clearfix row hidden"><div class="col-md-12 col-lg-12 col-sm-12 col-xs-12"><div spellcheck="false"  class="textinput textarea c_tx2 reply-area" contentEditable accesskey="q" style="border: 1px solid #dfe9ef;"  maxlength="800"></div><p class="tip error" visibility="hidden"></p></div><div class="col-md-offset-8 col-lg-offset-8 col-sm-offset-6 col-xs-offset-4 col-md-4 col-lg-4 col-sm-6 col-xs-8 text-right"><button class="btn vb-cancel" id="comment_cancel">' + "取消" + '</button><button class="btn btn-default  submit-sub" id="submit_comment">' + "提交" + '</button></div>'

                                var commentsList = $('<div class="comments-container"></div>');
                                var commentsListContainer = $('<div class="col-md-9 col-lg-9 col-sm-9"></div>');
                                $(reply).appendTo(commentsList);
                                commentsList.appendTo(commentsListContainer);
                                commentsListContainer.appendTo($(this).parents(".content"));
                                $(this).addClass("collapsed");
                                // tofix:copy too much
                                $(".reply-make:first input").focus(function () {
                                    // $(".reply-make .textarea").empty()
                                    $(".reply-make").removeClass("hidden");
                                    $(this).parents(".reply-make").addClass("hidden")
                                });
                                $(".reply-make .vb-cancel").click(function () {
                                    $(".reply-make .textarea").empty();
                                    $(".reply-make").removeClass("hidden");
                                    $(this).parents(".reply-make").addClass("hidden")
                                });
                                $(".reply-make .submit-sub").click(function () {
                                    var $that = $(this);
                                
                                    openLoginDlg();
                                
                                
                                })
                            }
                        }
                    });
                    $(".like").click(function () {
                    
                        openLoginDlg();
                    
                    
                    });
                    $(".report-to").click(function () {
                    
                        openLoginDlg();
                    
                    
                    });
                    if (listsLength > 5) {
                        var hideLists = $(".comment-display .list:gt(4)");
                        hideLists.addClass("hidden");
                        $(".comment-display~.pagi-container .show.more").removeClass("hidden");
                        $(".btn.show").click(function () {
                            var ismore = $(this).hasClass("more");
                            var lists = $(".comment-display .list");
                            var hideLists = $(".comment-display .list:gt(4)");
                            if (ismore) {
                                //显示全部
                                hideLists.removeClass("hidden");
                                $(this).html(getString("show_less")).removeClass("more").addClass("less")
                            } else {
                                //收起
                                hideLists.addClass("hidden");
                                $(this).html(getString("show_more")).removeClass("less").addClass("more")

                            }
                        })
                    }
                }
                initTagsAndFillCurrentUserIntelli(data.tag_summary_list,curUserInfo)
            }
        });
    }

    function initTagsAndFillCurrentUserIntelli(data,curUserInfo){
        $(".vote-list").html("");
        var selectedTagMaxLen = 5;

        var tags = data;
        var tagLen =tags?tags.length:0;
        //find seleted tags'id as array
        var content = "";
        var selectedTagArr = [];
        var isprivate = false;
        var selectedTag = [];
        if (curUserInfo) {
            $(".intelli-mine").click(function(){
                $(".exists").addClass("hidden");
                $(".comment-make").addClass("hidden");
                $("#comment_area").removeClass("hidden");
                $(".user").removeClass("hidden")
            });
            $("#comment_cancel").click(function(){
                $(".exists").removeClass("hidden");
                $(".user").addClass("hidden")
            });
            $(".exists").removeClass("hidden");
            $(".user").addClass("hidden");
            content = curUserInfo.comments;
            selectedTagArr = curUserInfo.tag_list;
            isprivate = curUserInfo.isAnonymous;
            selectedTag = selectedTagArr.map(function(ele,idx,arr){
                return ele.tag_id
            });
            selectedTagLen = selectedTag.length;
            $("#anoym").prop("checked",isprivate);
            if (content != "该用户只提交了标记,未说明详细原因,该情报真实性需进一步验证") {

                //has comments,fill textarea
                $("#comment_textarea").val(content);
                $("#comment_area").removeClass("hidden");
                $("#comment_area").siblings(".comment-make").addClass("hidden")
            } else {
                //has no comments
                $("#comment_area").addClass("hidden");
                $("#comment_area").siblings(".comment-make").removeClass("hidden")
            }

        } else {
            $(".exists").addClass("hidden");
            $(".user").removeClass("hidden")
        }
        if (tagLen > 0) {
            for(var i = 0;i < tagLen;i++){
                var cur = tags[i];
                var name = htmlEncodeByJquery(cur.tag_name);
                var id = cur.tag_id;
                var num = cur.tag_count;
                var clsname = selectedTag.includes(id)?(num==0?"voted no-vote":"voted"):(num==0?"before-vote no-vote":"before-vote");
                $('<a class="vote-tag '+clsname+'"><span class="tag-name">'+name+'</span>(<span class="tag-num" id="'+id+'">'+num+'</span>)</a>').appendTo(".vote-list")
            }
        }

        $(".vote-list .vote-tag").click(function(){
        
            openLoginDlg();
        
        
        });
        var tag_add_placeholer = "+(添加)";
        $('<div style="display:inline-block;"><input class="form-control" type="text" id="vote_other" placeholder="'+tag_add_placeholer+'" maxlength="20"><span class="glyphicon glyphicon-plus hidden"></span></div>').appendTo(".vote-list");
        var shouldAdd =false;
        $("#vote_other").siblings(".glyphicon-plus").click(function(){
            if (selectedTagLen < selectedTagMaxLen) {
                // selectedTagLen +=1
                addUserTag()
            } else {
                $(".info-tip").html("提交失败");
                $(".info-img").removeClass("success").addClass("error");
                $("#intelli_info").html("最多可选择5个标记");
                $("#common-modal").modal()
            }
        });
        detectInput($("#vote_other"),function(){
            var val = $(this).val();
            if (val != "") {
                //添加+按钮，执行 enter trigger
                $(this).siblings(".glyphicon-plus").removeClass("hidden")
            } else {
                $(this).siblings(".glyphicon-plus").addClass("hidden")
            }
        })
        $("#vote_other").keypress(function(event){
            e = event ? event :(window.event ? window.event : null);
            if(e.keyCode==13||shouldAdd){
                //enter trigger create
                if (selectedTagLen < selectedTagMaxLen) {
                    // selectedTagLen +=1
                    addUserTag()
                } else {
                    $(".info-tip").html("提交失败");
                    $(".info-img").removeClass("success").addClass("error");
                    $("#intelli_info").html("最多可选择5个标记");
                    $("#common-modal").modal()
                }
            }
        });
        var postData = {
            ipDomainHash:$("#ipDomainHash").val()
        };
        $("#vote_other").autoComplete({ url:"/getAllShowedTags",postData:postData});
        $("td.vote").html("");
        //get top5 tags
        var topLen = tags.length>5?5:tags.length;
        var noTag = 0;
        for(var i = 0;i < topLen;i++){
            var cur = tags[i];
            var num = cur.tag_count;

            if (num > 0){
                $('<li class="user-tag-li" id="user-tag-li-'+cur["tag_id"]+'"></li>').appendTo("td.vote");
                $('<span class="vote-tag voted" id="user-tag-'+cur["tag_id"]+'">'+htmlEncodeByJquery(cur.tag_name)+'('+num+')</span>').appendTo("#user-tag-li-"+cur["tag_id"]);
                $('<span class="user-tagger hidden" id="user-tagger-'+cur["tag_id"]+'"><a>首次标注：'+cur["first_tagger"]+'</a><a>最后标注：'+cur["last_tagger"]+'</a></span>').appendTo("#user-tag-li-"+cur["tag_id"]);
                continue;
            }
            if (num == 0 && i==0) {
                noTag = 1;
                $('<span class="tag gray-tag">'+htmlEncodeByJquery(cur.tag_name)+'('+num+')</span>').appendTo("td.vote")
                continue;
            }
            if (i<3 && noTag==1) {
                $('<span class="tag gray-tag">'+htmlEncodeByJquery(cur.tag_name)+'('+num+')</span>').appendTo("td.vote")
            }
        }

        $('.vote-tag.voted').hover(
            function () {
                var voteId = $(this).attr("id");
                var taggerId = voteId.replace("tag", "tagger");
                $("#"+taggerId).removeClass("hidden");
                },
            function () {
                var voteId = $(this).attr("id");
                var taggerId = voteId.replace("tag", "tagger");
                $("#"+taggerId).addClass("hidden");
            }
        );
        $('.user-tagger').hover(
            function () {
                $(this).removeClass("hidden");
            },
            function () {
                $(this).addClass("hidden");
            }
        );


        $('<a class="vote-advance add-user-tag hidden-xs hidden-sm"><img src="/static/img/add_tag.png" style="width:16px;height:16px;margin:0 4px" id="vote_advance_img">添加用户情报</a>').appendTo("td.vote");
        $(".vote-advance").click(function(){
            localStorage.setItem("redPoint","disappear");
            dealRedPoint();
            $("[href='#intell_community']").tab("show");

        });

        // 测试显示tag添加者
        setSubmitBtnStatus()
    }
</script>


<script type="text/javascript">

    function loadReply(listId,currentPage,isFirst){
        var postData = { //String ipDomainHash, long tagID, int currentPage
            ipDomainHash:$("#ipDomainHash").val(),
            tagID:listId,
            currentPage:currentPage
        };
        $.ajax({
            type:'POST',
            data:postData,
            url:'/getTagCommentsList',
            beforeSend:function(){
                var commentConta = $("#list"+listId).find('.comments-container');
                commentConta.html("");
                var $load = $('<div class="loader center-block"><div class="loader-inner blue ball-spin-fade-loader"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div></div>');
                if (commentConta.length > 0) {
                    $load.appendTo(commentConta)
                } else {
                    var commentsList = $('<div class="comments-container"></div>');
                    var commentsListContainer = $('<div class="col-md-9 col-lg-9 col-sm-9"></div>');
                    $load.appendTo(commentsList);
                    commentsList.appendTo(commentsListContainer);
                    commentsListContainer.appendTo($($("#list"+listId).find(".content")[0]))
                }
            },
            success:function(data){
//                console.log(data)
                var res = JSON.parse(data);
                if (res.response_code == 0) {
                    var lists = res.comments_list;
                    var curPage = res.current_page + 1;


                    var commentsList =$("#list"+listId).find('.comments-container');
                    var commentsListContainer =$("#list"+listId).find('.comments-container').parent("div");

                    var $btnComment =$("#list" + listId).find(".to-comment");
                    var contentConta = $($("#list"+listId).find(".content")[0]);
                    commentsList.html(""); //清空loader
                    var listsLength = lists?lists.length:0;
                    var listsCount = res.tag_comments_count?res.tag_comments_count:0;
                    // var oFragment = document.createDocumentFragment();
                    //start for
                    for(var i = 0; i < listsLength; i++){
                        var cur = lists[i];
                        var replyId = "reply"+cur.id;
                        var timeGap = getFormatedDate(cur.create_time);
                        var isReporter = cur.isReporter?"reported":"";
                        var imgPath = '/vb4/getUserImg?t=';
                        var imgName = cur.owner_user_image;
                        var imgSrc = imgPath + imgName;

                        var str = '<div class="list clearfix" id="'+replyId+'"><div class="col-md-1 col-lg-1 col-sm-2 hidden-xs portrait"><img src="'+imgSrc+'" style="width:200%;"></div><div class="col-md-11 col-lg-11 col-sm-10 col-xs-12 content"><div class="col-md-12 col-lg-12 col-sm-12 col-xs-12 name-container"><span class="mystrong" id="'+cur.owner_user_id+'">'+htmlEncodeByJquery(cur.owner_user_name)+'</span><span class="date">'+timeGap+'</span></div><div class="col-md-12 col-lg-12 col-sm-12 col-xs-12">'+(cur.target_user_name?"回复@<span class='mystrong'>"+htmlEncodeByJquery(cur.target_user_name)+"</span>: ":"")+(htmlEncodeByJquery(cur.comments).replace(/\n/g,"<br/>"))+'</div><div class="col-md-12 col-lg-12 col-sm-12 col-xs-12 oper-container"><a class="to" href="#replyArea"><div class="oper to-comment" data-original-title=""><i class="glyphicon glyphicon-comment" aria-hidden="true"></i>回复</div></a><div class="oper report-to '+isReporter+'">'+"举报"+'(<span class="num">'+Number(cur.report_count)+'</span>)</div></div></div></div>';

                        var commentsContainer = $(str);
                        commentsContainer.appendTo(commentsList)
                    }
                    // oFragment.appendChild(list[0])
                    //end for
                    var reply = '<div class="reply-make row"><div class="col-md-10 col-lg-10 col-sm-9 col-xs-9"><input type="text" class="form-control reply-area"></div><div class="col-md-2 col-lg-2 col-sm-3 col-xs-3 text-right"><button class="btn btn-default submit-sub" id="submit_tags">'+"提交"+'</button></div></div><div class="reply-make clearfix row hidden"><div id="replyArea"></div><div class="col-md-12 col-lg-12 col-sm-12 col-xs-12"><div spellcheck="false" class="textinput textarea c_tx2 reply-area" contentEditable accesskey="q" style="border: 1px solid #dfe9ef;"  maxlength="800"></div><p class="tip error" visibility="hidden"></p></div><div class="col-md-offset-8 col-lg-offset-8 col-sm-offset-6 col-xs-offset-4 col-md-4 col-lg-4 col-sm-6 col-xs-8 text-right"><button class="btn vb-cancel" id="comment_cancel">'+"取消"+'</button><button class="btn btn-default  submit-sub" id="submit_comment">'+"提交"+'</button></div>';
                    var pagiContainer =$('<div class="pagi-container"><button class="btn show more center-block hidden">'+"显示更多"+'</button><ul class="pagination vb-pagination hidden"><li><a href="#"><span aria-hidden="true">'+"首页"+'</span></a></li><li><a href="#" aria-label="Previous"><span aria-hidden="true">'+"上一页"+'</span></a></li> <li><a href="#">1</span></a></li> <li><a href="#">2</a></li> <li><a href="#">3</a></li><li><a href="#" aria-label="Next"><span aria-hidden="true">'+"下一页"+'</span></a></li><li><a href="#"><span aria-hidden="true">'+"尾页"+'</span></a></li></ul></div>');

                    pagiContainer.appendTo(commentsList);
                    $(reply).appendTo(commentsList);
                    commentsList.appendTo(commentsListContainer);
                    commentsListContainer.appendTo(contentConta);

                    $(".comments-container .pagination a").click(function(){
                        loadReply(listId,$(this).data("page"),false)
                    });
                    $btnComment.addClass("collapsed");
                    $(".comments-container .to-comment").click(function(){
                        var $that = $(this);

                        var $user = $that.parents(".oper-container").siblings(".name-container").find("span.mystrong");
                        var to_nickname = $user.text();
                        var uid = $user.prop("id");
                        var targetID = $that.parents(".list").prop("id");
                        var hasMention = $that.parents(".list").siblings(".reply-make").find(".mention").length > 0;

                        if ($.isFirefox()) {
                            if (!hasMention) {
                                $that.parents(".list").find(".textarea").html("");
                                $that.parents(".list").find(".textarea").append($('<img  onclick="return false;" tabindex="-1" class="c_tx3 mention" alt="">'));
                                $that.parents(".list").find(".textarea").append($(document.createElement("emptyTextNode")))
                            }
                            $that.parents(".list").siblings(".reply-make").find(".mention").prop("alt","回复@"+to_nickname+":").data("to_uid",uid).data("targetID",targetID)
                        }else{
                            if (!hasMention) {
                                $that.parents(".list").find(".textarea").html("");
                                $that.parents(".list").find(".textarea").append($('<button  onclick="return false;" tabindex="-1" contenteditable="false" class="c_tx3 mention"></button>'));
                                $that.parents(".list").find(".textarea").append($(document.createElement("emptyTextNode")))
                            }
                            $that.parents(".list").siblings(".reply-make").find(".mention").text("回复@"+to_nickname+":").data("to_uid",uid).data("targetID",targetID)
                        }
                        $(".reply-make").removeClass("hidden");
                        $(".reply-make:first").addClass("hidden")
                    });

                    $(".comments-container .report-to").click(function(){
                    
                        openLoginDlg();
                    
                    
                    });
                    //tofix : copy self
                    $(".reply-make:first input").focus(function(){
                        // $(".reply-make .textarea").empty()
                        $(".reply-make").removeClass("hidden");
                        $(this).parents(".reply-make").addClass("hidden")
                    });
                    $(".reply-make .vb-cancel").click(function(){
                        $(".reply-make .textarea").empty();
                        $(".reply-make").removeClass("hidden");
                        $(this).parents(".reply-make").addClass("hidden")
                    });
                    $(".reply-make .submit-sub").click(function(){
                        var $that = $(this);
                    
                        openLoginDlg();
                    
                    
                    });

                    if (curPage == 1) {
                        if (isFirst) {
                            if (listsCount > 5 ) {
                                var hideLists = $(".comments-container .list:gt(4)");
                                hideLists.addClass("hidden");
                                $(".comments-container .show").removeClass("hidden");
                                $(".comments-container .pagination").addClass("hidden")
                            }
                        } else {
                            if (listsCount > 10){
                                initPagi(listsCount,curPage);
                                $(".comments-container .pagination").removeClass("hidden")
                            }
                        }

                    } else  {
                        initPagi(listsCount,curPage)
                    }
                    $(".comments-container .btn.show").click(function(){
                        $(this).addClass("hidden");
                        hideLists.removeClass("hidden");
                        if (listsCount > 10) { initPagi(listsCount,curPage) }
                    })
                }
            },
            error:function(){
                console.warn("error:loadReply")
            }
        })
        // encode:targetUserID /comment
    }

    function saveTagCommentsReport(id,flag,me){
        var $this = me;
        var postData ={
            ipDomainHash:$("#ipDomainHash").val(),
            tagCommentsId:id,
            operation:flag==1?1:2
        };
        $.ajax({
            type:"POST",
            data:postData,
            url:'/saveTagCommentsReport',
            beforeSend:function(){

            },
            success:function(data){
                var res = JSON.parse(data);
                if (res.response_code==0) {
                    //success
                    var tar = $($($("#reply"+id).find(".report-to")).find("span.num"));
                    var val = tar.text();
                    tar.text(Number(val)+flag);
                    var clsname = "reported";
                    if (flag==1) {
                        tar.parents(".report-to").addClass(clsname)
                    } else {
                        tar.parents(".report-to").removeClass(clsname)
                    }
                }
            },
            error:function(){
                $(".info-tip").html("提交失败");
                $(".info-img").removeClass("success").addClass("error");
                $("#intelli_info").html("请重新提交或联系管理员contactus@threatbook.cn");
                $("#common-modal").modal()
            },
            complete:function(){
                $this.data('requestRunning', false);
            }
        })
    }


    function addReply(tagID,targetID,targetUserID,comments){
        // String ipDomainHash, String comments, long tagID, long targetID, String targetUserID
        targetID = targetID.split("reply")[1]; // reply1111
        var postData = {
            ipDomainHash:$("#ipDomainHash").val(),
            tagID:tagID,
            targetID:targetID,
            targetUserID:targetUserID,
            comments:comments
        };
        console.log(postData);
        $.ajax({
            type:'POST',
            data:postData,
            url:'/saveUserTagComments',
            beforeSend:function(){
                $("#list"+tagID).find(".submit-sub").text("发送中...")
            },
            success:function(data){
                var res = JSON.parse(data);
                if (res.response_code == "0") {
                    $("#list"+tagID).find(".submit-sub").text("提交");
                    var operComment = $("#list"+tagID).find(".to-comment span.num");
                    var num = Number(operComment.text()) + 1;
                    operComment.text(num);
                    loadReply(tagID,1,true)
                }
            },
            error:function(){
                console.warn("error:addReply")
            }
        })
    }

    function initPagi(listsCount,curPage){
        var pageCount = Math.ceil(listsCount / 10)
        $(".comments-container .pagination li:nth-child(1) a").data("page",1)
        $(".comments-container .pagination li:nth-child(7) a").data("page",pageCount)

        $(".comments-container .pagination li:nth-child(2) a").data("page",curPage - 1)
        $(".comments-container .pagination li:nth-child(6) a").data("page",curPage + 1)

        if (curPage == 1) {
            //当前为第一页,首页不显示
            $(".comments-container .pagination li:nth-child(1)").addClass("hidden")
            $(".comments-container .pagination li:nth-child(2)").addClass("disabled")
            $(".comments-container .pagination li:nth-child(3) a").text(curPage).data("page",curPage).parents("li").addClass("active")
            if (curPage + 1 <= pageCount) {
                $(".comments-container .pagination li:nth-child(4) a").text(curPage + 1).data("page",curPage + 1)
                $(".comments-container .pagination li:nth-child(6) a").data("page",curPage + 1)
                $(".comments-container .pagination li:nth-child(5)").addClass("hidden")
                if (curPage + 2 <= pageCount) {
                    $(".comments-container .pagination li:nth-child(5) a").text(curPage + 2).data("page",curPage + 2).parent("li").removeClass("hidden")
                }
            }
        } else if (curPage == pageCount) {
            //当前为最后一页,尾页不显示
            $(".comments-container .pagination li:nth-child(7)").addClass("hidden")
            $(".comments-container .pagination li:nth-child(6)").addClass("disabled")
            $(".comments-container .pagination li:nth-child(5) a").text(curPage).data("page",curPage).parents("li").addClass("active")
            if (curPage - 1 >= 1) {
                $(".comments-container .pagination li:nth-child(4) a").text(curPage - 1).data("page",curPage - 1)
                $(".comments-container .pagination li:nth-child(2) a").data("page",curPage - 1)
                $(".comments-container .pagination li:nth-child(3)").addClass("hidden")
                if (curPage - 2 >= 1) {
                    $(".comments-container .pagination li:nth-child(3) a").text(curPage - 2).data("page",curPage - 2).parent("li").removeClass("hidden")
                }
            }
        } else {
            //上一页、下一页、中间三页 【当前页总在中间】
            $(".comments-container .pagination li:nth-child(4) a").text(curPage).data("page",curPage).parents("li").addClass("active")
            if (curPage - 1 < 0) {
                $(".comments-container .pagination li:nth-child(2)").addClass("disabled")
                $(".comments-container .pagination li:nth-child(3)").addClass("hidden")
            } else {
                $(".comments-container .pagination li:nth-child(3) a").text(curPage - 1).data("page",curPage - 1)
            }
            if (curPage + 1 > pageCount) {
                $(".comments-container .pagination li:nth-child(6)").addClass("disabled")
                $(".comments-container .pagination li:nth-child(5)").addClass("hidden")
            } else {
                $(".comments-container .pagination li:nth-child(5) a").text(curPage + 1).data("page",curPage + 1)
            }

        }
        // $(".comments-container .btn.show").addClass("hidden")
        $(".comments-container .pagination").removeClass("hidden")
    }
    function getFormatedDate(date){
        var res = "";
        var now = new Date();
        var dateInput = new Date(date); //Date.parse(date) get time gap
        var duration = moment.duration(moment(now).diff(dateInput));
        var years = duration.asYears();
        var months = duration.asMonths();
        var days = duration.asDays();
        var hours = duration.asHours();
        var minutes = duration.asMinutes();
        var seconds = duration.asSeconds();

        var y = Math.floor(years);
        var mm = Math.floor(months);
        var d = Math.floor(days);
        var hh = Math.floor(hours);
        var m = Math.floor(minutes);
        var s = Math.floor(seconds);

        if (y > 0) {
            res = y + "年前"
        } else if (mm > 0) {
            res = mm + "月前"
        } else if (d > 0) {
            res = d + "天前"
        } else if (hh > 0) {
            res = hh + "小时前"
        } else if (m > 0) {
            res = m + "分前"
        } else if (s >0) {
            res = "刚刚"
        } else {
            console.warn("error:formated date diff")
        }
        return res;
    }

    function submitUserIntelli(){
        var $this = $(".submit-comment");
        var baseTags = Array.prototype.map.call($(".vote-list .voted:not(.u-tag)"), function(obj) {
            return $(obj).find("span.tag-name").text()
        });
        var newTags = Array.prototype.map.call($(".u-tag"), function(obj) {
            return $(obj).find("span.tag-name").text()
        });

        if (baseTags.length==0 && newTags.length==0) {
            $this.text("提交");
            $(".info-tip").html("提交失败");
            $(".info-img").removeClass("success").addClass("error");
            $("#intelli_info").html("请至少选择或输入一个标记");
            $("#common-modal").modal('show');
            return;
        }
        var isAnonymous = $("#anoym").prop("checked")?"true":"false";
        var tags = baseTags.concat(newTags);
        $.ajax({
            url:'/saveUserTags',
            type:'POST',
            data:{
                ipDomainHash:$("#ipDomainHash").val(),
                tags:tags.join(";"),
                comment:$("#comment_textarea").val().trim()==""?"该用户只提交了标记,未说明详细原因,该情报真实性需进一步验证":$("#comment_textarea").val().trim(),
                isAnonymous:isAnonymous  //是否匿名
            },
            beforeSend:function(){
                $this.prop("disabled","disabled");
                $this.text("发送中...")
            },
            error:function(e){
                console.warn("error_submitUserIntelli");
                $(".info-tip").html("提交失败");
                $(".info-img").removeClass("success").addClass("error");
                $("#intelli_info").html("请重新提交或联系管理员contactus@threatbook.cn");
                $("#common-modal").modal()
            },
            success:function(data){
                var res = JSON.parse(data);
                console.warn(res);
                if (res.response_code==0) {
                    loadData();
                    $(".info-tip").html("提交成功");
                    $(".info-img").removeClass("error").addClass("success");
                    $("#intelli_info").html("感谢您提供情报,帮助我们驱散网络中的黑暗。让这个世界又光明了一些");
                    $("#common-modal").modal('show');
                    setTimeout(function(){$("#common-modal").modal('hide')},3000)
                } else if (res.response_code==1) {
                    //sensitive
                    $(".info-tip").html("提交失败");
                    $(".info-img").removeClass("success").addClass("error");
                    $("#intelli_info").html(res.verbose_msg);
                    $("#common-modal").modal('show')
                }
                $this.text("提交");
                $this.removeAttr("disabled");
                $("#comment_textarea").val("");
                checkAvaLength_checked();
            }
        })
    }

    function setSubmitBtnStatus(){
        var hasSelectedTags = checkTagIsSelected();
        // 根据是否选择了Tag来设置submit是否可以点击
//        hasSelectedTags?$(".submit-comment").removeAttr("disabled"):$(".submit-comment").attr("disabled","disabled");
    }
    function checkTagIsSelected(){
        return $("#comment .vote-list").find(".vote-tag.voted").length > 0;
    }
    function getUserType(isAnonymous,isCompany){
        //"anoym" :anoymous,"":not anoymous
        var anoym = isAnonymous?"_anoym":"";
        //"comp" : company,"individual":individual
        var compOrindiv = isCompany?"comp":"individual";
        return compOrindiv + anoym + ".png"
    }
    //限制输入文字长度
    function checkAvaLength_checked(){
        var $textAera = $('#comment_textarea');
        var $info = $('#infoLength_comment');
        var extraNumber = $textAera.val().length;
        $info.html( "(" + extraNumber + " /800)");
    }
    function checkCanSubmitWithComments(){
        checkAvaLength_checked();
        var hasSelectedTags = checkTagIsSelected();
//        if (hasSelectedTags) {
//            $("#submit_comment").removeAttr('disabled')
//        } else {
//            $("#submit_comment").attr('disabled','disabled')
//        }
    }
    function htmlDecodeByJquery(str) {
        return $('<div/>').html(str).text();
    }
    function htmlEncodeByJquery(str) {
        return $('<div/>').text(str).html();
    }
    function getShrotenText(str,len){
        var res = str.substring(0,len);
        return {
            res:res,
            needShorten:str.length>len
        }
    }

    function addOrReduceSubmit(type,id,flag,$this){
        var postData = {
            userTagId:id.substring(4),
            operation:flag=="1"?1:2,
            ipDomainHash:$("#ipDomainHash").val(),
            kind:type=="like"?1:2
        };

        $.ajax({
            type:"POST",
            data:postData,
            url:'/saveTagPraiseReport',
            beforeSend:function(){

            },
            success:function(data){
                var res = JSON.parse(data);

                if (res.response_code==0) {
                    //success
                    //tofix
                    var tar = $($($($("#"+id).find("div:not(.comments-container) ."+type)).find("span.num"))[0]);
                    var val = tar.text();
                    tar.text(Number(val)+flag)
                    var clsname = type=="like"?"liked":"reported";
                    if (flag=="1") {
                        tar.parents("."+type).addClass(clsname)
                    } else {
                        tar.parents("."+type).removeClass(clsname)
                    }
                }
            },
            error:function(){
                $(".info-tip").html("提交失败");
                $(".info-img").removeClass("success").addClass("error");
                $("#intelli_info").html("请重新提交或联系管理员contactus@threatbook.cn");
                $("#common-modal").modal()
            },
            complete:function(){
                $this.data('requestRunning', false);
            }
        })
    }

    function addUserTag(){
    
        openLoginDlg();
    
    
    }

    function addNickname(){
        var name = $("#nickname").val()
        var res = /[0-9a-zA-Z\u4e00-\u9fa5\-_\|]{2,9}/.test(name)
        if (res) {
            //非空 ""
            $.post('/setUserNickName',{nickName:name},function(data){
                var res = JSON.parse(data)
                if (res.response_code == 0) {
                    //success
                    $("#add_nickname").modal('hide')
                    // $this.text("提交")
                    $(".info-tip").html("提交成功")
                    $(".info-img").removeClass("error").addClass("success")
                    $("#intelli_info").html("昵称保存成功,请重新提交内容")
                    $("#common-modal").modal('show')
                    setTimeout(function(){$("#common-modal").modal('hide')},3000)
                    // submitUserIntelli()
                } else if (res.response_code == -4) {
                    //nickname exists
                    $(".nick-error").text("该昵称已被占用")
                    $(".nick-error").removeClass("hidden")
                } else if (res.response_code == -5) {
                    //invalid
                    $(".nick-error").text('不包含特殊字符，长度在5个汉字或10个英文字符内，可包括"-"、"_"')
                    $(".nick-error").removeClass("hidden")
                } else if (res.response_code == -6) {
                    //contain sensitive
                    $(".nick-error").text("你提交的内容中包含敏感词")
                    $(".nick-error").removeClass("hidden")
                } else {
                    //error
                    console.warn("error:addNickname")
                }
            })
        } else {
            $(".nick-error").text('不包含特殊字符，长度在5个汉字或10个英文字符内，可包括"-"、"_"')
            $(".nick-error").removeClass("hidden")
        }

    }

    function dealRedPoint(){
        if (window.localStorage) {
            var point = localStorage.getItem("redPoint");
            if (point) {
                //exist
                $(".intelli-entrance").removeClass("warn")
            } else {
                //add point
                $(".intelli-entrance").addClass("warn")
            }
        }
    }
</script>



























            </div>
        </div>
    </div>

</div>

<script type="text/javascript">
    $(function () {
        window.cur_ip = "80.82.78.50"

        var intelli_records = $("#intelli_table > tbody > tr");
        initInfo(intelli_records, 5, "intelli_table", "intelli_btn_container");
        if (intelli_records.length > 0) {
            $("#intelli_table").removeClass("hidden");
        } else {
            $("#no_data_ti").removeClass("hidden");
        }

        var vb4_tag_records = $("#vb4_tag_table > tbody > tr");
        initInfo(vb4_tag_records, 5, "vb4_tag_table", "vb4_tag_btn_container");

        var event_records = $("#relateEvent_table > tbody > tr");
        initInfo(event_records, 5, "relateEvent_table", "relateEvent_btn_container");

        window.setTimeout(function () {
            loadHisDomains("80.82.78.50", true);            
        }, 10);

        window.setTimeout(function () {
            loadCAs("80.82.78.50");
        }, 10);

        window.setTimeout(function () {
            loadSamples("80.82.78.50");
        }, 10);


    })

    function loadHisDomains(ip, isOnlyCheck, isUsePoint) {
        $("#his_domains_loading").removeClass("hidden");
        var route = {url: function(args) { var pattern = '/7e2935f1ac5e47fd8ae79305f36200c8/ipcontroller/gethisdomain4ip?isUsePoint=:isUsePoint&d=:d&onlyCheck=:onlyCheck'; for (var key in args) { pattern = pattern.replace(':'+key, args[key] || ''); } return pattern; },method: 'GET'};
        var url = encodeURI(route.url({d: ip, onlyCheck: isOnlyCheck, isUsePoint: isUsePoint}));
        console.log(url);

        $("#his_domains").load(url, function (response, status, xhr) {
            console.log("History domains info load status: " + status);

            if (status && status.indexOf("error") >= 0) {
                console.log("Failed to fetch history domains info, error: " + response);
                $("#his_domains").html("");
                return;
            }
        });
    }

    function loadCAs(ip) {
        $("#ca_loading").removeClass("hidden");
        var route = {url: function(args) { var pattern = '/7e2935f1ac5e47fd8ae79305f36200c8/getIPCas?d=:ip'; for (var key in args) { pattern = pattern.replace(':'+key, args[key] || ''); } return pattern; },method: 'GET'};
        var url = encodeURI(route.url({ip: ip}));
        console.log(url);

        $("#ca_container").load(url, function (response, status, xhr) {
            console.log("CA for IP info load status: " + status);
            $("#ca_loading").addClass("hidden");

            if (status && status.indexOf("error") >= 0) {
                console.log("Failed to fetch ca info for IP, error: " + response);
                $("#ca_container").html("");
                return;
            }
        });
    }
    /*
      function loadSamples(ip) {
        $("#samples_loading").removeClass("hidden");
        var route = {url: function(args) { var pattern = '/7e2935f1ac5e47fd8ae79305f36200c8/domaincontroller/getsamples?d=:d'; for (var key in args) { pattern = pattern.replace(':'+key, args[key] || ''); } return pattern; },method: 'GET'};
    var url = encodeURI(route.url({d: ip}));
    console.log(url);
    
    $("#samples_container").load(url, function(response, status, xhr) {
      console.log("Samples for IP info load status: " + status);
      $("#samples_loading").addClass("hidden");

      if (status && status.indexOf("error") >= 0) {
        console.log("Failed to fetch samples for IP, error: " + response);
        $("#samples_container").html("");
        return;
      }
    });
  }
  */
    function loadSamples(domain) {
        $("#samples_loading").removeClass("hidden");
        var route = {url: function(args) { var pattern = '/7e2935f1ac5e47fd8ae79305f36200c8/domaincontroller/getsamples?d=:d'; for (var key in args) { pattern = pattern.replace(':'+key, args[key] || ''); } return pattern; },method: 'GET'};
        var url = encodeURI(route.url({d: domain}));
        console.log(url);

        $("#malware_tag").load(url, function (response, status, xhr) {
            console.log("Samples for IP info load status: " + status);
            $("#samples_loading").addClass("hidden");

            if (status && status.indexOf("error") >= 0) {
                console.log("Failed to fetch samples for IP, error: " + response);
                $("#malware_tag").html("");
                return;
            }
        });
    }

    // function loadVoteSummary() {
    //   var ip = "80.82.78.50";
    //   $("#vote_summary_loading").removeClass("hidden");
    //   var route = {url: function(args) { var pattern = '/7e2935f1ac5e47fd8ae79305f36200c8/apiwrapper2/getvotelogsummary?ipDomainHash=:ipDomainHash'; for (var key in args) { pattern = pattern.replace(':'+key, args[key] || ''); } return pattern; },method: 'GET'};
    //   var url = encodeURI(route.url({ipDomainHash: ip}));
    //   console.log(url);

    //   $("#vote_summary_container").load(url, function(response, status, xhr) {
    //     console.log("vote_summary info load status: " + status);
    //     $("#vote_summary_loading").addClass("hidden");

    //     if (status && status.indexOf("error") >= 0) {
    //       console.log("Failed to fetch vote_summary info, error: " + response);
    //       $("#vote_summary_container").html("");
    //       return;
    //     }
    //   });
    // }

    //function iocInfoShow(kind) {
    //    //$('#tabs a[href="#ip"]').tab('show');
    //    alert(kind);
    //}
</script>
<script type="text/javascript">
    $(function () {
        window.cur_ip = "80.82.78.50"

        var relate_url = $("#relateEvent_table .url")
        for (var i = 0; i < relate_url.length; i++) {
            var cur = $(relate_url[i])
            cur.text(formatUrl(cur.text(), 130))
        }
    })
</script><footer class="hidden-xs hidden-sm text-center" id="footer">
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-5">
                <ul class="list-inline text-left knowmore-list">
                    <li>
                        <a href="/guide" target="_blank" title="向导">向导</a>
                    </li>
                    <li>
                        <a href="/api" target="_blank" title="API">API</a>
                    </li>
                    <li>
                        <a href="/about" target="_blank" title="关于">关于</a>
                    </li>
                    <li>
                        <a href="/terms_of_service" target="_blank" title="关于">服务条款</a>
                    </li>
                    <li>
                        <a href="/privacy" target="_blank" title="关于">隐私政策</a>
                    </li>
                    <li>
                        <a href="/change_log" target="_blank" title="关于">更新日志</a>
                    </li>
                    <li>
                        <a href="/partner" target="_blank" title="关于">合作伙伴</a>
                    </li>
                </ul>
            </div>
            <div class="col-md-3">
                <ul class="list-inline follow-us">
                    <li>
                        <a class="follow facebook" href="https://www.facebook.com/ThreatBook-507527639411197" target="_blank"> </a>
                    </li>
                    <li>
                        <a class="follow linkedin" href="https://www.linkedin.com/company/threatbook?trk=top_nav_home" target="_blank"> </a>
                    </li>
                    <li>
                        <a class="follow twitter" href="https://twitter.com/@ThreatBookLabs" target="_blank"> </a>
                    </li>
                    <li>
                        <a class="follow wechat" href="#" id="wechat_container"> </a>
                    </li>
                </ul>
            </div>
            <div class="col-md-4 text-right">
                <ul class="list-inline contact-us">
                    <li>
                        <span class="follow phone"></span>010-57017961
                    </li>
                    <li>
                        <span class="follow email"></span>contactus@threatbook.cn
                    </li>
                </ul>
            </div>
            <div class="col-md-7 text-left">
            Copyright © ThreatBook.CN All Rights Reserved. 京ICP备15044984号 北京微步在线科技有限公司 京公网安备11010802018402号
            </div>
            <div class="col-md-5 text-right dropup">
                <span>语言切换</span>
                <a class="chg-lang dropdown" data-toggle="dropdown">
                <span class="lang" id="lang">Language
                </span>
                    <span class="glyphicon glyphicon-triangle-bottom">
                </span>
                </a>
                <ul class="dropdown-menu gray-border no-borderRadius vb-menu list-lang">
                    <li>
                        <a class="active" href="#" value="zh">中文</a>
                    </li>
                    <li>
                        <a href="#" value="en">English</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</footer>
<div class="hidden box-shadow-1" id="two_d_code">
    <div class=" pull-left">
        <h5 class="text-center">订阅号</h5>
        <img src="/static/img/subscribe.bmp"/>
    </div>
    <div class="pull-right">
        <h5 class="text-center">用户交流群</h5>
        <img src="/static/img/2d_code.jpg"/>
    </div>
</div>
<div aria-hidden="true" class="modal fade" id="dlg" role="dialog" tabindex="-1"></div><!--blank dialog for register and login ,will be loaded in-->
<div class="modal fade" id="modal_loading">
    <main class="loaded" id="load">
        <div class="loader">
            <div class="loader-inner ball-triangle-path">
                <div></div>
                <div></div>
                <div></div>
            </div>
        </div>
    </main>
</div>
<div class="modal fade" id="modal_loading_conflict">
    <img id="loading_conflict" src="/static/img/loading.gif"/>
</div>
<div class="modal fade" id="add_nickname" role="dialog" tabindex="-1">
    <div class="modal-dialog modal-sm">
        <div class="modal-content">
            <div class="modal-body clearfix">
                <div class="header">
                    <p class="info-content">
                        <span>设置社区用户名</span>
                        <input class="form-control" id="nickname" maxlength="20" placeholder='不包含特殊字符，长度在5个汉字或10个英文字符内，可包括"-"、"_"' type="text"/>
                        <span class="error nick-error hidden"></span>
                    </p>
                </div>
                <a class="btn btn-default center-block" id="addNickname">提交</a>
            </div>
        </div>
    </div>
</div>




<div class="modal fade" id="file_scan_confirmation_dialog" role="dialog" tabindex="-1">
<!--已经分析过的文件-->
<style type="text/css">
  .indent-one{
    text-indent: 1em;
    display: inline-block;
  }
  h2.title-info{
    margin-top: 45px;
    margin-bottom: 30px;
  }
  p.poptit-drc{
    line-height: 2;
  }
  p.last{
    margin-top: 40px;
  }
  p.last a.btn:first-child{
    width: 140px;
  }
  p.last a.btn:last-child{
    width: 175px;
  }
</style>
<div class="modal-dialog">
  <div class="modal-content text-left">
    <div class="modal-body">
      <button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">×</span></button>
      <h2 class="md-font-size blue title-info text-center">已经分析过的文件</h2>
      <p class="poptit-drc">
      <span class="indent-one">第一次分析时间：</span>
      <strong><span id="first_scan_time"> </span></strong> (<span id="first_scan_ago"></span>前)<br/>
        <span>最后一次分析时间：</span>
        <strong><span id="last_scan_time"></span></strong> (<span id="last_scan_ago"></span>前)
        
      </p>
      <p class="poptit-drc ">
        <span class="warn-info">检出率</span><strong class="warn-info mdr-font-size"> <span class="mdr-font-size" id="ratio"> </span> </strong> <br/>
        您可以查看最后的分析结果或重新分析。		
      </p>
      <p class="last text-center">
        <a class="btn white-container" href="" id="file_rescan_btn" type="button">重新分析</a>
        <a class="btn btn-default" href="" id="view_last_report_btn" type="button">最后一次的分析结果</a>
      </p>
    </div>   
  </div>
</div>
</div>
<!-- End of scan confirmation dialog -->
<!-- Begin of Upload progress dialog (the progress of uploading)-->
<div class="modal fade" id="upload_progress_dialog" role="dialog" tabindex="-1">
<!--file uploading...-->
<div class="modal-dialog modal-sm" id="uploading_container">
  <div class="modal-content text-center no-border">
    <div class="modal-body" id="uploading">
      <button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">×</span></button>
      <h2 class="modal-title text-center md-font-size blue title-info">上传文件中...</h2>
      <h5 class="title-msg xs-font-size gray">文件正在上传，请不要关闭窗口</h5>
      <div class="hidden" id="hash_progress_container">
        <p class="title-msg xs-font-size gray">正在计算文件哈希值...</p>
        <div class="progress active">
          <div class="progress-bar" id="hash_progress" role="progressbar" style="width: 0%;"></div>
        </div>
      </div>
      <div class="hidden" id="upload_progress_container">
        <h5 class="title-msg xs-font-size gray">上传文件进度：</h5>
        <div class="progress active">
          <div class="progress-bar" id="upload_progress_bar" role="progressbar" style="width: 0%;"></div>
        </div>
      </div>
      <div class="hidden gif-progress-bar" id="upload_progress_container2">
        <p class="title-msg xs-font-size gray">请稍候……</p>
        <span class="bar"></span>
      </div>
    </div>
  </div>
</div>
</div>
<!-- End of Upload progress dialog -->
<!-- Begin of adv query confirm  （to choose which payment to query）-->
<div class="modal fade" id="adv_confirmation_dialog" role="dialog" tabindex="-1">
﻿<style>
#point-modal {
  width: 400px;
}
.points-label {
  margin-right: 20px;
}
#point-modal .modal-body {
  padding: 30px 60px 0;
}
#point-modal .modal-footer {
  padding: 15px 30px 30px;
  border-top: 0;
  text-align: center;
}
#point-modal .modal-footer > button {
  width: 100px;
  border-radius: 3px;
}
#point-modal .modal-footer .cancel-btn {
  background-color: #f7f8f9;
}
.pay-choice {
  margin-bottom: 30px;
  text-align: center;
}
.point-info, .adv-info{
  text-align: left;
}
.point-info > div, .adv-info > div {
  margin-bottom: 15px;
  text-indent: 20px;
}
</style>
<div class="modal-dialog" id="point-modal">
    <div class="modal-content">
        <div class="modal-body">
            <form class="form-horizontal pay-choice" role="form">
                <input id="query_item" type="hidden" value=""/>
                <input id="query_kind" type="hidden" value=""/>
                <input id="point_desired" type="hidden" value=""/>

		<label class="points-label" for="points-buy">
                  <input class="points-buy" id="points-buy" name="query_payment" type="radio" value="point"/> 积分支付
		</label>
		<label class="adv-pay-label" for="adv-buy">
                  <input class="adv-buy" id="adv-buy" name="query_payment" type="radio" value="times"/> 高级查询支付
		</label> 
            </form>
	    <div class="point-info">
		<div class="">当前积分：<span id="point_count">300</span>  （积分）</div>
		<div class="">消费积分：<span id="point_desired">300</span>  （积分）</div>
		<div class="">剩余积分：<span id="point_left">300</span>  （积分）</div>
		<div class="" id="point_less">剩余积分不足，<a href="/nodev4/vb4/pointsDetails" target="_blank">查看积分</a></div>
            </div>
	    <div class="adv-info hidden">
	        <div class="">当前可用：<span id="times_dount">100</span>（次）</div>
		<div class="">本次使用：1（次）</div>
		<div class="">剩余次数：<span id="times_left">100</span>（次）</div>
	    </div>
        </div>
        <div class="modal-footer">
	    <button class="btn-pay btn btn-default" id="toLoad" onclick="javascript:loadAdvData()" type="submit">支付</button>
            <button class="cancel-btn btn btn-primary" data-dismiss="modal" type="button">取消</button>
	    <span class="hidden" id="tip">tip</span>
        </div>
    </div><!-- /.modal-content -->
</div><!-- /.modal -->

</div>
<!-- End of adv query confirm  （to choose which payment to query）-->
<link href="/static/css/common_dialog.css" rel="stylesheet" type="text/css"/>
<div class="modal fade" id="common-modal" role="dialog" tabindex="-1">
	<div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-body clearfix">
      <button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">×</span></button>
      <p class="text-center" id="info">请登录后再进行本操作！</p>
      <a class="btn btn-default center-block" id="login_close">立即登录</a>
      </div>
    </div>
	</div>
</div>
<script type="text/javascript">
	$(function(){
		$("#login_close").click(function(){
			$('#common-modal').modal('hide')
			openLoginDlg()
		})
	})
</script>
<script charset="utf-8" src="/static/js/cytoscape.min.js" type="text/javascript"></script>
<script src="/static/js/jquery.qtip.js"></script>
<script src="/static/js/cytoscape-qtip.js"></script>
<script id="baidu_script" type="text/javascript">
    var _hmt = _hmt || [];
    (function() {
        var hm = document.createElement("script");
        hm.src = "//hm.baidu.com/hm.js?7fe1ffa0ec1869ee64eeb064aa1eeb72";
        //var s = document.getElementsByTagName("script")[0];
        //s.parentNode.insertBefore(hm, s);
        var s = document.getElementById("baidu_script");
        s.parentNode.insertBefore(hm, s);
    })();
</script>

<script>
    // 跟第三方登录相关
    $(function () {
        var oauthLogined = localStorage.getItem("oauth_login_success");
        localStorage.removeItem("oauth_login_success");
        console.log("remove oauth_login_success： "+oauthLogined);
        if (oauthLogined == 0) {
            openLoginDlg();
        }
    });

</script>
<!-- start Mixpanel -->
<!-- <script src="/static/js/maidian.js" type="text/javascript" charset="utf-8"></script> --></body></html><!-- Begin of scan confirmation dialog （to choose the last result or reanalysis）-->
    """
    soup = BeautifulSoup(html_doc)
    # print(soup.prettify())
    # print(soup.find(id="tag_td"))
    # print(soup.find(id="vb4_tag_table"))
    # shequ = soup.find(id="vb4_tag_table")
    # print('=== shequ : ' , shequ)
    # print(soup.find("span","vb4-tag voted"))
    # 微步情报   id="tag_td"

    # 社区用户情报
    shequ = soup.find("span","vb4-tag voted")
    print(shequ)
    print(shequ.string)
    # 威胁情报
    threads = soup.find(id="intelli_table")
    threadList = threads.find_all('td')
    print('=== zero : ')
    print(threadList[0])
    print('=== start parse list :')
    listSize = len(threadList)
    for ii in range(listSize):
        if (ii+1)%3 ==0:
            if threadList[ii].string is None:
                print('===  :  none')
            else:
                print(threadList[ii].string)
    # for td in threadList:
    #     print(td.string)
    # 地理位置
    infoTab = soup.find("table","table table-condensed table-borderless pull-left res-brief")
    print('=== table information : ', infoTab)
    trList = infoTab.find_all('tr')
    print('=== gero information :')
    geroTrObj = trList[1]
    print('gero obj : ',geroTrObj)
    gero_current = geroTrObj.find('td').string.strip()
    print('=== gero_current : ',gero_current)
    print('gero : ',''.join(gero_current.split()))


