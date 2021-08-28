#coding:utf-8
import requests
import sys
import os
os.system('cls' if os.name == 'nt' else 'clear')
print ("""
#########################################################
# Coder Cüneyt TANRISEVER  // Admin Panel Bulucu        #
# Kullanimi url giriniz.                                #
# Ardindan pro bulduklarini en son liste halinde verir  #
# Hepsi bu kadar kolay gelsin.                          #
########################################################\n""")

panel = ['admin/', 'administrator/', 'admin1/', 'admin2/', 'admin3/', 'admin4/', 'admin5/', 'usuarios/', 'usuario/', 'moderator/', 'webadmin/', 'adminarea/', 'bb-admin/', 'adminLogin/', 'admin_area/', 'panel-administracion/', 'instadmin/', 'memberadmin/', 'administratorlogin/', 'adm/', 'admin/account.php', 'admin/index.php', 'admin/login.php', 'admin/admin.php', 'admin_area/admin.php', 'admin_area/login.php', 'siteadmin/login.php', 'siteadmin/index.php', 'siteadmin/login.html', 'admin/account.html', 'admin/index.html', 'admin/login.html', 'admin/admin.html', 'admin_area/index.php', 'bb-admin/index.php', 'bb-admin/login.php', 'bb-admin/admin.php', 'admin/home.php', 'admin_area/login.html', 'admin_area/index.html', 'admin/controlpanel.php', 'admin.php', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html', 'adminpanel.html', 'webadmin.html', 'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'admin/admin_login.html', 'admin_login.html', 'panel-administracion/login.html', 'admin/cp.php', 'cp.php', 'administrator/index.php', 'administrator/login.php', 'nsw/admin/login.php', 'webadmin/login.php', 'admin/admin_login.php', 'admin_login.php', 'administrator/account.php', 'administrator.php', 'admin_area/admin.html', 'pages/admin/admin-login.php', 'admin/admin-login.php', 'admin-login.php', 'bb-admin/index.html', 'bb-admin/login.html', 'acceso.php', 'bb-admin/admin.html', 'admin/home.html', 'login.php', 'modelsearch/login.php', 'moderator.php', 'moderator/login.php', 'moderator/admin.php', 'account.php', 'pages/admin/admin-login.html', 'yonetim', 'yonetici', 'yonet', 'Yonet', 'Yonetim', 'Yonetici', 'YONETIM', 'YONETICI', 'YONET', 'yonet.php', 'yonetim.php', 'yonetici.php', 'admin/admin-login.html', 'admin-login.html', 'controlpanel.php', 'admincontrol.php', 'admin/adminLogin.html', 'adminLogin.html', 'home.html', 'rcjakar/admin/login.php', 'adminarea/index.html', 'adminarea/admin.html', 'webadmin.php', 'webadmin/index.php', 'webadmin/admin.php', 'admin/controlpanel.html', 'admin.html', 'admin/cp.html', 'cp.html', 'adminpanel.php', 'moderator.html', 'administrator/index.html', 'administrator/login.html', 'user.html', 'administrator/account.html', 'administrator.html', 'login.html', 'modelsearch/login.html', 'moderator/login.html', 'adminarea/login.html', 'panel-administracion/index.html', 'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html', 'admincontrol/login.html', 'adm/index.h tml', 'adm.html', 'moderator/admin.html', 'user.php', 'account.html', 'controlpanel.html', 'admincontrol.html', 'panel-administracion/login.php', 'wp-login.php', 'adminLogin.php', 'admin/adminLogin.php', 'home.php', 'adminarea/index.php', 'adminarea/admin.php', 'adminarea/login.php', 'panel-administracion/index.php', 'panel-administracion/admin.php', 'modelsearch/index.php', 'modelsearch/admin.php', 'admincontrol/login.php', 'adm/admloginuser.php', 'admloginuser.php', 'admin2.php', 'admin2/login.php', 'admin2/index.php', 'usuarios/login.php', 'adm/index.php', 'adm.php', 'affiliate.php', 'adm_auth.php', 'memberadmin.php', 'administratorlogin.php', 'administrador', 'painel', 'entrada', 'membro', 'login_administrador', 'administrateur', 'panneau', 'entr\xc3\x83\xc2\xa9e', 'panel', 'membre', 'private.php', 'photoalbum/upload/', '_vti_pvt/', ':5800/', 'phpMyAdmin/', 'config.html/', '_private/', 'admin1.php', 'admin1.html', 'admin2.html', 'yonetim.html', 'yonetici.html', 'controlpanel/', 'admin1.asp', 'yonetim.asp', 'yonetici.asp', 'fileadmin/', 'fileadmin.php', 'fileadmin.asp', 'fileadmin.html', 'administration/', 'administration.php', 'administration.html', 'sysadmin.php', 'sysadmin.html', 'phpmyadmin/', 'myadmin/', 'sysadmin.asp', 'sysadmin/', 'ur-admin.asp', 'ur-admin.php', 'ur-admin.html', 'ur-admin/', 'Server.php', 'Server.html', 'Server.asp', 'Server/', 'wp-admin/', 'administr8.php', 'administr8.html', 'administr8/', 'administr8.asp', 'administratie/', 'admins/', 'admins.php', 'admins.asp', 'admins.html', 'administrivia/', 'Database_Administration/', 'WebAdmin/', 'useradmin/', 'sysadmins/', 'system-administration/', 'administrators/', 'pgadmin/', 'directadmin/', 'staradmin/', 'ServerAdministrator/', 'SysAdmin/', 'administer/', 'LiveUser_Admin/', 'sys-admin/', 'typo3/', 'panel/', 'cpanel/', 'cPanel/', 'cpanel_file/', 'platz_login/', 'rcLogin/', 'blogindex/', 'formslogin/', 'autologin/', 'support_login/', 'meta_login/', 'manuallogin/', 'simpleLogin/', 'loginflat/', 'utility_login/', 'showlogin/', 'memlogin/', 'members/', 'login-redirect/', 'sub-login/', 'wp-login/', 'login1/', 'dir-login/', 'login_db/', 'xlogin/', 'smblogin/', 'customer_login/', 'UserLogin/', 'login-us/', 'acct_login/', 'bigadmin/', 'project-admins/', 'phppgadmin/', 'pureadmin/', 'sql-admin/', 'radmind/', 'openvpnadmin/', 'wizmysqladmin/', 'vadmind/', 'ezsqliteadmin/', 'hpwebjetadmin/', 'newsadmin/', 'adminpro/', 'Lotus_Domino_Admin/', 'bbadmin/', 'vmailadmin/', 'Indy_admin/', 'ccp14admin/', 'irc-macadmin/', 'banneradmin/', 'sshadmin/', 'phpldapadmin/', 'macadmin/', 'administratoraccounts/', 'admin4_account/', 'admin4_colon/', 'radmind-1/', 'Super-Admin/', 'AdminTools/', 'cmsadmin/', 'SysAdmin2/', 'globes_admin/', 'cadmins/', 'phpSQLiteAdmin/', 'navSiteAdmin/', 'server_admin_small/', 'logo_sysadmin/', 'server/', 'database_administration/', 'power_user/', 'system_administration/', 'ss_vms_admin_sm/', 'admin.%EXT%', 'login.htm', 'login/', 'login.%EXT%', 'admin/login.htm', 'admin/home.%EXT%', 'admin/controlpanel.htm', 'admin/cp.%EXT%', 'admin/adminLogin.htm', 'admin/admin_login.%EXT%', 'admin/controlpanel.%EXT%', 'admin/admin-login.%EXT%', 'admin-login.%EXT%', 'admin/account.%EXT%', 'admin/admin.%EXT%', 'admin.htm', 'adminitem/', 'adminitem.%EXT%', 'adminitems/', 'adminitems.%EXT%', 'administrator/login.%EXT%', 'administrator.%EXT%', 'administration.%EXT%', 'adminlogin.%EXT%', 'admin_area/admin.%EXT%', 'admin_area/login.%EXT%', 'manager/', 'manager.%EXT%', 'letmein/', 'letmein.%EXT%', 'superuser/', 'superuser.%EXT%', 'access/', 'access.%EXT%', 'sysadm/', 'sysadm.%EXT%', 'superman/', 'supervisor/', 'panel.%EXT%', 'control/', 'control.%EXT%', 'member/', 'member.%EXT%', 'members.%EXT%', 'user/', 'user.%EXT%', 'cp/', 'uvpanel/', 'manage/', 'manage.%EXT%', 'management/', 'management.%EXT%', 'signin/', 'signin.%EXT%', 'log-in/', 'log-in.%EXT%', 'log_in/', 'log_in.%EXT%', 'sign_in/', 'sign_in.%EXT%', 'sign-in/', 'sign-in.%EXT%', 'users/', 'users.%EXT%', 'accounts/', 'accounts.%EXT%', 'bb-admin/login.%EXT%', 'bb-admin/admin.%EXT%', 'administrator/account.%EXT%', 'relogin.htm', 'relogin.html', 'check.%EXT%', 'relogin.%EXT%', 'processlogin.%EXT%', 'checklogin.%EXT%', 'checkuser.%EXT%', 'checkadmin.%EXT%', 'isadmin.%EXT%', 'authenticate.%EXT%', 'authentication.%EXT%', 'auth.%EXT%', 'authuser.%EXT%', 'authadmin.%EXT%', 'cp.%EXT%', 'modelsearch/login.%EXT%', 'moderator.%EXT%', 'controlpanel.%EXT%', 'admincontrol.%EXT%', 'adminpanel.%EXT%', 'fileadmin.%EXT%', 'sysadmin.%EXT%', 'admin1.%EXT%', 'admin1.htm', 'admin2.%EXT%', 'yonetim.%EXT%', 'yonetici.%EXT%', 'ur-admin.%EXT%', 'Server.%EXT%', 'administr8.%EXT%', 'webadmin.%EXT%', 'admins.%EXT%', 'adm.%EXT%', 'admin_login.%EXT%', 'panel-administracion/login.%EXT%', 'pages/admin/admin-login.%EXT%', 'pages/admin/', 'acceso.%EXT%', 'admincp/login.%EXT%', 'admincp/', 'admincontrol/', 'affiliate.%EXT%', 'adm_auth.%EXT%', 'memberadmin.%EXT%', 'administratorlogin.%EXT%', 'modules/admin/', 'administrators.%EXT%', 'siteadmin/', 'siteadmin.%EXT%', 'adminsite/', 'kpanel/', 'vorod/', 'vorod.%EXT%', 'vorud/', 'vorud.%EXT%', 'adminpanel/', 'PSUser/', 'secure/', 'webmaster/', 'webmaster.%EXT%', 'autologin.%EXT%', 'userlogin.%EXT%', 'admin_area.%EXT%', 'cmsadmin.%EXT%', 'security/', 'usr/', 'root/', 'secret/', 'admin/login.%EXT%', 'admin/adminLogin.%EXT%', 'moderator/login.%EXT%', 'moderator/admin.%EXT%', '0admin/', '0manager/', 'aadmin/', 'cgi-bin/login%EXT%', 'login1%EXT%', 'login_admin/', 'login_admin%EXT%', 'login_out/', 'login_out%EXT%', 'login_user%EXT%', 'loginerror/', 'loginok/', 'loginsave/', 'loginsuper/', 'loginsuper%EXT%', 'login%EXT%', 'logout/', 'logout%EXT%', 'secrets/', 'super1/', 'super1%EXT%', 'super_index%EXT%', 'super_login%EXT%', 'supermanager%EXT%', 'superman%EXT%', 'superuser%EXT%', 'supervise/', 'supervise/Login%EXT%', 'super%EXT%']
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
rq=requests.session() 
rq.headers.update(headers)
yonlendirme=[]
bulun=[]
def urlduzelt():
    global urlc
    url=raw_input("Url giriniz // site adresini giriniz = ")
    if "https" and "http" not in url[:5]:
        urls="http://"+url
        if "/" not in urls[-1:]:
            urlc= urls+"/"
            calis()
    if "https" and "http"  in url[:5]:
        if "/" not in url[-1:]:
            urlc= url+"/"
            calis()
    if "https" and "http"  in url[:5]:
        if "/" in url[-1:]:
            urlc= url
            calis()
    if "https" and "http" not in url[:5]:
        if "/" in url[-1:]:
            urlc= "http://"+url
            
            calis()
def calis():
    for i in panel:
        urld=urlc+i
        try:
            res=rq.get(urld,timeout=30)
            rm=res.status_code
        
            print "Denenen url = %s"%(urld)
            if rm == 302:
                print ">>>>>[302] Admin Panel bulundu = %s <<<<<"%(urld)

          
            if rm == 200:
                print ">>>>>[200] Admin Panel bulundu = %s <<<<<"%(urld)
                bulun.append(urld)
            if rm == 301:
                print ">>>>> [301] Admin Panel bulundu = %s <<<<<"%(urld)
                yonlendirme.append(urld)
        except requests.exceptions.RequestException as hata: 
            print "url hatali boyke bir adres yok"
            sys.exit()
        except requests.exceptions.Timeout:
            print "baglanti 30 sn gecti url atlandi "
            continue
        except requests.exceptions.TooManyRedirects:
            print "Baglanti kotu url atlandi"
            continue
        except requests.exceptions.HTTPError as hata1: 
            print hata1
            print "http hatasi url atlandi"
            continue
        except requests.exceptions.ConnectionError as hata2: 
            print "baglanti hatasi url atlandi"
            continue
            
    if yonlendirme==[] and bulun==[]:
        print " \nAdmin panel bulunamadi"
    if yonlendirme !=[] and bulun!= []:
        print "*"*40
        for i in yonlendirme:
            print "[301] url = %s"%(i)
        for j in bulun:
            print "[200] url = %s"%(j)
    if yonlendirme !=[] and bulun==[]:
        print "*"*40
        for i in yonlendirme:
            print "[301] url = %s"%(i)
    if yonlendirme==[] and bulun !=[]:
        print "*"*40
        for j in bulun:
            print "[200] url = %s"%(j)


urlduzelt()
