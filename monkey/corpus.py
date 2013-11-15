import os, shutil, random

class Corpus: 
	def __init__(self, name, percent):
		self.name = name
		self.cd = os.path.dirname(os.path.realpath(__file__))
		self.imagedir = os.path.join(self.cd, "corpus")
		self.newimagedir = os.path.join(self.cd, self.name)	

		# Create and rework paths.
		
		if os.path.isdir(self.newimagedir):
			shutil.rmtree(self.newimagedir)
			os.makedirs(self.newimagedir)			
	
		for root, dirs, files in os.walk(self.imagedir):
			for subdir in dirs:
				os.makedirs(os.path.join(self.newimagedir, subdir))

		# Now add the images.

		self.images = []
		self.unused = {} 
		for subdir in os.listdir(self.imagedir):
			fullpath = os.path.join(self.imagedir, subdir)
			self.images = os.listdir(fullpath)
			self.unused[subdir] = os.listdir(fullpath)	
			for i in range(0, int(len(self.images)*percent/100.0)):
				image = random.choice(self.images)
				self.images.remove(image)
				self.unused[subdir].remove(image)
				filepath = os.path.join(self.imagedir, subdir, image) 
				target = os.path.join(self.newimagedir, subdir)
				print filepath, target, "\n"
				shutil.copy(filepath, target)	
		

		

	def getNextImage(self, name):
		item = random.choice(self.unused[name])
		self.unused[name].remove(item)
		fullpath = os.path.join(self.imagedir, name, item)
		target = os.path.join(self.newimagedir, name)
		shutil.copy(fullpath, target)
		return fullpath	
	
