from dataclasses import dataclass

RUNS_PER_DOMAIN = 5

CONCURRENT_REQUESTS = 100

CONNECT_TIMEOUT = 8

READ_TIMEOUT = 15

DOWNLOAD_SIZE = 32768

DNS_SERVERS = {
    "Cloudflare-1": "1.1.1.1",
    "Cloudflare-2": "1.0.0.1",

    "Quad9-1": "9.9.9.9",
    "Quad9-2": "149.112.112.112",

    "OpenDNS-1": "208.67.222.222",
    "OpenDNS-2": "208.67.220.220",

    "Oracle": "169.254.169.254",
}

DOMAINS = [

    "web.whatsapp.com",
    "redirector.googlevideo.com",

    "instagram.fruh7-1.fna.fbcdn.net",
    "fna-instagram-shv-01-fruh5.fbcdn.net",
    "scontent-pmo1-1.xx.fbcdn.net",

    "clients3.google.com",
    "video-downloads.googleusercontent.com",

    "release-assets.githubusercontent.com",

    "audio4-ak.spotifycdn.com",

    "updates.cdn-apple.com",
    "6-courier.push.apple.com",

    "ws.chatgpt.com",

    "kws4.web.telegram.org",

    "v77.tiktokcdn.com",
    "sf16-va.tiktokcdn-us.com",

    "ipv4-c001-jed001-itcsa-isp.1.oca.nflxvideo.net",

    "jed-speed.itc.net.sa.prod.hosts.ooklaserver.net",
    "jed-speedtest.saudi.net.sa",

    "speedtest.malang.telkomsel.com.prod.hosts.ooklaserver.net",
    "speedtest.surabaya.myrepublic.net.id.prod.hosts.ooklaserver.net",
    "yogyakarta.speedtest.telkom.net.id",

    "nusukapp.nusuk.sa",
    "reg.qm.edu.sa",
    "snf3.nic.gov.sa",
    "moi.gov.sa",

    "siskohatkes.haji.go.id",
    "data.go.id",
]