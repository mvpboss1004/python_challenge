hint = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
in_tab = [chr(c) for c in range(ord('a'), ord('a')+26)]
out_tab = in_tab[2:] + in_tab[:2]
trans = str.maketrans(''.join(in_tab), ''.join(out_tab))
print(hint.translate(trans))
print('http://www.pythonchallenge.com/pc/def/%s.html' % 'map'.translate(trans))