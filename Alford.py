# 1) Verification
def verif(self):   #fct de recursif, tjr commencer par la base 
  if self is None:
    return True, sys.maxint, - sys.maxint -1
  okG, minG, maxG = verif(self.fils[0])    #pr la Gauche  相当于recursif 3 fois 
  okD, minD, maxD = verif(self.fils[1])   # pr la partie droit
  if self.fils[0] is None:
    mini = self.valeur
  else:
    mini = minG
  if self.fils[1] is None:
    maxi = self.valeur
  else:
    maxi = maxD
  if okG and okD and self.valeur < minD and self.valeur > maxG:
    return True, mini, maxi
  else:
    return False, mini, maxi
  
  
  # 2)
  def supprimer(self.val):
    if not self:   #if self is None:
      raise ValueError ("valeur n´est pas dans l´ARB")
		if self.valeur < val:
			self.files[1].supprimer(val)
		elif self.valeur > val:
			self.files[0].supprimer(val)
		else:
			if self.fils[0] is None and self.fils[1] is None:
				self = None
			elif self.fils[0] is None:
				self = self.fils[1]
			elif self.fils[1] is None:
				self = self.fils[0]
			else:
				succ = self.fils[0].supprime_max()
				self.valeur = succ
				
	def supprime_max(self):    #2eme fct pr 2)
		maxi = self.valeur
		if self.valeur[1] is None:
			self = self.fils[0]
			return maxi
		else:
			return self.fils[1].supprime_max()
#tri par tas
def tri_tas(liste):
	transfo_tas(liste, 1)
	for j in range(len(liste)):
		liste[0],liste[-j-1] = liste[-j-1],liste[0]
		tasser(liste[:-j-1],1)
	return liste
			
		
				


			
    
    
