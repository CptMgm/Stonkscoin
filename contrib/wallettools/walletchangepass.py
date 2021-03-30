from jsonrpc import ServiceProxy
access = ServiceProxy("http://127.0.0.1:3113")
pwd = raw_input("Enter old wallet passphrase: ")
pwd2 = raw_input("Enter new wallet passphrase: ")
access.walletpassphrasechange(pwd, pwd2)
