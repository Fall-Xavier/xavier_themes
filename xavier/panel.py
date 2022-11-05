import os
from xavier.emoji import Emoji
    
class Panel:
	
	def __init__(self,text,widht=None,colorpanel=None,colortext=None):
		self.text = text
		self.widht = widht
		self.colorpanel = colorpanel
		self.colortext = colortext
		self.simpan = []
		self.GetPanel()
		
	def GetPanel(self):
		if self.widht == None:
			self.widht = os.get_terminal_size().columns
		if self.colorpanel == None:
			self.colorpanel = "DEFAULT"
		if self.colortext == None:
			self.colortext = "DEFAULT"
		print(f"{self.GetColor(self.colorpanel)}╭"+"─"*int(self.widht-2)+"╮")
		print(f"{self.GetColor(self.colorpanel)}│{self.GetColor(self.colortext)}{self.text}{self.GetColor(self.colorpanel)}"+" "*(self.widht - len(self.text) - 2)+"│")
		print(f"{self.GetColor(self.colorpanel)}╰"+"─"*int(self.widht-2)+"╯")
		
	def GetColor(self,color=None):
		warna = {
			"RED": "\x1b[91m",
			"GREEN": "\x1b[92m",
			"YELLOW": "\x1b[93m",
			"BLUE": "\x1b[94m",
			"ORANGE": "\x1b[95m",
			"CYAN": "\x1b[96m",
			"WHITE": "\x1b[97m",
			"BLACK": "\x1b[30m",
			"DEFAULT": "\x1b[39m"
			}
		return warna.get(color)
		
	def GetEmoji(self,emoji=None):
		emot = {}
		data = sorted((v, k) for k, v in Emoji.items())
		for emoticon, kode in data:
			emot.update({emoji:kode})
		print(emot.get(emoji))
		
		
#if __name__=="__main__":
	#teks = input(" masukan teks : ")
	#ukuran = int(input(" masukan ukuran : "))
	#Panel().GetPanel("aku sayang kamu sampai mati love you ayang mmuuah",widht=60,colortext="HIJAU")
	
	
	
	
