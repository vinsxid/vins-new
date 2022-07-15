#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅ **Perintah Admin**

**c** singkatan dari pemutaran Channel.

/pause atau /cpause - Jeda musik yang diputar.
/resume atau /cresume- Lanjutkan musik yang dijeda.
/mute atau /cmute- Matikan musik yang diputar.
/unmute atau /cunmute- Suarakan musik yang dibisukan.
/skip atau /cskip- Lewati musik yang sedang diputar.
/stop atau /cstop- Hentikan pemutaran musik.
/shuffle atau /cshuffle- Secara acak mengacak daftar putar yang antri.
/seek atau /cseek - Teruskan Cari musik sesuai durasi Anda.
/seekback atau /cseekback - Mundur Carilah musik sesuai durasi Anda.
/restart - Mulai ulang bot untuk obrolan Anda.


✅ **Lewati Spesifik:**
/skip atau /cskip [Nomor(contoh: 3)] - Melewati musik ke nomor antrian yang ditentukan. Contoh: /skip 3 akan melewatkan musik ke musik antrian ketiga dan akan mengabaikan musik 1 dan 2 dalam antrian.

✅ **Putar loop:**
/loop atau /cloop [enable|disable] atau [Angka 1-10] - Saat diaktifkan, bot memutar musik yang sedang diputar menjadi 1-10 kali pada obrolan suara. Default ke 10 kali.

✅ **Pengguna Auth:**
Pengguna Auth dapat menggunakan perintah admin tanpa hak Admin di Grup Anda.

/auth [Username] - Tambahkan pengguna ke AUTH LIST dari grup.
/unauth [Username] - Hapus pengguna dari AUTH LIST grup.
/authusers - Periksa DAFTAR AUTH grup."""


HELP_2 = """✅ **Perintah Putar:**

Perintah yang tersedia = play , vplay , cplay

Perintah PlayForce = playforce , vplayforce , cplayforce

**c** singkatan dari pemutaran Channel.
**v** singkatan dari pemutaran video.
**force** singkatan dari play force.

/play atau /vplay atau /cplay - Bot akan mulai memainkan kueri yang Anda berikan di obrolan suara atau Streaming tautan langsung di obrolan suara.

/playforce atau /vplayforce atau /cplayforce - **Play Force** menghentikan trek yang sedang diputar pada obrolan suara dan mulai memutar trek yang dicari secara instan tanpa mengganggu/mengosongkan antrian.

/channelplay [Nama pengguna atau id obrolan] atau [Disable] - Hubungkan saluran ke grup dan streaming musik di obrolan suara saluran dari grup Anda.


✅ **Daftar Putar Server Bot:**
/playlist  - Periksa Daftar Putar Tersimpan Anda di Server.
/deleteplaylist - Hapus semua musik yang disimpan di daftar putar Anda.
/play - Mulai mainkan Daftar Putar Tersimpan Anda dari Server."""


HELP_3 = """✅ **Perintah Bot:**

/stats - Dapatkan 10 Trek Global Stats Teratas, 10 Pengguna Bot Teratas, 10 Obrolan Teratas di bot, 10 Teratas Dimainkan dalam obrolan, dll.

/sudolist - Periksa Daftar Sudo.

/lyrics [Nama Musik] - mencari Lirik untuk Musik.

/song [Nama Trek] atau [Tautan YT] - Unduh trek apa pun dari youtube dalam format mp3 atau mp4.

/player -  Dapatkan Panel interaktif.

**c** singkatan dari pemutaran saluran.

/queue atau /cqueue - Periksa Daftar Antrian Musik."""

HELP_4 = """✅ **Perintah Ekstra:**
/start - Mulai Bot Musik.
/help - Dapatkan Menu Pembantu Perintah dengan penjelasan rinci tentang perintah.
/ping- Ping Bot dan periksa statistik RAM, CPU, dll dari Bot.

✅ **Pengaturan Grup:**
/settings - Dapatkan pengaturan grup lengkap dengan tombol sebaris.

🔗 **Opsi di Pengaturan:**

1️⃣ Anda dapat mengatur **Kualitas Audio** Anda ingin streaming di obrolan suara.

2️⃣ Anda dapat mengatur **Kualitas Video** Anda ingin streaming di obrolan suara.

3️⃣ **Pengguna Auth:** Anda dapat mengubah mode perintah admin dari sini ke semua orang atau hanya admin. Jika semua orang, siapa pun yang ada di grup Anda dapat menggunakan perintah admin (seperti /skip /stop dll)

4️⃣ **Mode Bersih:** Saat diaktifkan, hapus pesan bot setelah 5 menit dari grup Anda untuk memastikan obrolan Anda tetap bersih dan baik.

5️⃣ **Perintah Bersih:** Saat diaktifkan, Bot akan menghapus perintah yang dieksekusi (/play /pause /shuffle /stop dll)

6️⃣ **Pengaturan Putar:**

/playmode - Dapatkan panel pengaturan pemutaran lengkap dengan tombol tempat Anda dapat mengatur pengaturan pemutaran grup Anda. 

Pilihan di Playmode:

1️⃣ **Mode Pencarian** [Direct atau Inline] - Mengubah mode pencarian Anda saat Anda memberikan mode /play

2️⃣ **Perintah Admin** [Semuanya atau Admin] - Jika semua orang, siapa pun yang ada di grup Anda akan dapat menggunakan perintah admin seperti (/skip /stop dll)

3️⃣ **Tipe Perintah** [Semuanya atau Admin] - Jika admin, hanya admin yang ada di grup yang dapat memutar musik di obrolan suara."""

HELP_5 = """⛑️ **ADD & REMOVE ADMIN SUDO:**
/addsudo [Username atau Balas ke pengguna] - Tambah admin Sudo
/delsudo [Username atau Balas ke pengguna] - Hapus admin Sudo

🛃 **HEROKU:**
/usage - Penggunaan Dyno.

🌐 **KONFIGURASI VARS:**
/get_var - Dapatkan config var dari Heroku atau .env
/del_var - Hapus semua var di Heroku atau .env
/set_var [Nama Var] [Value] - Setel Var atau Perbarui Var di heroku atau .env. Pisahkan Var dan Nilainya dengan spasi.

🤖 **PERINTAH BOT:**
/reboot - Memulai ulang Bot di Server. **Gunakan saat mendesak**
/restart - Memulai ulang Bot Anda.
/update - Update Bot.
/speedtest - Check server speed.
/maintenance [enable|disable] - Mode Maintenance.
/logger [enable|disable] - Bot mencatat kueri yang dicari di logger.
/get_log [Nomor Line] - Dapatkan log bot Anda dari heroku atau vps. Bekerja untuk keduanya.

📈 **PERINTAH STATIS:**
/activevoice - Periksa obrolan suara aktif di bot.
/activevideo - Periksa obrolan video aktif di bot.
/stats - Periksa Statistik Bot.

⚠️ **FUNGSI BLACKLIST CHAT:**
/blacklistchat [CHAT_ID] - Daftar hitam obrolan apa pun dari menggunakan Bot Musik.
/whitelistchat [CHAT_ID] - Daftar putih obrolan apa pun yang masuk daftar hitam dari menggunakan Bot Musik.
/blacklistedchat - Periksa semua obrolan yang masuk daftar hitam.

👤 **FUNGSI TERBLOKIR:**
/block [Username atau Balas ke pengguna] - Mencegah pengguna menggunakan perintah bot.
/unblock [Username atau Balas ke pengguna] - Hapus pengguna dari Daftar Blokir Bot.
/blockedusers - Periksa Daftar Pengguna yang diblokir.

👤 **FUNGSI GBAN:**
/gban [Username atau Balas ke pengguna] - Gban pengguna dari semua obrolan grup bot akan hentikan dia menggunakan bot Anda.
/ungban [Username atau Balas ke pengguna] - Hapus pengguna dari Daftar gbanned Bot dan izinkan dia menggunakan bot Anda.
/gbannedusers - Periksa Daftar Pengguna Gbanned.

🎥 **FUNGSI VIDEOCALL:**
/set_video_limit [Obrolan yang diizinkan] - Tetapkan Jumlah Obrolan maksimum yang diizinkan untuk Panggilan Video dalam satu waktu. Default untuk 3 obrolan.
/videomode [download|m3u8] - Jika mode unduh diaktifkan, Bot akan mengunduh video alih-alih memutarnya dalam bentuk M3u8. Secara default ke M3u8. Anda dapat menggunakan mode unduhan saat kueri apa pun tidak diputar dalam mode m3u8.

⚡️ **FUNGSI BOT PRIBADI:**
/authorize [CHAT_ID] - Izinkan obrolan untuk menggunakan bot Anda.
/unauthorize [CHAT_ID] - Larang obrolan menggunakan bot Anda.
/authorized - Periksa semua obrolan yang diizinkan dari bot Anda.

🌐 **FUNGSI BROADCAST:**
/broadcast [Message atau Balas pesan] - Siarkan pesan apa pun ke Obrolan yang akses oleh Bot.

Opsi untuk Broadcast:
**-pin** : Ini akan menyematkan pesan Anda.
**-pinloud** : Ini akan menyematkan pesan Anda dengan pemberitahuan.
**-user** : Ini akan menyiarkan pesan Anda ke pengguna yang telah memulai bot Anda.
**-assistant** : Ini akan menyiarkan pesan Anda dari akun asisten bot Anda.
**-nobot** : Ini akan memaksa bot Anda untuk tidak menyiarkan pesan.

**Contoh:** `/broadcast -user -assistant -pin Hello Testing`

"""
