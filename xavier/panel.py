import os
from xavier.emoji import Emoji
    
class Panel:
	
	def __init__(self,text,widht=None,colorpanel=None,colortext=None):
		self.text = text
		self.widht = widht
		self.colorpanel = colorpanel
		self.colortext = colortext
		self.simpan = []
		if self.widht in ["fit","FIT"]:
			self.Fit()
		else:
			GetPanel()
		
	def GetPanel(self):
		if self.GetEmoji() == True:
			jumemot = len(em)
			minus = 2 + jumemot
			print(f"{self.GetColor(self.GetColorPanel())}╭"+"─"*int(self.GetWidht()-2)+"╮")
			print(f"{self.GetColor(self.GetColorPanel())}│{self.GetColor(self.GetColorText())}{self.text}{self.GetColor(self.GetColorPanel())}"+" "*(self.GetWidht() - len(self.text) - minus)+"│")
			print(f"{self.GetColor(self.GetColorPanel())}╰"+"─"*int(self.GetWidht()-2)+"╯")
		else:
			print(f"{self.GetColor(self.GetColorPanel())}╭"+"─"*int(self.GetWidht()-2)+"╮")
			print(f"{self.GetColor(self.GetColorPanel())}│{self.GetColor(self.GetColorText())}{self.text}{self.GetColor(self.GetColorPanel())}"+" "*(self.GetWidht() - len(self.text) - 2)+"│")
			print(f"{self.GetColor(self.GetColorPanel())}╰"+"─"*int(self.GetWidht()-2)+"╯")
		
	def Fit(self):
		if self.GetEmoji() == True:
			minus = len(em)
			print(f"{self.GetColor(self.GetColorPanel())}╭"+"─"*(len(self.text) + minus)+"╮")
			print(f"{self.GetColor(self.GetColorPanel())}│{self.GetColor(self.GetColorText())}{self.text}{self.GetColor(self.GetColorPanel())}"+"│")
			print(f"{self.GetColor(self.GetColorPanel())}╰"+"─"*(len(self.text) + minus)+"╯")
		else:
			print(f"{self.GetColor(self.GetColorPanel())}╭"+"─"*(len(self.text))+"╮")
			print(f"{self.GetColor(self.GetColorPanel())}│{self.GetColor(self.GetColorText())}{self.text}{self.GetColor(self.GetColorPanel())}"+"│")
			print(f"{self.GetColor(self.GetColorPanel())}╰"+"─"*(len(self.text))+"╯")
			
	def GetWidht(self):
		if self.widht == None:
			self.widht = os.get_terminal_size().columns
		else:
			self.widht = self.widht
		
		return self.widht
		
	def GetColorPanel(self):
		if self.colorpanel == None:
			self.colorpanel = "DEFAULT"
		else:
			self.colorpanel = self.colorpanel
			
		return self.colorpanel
		
	def GetColorText(self):
		if self.colortext == None:
			self.colortext = "DEFAULT"
		else:
			self.colortext = self.colortext
			
		return self.colortext
		
	def GetColor(self,color=None):
		coloring = {
			"RED": "\x1b[91m",
			"GREEN": "\x1b[92m",
			"YELLOW": "\x1b[93m",
			"BLUE": "\x1b[94m",
			"ORANGE": "\x1b[95m",
			"CYAN": "\x1b[96m",
			"WHITE": "\x1b[97m",
			"BLACK": "\x1b[30m",
			"DEFAULT": "\x1b[39m",
			"NO_COLOR": "\x1b[39m"
			}
		return coloring.get(color)
		
	def GetEmoji(self):
		global em
		try:
			emot = {}
			emoticon = []
			data = sorted((v, k) for k, v in Emoji.items())
			for emoji, kode in data:
				#emot.update({emoji:kode})
				emoticon.append(emoji)
			em = [c for c in self.text if c in emoticon]
			
			return em[0] in emoticon
		except:
			return False
		
